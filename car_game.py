
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("stop the car")
    elif command == "help":
        print("""
start
stop
quit
        """)
    elif command == "quit":
        print("quit")
        break
    else:
        print("You didn't enter the right command")