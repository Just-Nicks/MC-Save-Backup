# EN

# ⛏️ MC Saves Backup

## Description

* Tired of manually opening your Minecraft instances every time you want to back up your modded worlds? With this Python script, you can create backups quickly and easily.

* All saves are copied to:

```text
C:/Users/{username}/Documents/Saves Backups MC/{loader}/{instance_path}
```

* No need to create this folder yourself. The script automatically creates it when needed.

## 🚨 Warnings

* The script deletes all files from the selected instance's backup folder if any saves or files already exist in:

```text
C:/Users/{username}/Documents/Saves Backups MC/{loader}/{instance_path}
```

It then copies the latest saves. For this reason, do not store any important files in this directory.

* Example:

```text
C:/Users/{username}/Documents/Saves Backups MC/modrinth/Fabric 1.20.*
```

In this example, the **Fabric 1.20.*** **instance** was selected in the **Modrinth** **loader**. When the backup is run again, the script will remove the old saves from that folder and copy the new ones.

* This behavior is intentional and helps prevent conflicts with outdated files, reducing the chance of issues with your saved worlds.

* I am not responsible for lost worlds or any data loss resulting from the use of this script.

* Do not worry about the original instance folder. The script only copies files and does not modify or delete the original saves.

### This project includes a `.exe` file for users who do not want to install Python.

## ‼️ Requirements

This script uses a few libraries that are required to run the `.py` version:

```python
Python >= 3.14.6
rich >= 15.0.0
```

If you want a quick installation, use the included `requirements.txt` file.

- use on cmd
```python
python pip install -r requiments.txt
```

### This traduction its make by chat-gpt

------------------------------------------------------------------------------------------------------------------------------------------------------------

# PT-BR

# ⛏️ MC Saves Backup

## Descrição

* Cansado de entrar manualmente nas suas instâncias do Minecraft para fazer backup dos seus mundos com mods? Agora você pode usar um script em Python para realizar esse backup de forma rápida e prática.

* Todos os saves são copiados para a pasta:

```text
C:/Users/{username}/Documents/Saves Backups MC/{loader}/{instance_path}
```

* Não se preocupe em criar essa pasta. O script faz isso automaticamente.

## 🚨 Avisos

* O script apaga todos os arquivos da instância que está sendo copiada caso já exista algum save ou arquivo em:

```text
C:/Users/{username}/Documents/Saves Backups MC/{loader}/{instance_path}
```

Em seguida, ele copia os saves mais recentes. Portanto, não deixe nenhum arquivo importante nessa pasta.

* Exemplo:

```text
C:/Users/{username}/Documents/Saves Backups MC/modrinth/Fabric 1.20.*
```

Nesse exemplo, foi selecionada a **instância** `Fabric 1.20.*` no **loader** `Modrinth`. Ao executar o backup novamente, o script removerá os saves antigos dessa pasta e copiará os novos.

* O script faz isso com o objetivo de evitar conflitos com arquivos antigos e reduzir a chance de problemas nos seus mundos salvos.

* Não me responsabilizo por mundos perdidos ou qualquer perda de dados decorrente do uso deste script.

* Não se preocupe com a pasta original da instância. O script apenas copia os arquivos e não modifica nem remove os saves originais.

### Este projeto acompanha um arquivo `.exe` para quem não deseja instalar o Python.

## ‼️ Requisitos

Este script utiliza algumas bibliotecas necessárias para executar a versão `.py`:

```python
Python >= 3.14.6
rich >= 15.0.0
```

Caso queira uma instalação rápida, utilize o arquivo `requirements.txt`.

- use no terminal
```python
python pip install -r requiments.txt
```
