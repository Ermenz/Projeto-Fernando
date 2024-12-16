from tela_detalhes import TelaDetalhes
from tela_relatorio import TelaRelatorio

btn_detalhes = tk.Button(button_frame, text="Detalhes", width=10, command=lambda: TelaDetalhes(root))
btn_detalhes.grid(row=0, column=4, padx=5)

btn_relatorio = tk.Button(button_frame, text="Relatório", width=10, command=lambda: TelaRelatorio(root))
btn_relatorio.grid(row=0, column=5, padx=5)
