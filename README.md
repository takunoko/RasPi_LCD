# Raspberry PI の起動時にLCDにいろいろ表示させよう

### 各ファイルの概要
- gip.py  
	グローバルIPを取得してくる

- lip.py  
	ローカルのIPを取得

- lcd.py	
	i2cを用いてLCDに表示するための関数

- gpio.py
	gpio(ボタン入力)を使うための関数

- lcd_ip.py
	ボタンの入力でグローバルIPとローカルIPを交互に表示してくれる。
	全体を結合したものって感じ。
