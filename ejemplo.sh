function suma(){
	echo "La suma es: " $(($1+$2))
}

read -e -p "olademar: " x

function factorial(){
	fact=1
	for ((n=1;n<=$1;n++))
	do
		let fact=$(($fact*$n))
	done
	echo $fact
}

factorial x
