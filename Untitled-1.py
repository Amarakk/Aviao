from graphics import *
import random

win = GraphWin('teste',500,500)
vml = Image(Point(50,100),'aviao1.png')
prt = Image(Point(50,300),'aviao2.png')
vml.draw(win)
prt.draw(win)
chegada1 = Line(Point(10,0),Point(10,500))
chegada2 = Line(Point(490,0),Point(490,500))
chegada1.draw(win)
chegada2.draw(win)
while True:
    mover1 = random.randint(1,5)
    mover2 = random.randint(1,5)
    vml.move(mover1,0)
    prt.move(mover2,0)
    x1=vml.getAnchor().getX()
    x2=prt.getAnchor().getX()

    if x1>490:
        texto=Text(Point(200,200),'jogador 1 ganhou')
        texto.draw(win)
        win.getMouse()
        win.close()
    if x2>490:
        texto=Text(Point(200,200),'jogador 2 ganhou')
        texto.draw(win)
        win.getMouse()
        win.close()

    key= win.checkKey()
    if key == 'space':
        x1=vml.getAnchor().getX()
        x2=prt.getAnchor().getX()
        vml.undraw()
        prt.undraw()
        vml = Image(Point(x1,100),'aviao1i.png')
        prt = Image(Point(x2,300),'aviao2i.png')
        vml.draw(win)
        prt.draw(win)
        while True:
            x1=vml.getAnchor().getX()
            x2=prt.getAnchor().getX()
            mover1 = random.randint(1,5)*-1
            mover2 = random.randint(1,5)*-1
            vml.move(mover1,0)
            prt.move(mover2,0)
            if x1<10:
                texto=Text(Point(200,200),'jogador 1 ganhou')
                texto.draw(win)
                win.getMouse()
                win.close()
            if x2<10:
                texto=Text(Point(200,200),'jogador 2 ganhou')
                texto.draw(win)
                win.getMouse()
                win.close()
            key= win.checkKey()
            if key == 'space':
                x1=vml.getAnchor().getX()
                x2=prt.getAnchor().getX()
                vml.undraw()
                prt.undraw()
                vml = Image(Point(x1,100),'aviao1.png')
                prt = Image(Point(x2,300),'aviao2.png')
                vml.draw(win)
                prt.draw(win)
                break
            time.sleep(1/60)
    time.sleep(1/60)

