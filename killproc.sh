rm _temp
read -p "kill proc at socket " socket1
firefoxps=`ps -C "firefox" -o "%p" --no-headers`
lsof -i -tcp:$socket1 > _temp
while read -r line;
do  {
	if [ $line != $firefoxps ]
	then kill -9 $line;
	fi;
}
done < _temp
rm _temp
