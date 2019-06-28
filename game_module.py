#game module
import os
import threading
from colorama import Fore, Back, Style, init
init()

version = 1
rules = "Your goal is to earn 1000000@. Good luck,have fun.         (there is no save system)"
commands = ('/rules', '/help', '/buyw', '/clear', '/balance', '/b', '/stats', '/sellw')
status = 'beginner'
balance = 15
WorkerBots = 0
WorkerBotsSalary = 1

stats = '''
    WorkerBots: {0}
    Money: {1}@
    Status: {2}
'''.format(WorkerBots, balance, status)

def clear_console():
    os.system('clear')

print(Fore.CYAN + Back.BLACK)
clear_console()

def sell_w_bot():
    global WorkerBots
    global balance
    if WorkerBots >= 1:
        WorkerBots -= 1
        balance += 5

def add_w_bot():
    global WorkerBots
    global balance
    if balance > 5:
        WorkerBots += 1
        balance -= 5
    else:
        print('Not enough money')

def choise(us_input):
    if us_input == '/help':
        clear_console()
        print(commands)
    elif us_input == '/buyw':
        clear_console()
        add_w_bot()
        print("Your WorkerBots: {0}".format(WorkerBots))
    elif us_input == '/stats':
        clear_console()
        print(stats)
    elif us_input == '/clear':
        clear_console()
    elif us_input not in commands:
        clear_console()
        print('unknown command')
    elif us_input == '/sellw':
        clear_console()
        sell_w_bot()
        print('WorkerBots:{0}'.format(WorkerBots))
    elif us_input == '/balance' or '/b':
        clear_console()
        print(str(balance) + '@');

def Bots_earnings():
  threading.Timer(2.0, Bots_earnings).start()
  global balance
  global WorkerBots
  balance += WorkerBots * WorkerBotsSalary

Bots_earnings()

running = True
while running:
    if balance <= 0:
        print('You lose, no money let in your pocket')
        running = False
    elif balance > 0 :
        inp = raw_input('Terminal... ')
        choise(inp)
