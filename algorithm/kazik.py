# https://www.magicweb.pl/programowanie/frontend/alternatywa-dla-if-else-oraz-switch/
#
# export const getBonus = (user) =>
# {
#     if (user.type == 'standard') {
#         // logika
#         return 10;
#     } else if (user.type == 'premium') {
#         // logika
#         return 20;
#     } else if (user.type == 'vip') {
#         // logika
#         return 30;
#     }
#     // logika default
#     return 0;
# }
#
# export const getBonus = (user) =>
# {
#     switch (user.type) {
#         case 'standard':
#             return getBonusStandardUserType(user);
#         case 'premium':
#             return getBonusPremiumUserType(user);
#         case 'vip':
#             return getBonusVipUserType(user);
#         default:
#             return getBonusDefaultUserType(user);
#     }
# }
#
# export const getBonus = (user) =>
# {
#     const conditions = {
#         standard: getBonusStandardUserType,
#         premium: getBonusPremiumUserType,
#         vip: getBonusVipUserType,
#         default: getBonusDefaultUserType
#     };
#     return ((user.type in conditions) ? conditions[user.type] : conditions.default)(user);
# }
#

class User:
    STANDARD = 'Standard'
    PREMIUM = 'Premium'
    VIP = 'Vip'
    def __init__(self, type=None):
        self.type = type


class Base:
    @staticmethod
    def get_bonus_standard_user_type(user):
        return 10

    @staticmethod
    def get_bonus_premium_user_type(user):
        return 20

    @staticmethod
    def get_bonus_vip_user_type(user):
        return 30

    @staticmethod
    def get_bonus_default_user_type(user):
        return 0

    def get_bonus(self, user):
        if user.type == 'standard':
            return __class__.get_bonus_standard_user_type(user)
        elif user.type == 'premium':
            return __class__.get_bonus_premium_user_type(user)
        elif user.type == 'vip':
            return __class__.get_bonus_vip_user_type(user)
        return __class__.get_bonus_default_user_type(user)


class Kazik(Base):
    def get_bonus(self, user):
        conditions = {User.STANDARD: __class__.get_bonus_standard_user_type,
                      User.PREMIUM: __class__.get_bonus_premium_user_type,
                      User.VIP: __class__.get_bonus_vip_user_type,
                      'default': __class__.get_bonus_default_user_type}
        return conditions[user.type](user) if user.type in conditions else conditions['default'](user)


# print('Kazik')
# print(Kazik().get_bonus(User(User.STANDARD)))
# print(Kazik().get_bonus(User(User.PREMIUM)))
# print(Kazik().get_bonus(User(User.VIP)))
# print(Kazik().get_bonus(User()))


class UserType:
    class Default:
        bonus = 0
        def annual(self, value):
            return (value * 12) + self.bonus

    class Standard(Default):
        bonus = 10

    class Premium(Default):
        bonus = 20
        def annual(self, value):
            return (value * 12) + (self.bonus*2)

    class Vip(Default):
        bonus = 30
        def annual(self, value):
            return ((value * 12) + self.bonus) * 2

    def __getattribute__(self, item):
        return self.item



class User:
    type: UserType
    def __init__(self, type: UserType = UserType.Default):
        self.type = type

class Armando:
    def get_bonus(self, user: User):
        return user.type.bonus
    def get_annual(self, user: User, value):
        func = getattr(user.type, 'annual')
        return func(value)

# print('Armando')
#
# print(Armando().get_bonus(User(UserType.Default())))
# print(Armando().get_annual(User(UserType.Default()), 50))
#
# print(Armando().get_bonus(User(UserType.Standard())))
# print(Armando().get_annual(User(UserType.Standard()), 100))
#
# print(Armando().get_bonus(User(UserType.Premium())))
# print(Armando().get_annual(User(UserType.Premium()), 200))
#
# print(Armando().get_bonus(User(UserType.Vip())))
# print(Armando().get_annual(User(UserType.Vip()), 500))




class UserType:
    class Default:
        def bonus(self):
            return 0
    class Standard:
        def bonus(self):
            return 10
    class Premium:
        def bonus(self):
            return 20
    class Vip:
        def bonus(self):
            return 30
    def bonus(self):
        return self.bonus()

class User:
    pass

def get_bonus(user):
    return getattr(user.type, 'bonus')()

user = User()
user.type = UserType.Premium()
print(get_bonus(user))
