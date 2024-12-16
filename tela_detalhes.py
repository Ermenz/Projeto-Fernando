import tkinter as tk
from tkinter import Toplevel, messagebox

def TelaDetalhes(parent):
    detalhes_window = Toplevel(parent)
    detalhes_window.title("Detalhes do Funcionário")
    detalhes_window.geometry("400x300")

    # Simulação de detalhes de um funcionário
    detalhes = {
        "Nome": "João Silva",
        "CPF": "12345678901",
        "Endereço": "Rua das Flores, 123",
        "Contato": "(11) 98765-4321",
        "Cargo": "Gerente",
        "Data de Nascimento": "01/01/1980"
    }

    row = 0
    for key, value in detalhes.items():
        tk.Label(detalhes_window, text=f"{key}:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        tk.Label(detalhes_window, text=value).grid(row=row, column=1, sticky="w", padx=10, pady=5)
        row += 1

    # Botão para fechar a janela
    tk.Button(detalhes_window, text="Fechar", command=detalhes_window.destroy).grid(row=row, column=0, columnspan=2, pady=10)
