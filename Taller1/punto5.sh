#Variacion sin repetición

n=20
r=3
den=$(($n-$r))

fact1=1
fact2=1
for ((x=1;x<=$n;x++))
do
	let fact1=$(($fact1*$x))
done
for ((y=1;y<=$den;y++))
do
	let fact2=$(($fact2*$y))
done

var=$(($fact1/$fact2))
echo $var


