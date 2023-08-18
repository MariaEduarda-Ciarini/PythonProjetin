import requests
class SearchAddress:
    def __init__(self, cep):
        cep = str(cep)
        if self.zip_code_valid(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Invalid!!")

    def __str__(self):
        return  self.format_cep()

    def zip_code_valid(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def access_via_zip_code(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados ['bairro'],
            dados ['localidade'],
            dados ['uf']
        )