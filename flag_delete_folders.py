# BORRAR ELEMENTOS DE MAS DE 15 DIAS

import os, time, shutil # os es libreria para interactuar con el SO, time es libreria para trabajar con el tiempo, shutil es libreria para borrar carpetas q aun tengan files dentro
from pathlib import Path # clase q me permite generar la ruta donde estoy parado

# path_to_delete = '/home/gcarrara/Documents/backup ibm'  # Variable que representa la carpeta que contiene las carpetas que se borraran si tienen mas de 15 dias

flag = 0

path_to_delete = Path() # me devuelve ruta donde estoy parado (.)
now = time.time() # tiempo q representa instante actual

str_path = os.path.join(path_to_delete, "failed_backup.log")

if Path(str_path).exists():
    Path(os.path.join(path_to_delete, "crontab_failed.log")).touch()
    flag = 1


while flag == 0:
    for f in os.listdir(path_to_delete):  # ciclo usado para borrar elementos de mas de 15 dias
        f = os.path.join(path_to_delete, f) # 'f' es la ruta que se va a borrar si cumple la condicion
        if os.stat(f).st_mtime < now - 15 * 86400:  # os.stat(f) devuele las estadisticas del elemento f y st.mtime es un atributo de ese objeto q representa fecha de la ultima modificacion
            if os.path.isdir(f): # isdir(f) es una funcion q devuelve Verdadero si se trata de una carpeta
                shutil.rmtree(f) # rmtree(f) borra la carpeta
                print(f'Deleted item {f}')  # imprime en la consola el elemento borrado
            else:
                os.remove(f) # borra si es archivo
                print(f'Deleted item {f}') # imprime en la consola el elemento borrado
    flag = 1
