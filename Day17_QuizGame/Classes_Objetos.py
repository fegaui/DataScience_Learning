# como criar classes ex: modelo de usuários

#definir a classe:
class User:
    #definir o construtor
    def __init__(self, user_id, user_name):
        #inicializar atributos
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Felipe")
user_2 = User("002", "Isabela")         

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)