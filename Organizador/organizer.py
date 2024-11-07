import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def criar_subpastas(diretorio):
    categorias = ['Imagens', 'Documentos', 'Vídeos', 'Outros', 'PDFs', 'Excel']
    for categoria in categorias:
        caminho = os.path.join(diretorio, categoria)
        if not os.path.exists(caminho):
            os.makedirs(caminho)

def organizar_arquivos(diretorio):
    tipos_arquivos = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documentos': ['.docx', '.txt', '.doc'],
        'PDFs': ['.pdf'],
        'Excel': ['.xlsx', '.csv'],
        'Vídeos': ['.mp4', '.mov', '.mkv'],
    }

    criar_subpastas(diretorio)

    for arquivo in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, arquivo)
        
        if os.path.isfile(caminho_completo):
            movido = False
            for categoria, extensoes in tipos_arquivos.items():
                if arquivo.endswith(tuple(extensoes)):
                    shutil.move(caminho_completo, os.path.join(diretorio, categoria, arquivo))
                    print(f'Movido {arquivo} para {categoria}')
                    movido = True
                    break
            
            if not movido:
                shutil.move(caminho_completo, os.path.join(diretorio, 'Outros', arquivo))
                print(f'Movido {arquivo} para Outros')

def selecionar_diretorio():
    pasta_selecionada = filedialog.askdirectory(title="Selecione uma pasta para organizar")
    if pasta_selecionada:
        organizar_arquivos(pasta_selecionada)
        messagebox.showinfo("Organização Completa", "Os arquivos foram organizados com sucesso!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Organizador de Arquivos")
root.geometry("300x150")

botao = tk.Button(root, text="Selecionar Pasta", command=selecionar_diretorio)
botao.pack(pady=20)

root.mainloop()