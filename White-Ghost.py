import ipaddress
import subprocess
import platform
import sys

def ping_at(ip):
    # İşletim sistemine göre ping parametresi
    if platform.system().lower() == "windows":
        param = "-n"
    else:
        param = "-c"
    
    # Komutu çalıştır
    result = subprocess.run(
        ["ping", param, "1", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode == 0:
        print("✅ Ping başarılı!")
    else:
        print("❌ Ping başarısız!")

def ag_tara(network):
    result = subprocess.run(
        ["nmap", "-sn", network],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)

def port_tara(ip):
    result = subprocess.run(
        ["nmap", "-p-", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)
def os_tara(ip):
    result = subprocess.run(
        ["nmap", "-O", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)
def sv_tara(ip):
    result = subprocess.run(
        ["nmap", "-sV", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result.stdout)

# ---- IP DOĞRULAMA KISMI ----
print("""
            ----------------------------------
            |                                |
            |   WELCOME TO THE WHITE GHOST   |
            |                                |
            |  ( BEYAZ HAYALETE HOŞ GELDİN)  |
            |                                |
            ---------------------------------- 
      """)
while True:
    print("""
      -------------------- Menü --------------------
      |                                            |
      |  1) Ağ cihazlarını tara                    |
      |  2) ip Taraması Yap                        |
      |  3) Çıkış                                  |
      |                                            |
      ----------------------------------------------
      Not: Yapmak istediğiniz seçimin numarasını tuşlayınız. 
      """)

    secim = input("Seçim ypınız: ")
    if secim == "1":
       network = input("Ağ bloğunu girin (örn 192.168.1.0/24): ")
       ag_tara(network)
    elif secim == "2":
        while True:
            ip = input("IP adresi girin: ").strip()
            try:
                ipaddress.ip_address(ip)
                break
            except ValueError:
                print("❌ Hatalı IP! Lütfen tekrar deneyin.")
        while True:
            print("""
              -------------------- MENÜ --------------------
              |                                            |
              |  1) Ping At                                |
              |  2) Port Taraması                          |
              |  3) İşletim Sistemi Taraması               |
              |  4) Servis Versiyon Taraması               |
              |  5) Geri                                   |
              |  6) Çıkış                                  |
              |                                            |
              ----------------------------------------------
             """)
            secim2 = input("Seçim Ypınız: ")
            if secim2 == "1":
                ping_at(ip)
            elif secim2 == "2":
                port_tara(ip)
            elif secim == "3":
                os_tara(ip)
            elif secim2 == "4":
                sv_tara(ip)
            #elif secim == "5":
            elif secim2 == "6":
                sys.exit()
    elif secim == "3":
        sys.exit()