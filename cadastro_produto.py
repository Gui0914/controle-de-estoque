import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

class ControleEstoque:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Estoque")

        # Configurações de estilo
        self.root.geometry("400x300")  # Tamanho da janela
        self.root.resizable(False, False)  # Janela não redimensionável
        self.root.configure(bg="#F0F0F0")  # Cor de fundo

        # Fontes
        label_font = ("Arial", 12)
        entry_font = ("Arial", 10)

        # Espaçamento
        padding_y = 5
        padding_x = 10

        # Rótulos e entradas
        self.empresa_label = tk.Label(root, text="Nome da Empresa:", font=label_font, bg="#F0F0F0")
        self.empresa_entry = tk.Entry(root, font=entry_font, borderwidth=2, relief="solid")

        self.codigo_label = tk.Label(root, text="Código do Produto:", font=label_font, bg="#F0F0F0")
        self.codigo_entry = tk.Entry(root, font=entry_font, borderwidth=2, relief="solid")

        self.descricao_label = tk.Label(root, text="Descrição:", font=label_font, bg="#F0F0F0")
        self.descricao_entry = tk.Entry(root, font=entry_font, borderwidth=2, relief="solid")

        self.operacoes_label = tk.Label(root, text="Operações:", font=label_font, bg="#F0F0F0")
        self.operacoes_entry = tk.Entry(root, font=entry_font, borderwidth=2, relief="solid")

        self.banho_label = tk.Label(root, text="Banho:", font=label_font, bg="#F0F0F0")
        self.banho_entry = tk.Entry(root, font=entry_font, borderwidth=2, relief="solid")

        self.valor_label = tk.Label(root, text="Valor por Batida:", font=label_font, bg="#F0F0F0")
        self.valor_entry = tk.Entry(root, font=entry_font, borderwidth=2, relief="solid")

        # Botões
        self.adicionar_button = tk.Button(root, text="Adicionar Produto", command=self.adicionar_produto, font=label_font, bg="#4CAF50", fg="white")

        # Organização dos elementos na grade
        row_index = 0
        for label, entry in [
            (self.empresa_label, self.empresa_entry),
            (self.codigo_label, self.codigo_entry),
            (self.descricao_label, self.descricao_entry),
            (self.operacoes_label, self.operacoes_entry),
            (self.banho_label, self.banho_entry),
            (self.valor_label, self.valor_entry),
        ]:
            label.grid(row=row_index, column=0, sticky="w", padx=padding_x, pady=padding_y)
            entry.grid(row=row_index, column=1, sticky="ew", padx=padding_x, pady=padding_y)
            row_index += 1

        # Botão
        self.adicionar_button.grid(row=row_index, column=0, columnspan=2, pady=padding_y)

        # Caminho para o diretório "Documentos"
        self.documentos_path = os.path.join(os.path.expanduser("~"), "Documents")

        # Verifica e cria o diretório se não existir
        if not os.path.exists(self.documentos_path):
            os.makedirs(self.documentos_path)

    def adicionar_produto(self):
        empresa = self.empresa_entry.get()
        codigo = self.codigo_entry.get()
        descricao = self.descricao_entry.get()
        operacoes = self.operacoes_entry.get()
        banho = self.banho_entry.get()
        valor = self.valor_entry.get()

        try:
            # Cria um diretório para cada produto usando o código como nome do diretório
            produto_path = os.path.join(self.documentos_path, codigo)
            os.makedirs(produto_path, exist_ok=True)

            # Caminho para o arquivo CSV do produto
            file_path = os.path.join(produto_path, f"{codigo}_info.csv")

            # Adiciona as informações ao arquivo CSV do produto
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Empresa", "Código", "Descrição", "Operações", "Banho", "Valor"])
                writer.writerow([empresa, codigo, descricao, operacoes, banho, valor])

            # Exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso.")
        except Exception as e:
            # Exibe uma mensagem de erro se algo der errado
            messagebox.showerror("Erro", f"Erro ao adicionar produto: {e}")

        # Limpa os campos de entrada
        self.empresa_entry.delete(0, tk.END)
        self.codigo_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)
        self.operacoes_entry.delete(0, tk.END)
        self.banho_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ControleEstoque(root)
    root.mainloop()
