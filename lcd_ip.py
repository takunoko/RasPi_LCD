# coding: utf-8
# IPアドレスを取得してLCDに表示する。

# import ip
import lip
import lcd
import sys

if __name__ == "__main__":
	lcd = lcd.i2clcd()
	ip = lip.get_lipadd('eth0')

	# IPアドレスの表示
	lcd.clear()
	lcd.setaddress(0, 0)
	lcd.puts('Local IP Address')

	ip_len = len(ip)
	lcd.setaddress(1, 16-ip_len)
	lcd.puts(ip)

	sys.exit()
