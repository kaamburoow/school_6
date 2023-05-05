import hashlib

print("Здравей!")
myPass=str("52d0ad01b41ce3b690d4152e4689df3fd51d778df4c1431607ad1ed8424a9e04c0e69f3fcff0413487a3ab1fc3d32082ae69bd7091fb75c2aa0f07c99dd12152")
name=input("Как се казваш? ")
pswd=input("Каква е твоята парола? ")
pswdEncrypted0=str(hashlib.md5(pswd.encode()).hexdigest())
pswdEncrypted1=str(hashlib.sha1(pswdEncrypted0.encode()).hexdigest())
pswdEncrypted2=str(hashlib.sha256(pswdEncrypted1.encode()).hexdigest())
pswdEncrypted3=str(hashlib.sha384(pswdEncrypted2.encode()).hexdigest())
pswdEncrypted4=str(hashlib.sha512(pswdEncrypted3.encode()).hexdigest())
if(pswdEncrypted4 == myPass):
    print("Здравей, " + name.capitalize() + "!")
else:
    print("Грешна парола!")
