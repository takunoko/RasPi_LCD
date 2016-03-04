# coding: utf-8
# キー入力テスト
import RPi.GPIO as GPIO
import time

# コールバック関数
def switch_callback(gpio_pin):
	time.sleep(0.03)
	if GPIO.input(gpio_pin) != 1:
		return
	print("Push : " + str(gpio_pin))

# 入力を使うための初期化
def init_gpio(IO_NO, callback_func):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(IO_NO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(IO_NO, GPIO.RISING)
	GPIO.add_event_callback(IO_NO, callback_func)

# 入力待ち状態
def wait_input():
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()

# コールバックの定義
if __name__=="__main__":
	IO_NO = 4
	init_gpio(IO_NO, switch_callback)
	print("press ^C to exit program ...\n")

	wait_input()
	print("Program exit\n")
