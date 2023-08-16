from cpf_cnpj import Documento

#exemple_cnpj = "14578440000135"

#exemple_cpf = "74644986070"

cpf_um = ("15316264754")
documento = Documento.create_documento(cpf_um)

print(documento)