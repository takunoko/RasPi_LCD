# coding: utf-8
# IP$B%"%I%l%9$r<hF@$7$F(BLCD$B$KI=<($9$k!#(B

# import ip
import lip
import lcd
import sys

if __name__ == "__main__":
	lcd = lcd.i2clcd()
	ip = lip.get_lipadd('eth0')

	# IP$B%"%I%l%9$NI=<((B
	lcd.clear()
	lcd.setaddress(0, 0)
	lcd.puts('Local IP Address')

	ip_len = len(ip)
	lcd.setaddress(1, 16-ip_len)
	lcd.puts(ip)

	sys.exit()
