from .pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, id, nome, logradouro, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj, nome_fantasia, website=""):
        super().__init__(id, nome, logradouro, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj)
        self.nome_fantasia = nome_fantasia
        self.website = website