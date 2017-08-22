#--------------------------------------------
#mohammad reza barazesh 91521059

#niaz be ketab khane pywin32 darad !
import win32gui

# in canvas khode safeye computer ast
canvas = win32gui.GetDC(0)
cmd = win32gui.FindWindow(None,r"C:\Windows\system32\cmd.exe")
#canvas 2 safeye cmd ast . in handle ba estefade az title window peida mishavad
canvas2 = win32gui.GetDC(cmd)

def draw(i,x,y):
    file = open(i)
    text = file.readlines()
    firstx=x
    for i in text :
        x=firstx
        for j in i :
            print(x,y)
            color = None
            if j == '*' :
                color = 0xff0000
            if j == '@' :
                color = 0x00ff00
            if j == '$' :
                color = 0x0000ff
            if j == '#' :
                color = 0xff00ff
            if color != None :
                for m in range(10):
                    for n in range(10) :
                        win32gui.SetPixel(canvas2,x+m,y+n,color)
            x += 10
        y+=10

#draw(file name , mokhtasat ) ke yek file matni ra dar mokhtasate dade shode chap mikonad

draw ("t.txt",0,0)
