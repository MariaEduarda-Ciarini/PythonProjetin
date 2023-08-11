import contatos_utils
try:
    # contatos = contatos_utils.csv_para_contatos('contatos.csv')
    # contatos_utils.contatos_para_pickle('contatos, contatos.pickle')

    # contatos = contatos_utils.pickle_para_contatos('contatos.pickle')
    # contatos_utils.contatos_para_json(contatos, 'contatos.json')

    contatos = contatos_utils.json_para_contatos('contatos.json')


    for contato in contatos:
        print(f'{contato.id} - {contato.name} - {contato.email}')
except FileNotFoundError:
        print('File not found')
except PermissionError:
        print('No write permission')
