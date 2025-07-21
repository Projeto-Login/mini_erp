import tkinter as tk
from .database import create_table
from .ui import MiniERP

def main():
    # Criar a tabela do banco de dados se não existir
    create_table()

    # Configurar a interface gráfica
    root = tk.Tk()
    app = MiniERP(root)
    root.mainloop()

if __name__ == "__main__":
    main()
