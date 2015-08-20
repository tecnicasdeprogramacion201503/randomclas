ECHO 
echo ahora vamos a seleccionar una persona
python aleatorio.py > el_seleccionado.txt

erase "los_seleccionados.txt"
echo ahora_vamos _a seleccionar un grupo de gente
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt

start notepad "los_seleccionados.txt"
start notepad "el_seleccionado.txt"