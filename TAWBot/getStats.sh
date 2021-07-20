#/bin/bash
###########################
# Serverstats Script
###########################

#Remove the old file

rm serverStatus.txt
{
echo "Hello **$USER**\n"
echo "Today is**\n" 

date

echo "**\n"
echo "Here are the server stats as of **$(date +"%T"**)\n"

if ps aux |grep -v "grep" | "liquidsoap"
then
	echo "Liquidsoap is **ONLINE**\n"

else	echo "Liquidsoap is **OFFLINE**\n"

fi

echo "Our Uptime is :\n**"

uptime

echo "**\n"

echo "Vmstat says :\n**" 

vmstat

echo "**\n"

echo "Mpstat says : \n**"

mpstat

echo "**\n"

} >> serverStatus.txt
