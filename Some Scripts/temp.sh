#!/bin/bash
# Script: temp.sh
# Purpose: Display the ARM CPU and GPU  temperature and voltages of Raspberry Pi 2/3 
# Author: Luchezar Velkov
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo -e "\n\t\t`tput smso`  S Y S T E M    I N F O R M A T I O N  `tput rmso`"
echo -e "\n\t\tThe CPU temp is:\t\t\c"
vcgencmd measure_temp|awk -F "=" '{print $2}'
echo -e "\t\tThe GPU temp is:\t\t\c"
/opt/vc/bin/vcgencmd measure_temp|awk -F "=" '{print $2}'
echo -e "\t\tThe Core voltage is:\t\t\c"
/opt/vc/bin/vcgencmd measure_volts core|awk -F "=" '{print $2}'
echo -e "\t\tThe sdram Core voltage is:\t\c"
/opt/vc/bin/vcgencmd measure_volts sdram_c|awk -F "=" '{print $2}'
echo -e "\t\tThe sdram I/O voltage is:\t\c"
/opt/vc/bin/vcgencmd measure_volts sdram_i|awk -F "=" '{print $2}'
echo -e "\t\tThe sdram PHY voltage is:\t\c"
/opt/vc/bin/vcgencmd measure_volts sdram_p|awk -F "=" '{print $2 "\n"}'
