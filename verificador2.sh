pass=0
function checkvalue(){
	if [[ $pass -eq 0 || $pass -eq 1]]; then
		let pass= 1
	else
		echo "ERROR* Intente de nuevo"
}


