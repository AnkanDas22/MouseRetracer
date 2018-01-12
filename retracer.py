import pyautogui
from msvcrt import getch

pyautogui.FAILSAFE=False
    #code for recording
while(True):
    i=0
    j=0
    x=[]
    y=[]
    m=int(input("Input number of maximum number of cursor position changes\n"))
    print("START MOVING THE MOUSE")
    while(j<=m):
        curX,curY=pyautogui.position()
        if(i==0):
            lastX=curX
            lastY=curY
            i=1
        if(curX!=lastX and curY!=lastY):
            x.append(curX-lastX)
            y.append(curY-lastY)
            j=j+1
            lastX=curX
            lastY=curY
            print(curX,curY)
        elif(curX!=lastX):
            x.append(curX-lastX)
            y.append(curY-lastY)
            j=j+1
            lastX=curX
            print(curX,curY)
        elif(curY!=lastY):
            x.append(curX-lastX)
            y.append(curY-lastY)
            j=j+1
            lastY=curY
            print(curX,curY)

    #for the delay before the retracing/drawing is done
    try:
        n=int(input("Enter the delay before drawing/retracing is started\nPress Enter if you want 50 as default\n"))
        for i in range(n):
            x.insert(i,0)
            y.insert(i,0)
    except ValueError:
        n=50
        for i in range(n):
            x.insert(i,0)
            y.insert(i,0)
    m=m+n
        #code for retracing
    j=0
    xx=input("Do you want to 'drag and draw' or just 'retrace path without click and draw'?\nEnter \"Drag/Draw/0\" for dragging and drawing\nOr, Enter \"Retrace/1\" for just retracing without drawing\n")
    xxx=input("Enter anything once you've put the cursor at the point you want to start!\n")
    try:
        if(xx=='0' or xx.upper()=='DRAG' or xx.upper()=='DRAW'):
            print("Dragging and drawing\n")
            for j in range(m+1):
                pyautogui.dragRel(x[j],y[j])
                
        if(xx=='1' or xx.upper()=='RETRACE'):
            print("Moving and retracing path\n")
            while(j<=m):
                pyautogui.moveRel(x[j],y[j])
                j=j+1
    except IndexError:
        pass
    print("The cursor retraced itself (hopefully) or drew something!\n")
    p=input("Wanna do it again?\nEnter 1/Yes for YES\nOtherwise, press Enter without typing anything\n")
    if(p=='1' or p.upper()=="YES"):
        pass
    else:
        break
print("Made by Ankan Das\n")
kek=input("Press 'Enter' key to exit\n")
