def botles():
    bottles = int(99)
    while bottles > 1:
        print(f"{bottles} , Bottles of Beer on the Wall.... 1 is down and, {bottles-1}, Are Left ... ")
        if bottles == 2:
            print(f"{bottles} , Bottles of Beer on the Wall.... 1 is down and, {bottles-1}, Are Left ... ")
        elif bottles == 1:
            print(f"{bottles} , Bottles of Beer on the Wall.... 1 is down and, {bottles-1}, is Left ... ")
        else :
            pass
        bottles-=1

botles()
    
