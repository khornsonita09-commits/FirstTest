print("     Welcome to the Break Loop!")
print("        ====== Login ======")
name = input("Type your name: ")
password = input("Type your password: ")

print("        ======  CMD  ======")
while True:
    cmd = input("Enter command(or 'quit'): ")
    if cmd.lower() == "quit":
        print("Goodbye Besdong ")
        break
    print(f"Executing command: {cmd} ...")