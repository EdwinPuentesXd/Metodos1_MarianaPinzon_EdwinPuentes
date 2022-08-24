function factorial(){
	fact=1
	for ((n=1;n<=$1;n++))
	do
		let fact=$(($fact*$n))
	done
	echo $fact
}

factorial $1
