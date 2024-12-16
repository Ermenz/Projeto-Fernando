import tkinter as tk
from tkinter import Toplevel

def TelaRelatorio(parent):
    relatorio_window = Toplevel(parent)
    relatorio_window.title("Relatório de Funcionários")
    relatorio_window.geometry("500x400")

    # Simulação de uma lista de funcionários
    funcionarios = [
        {"Nome": "João Silva", "CPF": "12345678901", "Cargo": "Gerente"},
        {"Nome": "Maria Oliveira", "CPF": "09876543210", "Cargo": "Vendedora"},
        {"Nome": "Carlos Souza", "CPF": "56789012345", "Cargo": "Analista"}
    ]

    # Títulos das colunas
    tk.Label(relatorio_window, text="Nome", font=("Arial", 10, "bold"), anchor="w", width=20).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(relatorio_window, text="CPF", font=("Arial", 10, "bold"), anchor="w", width=20).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(relatorio_window, text="Cargo", font=("Arial", 10, "bold"), anchor="w", width=20).grid(row=0, column=2, padx=5, pady=5)

    # Listagem dos funcionários
    for i, func in enumerate(funcionarios, start=1):
        tk.Label(relatorio_window, text=func["Nome"], anchor="w").grid(row=i, column=0, padx=5, pady=2)
        tk.Label(relatorio_window, text=func["CPF"], anchor="w").grid(row=i, column=1, padx=5, pady=2)
        tk.Label(relatorio_window, text=func["Cargo"], anchor="w").grid(row=i, column=2, padx=5, pady=2)

    # Botão para fechar
    tk.Button(relatorio_window, text="Fechar", command=relatorio_window.destroy).grid(row=len(funcionarios) + 1, column=0, columnspan=3, pady=10)
