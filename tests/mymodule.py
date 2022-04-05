# Metodo que te devuelve una lista si ha reconocido personas en el frame, este te dara el bounding box de estas
def reconWalker(bounding_box):
    return len(bounding_box) > 0


# Metodo que te devuelve si una persona o un grupo ha entrado en la tienda o no y de salida te da el numero de personas que lo han hecho
def enterShop(client):
    return client.entran


# Metodo que te devuelve si una persona o un grupo ha miradodo el escaparate y de salida te da el numero de personas que lo han hecho
def stopByShop(client):
    return client.esperan


# Metodo que te devuelve si una persona o un grupo ha entrado al recibidor de la tienda y de salida te da el numero de personas que lo han hecho
def doNotEnterShop(client):
    return client.no_pasan


# Metodo que te devuelve cuantas personas han entrado y salido simultaneamente
def enterExitCrossing(frame):
    return enterShop(frame)


# Metodo que te devuelve cuantas personas han entrado, salido y vuelto a entrar
def enterExit(frame):
    return enterShop(frame) - 1


# Metodo que te devuelve cuantas personas han entrado y cuantas se han quedado en el escaparate
def enterStop(frame):
    return enterShop(frame), stopByShop(frame)


# Metodo que te devuelve cuantas personas han entrado a la tienda pero no han pasado hasta el final
def moveIn(frame):
    return doNotEnterShop(frame)


# Mira escaparate para se mueve y entra o se mueve sale mira escaparate y entra
def stopMoveEnter(frame):
    return enterShop(frame), stopByShop(frame), doNotEnterShop(frame)


# Metodo que te devuelve cuantas personas han mirado el escaparate, se han quedado en el recibidor y han salido
def stopMove(frame):
    return stopByShop(frame), doNotEnterShop(frame)
