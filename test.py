users = open('user.txt', 'r', encoding='utf-8')
users = users.read().split('\n')
print(users)