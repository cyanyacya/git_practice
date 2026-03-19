#sudo unzstd BT_RAM_CODE_MT7922_1_1_hdr.bin.zst
#sudo unzstd BT_RAM_CODE_MT7961_1_2_hdr.bin.zst
#sudo unzstd BT_RAM_CODE_MT7961_1a_2_hdr.bin.zst

#sudo cp /lib/firmware/mediatek/BT_RAM_CODE_MT7922_1_1_hdr.bin \                                                                         19:25 
#        /lib/firmware/mediatek/mt7925/

#sudo cp /lib/firmware/mediatek/BT_RAM_CODE_MT7961_1_2_hdr.bin \
#        /lib/firmware/mediatek/mt7925/

#sudo cp /lib/firmware/mediatek/BT_RAM_CODE_MT7961_1a_2_hdr.bin \
#        /lib/firmware/mediatek/mt7925/


#sudo mkdir -p /etc/pacman.d/hooks                                                                                                                            19:24 
#sudo nano /etc/pacman.d/hooks/90-mediatek-bt-unzstd.hook

#[Trigger]
#Operation = Install
#Operation = Upgrade
#Type = Package
#Target = linux-firmware-mediatek

#[Action]
#Description = Decompress MediaTek Bluetooth firmware
#When = PostTransaction
#Exec = /usr/bin/bash -c 'cd /lib/firmware/mediatek && for f in BT_RAM_CODE_*.zst; do unzstd -f "$f"; done'

sudo mkdir -p /lib/firmware/mediatek/mt7925

sudo cp /lib/firmware/mediatek/BT_RAM_CODE_MT7922_1_1_hdr.bin \
        /lib/firmware/mediatek/mt7925/

sudo cp /lib/firmware/mediatek/BT_RAM_CODE_MT7961_1_2_hdr.bin \
        /lib/firmware/mediatek/mt7925/

sudo cp /lib/firmware/mediatek/BT_RAM_CODE_MT7961_1a_2_hdr.bin \
        /lib/firmware/mediatek/mt7925/


sudo modprobe btmtk


#sudo pacman -S linux linux-headers

sudo modprobe btmtk

echo -n "0489 e10a" | sudo tee /sys/bus/usb/drivers/btusb/new_id

#sudo pacman -S linux-lts linux-lts-headers

sudo systemctl stop bluetooth

sudo rm -rf /var/lib/bluetooth/*


sudo rmmod btusb btmtk
sudo modprobe btmtk
sudo modprobe btusb

sudo systemctl start bluetooth

