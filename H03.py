import turtle

#harjutus03.1
nimi = "Marten"
vanus = 19
pikkus = 1.90


print(nimi, ",", vanus,"aastat vana ja pikkus on", pikkus, "m")
# print(nimi+","+str(vanus)" on aastat vana ja pikkus on "+str(pikkus)+"m")
# print(nimi+, ",", +vanus+,"aastat vana ja pikkus on", +pikkus+, "m")

sihtkoht = "Haapsalu"
peavade_arv = 5
oobimise_hind = 100.50
kokku = peavade_arv * oobimise_hind
print(sihtkoht, "reis kestab", peavade_arv, "päevade ja maksab kokku", kokku,"€")

kylje_pikkus = 100
nurk = 90
kurjundi_varv = "blue"
x = 110
kordaja = x * 1.15
turtle.pencolor(kurjundi_varv)
for i in range(3):
    for i in range(4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    x = x * 2
    print(x)
    

turtle.done()