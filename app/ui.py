import tkinter as tk
from tkinter import messagebox

class MiniERP:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini ERP - Cadastro de Clientes")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self._criar_widgets()

    def _criar_widgets(self):
        # Título
        titulo = tk.Label(self.root, text="Cadastro de Clientes", font=("Arial", 16))
        titulo.pack(pady=10)

        # Frame para o formulário
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        # Nome
        tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.nome_entry = tk.Entry(form_frame, width=30)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        # Email
        tk.Label(form_frame, text="E-mail:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botões
        botoes_frame = tk.Frame(self.root)
        botoes_frame.pack(pady=15)

        salvar_btn = tk.Button(botoes_frame, text="Salvar", command=self.salvar_dados, width=10)
        salvar_btn.grid(row=0, column=0, padx=10)

        limpar_btn = tk.Button(botoes_frame, text="Limpar", command=self.limpar_campos, width=10)
        limpar_btn.grid(row=0, column=1, padx=10)

    def salvar_dados(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        if not nome or not email:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        # Aqui você pode inserir no banco de dados futuramente
        print(f"Salvando: Nome={nome}, Email={email}")
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

