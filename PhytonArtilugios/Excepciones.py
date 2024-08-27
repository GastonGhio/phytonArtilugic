while 1==1:

    try:
        a=int(input("pon numero "))
        b=int(input("pon otro numero"))
        c = a/b
        break
    except ZeroDivisionError:
        print("nose puede dividir por 0")
    except ValueError:
        print("no se puede dididir por string")
    finally:
        print("siempre pasamos por aqui")    
    print("ultima linea")