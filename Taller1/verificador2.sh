pass=0
function checkvalue(){
	if [[ 0 -eq "$pass" ]] || [[ 1 -eq "$pass" ]];then
		let pass=1
		echo "Ahora pass es igual a 1"
	else
		echo "ERROR* Intente de nuevo"
	fi
}
while [ 0 -eq $pass ]
do
	read -p "Ingrese un parámetro: " pass
done
