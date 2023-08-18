import requests
from cep import SearchAddress

cep = 18406275
object_cep = SearchAddress(cep)

# object_cep.access_via_zip_code()
# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

bairro, cidade, uf = object_cep.access_via_zip_code()
print(bairro, cidade, uf)