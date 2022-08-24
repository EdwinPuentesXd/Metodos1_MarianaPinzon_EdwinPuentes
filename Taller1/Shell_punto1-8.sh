read -p "Ingrese el nombre del archivo que desea leer: " file
linea=1
while read LREAD
do
    array[$linea]=${LREAD}
    let linea=$(($linea+1))
done < ${file}
echo ${array[3]}
