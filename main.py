def print_hi(program):
    print(f'{program}')

if __name__ == '__main__':
    print_hi('''
    ------------------------------------------------------------------------------------------------------
    |                                                                                                    |
    |   ________                   ____                 .__             ___________ ___ ___  _________   |
    |  /  _____/   ____  _______  / ___\  ____    ____  |__|___  ___    \__    ___//   |   \ \_   ___ \  | 
    | /   \  ___  /  _ \ \_  __ \/ /_/  >/  _ \  /    \ |  |\  \/  /      |    |  /    ~    \/    \  \/  |
    | \    \_\  \(  <_> ) |  | \/\___  /(  <_> )|   |  \|  | >    <       |    |  \    Y    /\     \____ |
    |  \______  / \____/  |__|  /_____/  \____/ |___|  /|__|/__/\_ \      |____|   \___|_  /  \______  / |
    |         \/                                     \/           \/                     \/          \/  |                                                                                            
    |                                                                                                    |
    |                                                                                         by: Kotaka |
    ------------------------------------------------------------------------------------------------------

    1. Wifi (Coming soon...)
    2. Instagram
    3. Gmail (Coming soon...)
    ''')
    options = input('Write your option: ')
    match options:
        case "1":
            print('You chose wifi option (Coming soon...)')

        case "2":
            print('You chose instagram option')
            instagramUser = input('Username: @')
            try:
                with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as file:
                    user_found = False
                    for line in file:
                        if instagramUser in line:
                            print('Your username is: ' +  line.strip())
                            user_found = True
                            break
                    if not user_found:
                        print(f"Username '@{instagramUser}' not found in rockyou.txt.")
            except FileNotFoundError:
                print("O arquivo rockyou.txt não foi encontrado.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        case "3":
            print('You chose gmail option (Coming soon...)')