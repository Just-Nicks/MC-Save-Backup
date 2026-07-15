import os
import shutil 
import time

from rich.console import Console
from rich.progress import track
from rich.prompt import Prompt, Confirm
from rich.theme import Theme

themes = Theme({"error": "red bold", "warning": "yellow bold", "success": "green"})

console = Console(theme=themes)

username = os.getenv("USERNAME")

def curseforge():
    while True:
        os.system('cls')
    
        console.print("[orange3][+] CurseForge[/orange3] selecionado")
        instance_path = Prompt.ask("[yellow][?][/yellow] Digite o nome da instancia")

        if not os.path.exists(f"C:/Users/{username}/curseforge/minecraft/Instances/{instance_path}"):
            console.print("[error][-][/error] A instancia digitada nao existe")
            time.sleep(3)
            continue
        else:
            console.print("[success][+][/success] A instancia foi encontrada!")
            make_backup("curseforge", instance_path)
            break

def modrinth():
    while True:
        os.system('cls')

        console.print("[green][+] Modrinth[/green] selecionado")
        instance_path = Prompt.ask("[yellow][?][/yellow] Digite o nome da instancia")

        if not os.path.exists(f"C:/Users/{username}/AppData/Roaming/ModrinthApp/profiles/{instance_path}"):
            console.print("[error][-][/error] A instancia digitada nao existe")
            time.sleep(3)
            continue
        else: 
            console.print("[success][+][/success] A instancia foi encontrada!")
            make_backup("modrinth", instance_path)
            break


def make_backup(loader, instance_path):
    final_path = f"C:/Users/{username}/Documents/Saves Backups MC/{loader}/{instance_path}"

    if loader == "curseforge":
        saves_path = f"C:/Users/{username}/curseforge/minecraft/Instances/{instance_path}/saves"
    elif loader == "modrinth":
        saves_path = f"C:/Users/{username}/AppData/Roaming/ModrinthApp/profiles/{instance_path}/saves"

    saves = os.listdir(saves_path)

    if not saves:
        console.print("[error][-][/error] A pasta de saves esta vazia")
        time.sleep(3)
        return

    os.system('cls' if os.name == 'nt' else 'clear')

    if os.path.exists(final_path):
        console.print("[warning][!][/warning] Existem arquivos no diretorio final!")
        confirmation = Confirm.ask("[yellow][?][/yellow] Deseja continuar?")

        if confirmation:
            console.print("[warning][!][/warning] Deletando arquivos antigos!")
            shutil.rmtree(final_path)
            time.sleep(5)
        else:
            console.print("[warning][!][/warning] Processo finalizado!")
            time.sleep(3)
            return True
    
    os.makedirs(final_path)

    try:
        for save in track(saves, description="[success][+][/success] Copiando saves!"):
            save_origin = os.path.join(saves_path, save)
            final_origin = os.path.join(final_path, save)

            if os.path.isdir(save_origin):
                shutil.copytree(save_origin, final_origin)
            else:
                shutil.copy2(save_origin, final_origin)
            
            time.sleep(0.01)

        console.print("[success][+][/success] Backup realizado com sucesso!")
        console.input("Pressione ENTER para sair!")

    except Exception as e:
        console.print(f"[error][-][/error] {e}")
        time.sleep(5)
        return


if __name__ == "__main__":
    mod_loader = Prompt.ask("Digite o app desejado:", choices=["1", "CurseForge",  "2", "Modrinth"], case_sensitive=False)
    if mod_loader.lower() == "curseforge" or mod_loader == "1":
        curseforge()

    elif mod_loader.lower() == "modrinth" or mod_loader == "2":
        modrinth()