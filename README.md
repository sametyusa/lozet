# Lozet
Linux bilgisayarın donanım bilgilerini özetleyen script.
<p>Linux makinenin RAM, Hard disk, işlemci ve ağ donanımlarının bilgilerini birçok Linux dağıtımında entegre gelen programları kullanarak gösterir</p>
<p>Kullanılan programlar: lshw, grep, fdisk, lscpu, uname, df, ifconfig, lsblk, free, cut</p>
<p>Ubuntu Server 16.04 üzerinde test edildi</p>
# Kullanımı
lozet.py dosyasını indirdikten sonra çalıştırma izni verin<br>
<code>chmod u+x lozet.py</code> <br>
Scripti çalıştırmak için terminalde<br>
<code>./lozet.py</code> yazın.
# Parametreler
Parametre kullanmazsanız özet bilgi görürsünüz. Aynı anda bir parametre girilebilir
Örnek kullanım:<br>
<code>./lozet.py net</code>
## <code>net</code>
Ağ kart(lar)ının bilgilerini gösterir
## <code>cpu</code>
İşlemci(ler)in bilgilerini gösterir
## <code>ram</code>
Bellek(ler)in bilgilerini gösterir
## <code>hdd</code>
Sabit disk(ler) ve bölümlerinin bilgilerini gösterir
