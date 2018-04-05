#!/bin/sh

echo -ne "Content-Type: text/plain\r\n\r\n"
echo -ne "Setting network configuration to factory defaults..."

mount -o rw,remount /userfs
if [ $? -ne 0 ]; then
	echo "Error (rw remount)\r\n"
	exit 1
fi

rm -rf /usr/local/etc/config/netconfig
if [ $? -ne 0 ]; then
	echo "Error (rm)\r\n"
	exit 1
fi

mount -o ro,remount /userfs
if [ $? -ne 0 ]; then
	echo "Error (ro remount)\r\n"
	exit 1
fi

echo -ne "done.\r\n"

echo -ne "Rebooting...\r\n"
/sbin/reboot
