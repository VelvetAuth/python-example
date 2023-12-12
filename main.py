from vauth import api
import getpass
import msvcrt
import os

def getpass_masked(prompt='Password: '):
    print(prompt, end='', flush=True)
    password = b''
    while True:
        char = msvcrt.getch()
        if char == b'\r' or char == b'\n':
            break
        elif char == b'\x08':  # Backspace
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    print()  # Move to the next line after password entry
    return password.decode('utf-8')

def watermark():
    os.system('cls')
    print('--> VelvetAuth Example <--')


VelvetAuth = api("program version", "program key", "encryption key")

VelvetAuth.ServerResponse()

watermark()

option = int(
    input('write your option : \n1) Login\n2) Register\n3) Activate\n4) All In One\n')
)

if option == 1:
    watermark()

    _user = input('username : ')

    watermark()

    #change getpass_maked to input if u want to show password
    _pass = getpass_masked('password : ')

    watermark()

    if VelvetAuth.LoginResponse(_user, _pass):
        user_data = VelvetAuth.user_data

        print(user_data.username)

        print(user_data.email)

        print(user_data.expires)

        print(user_data.var)

        print(user_data.rank)
    else:
        print(':ddd !!!')

elif option == 2:
    watermark()

    _user = input('username: ')

    watermark()

    _email = input('email: ')

    watermark()

    #change getpass_maked to input if u want to show password
    _pass = getpass_masked('password: ')

    watermark()

    _token = input('token: ')

    watermark()

    if VelvetAuth.RegisterResponse(_user, _email, _pass, _token):
        print('registered successfully!!')
    else:
        print(':(((')

elif option == 3:
    watermark()

    _user = input('username: ')

    watermark()

    _token = input('token: ')

    watermark()

    if VelvetAuth.UpdateResponse(_user, _token):
        print('activated successfully!!')
    else:
        print(':(((')

elif option == 4:
    watermark()

    _token = input('token: ')

    watermark()

    if VelvetAuth.ResponseKey(_token):
        user_data = VelvetAuth.user_data

        print(user_data.username)

        print(user_data.email)

        print(user_data.expires)

        print(user_data.var)

        print(user_data.rank)
    else:
        print(':ddd !!!')
else:
    print('not available option')
