import base64
 #图文件lady.jpg，自行更改
picturepath= "th.png"      
f=open(picturepath,'rb')
#读取文件内容，转换为base64编
pbs64=base64.b64encode(f.read()) 
f.close()
#print(pbs64)
mf=open("bs64.txt","wb")
mf.write(pbs64)
mf.close

