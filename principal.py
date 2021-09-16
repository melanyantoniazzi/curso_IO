import contatos_utils

try:
    contatos = contatos_utils.csv_para_contatos('dados/contatos.csv')

    # contatos_utils.contatos_para_pickle(contatos, 'dados/contatos.pickle')
    # contatos = contatos_utils.pickle_para_contatos('dados/contatos.pickle')

    contatos_utils.contatos_para_json(contatos, 'dados/contatos.json')
    contatos = contatos_utils.json_para_contatos('dados/contatos.json')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')


#Podemos fechar os arquivos utilizando um bloco try/finally, mas o Python já nos deixa uma palavra reservada chamada with. Com ela conseguimos 
# gerenciar o contexto de abertura do arquivo. Isto é, o arquivo só permanece aberto dentro do escopo do bloco, e, após isso, o contexto 
# do arquivo é fechado, ou seja, o método close() é invocado.

#contato_carol = '11,Carol,carol@carol.com.br\n'
#contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

#with open('dados/contatos-escrita.csv', encoding='latin_1', mode='w') as arquivo1:
#    arquivo1.write(contato_carol)

#with open('dados/contatos-escrita.csv', encoding='latin_1', mode='a') as arquivo2:
#    arquivo2.write(contato_andreza)

#arquivo2.write('Nova linha')

#try:
#    with open('dados/contatos.csv', encoding='latin_1') as arquivo_contatos:
#        for linha in arquivo_contatos:
#            print(linha, end='')
#except FileNotFoundError:
#    print('Arquivo não encontrado')
#except PermissionError:
#    print('Sem permissão de escrita')
