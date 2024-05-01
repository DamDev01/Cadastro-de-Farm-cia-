import tkinter as tk
from tkinter import messagebox
from model.associado import Associado
from model.colaborador import Colaborador
from model.fornecedor import Fornecedor

def cadastrar():
    categoria = var_categoria.get()
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    numero = entry_numero.get()
    cep = entry_cep.get()
    bairro = entry_bairro.get()
    cidade = entry_cidade.get()
    uf = entry_uf.get()
    telefone = entry_telefone.get()
    cpf_cnpj = entry_cpf_cnpj.get()

    if categoria == "Associado":
        situacao = entry_situacao.get()
        numero_associado = entry_numero_associado.get()
        pessoa = Associado(nome, endereco, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj, situacao, numero_associado)
    elif categoria == "Colaborador":
        cargo = entry_cargo.get()
        pessoa = Colaborador(nome, endereco, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj, cargo)
    elif categoria == "Fornecedor":
        nome_fantasia = entry_nome_fantasia.get()
        website = entry_website.get()
        pessoa = Fornecedor(nome, endereco, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj, nome_fantasia, website)

    messagebox.showinfo("Sucesso", f"{categoria} cadastrado com sucesso!")

root = tk.Tk()
root.title("Cadastro")

# Adicionando opções de categoria
var_categoria = tk.StringVar()
var_categoria.set("Associado")
label_categoria = tk.Label(root, text="Categoria:")
label_categoria.grid(row=0, column=0)
opcoes_categoria = ["Associado", "Colaborador", "Fornecedor"]
opcoes_categoria_menu = tk.OptionMenu(root, var_categoria, *opcoes_categoria)
opcoes_categoria_menu.grid(row=0, column=1)

# Adicionando campos de entrada comuns a todas as categorias
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=1, column=1)

label_endereco = tk.Label(root, text="Endereço:")
label_endereco.grid(row=2, column=0)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=2, column=1)

label_numero = tk.Label(root, text="Número:")
label_numero.grid(row=3, column=0)
entry_numero = tk.Entry(root)
entry_numero.grid(row=3, column=1)

label_cep = tk.Label(root, text="CEP:")
label_cep.grid(row=4, column=0)
entry_cep = tk.Entry(root)
entry_cep.grid(row=4, column=1)

label_bairro = tk.Label(root, text="Bairro:")
label_bairro.grid(row=5, column=0)
entry_bairro = tk.Entry(root)
entry_bairro.grid(row=5, column=1)

label_cidade = tk.Label(root, text="Cidade:")
label_cidade.grid(row=6, column=0)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=6, column=1)

label_uf = tk.Label(root, text="UF:")
label_uf.grid(row=7, column=0)
entry_uf = tk.Entry(root)
entry_uf.grid(row=7, column=1)

label_telefone = tk.Label(root, text="Telefone:")
label_telefone.grid(row=8, column=0)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=8, column=1)

label_cpf_cnpj = tk.Label(root, text="CPF/CNPJ:")
label_cpf_cnpj.grid(row=9, column=0)
entry_cpf_cnpj = tk.Entry(root)
entry_cpf_cnpj.grid(row=9, column=1)

# Funções para alternar entre campos de entrada conforme a categoria selecionada

def mostrar_campos_associado():
    label_situacao.grid(row=10, column=0)
    entry_situacao.grid(row=10, column=1)
    label_numero_associado.grid(row=11, column=0)
    entry_numero_associado.grid(row=11, column=1)
    label_cargo.grid_forget()
    entry_cargo.grid_forget()
    label_nome_fantasia.grid_forget()
    entry_nome_fantasia.grid_forget()
    label_website.grid_forget()
    entry_website.grid_forget()

def mostrar_campos_colaborador():
    label_cargo.grid(row=10, column=0)
    entry_cargo.grid(row=10, column=1)
    label_situacao.grid_forget()
    entry_situacao.grid_forget()
    label_numero_associado.grid_forget()
    entry_numero_associado.grid_forget()
    label_nome_fantasia.grid_forget()
    entry_nome_fantasia.grid_forget()
    label_website.grid_forget()
    entry_website.grid_forget()

def mostrar_campos_fornecedor():
    label_nome_fantasia.grid(row=10, column=0)
    entry_nome_fantasia.grid(row=10, column=1)
    label_website.grid(row=11, column=0)
    entry_website.grid(row=11, column=1)
    label_situacao.grid_forget()
    entry_situacao.grid_forget()
    label_numero_associado.grid_forget()
    entry_numero_associado.grid_forget()
    label_cargo.grid_forget()
    entry_cargo.grid_forget()

# Adicionando campos específicos para cada categoria
label_situacao = tk.Label(root, text="Situação:")
entry_situacao = tk.Entry(root)

label_numero_associado = tk.Label(root, text=" Número Associado:")
entry_numero_associado = tk.Entry(root)

label_cargo = tk.Label(root, text="Cargo:")
entry_cargo = tk.Entry(root)

label_nome_fantasia = tk.Label(root, text="Nome Fantasia:")
entry_nome_fantasia = tk.Entry(root)

label_website = tk.Label(root, text="Website:")
entry_website = tk.Entry(root)

# Adicionando botões de rádio para alternar entre as categorias
tk.Radiobutton(root, text="Associado", variable=var_categoria, value="Associado", command=mostrar_campos_associado).grid(row=0, column=2, sticky="w")
tk.Radiobutton(root, text="Colaborador", variable=var_categoria, value="Colaborador", command=mostrar_campos_colaborador).grid(row=1, column=2, sticky="w")
tk.Radiobutton(root, text="Fornecedor", variable=var_categoria, value="Fornecedor", command=mostrar_campos_fornecedor).grid(row=2, column=2, sticky="w")


# Por padrão, mostramos os campos associados
mostrar_campos_associado()

# Botão para cadastrar
button_cadastrar = tk.Button(root, text=" Cadastrar", command=cadastrar)
button_cadastrar.grid(row=12, columnspan=2)

root.mainloop()
