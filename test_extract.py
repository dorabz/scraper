import unittest
from extract import extract_info_from_website

class TestWebsiteExtractionIntegration(unittest.TestCase):

    def test_extraction_pepsico(self):
        url = 'https://contact.pepsico.com/pepsi'
        info = extract_info_from_website(url)

        expected_phone_numbers = ['+385 1 563 45 92']
        expected_logo_url = 'https://contact.pepsico.com/files/brands/1531511621/pepsi@2x.png'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)

    def test_extraction_illion(self):
        url = 'https://illion.com.au/'
        info = extract_info_from_website(url)

        expected_phone_numbers = ['13 23 33']
        expected_logo_url = 'https://www.illion.com.au/wp-content/uploads/2019/03/ION-RGB-Gradient-64.png'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)

    def test_extraction_cialdnb(self):
        url = 'https://www.cialdnb.com/pt-br/'
        info = extract_info_from_website(url)

        expected_phone_numbers = []
        expected_logo_url = 'https://www.cialdnb.com/wp-content/uploads/2020/01/logo-cialdnb-color.png'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)

    def test_extraction_fortinet(self):
        url = 'https://www.fortinet.com/corporate/about-us/contact-us'
        info = extract_info_from_website(url)

        expected_phone_numbers = ['+1 408 235 7700', '+1 408 235 7737', '+1 833 308 3247', '+1 703 915 3817',
                                  '+1 866 868 3678', '+1 415 237 3234', '+33 (0)4 8987 0576']
        expected_logo_url = 'https://www.fortinet.com/content/dam/fortinet/images/general/fortinet-logo.svg'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)

    def test_extraction_petrobras(self):
        url = 'https://petrobras.com.br/en/contact-us/'
        info = extract_info_from_website(url)

        expected_phone_numbers = ['0800 7289001', '0800 28 28280']
        expected_logo_url = 'https://petrobras.com.br/lumis-theme/br/com/petrobras/website/theme/petrobras-website/assets/img/logo.svg'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)

    def test_extraction_cmsenergy(self):
        url = 'https://www.cmsenergy.com/contact-us/default.aspx'
        info = extract_info_from_website(url)

        expected_phone_numbers = ['827 01 28 22', '(517) 788 0550', '(517) 768 3376', '(800) 390 1220', '(517) 788 6538', '(517) 788 2395', '(517) 788 2394']
        expected_logo_url = 'https://s26.q4cdn.com/888045447/files/design/ClientLogo.png'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)

    def test_extraction_phosagro(self):
        url = 'https://www.phosagro.com/contacts/'
        info = extract_info_from_website(url)

        expected_phone_numbers = ['+7 (495) 956 19 02', '+7 (495) 231 31 15', '+7 (495) 232 96 89', '+7 (929) 600 46 42', '+7 (820) 259 32 32', '+74959561902',
                                  '+41417470370', '84959560964', '+74952312747', '+79255862405']
        expected_logo_url = 'https://www.phosagro.com/local/templates/.default/img/fosagro-logo-en--coloured.svg'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)

    def test_extraction_zaba(self):
        url = 'https://www.zaba.hr/home/en'
        info = extract_info_from_website(url)

        expected_phone_numbers = ['08000024']
        expected_logo_url = 'https://www.zaba.hr/home/static/img/zaba_logo.svg'
        
        self.assertEqual(info["phone_numbers"], expected_phone_numbers)
        self.assertEqual(info["logo_url"], expected_logo_url)


if __name__ == '__main__':
    unittest.main()
