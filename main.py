import tkinter as tk

dados = [
    ("usuario1", "senha1"),
    ("usuario2", "senha2"),
    ("usuario3", "senha3")
]

janela = tk.Tk()
janela.title("Página de Login")
janela.geometry("500x400")

tk.Label(janela, text="Bem-vindo! Por favor, faça login.").pack()
tk.Label(janela, text="Usuário:").pack()
usuario_entry = tk.Entry(janela)
usuario_entry.pack()

tk.Label(janela, text="Senha:").pack()
senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

msg_label = tk.Label(janela)

def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    
    if (usuario, senha) in dados:
        msg_label.config(text="Login bem-sucedido!")
    else:
        msg_label.config(text="Usuário ou senha incorretos.")

tk.Button(janela, text="Login", command=login).pack()

pagina_sistema = tk.Frame(janela)
tk.Label(pagina_sistema, text="Bem-vindo ao sistema!").pack()

msg_label.pack()


janela.mainloop()

