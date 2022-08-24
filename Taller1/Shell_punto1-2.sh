function help(){

	echo "ERROR* Debe incluir tres parametros: Posición inicial, Velocidad inicial y Tiempo total"
}

if ! [ $# -eq 3 ]; then
	help
	exit 1
else
	echo "Corriendo programa..."
fi
