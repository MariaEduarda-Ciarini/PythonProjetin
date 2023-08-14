import re

class ExtractorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.validation_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validation_url(self):
        if not self.url:
            raise ValueError("The url is empty")

        default_url = re.compile('(http(s)?://)?(www\.)?serasaczx\.com\.br/exchange\?currencyOrigin=real')
        match = default_url.match(self.url)
        if not match:
            raise ValueError("The URL is not valid.")

    def get_url_base(self):
        question_mark_index = self.url.find('?')
        url_base = self.url[:question_mark_index]
        return url_base

    def get_url_parameters(self):
        question_mark_index = self.url.find('?')
        url_parameters = self.url[question_mark_index+1:]
        return url_parameters

    def get_value_parameter(self, search_parameter):
        index_parameter = self.get_url_parameters().find(search_parameter)
        index_value = index_parameter + len(search_parameter) + 1
        index_and_ampersand = self.get_url_parameters().find('&', index_value)
        if index_parameter == -1:
            value = self.get_url_parameters()[index_value:]
        else:
            value = self.get_url_parameters()[index_value:index_and_ampersand]
        return value

url = "serasaczx.com.br/exchange?amount=100&currencyOrigin=real"
extractor_url = ExtractorURL(url)
value_qtd = extractor_url.get_value_parameter("amount")
print(value_qtd)
