echo Ahora vamos a seleccionar una persona.
python aleatorio.py > el_seleccionado.txt

del "los_seleccionados.txt"
echo Ahora vamos a seleccionar un grupo de gente.
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
python aleatorio.py >> los_seleccionados.txt
cls
rem Codigo para abrir los seleccionados en Notepad++
rem path = %path%;C:\Program Files (x86)\Notepad++
rem path = %path%;C:\Program Files\Notepad++
rem notepad++ el_seleccionado.txt
rem notepad++ los_seleccionados.txt
start notepad el_seleccionado.txt
start notepad los_seleccionados.txt