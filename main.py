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
    
    Note: name your attack txt password.txt and move it into the Gorgonix-THC folder to use the program
    
    ''')
    options = input('Write your option: ')
    match options:
        case "1":
            print('You chose wifi option (Coming soon...)')

        #use selenium
        case "2":
            print('You chose instagram option')
            instagramUser = input('Username: @')
            try:
                with open("password.txt", "r", encoding="utf-8", errors="ignore") as file:
                    user_found = False
                    for line in file:
                        if instagramUser in line:
                            print('Your password is: ' + line.strip())
                            user_found = True
                            break
                    if not user_found:
                        print(f"The user's password was not found in your password.txt")
            except FileNotFoundError:
                print("password.txt is not found in the folder.")
            except Exception as e:
                print(f"Error: {e}")

        case "3":
            print('You chose gmail option (Coming soon...)')