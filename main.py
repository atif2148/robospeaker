import os

if __name__ == '__main__':
    print("Welcome to robo speaker 1.0.0, Developed by Atif Riaz")
    while True:
        userinput = input("Enter what you want me to speak: ")
        if userinput == "q":
            os.system("Say 'Have a good day!'")
            break
        command = f"say {userinput}"
        os.system(command)
