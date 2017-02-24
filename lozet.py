#!/usr/bin/python
# -*- coding:utf-8 -*-
import platform
import sys
import os
import socket
"""Linux makinenin temel bilgilerini getirir
	Yazan: Samet Atalar <sametyusa@gmail.com>
	http://github.com/sametyusa"""
"""Copyright (c) 2016 Samet Atalar
    sametyusa@gmail.com
    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:
    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
def ozet():
	mavi='\033[94m'
	sonrenk='\033[0m'
	pembe='\033[95m'
	print(pembe+"SİSTEM HAKKINDA ÖZET BİLGİLER"+sonrenk)

	print(mavi+"İŞLETİM SİSTEMİ BİLGİLERİ"+sonrenk)
	print("Makinenin adı: "+ platform.node())
	dagitim_adi=os.popen("cat /etc/os-release |grep PRETTY_NAME | cut -d= -f2")
	print("Linux dağıtımı: "+ dagitim_adi.read().strip())
	kernel_surum=os.popen("uname -r")
	print("Linux Kernel Sürümü:" + kernel_surum.read())

	#İşlemci Bilgileri
	print(mavi+"İŞLEMCİ BİLGİLERİ"+sonrenk)
	cpu_uretici=os.popen("lscpu | grep 'Vendor' | cut -d' ' -f15")
	print("İşlemci üreticisi: "+ cpu_uretici.read().strip())
	isl=platform.processor()
	islemci=""
	if isl=="x86_64" or isl=="amd64":
		islemci="64-bit"
	else:
		islemci="32-bit"
	print("İşlemci mimarisi: "+ islemci)

	#RAM Bilgileri
	print("")
	print(mavi+"RAM BİLGİLERİ"+sonrenk)
	ram_top=os.popen("free -h |grep 'Mem:' |cut -d' ' -f12") #Toplam RAM kapasitesi
	ram_kul=os.popen("free -h | grep 'Mem:' | cut -d' ' -f20") #Kullanılan RAM kapasitesi
	print("Kullanılan/Toplam RAM: "+ ram_kul.read().strip() +"/"+ram_top.read())

	#Harddisk Bilgileri
	print(mavi+"DEPOLAMA BİLGİLERİ"+sonrenk)
	print("Bölüm		Toplam	Dolu	Boş") #Başlık yazısı
	print(os.popen("df -h | grep ^/dev |cut -c1-35").read())

	#Ağ bilgileri
	print(mavi+"AĞ BİLGİLERİ"+sonrenk)
	print("IPv4 Adresi: "+ socket.gethostbyname(socket.gethostname()))
	ipv6=os.popen("ip -f inet6 add sho  | grep inet6 | grep -v ::1 | cut -d' ' -f6")
	print("IPv6 Adresi: "+ ipv6.read().strip())
	#Makinenin ağdaki tam adı
	print("FQDN: "+ socket.getfqdn())

def net():
	#Ağ bilgilerini gösterir
	aygitlar=os.listdir("/sys/class/net")
	aygit_say=len(aygitlar) #Ağ aygıtı sayısı
	i=0
	while i<aygit_say:
		mac=open("/sys/class/net/"+aygitlar[i]+"/address","r") #MAC Adresi
		simdiki_aygit=aygitlar[i]
		ipv4=os.popen("ifconfig "+simdiki_aygit+" | grep 'inet addr:' |cut -d: -f2 |cut -d' ' -f1")
		ipv6=os.popen("ifconfig "+simdiki_aygit+" | grep 'inet6 addr:' | cut -d' ' -f13")
		maske=os.popen("ifconfig "+simdiki_aygit+" | grep 'Mask:' | cut -d: -f4")
		print("CİHAZ: "+simdiki_aygit)
		print("MAC Adresi: "+mac.read().strip())
		print("IPv4 Adresi: "+ipv4.read().strip())
		print("Ağ maskesi: "+maske.read().strip())
		print("IPv6 Adresi: "+ipv6.read())
		i+=1
def cpu():
	#işlemci ayrıntıları
	cpu_model=os.popen("cat /proc/cpuinfo | grep 'model name' | cut -d: -f2")
	print("İşlemci Modeli: "+ cpu_model.read().strip())
	cpu_mimari=os.popen("lscpu | grep 'Architecture' | cut -d: -f2 | cut -d' ' -f11")
	if cpu_mimari.read().strip()=="x86_64" or cpu_mimari.read().strip()=="amd64":
		print("İşlemci Mimarisi: 64-bit")
	else:
		print("İşlemci Mimarisi: 32-bit")
	cpu_cache=os.popen("cat /proc/cpuinfo | grep 'cache size' | cut -d: -f2")
	print("Cache boyutu: "+cpu_cache.read().strip())
	cpu_cekirdek=os.popen("cat /proc/cpuinfo | grep 'cpu cores' | cut -d: -f2")
	print("Çekirdek sayısı: "+cpu_cekirdek.read().strip())

def ram():
	#RAM ayrıntıları
	print("Bu komut root yetkileri gerektirebilir")
	lshw=os.popen("lshw")
	if "command not found" in lshw.read():
		print("lshw paketi kurulu değil.")
	else:
		ram_sayi_sor=os.popen("sudo lshw -c memory | grep '*-bank' | wc -l")
		ram_sayi=int(ram_sayi_sor.read().strip())
		i=0
		ram_top=os.popen("free -h |grep 'Mem:' |cut -d' ' -f12") #Toplam RAM kapasitesi
		print("Toplam RAM kapasitesi: "+ram_top.read().strip())
		ram_kul=os.popen("free -h | grep 'Mem:' | cut -d' ' -f20") #Kullanılan RAM kapasitesi
		print("Kullanılan RAM kapasitesi: "+ram_kul.read().strip())
		print("Toplam RAM slotu sayısı: "+ str(ram_sayi))
		while i<ram_sayi:
			print(str(i)+". slot")
			ram_model=os.popen("sudo lshw -c memory | grep -w *-bank:"+str(i)+" -A 2 | grep 'product' | cut -d: -f2")
			print("RAM Modeli: "+ ram_model.read().strip())
			ram_uretici=os.popen("sudo lshw -c memory | grep -w *-bank:"+str(i)+" -A 3 | grep 'vendor' |cut -d: -f2")
			print("Üretici: "+ ram_uretici.read().strip())
			ram_kapasite=os.popen("sudo lshw -c memory | grep -w *-bank:"+str(i)+" -A 6 | grep 'size' | cut -d: -f2")
			print("Kapasite: "+ram_kapasite.read().strip())
			i+=1
def hdd():
	#Harddisk bilgileri
	hdd=os.popen("lsblk -io KNAME,LABEL,TYPE,VENDOR,MODEL,SIZE | grep -v 'KNAME'")
	print("ADI ETIKET TÜRÜ  ÜRETİCİ  MODEL BOYUT")
	print(hdd.read())
if len(sys.argv)<2:
	ozet()
else:
	if sys.argv[1]=="net":
		net()
	elif sys.argv[1]=="cpu":
		cpu()
	elif sys.argv[1]=="ram":
		ram()
	elif sys.argv[1]=="hdd":
		hdd()
	elif sys.argv[1]=="h" or sys.argv[1]=="yardim" or sys.argv[1]=="help":
		print("""Donanım bilgilerini özet geçen script\n
Yazan: Samet Atalar <sametyusa@gmail.com>
http://github.com/sametyusa\n
Bu script MIT Lisansı ile lisanslıdır\n
Parametreler\n
net	:	Ağ kartlarının bilgilerini getirir
cpu	:	İşlemci(ler)in bilgilerini getirir
ram	:	RAM(ler)in bilgilerinin getirir. Root yetkileri gereklidir
hdd	:	Harddisk(ler)in ve bölümlerinin bilgilerini getirir
h	:	Bu yardım metnini gösterir
yardim	:	Bkz. h
help	:	Bkz. h
""")
	else:
		print("Yanlış parametre")
