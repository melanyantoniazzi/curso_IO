import csv, pickle, json
from contato import Contato

# latin_1 é um encoding
#vamos começar pela função que traz os dados do csv para o objetos Python. Nessa função abriremos o arquivo utilizando o with e invocaremos
#  a função reader() do módulo csv passando o arquivo aberto como parâmetro.
#s arquivos pickle são binários.


def csv_para_contatos(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            id, nome, email = linha

            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos

#pickle organiza objetos

def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)

def _contato_para_json(contato):
    return contato.__dict__

#vamos criar as funções que serializam os objetos em JSON, para isso, vamos utilizar a função dump() do módulo json e passar como parâmetro
#  default a função que realiza a conversão dos objetos do tipo contato:

#Como a função load() devolve um dicionário em que cada chave é um atributo do objeto, podemos desempacotar esse dicionário no construtor da
#  classe Contato.

def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            c = Contato(**contato)
            contatos.append(c)

    return contatos