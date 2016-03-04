# coding: utf-8
# Python からi2cでlcdを触ってみる。テスト

import smbus  # sudo apt-get install python-smbus
import time

class i2clcd:
	i2c = smbus.SMBus(1)
	addr = 0x3e
	contrast = 12		# 0~63  5Vで動作させる場合はあまり大きくしすぎると全て真っ黒になってしまう。

	def __init__(self):
		self.i2c.write_byte_data(self.addr, 0, 0x38)
		self.i2c.write_byte_data(self.addr, 0, 0x39)
		self.i2c.write_byte_data(self.addr, 0, 0x14)
		self.i2c.write_byte_data(self.addr, 0, (0x70 | (self.contrast & 0x0f)))		# コントラスト
		self.i2c.write_byte_data(self.addr, 0, (0x54 | ((self.contrast >> 4) & 0x03)))      # contrast/icon/power
		self.i2c.write_byte_data(self.addr, 0, 0x6c)    # follower control
		time.sleep(0.2)

	def clear(self):
		self.i2c.write_byte_data(self.addr, 0, 0x38)    # function set(IS=0)
		self.i2c.write_byte_data(self.addr, 0, 0x0C)    # Display On
		self.i2c.write_byte_data(self.addr, 0, 0x01)    # Clear Display
		self.i2c.write_byte_data(self.addr, 0, 0x06)    # Entry Mode Set
		time.sleep(0.2)

	def puts(self, msg):
		self.i2c.write_byte_data(self.addr, 0, 0x38)    # function set(IS=0)
		[self.i2c.write_byte_data(self.addr, 0x40, ord(c)) for c in msg]

	def setaddress(self, line, col):
		self.i2c.write_byte_data(self.addr, 0, 0x38)    # function set(IS=0)
		self.i2c.write_byte_data(self.addr, 0, 0x80 | (0x40 if line > 0 else 0) | col)

	def setcg(self, no, cg):
		self.i2c.write_byte_data(self.addr, 0, 0x38)    # function set(IS=0)
		self.i2c.write_byte_data(self.addr, 0, 0x40 | (no << 3))
		[self.i2c.write_byte_data(self.addr, 0x40, c) for c in cg]

	def putcg(self, line, col, no):
		self.setaddress(line, col)
		self.i2c.write_byte_data(self.addr, 0x40, no)

if __name__ == "__main__":
	lcd = i2clcd()
	lcd.clear()
	# show string
	lcd.setaddress(0, 0)
	lcd.puts('  Raspberry Pi')
	lcd.setaddress(1, 0)
	lcd.puts('AQM1602XA-RN-GBW')
