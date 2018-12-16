def volume():
    volumes = [1,3,9,8,13,25,78,45,68,54,27,33,12,92,98,76,51,78,97,94,51,1232484,789]
    print(volumes)
    for x in volumes:
        if x>40:
            print("c'est trop fort")
        if x<10:
            print("c'est trop bas")
        else:
            print(str(x) + "c'est bon")
volume()