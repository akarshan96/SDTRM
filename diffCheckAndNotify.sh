#!/bin/sh

# Diff check and Mail Notifier
#sh /home/xeon/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Ambala_Division_Office/md5checker.sh
#sh /home/xeon/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Faridabad_Divisional_Office/md5checker.sh
#sh /home/xeon/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Gurugram_Divisional_Office/md5checker.sh
#sh /home/xeon/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Hisar_Divisional_Office/md5checker.sh
#sh /home/xeon/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Karnal_Divisional_Office/md5checker.sh
#sh /home/xeon/Nextcloud/Haryana_State_Dealer_Tax_Monitor_SheetsRohtak_Divisional_Office/md5checker.sh

max=1000000

for i in `seq 2 $max`
do
	notify-send running

        # Diff checking and Notify

	cd ~/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Faridabad_Divisional_Office/
	pushd `dirname $0` > /dev/null
	SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
	notify-send $SCRIPTPATH
	./md5checker.sh
	sleep 10
	popd > /dev/null

	cd ~/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Rohtak_Divisional_Office/
	pushd `dirname $0` > /dev/null
	SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
	notify-send $SCRIPTPATH
	./md5checker.sh
	sleep 10
	popd > /dev/null

	cd ~/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Karnal_Divisional_Office/
	pushd `dirname $0` > /dev/null
	SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
	notify-send $SCRIPTPATH
	./md5checker.sh
	sleep 10
	popd > /dev/null

	cd ~/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Hisar_Divisional_Office/
	pushd `dirname $0` > /dev/null
	SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
	notify-send $SCRIPTPATH
	./md5checker.sh
	sleep 10
	popd > /dev/null

	cd ~/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Gurugram_Divisional_Office/
	pushd `dirname $0` > /dev/null
	SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
	notify-send $SCRIPTPATH
	./md5checker.sh
	sleep 10
	popd > /dev/null

	cd ~/Nextcloud/Haryana_State_Dealer_Tax_Monitor_Sheets/Ambala_Division_Office/
	pushd `dirname $0` > /dev/null
	SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
	notify-send $SCRIPTPATH
	./md5checker.sh
	sleep 10
	popd > /dev/null

done
