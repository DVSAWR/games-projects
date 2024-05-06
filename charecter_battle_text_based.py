import os

os.system('')


class Charecter:
    race = 'Human'

    def __init__(self,
                 name: str,
                 health: int):
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f'{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}')


class HealthBar:
    symbol_remaining: str = '█'
    symbol_lost: str = '_'
    barrier: str = '|'
    colors: dict = {'red': '\033[91m',
                    'green': '\033[92m',
                    'default': '\033[0m'}

    def __init__(self,
                 entity,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = ''):
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors['default']

    def update(self):
        self.current_value = self.entity.health

    def draw(self):
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f'\n{self.entity.name} HP: {self.entity.health}/{self.entity.health_max}')
        print(f'{self.barrier}'
              f'{self.color if self.is_colored else ""}'
              f'{remaining_bars * self.symbol_remaining}'
              f'{lost_bars * self.symbol_lost}'
              f'{self.colors["default"] if self.is_colored else ""}'
              f'{self.barrier}')


class Hero(Charecter):
    def __init__(self,
                 name: str,
                 health: int):
        super().__init__(name=name, health=health)

        self.health_bar = HealthBar(self, color='green')

    def equip(self, weapon):
        self.weapon = weapon


class Enemy(Charecter):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon):
        super().__init__(name=name, health=health)

        self.weapon = weapon
        self.health_bar = HealthBar(self, color='red')


class Weapon:
    def __init__(self,
                 name: str,
                 type: str,
                 damage: int,
                 value: int):
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value


# Weapon
fists = Weapon(name='Fists',
               type='Fists',
               damage=5,
               value=0)
iron_sword = Weapon(name='Iron sword',
                    type='Sword',
                    damage=20,
                    value=15)
short_bow = Weapon(name='Short bow',
                   type='Bow',
                   damage=11,
                   value=8)
# Characters
hero = Hero(name='HERO',
            health=100)
hero.equip(iron_sword)

enemy = Enemy(name='ENEMY',
              health=100,
              weapon=short_bow)

while True:
    os.system('cls')

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    if enemy.health_bar.current_value == 0:
        print(f'\n{hero.name} WIN')
        break

    if hero.health_bar.current_value == 0:
        print(f'\n{enemy.name} WIN')
        break

    input()
