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
    
        console.print("[orange3][+] Curseforge[/orange3] selected!")
        instance_path = Prompt.ask("[yellow][?][/yellow] Enter the instance name")

        if not os.path.exists(f"C:/Users/{username}/curseforge/minecraft/Instances/{instance_path}"):
            console.print("[error][-][/error] The typed instantiation does not exist")
            time.sleep(3)
            continue
        else: 
            console.print("[success][+][/success] The instance was found!")
            make_backup("curseforge", instance_path)
            break

def modrinth():
    while True:
        os.system('cls')

        console.print("[green][+] Modrinth[/green] selected!")
        instance_path = Prompt.ask("[yellow][?][/yellow] Enter the instance name")

        if not os.path.exists(f"C:/Users/{username}/AppData/Roaming/ModrinthApp/profiles/{instance_path}"):
            console.print("[error][-][/error] The typed instantiation does not exist")
            time.sleep(3)
            continue
        else: 
            console.print("[success][+][/success] The instance was found!")
            make_backup("modrinth", instance_path)
            break


def make_backup(loader, instance_path):
    if loader == "minecraft":
        final_path = f"C:/Users/{username}/Documents/Saves Backups MC/{loader}"
    else:
        final_path = f"C:/Users/{username}/Documents/Saves Backups MC/{loader}/{instance_path}"

    if loader == "minecraft":
        saves_path = f"C:/Users/{username}/AppData/Roaming/.minecraft/saves"
    elif loader == "curseforge":
        saves_path = f"C:/Users/{username}/curseforge/minecraft/Instances/{instance_path}/saves"
    elif loader == "modrinth":
        saves_path = f"C:/Users/{username}/AppData/Roaming/ModrinthApp/profiles/{instance_path}/saves"

    saves = os.listdir(saves_path)

    if not saves:
        console.print("[error][-][/error] The saves folder is empty")
        time.sleep(3)
        return

    os.system('cls')

    if os.path.exists(final_path):
        console.print("[warning][!][/warning] There are files in the final directorate!")
        confirmation = Confirm.ask("[yellow][?][/yellow] Do you want to continue?")

        if confirmation:
            console.print("[warning][!][/warning] Deleting existing files!")
            shutil.rmtree(final_path)
            time.sleep(5)
        else:
            console.print("[warning][!][/warning] Process cancelled by the user!")
            time.sleep(3)
            return True
    
    os.makedirs(final_path)

    try:
        for save in track(saves, description="[success][+][/success] Copying saves!"):
            save_origin = os.path.join(saves_path, save)
            final_origin = os.path.join(final_path, save)

            if os.path.isdir(save_origin):
                shutil.copytree(save_origin, final_origin)
            else:
                shutil.copy2(save_origin, final_origin)
            
            time.sleep(0.01)

        console.print("[success][+][/success] Backup completed successfully!")
        console.input("Press ENTER to exit!")

    except Exception as e:
        console.print(f"[error][-][/error] {e}")
        time.sleep(5)
        return


if __name__ == "__main__":
    console.print("1 Minecraft Launcher")
    console.print("[orange3]2 Curseforge[/orange3]")
    console.print("[green]3 Modrinth[/green]")
    mod_loader = Prompt.ask("Select your launcher", choices=["1", "minecraft launcher", "2", "CurseForge",  "3", "Modrinth"], case_sensitive=False, show_choices=False)
    if mod_loader.lower() == "minecraft launcher" or mod_loader == "1":
        make_backup("minecraft", None)

    elif mod_loader.lower() == "curseforge" or mod_loader == "2":
        curseforge()

    elif mod_loader.lower() == "modrinth" or mod_loader == "3":
        modrinth()