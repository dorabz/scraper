import requests
from bs4 import BeautifulSoup
import re
import sys
from urllib.parse import urljoin

def extract_phone_numbers(content, soup):
    phone_tag = soup.find('ul', class_='contact-info')
    if phone_tag:
        phone = phone_tag.find('a', href='#')
        if phone:
            return [phone.get_text(strip=True)]
    
    pattern = re.compile(r'(\+\d{1,3}[-.\s]?)?(\d{2,4}[-.\s]?\d{2,4}[-.\s]?\d{2,4}[-.\s]?\d{0,4})')
    raw_numbers = pattern.findall(content)
    
    cleaned_numbers = [re.sub(r"[^0-9\+\(\)]", "", number[0]) for number in raw_numbers if number[0].strip()]
    
    return cleaned_numbers

def extract_logo_url(soup, base_url):
    meta_logo = soup.find("meta", property="og:image")
    if meta_logo:
        return urljoin(base_url, meta_logo["content"])

    favicon = soup.find("link", rel="shortcut icon")
    if favicon:
        return urljoin(base_url, favicon["href"])

    patterns = [
        {"alt": re.compile("logo", re.I)},
        {"class": re.compile("logo", re.I)},
        {"id": re.compile("logo", re.I)},
        {"class": re.compile("brand", re.I)},
        {"class": re.compile("header", re.I)},
        {"alt": re.compile("illion", re.I)}
        ]

    for pattern in patterns:
        logo = soup.find("img", pattern)
        if logo:
            return urljoin(base_url, logo.get("src", ""))

    for pattern in patterns:
        logo_svg = soup.find("svg", pattern)
        if logo_svg:
            logo_container = logo_svg.find_parent()
            if logo_container and logo_container.name == "a":
                href = logo_container.get("href", "")
                return urljoin(base_url, href)

    return None

def extract_info_from_website(url):
    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')
    phone_numbers = extract_phone_numbers(content, soup)
    logo_url = extract_logo_url(soup, url)

    return {
        "phone_numbers": phone_numbers,
        "logo_url": logo_url
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script_name.py <website_url>")
        sys.exit(1)

    url = sys.argv[1]

    info = extract_info_from_website(url)

    if info["phone_numbers"]:
        print(", ".join(info["phone_numbers"]))
    else:
        print("None")

    print(info["logo_url"] or "None")
