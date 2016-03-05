# coding: utf-8
# IPアドレスを取得してLCDに表示する。

import sys
import time
import RPi.GPIO as GPIO

import lip
import gip
import lcd
import gpio

# mode:0 ローカル		IP
# mode:1 グローバル	IP
mode = 0

# GPIOに使うピン番号
IO_NO = 4

lip_add = "lIP Not init!!!"
gip_add = "gIP NOT init!!!"

# コールバック関数
def switch_callback(gpio_pin):
	time.sleep(0.03)
	if GPIO.input(gpio_pin) != 1:
		return

	# 正しいキーが押されてた際の処理
	global mode
	if mode == 1:
	        lip_add = lip.get_lipadd('eth0')
		show_ip('Local IP pi@', lip_add)
		mode = 0
	else:
	        gip_add = gip.get_ipadd()
		show_ip('Global IP pi@', gip_add)
		mode = 1

# IPアドレスの表示
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

	# 初回起動時はローカルIPを表示
	show_ip('Local IP pi@', lip_add)

	# 入力待ち
	gpio.wait_input()

	sys.exit()
