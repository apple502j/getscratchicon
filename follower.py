import requests

def isUser(str):
	try:
		requests.get('https://api.scratch.mit.edu/users/' + str).id
		return True
	except:
		return False

try:
	sizedict={1:"90x90",2:"60x60",3:"55x55",4:"50x50",5:"32x32"}
	print("フォロワー画像一斉取得")
	username=input("ユーザー名を入力:")
	while isUser(username):
		username=input("ユーザー名を入力:")
	print("画像サイズ一覧")
	for i in sizedict:
		if i==0:
			continue
		print(str(i)+":"+sizedict[i])
	size=input("サイズを選択(1-5):")
	while int(size) not in sizedict:
		size=input("サイズを選択(1-5):")
	size=int(size)
	userinfo=requests.get('https://api.scratch.mit.edu/users/' + username + '/followers').json()
	for i in userinfo:
		image=requests.get(i['profile']['images'][sizedict[size]]).content
		file=open(i['username'] + '.png','wb')
		file.write(image)
		file.close()
	print('終了しました')

except KeyboardInterrupt:
	pass
except MemoryError:
	print("メモリ不足のため停止します。")
	pass
except:
	pass