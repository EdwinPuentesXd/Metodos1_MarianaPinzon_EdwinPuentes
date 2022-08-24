if [[ -f $(pwd)/data ]];then
	echo "La carpeta existe"
else
	mkdir $(pwd)/data
fi
