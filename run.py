#!/usr/bin/env python3.6
from user import User
from credential import Credentials

def create_user(user_name,account,password):
    '''
    Function that create a new user
    '''
    new_user = User(user_name,account,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''    
    user.save_user()

# def generate_password();
#     '''
#     Function that generates a password
#     '''


def create_credential(account,username,account_password):
    '''
    Function that create a new credential
    '''   
    new_credential = Credentials(account,username,account_password)
    return new_credential

def save_credential(credential):
    '''
    Function that save credential
    '''   
    credential.save_credential()

def del_credential(credential):
    '''
    Function that delete credential 
    '''    
    credential.delete_credential()

def display_credential():
    '''
    Function that return all saved credential
    '''
    return Credentials.display_credential() 

def main():
    print("Hello Welcome to password locker. Insert your password ?....")
    print('\n')  

    while True:
                    print("use these short code: cc - create a new credential,dc - diplay credential") 

                    short_code = input().lower()

                    if short_code == "cc":
                        print("Create a Credential")
                        print("="*10)

                        print("account ...")
                        account = input()

                        print ("username ...")
                        username = input()

                        print (".account_password ...")
                        account_password = input()

                        save_credential(create_credential(account,username,account_password))
                        print('\n')
                        print(f"New Credential {account} {username} {account_password} created")
                        print('\n')
                    elif short_code == "dc":

                            if display_credential():
                                   print ("Here  are the list of all your credential")
                                   print('\n')

                                   for credential in display_credential():
                                         print(f"{credential.account} {credential.username} ...{credential.account_password} ")
                                   print('\n') 
                            else:
                                   print('\n')
                                   print("you credential have not been saved yet") 
                                   print('\n')        


if __name__ == '__main__':

    main()