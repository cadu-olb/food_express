import tkinter as tk
from tkinter import messagebox
from funcoes import limpar_console, voltar_ao_menu  # Importando as funções

# Lista de restaurantes
restaurantes = [
    {"nome": "Mamamia", "cozinha": "Pizzaria", "ativo": False},
    {"nome": "Tostadin", "cozinha": "Churrascaria", "ativo": True},
    {"nome": "JaponFood", "cozinha": "Japonês", "ativo": False}
]

# Funções de operação
def cadastrar_restaurante():
    nome = entry_nome.get().strip()
    cozinha = entry_cozinha.get().strip()
    
    if any(rest["nome"].lower() == nome.lower() for rest in restaurantes):
        messagebox.showwarning("Nome Duplicado", f"Já existe um restaurante cadastrado com o nome '{nome}'.")
        return

    if nome and cozinha:
        restaurantes.append({"nome": nome, "cozinha": cozinha, "ativo": False})
        messagebox.showinfo("Sucesso", f"Restaurante '{nome}' de cozinha '{cozinha}' cadastrado com sucesso! (Inativo por padrão)")
        entry_nome.delete(0, tk.END)
        entry_cozinha.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")

def listar_restaurantes():
    lista_text.delete("1.0", tk.END)  
    restaurantes_ativos = [rest for rest in restaurantes if rest["ativo"]]
    if restaurantes_ativos:
        for i, rest in enumerate(restaurantes_ativos, 1):
            lista_text.insert(tk.END, f"{i}. {rest['nome']} - Cozinha: {rest['cozinha']}\n")
    else:
        lista_text.insert(tk.END, "Nenhum restaurante ativo cadastrado.\n")

def ativar_restaurante():
    nome = entry_nome.get().strip()
    for rest in restaurantes:
        if rest["nome"].lower() == nome.lower():
            if not rest["ativo"]:
                rest["ativo"] = True
                messagebox.showinfo("Ativação", f"Restaurante '{nome}' de cozinha '{rest['cozinha']}' ativado com sucesso!")
            else:
                messagebox.showinfo("Informação", f"Restaurante '{nome}' já está ativo.")
            return
    messagebox.showerror("Erro", "Restaurante não encontrado. Cadastre-o antes de ativar.")

def excluir_restaurante():
    nome = entry_nome.get().strip()
    for i, rest in enumerate(restaurantes):
        if rest["nome"].lower() == nome.lower():
            del restaurantes[i]
            messagebox.showinfo("Exclusão", f"Restaurante '{nome}' excluído com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_cozinha.delete(0, tk.END)
            voltar_ao_menu()  # Adiciona a espera antes de voltar ao menu
            return
    messagebox.showerror("Erro", "Restaurante não encontrado para exclusão.")

# Configuração da Interface Principal
root = tk.Tk()
root.title("Food Express")
root.geometry("500x600")
root.configure(bg="#fff5e1")

font_titulo = ("Arial", 18, "bold")
font_labels = ("Arial", 14)
font_botoes = ("Arial", 12, "bold")

# Widgets de interface
label_titulo = tk.Label(root, text="Food Express", font=font_titulo, bg="#fff5e1", fg="#d35400")
label_titulo.pack(pady=10)

frame = tk.Frame(root, bg="#ffebcd", padx=10, pady=10)
frame.pack(pady=10, padx=10)

label_nome = tk.Label(frame, text="Nome do Restaurante:", font=font_labels, bg="#ffebcd")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_cozinha = tk.Label(frame, text="Tipo de Cozinha:", font=font_labels, bg="#ffebcd")
label_cozinha.grid(row=1, column=0, padx=5, pady=5)
entry_cozinha = tk.Entry(frame, width=30)
entry_cozinha.grid(row=1, column=1, padx=5, pady=5)

# Botões de Ações
btn_cadastrar = tk.Button(root, text="Cadastrar Restaurante", command=cadastrar_restaurante, bg="#28a745", fg="white", font=font_botoes)
btn_cadastrar.pack(pady=5)

btn_listar = tk.Button(root, text="Listar Restaurantes", command=listar_restaurantes, bg="#007bff", fg="white", font=font_botoes)
btn_listar.pack(pady=5)

btn_ativar = tk.Button(root, text="Ativar Restaurante", command=ativar_restaurante, bg="#ffc107", fg="black", font=font_botoes)
btn_ativar.pack(pady=5)

btn_excluir = tk.Button(root, text="Excluir Restaurante", command=excluir_restaurante, bg="#dc3545", fg="white", font=font_botoes)
btn_excluir.pack(pady=5)

# Área de Exibição da Lista
lista_text = tk.Text(root, height=10, width=50, bg="#f7f7f7", font=("Arial", 12))
lista_text.pack(pady=10)

root.mainloop()
