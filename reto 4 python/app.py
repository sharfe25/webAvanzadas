users = {
    "user1": {"password": "pass1", "level": "user"},
    "admin1": {"password": "pass2", "level": "administrator"},
    "superuser1": {"password": "pass3", "level": "superuser"}
}

def authenticateUser(func):
    def wrapper(username, password, *args, **kwargs):
        if username in users and users[username]["password"] == password:
            user_level = users[username]["level"]
            if user_level == "user":
                return func(username, *args, **kwargs)
            elif user_level == "administrator":
                return func(username, *args, **kwargs)
            elif user_level == "superuser":
                return func(username, *args, **kwargs)
        return "Unauthorized access."
    return wrapper

# Functions protected by authentication levels
@authenticateUser
def userFunction(username):
    return f"Welcome, {username} (user)!"

@authenticateUser
def adminFunction(username):
    return f"Welcome, {username} (administrator)!"

@authenticateUser
def superuserFunction(username):
    return f"Welcome, {username} (superuser)!"


def __init__():
    user = input("User: ")
    password = input("Password: ")
    print(userFunction(user, password))
    adminUser = input("Admin User: ")
    adminPassword = input("Password: ")
    print(adminFunction(adminUser, adminPassword))
    superUser = input("Super User: ")
    superPassword = input("Password: ")
    print(superuserFunction(superUser, superPassword))
    
__init__()
    
