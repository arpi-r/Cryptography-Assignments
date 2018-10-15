f=open("caesar_cipher_text","r")
if f.mode=='r':
	contents=f.read()
f.close()
l=[0]*26
for i in range(len(contents)):
	x=ord(contents[i])
	if x>=97 and x<=122:
		l[x-97]=l[x-97]+1
shift=(l.index(max(l))-4)%26

plaintext=['']*len(contents)

for i in range(len(contents)):
	x=ord(contents[i])
	if x>=97 and x<=122:
		plaintext[i]=chr(int((x-97-shift)%26)+97)
	else:
		plaintext[i]=contents[i]
f=open("caesar_plain_text","w")
f.write(''.join(plaintext))
f.close()
print("done")



