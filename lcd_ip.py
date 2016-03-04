# coding: utf-8
# IP$B%"%I%l%9$r<hF@$7$F(BLCD$B$KI=<($9$k!#(B

import sys
import time
import RPi.GPIO as GPIO

import lip
import gip
import lcd
import gpio

# mode:0 $B%m!<%+%k(B		IP
# mode:1 $B%0%m!<%P%k(B	IP
mode = 0

# GPIO$B$K;H$&%T%sHV9f(B
IO_NO = 4

lip_add = "lIP Not init!!!"
gip_add = "gIP NOT init!!!"

# $B%3!<%k%P%C%/4X?t(B
def switch_callback(gpio_pin):
	time.sleep(0.03)
	if GPIO.input(gpio_pin) != 1:
		return

	# $B@5$7$$%-!<$,2!$5$l$F$?:]$N=hM}(B
	global mode
	if mode == 0:
		show_ip('Local IP pi@', lip_add)
		mode = 1
	else:
		show_ip('Global IP pi@', gip_add)
		mode *= 0

# IP$B%"%I%l%9$NI=<((B
def show_ip(msg, ip):
	lcd.clear()
	lcd.setaddress(0, 0)
	lcd.puts(msg)

	ip_len = len(ip)
	lcd.setaddress(1, 16-ip_len)
	lcd.puts(ip)

if __name__ == "__main__":
	lcd = lcd.i2clcd()
	gpio.init_gpio(IO_NO, switch_callback)

	lip_add = lip.get_lipadd('eth0')
	gip_add = gip.get_ipadd()

	# $BF~NOBT$A(B
	gpio.wait_input()

	sys.exit()
