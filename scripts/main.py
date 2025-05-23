import os
import shutil

SERVER_DIR = "C:\\GABRIEL\\CheckPoint_Cyber_Security\\data\\servidor"
os.makedirs(SERVER_DIR, exist_ok=True)

def upload_file(filepath):
    filename = os.path.basename(filepath)
    shutil.copy(filepath, os.path.join(SERVER_DIR, filename))
    print(f"Arquivo {filename} enviado para o servidor.")

def list_files():
    print("Arquivos no servidor:")
    for f in os.listdir(SERVER_DIR):
        print(f"- {f}")

def delete_file(filename):
    path = os.path.join(SERVER_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        print(f"Arquivo {filename} removido.")
    else:
        print("Arquivo não encontrado.")

def export_file(filename, destino):
    path = os.path.join(SERVER_DIR, filename)
    if os.path.exists(path):
        shutil.copy(path, destino)
        print(f"Arquivo {filename} exportado para {destino}.")
    else:
        print("Arquivo não encontrado.")

while True:
    print("\n[1] Upload\n[2] Listar\n[3] Excluir\n[4] Exportar\n[0] Sair")
    op = input("Escolha: ")
    if op == "1":
        upload_file(input("Caminho do arquivo: "))
    elif op == "2":
        list_files()
    elif op == "3":
        delete_file(input("Nome do arquivo: "))
    elif op == "4":
        export_file(input("Nome do arquivo: "), input("Destino: "))
    elif op == "0":
        break
