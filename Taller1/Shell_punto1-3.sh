pass=0
function checkvalue(){
	if [[ 0 -eq "$xd" ]] || [[ 1 -eq "$xd" ]];then
		if [[ -z "$xd" ]];then
			echo "ERROR* Debe ingresar algún parámetro"
		else
			let pass=1
			echo "Ahora pass es igual 1, terminando ciclo..."
		fi
	else
		echo "ERROR* Intente de nuevo"
	fi
}
while [ 0 -eq $pass ]
do
	read -p "Ingrese un parámetro: " xd
	checkvalue $xd
done

