print('****welcome****')
x=bool(input("wanna paly game(yes or leave empty or no: ) "))
if x==True:
    started=False
    print('type help for commands')
    c=""
    while True:
        c=input("> ")
        if c=="start":
            if started:
                print('car alredy running')
            else:
                started=True
                print("car started,ready to go .....")
        if c=="stop":
            if not started:
                print('car is already stedy')
            else:
                started=False
                print("car stoped.....")
        if c=="quit":
            break
        if c=="help":
            print('''
start=start car.
stop=stop car.
quite=stop game.''')
        

else:
    print("so you are to busy to play huh")
