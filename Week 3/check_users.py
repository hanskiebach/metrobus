def check_users(current_users, new_users): 
    pass
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"Username is in use. Please enter a new username")
        else:
            print("Congratulations! This username is available")

if __name__ == "__main__":
    current_us = ['chris', 'haritha', 'sally' , 'darnell' , 'superman']
    new_us = ['george' , 'ringo' , 'superman' , 'hannibal', 'SUPERMAN']
    check_users(current_us, new_us)