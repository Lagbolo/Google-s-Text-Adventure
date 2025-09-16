from sys import exit
import time
global commands
global inventory
global friends
global clues

commands = ('north', 'south', 'east', 'west', 'up', 'down', 'grab', 'why', 'inventory', 'use', 'help', 'exits', 'friends')

inventory = []

friends = ['\033[0;31mred o missing', '\033[0;31myellow o missing', '\033[0;31mblue g missing', '\033[0;31mgreen l missing', '\033[0;31mred e missing\033[0;0m']

clues = '''1. I am the beginning of everything, the end of everywhere. I'm the beginning of eternity, the end of time and space. What am I?
2. I am the loneliest number.
3. Check the clue number.
4. Take a number. Double it. Add 21. Subtract 15. Divide by 2. Subtract your original number.
5. To make this number even, you take the s out.'''

def Menu():
  print("Would you like to play a game? (yes/no)")
  while True:
    choice = input()
    if choice == 'yes':
      main()
    elif choice == 'no':
      print("The only winning move is not to play.")
      exit()
    else:
      print(f"{choice} not acceptable")

def get_choice(room, dir):
  if dir in ('n', 'north'):
    choice = 0
  elif dir in ('e', 'east'):
    choice = 1
  elif dir in ('s', 'south'):
    choice = 2
  elif dir in ('w', 'west'):
    choice = 3
  elif dir in ('u', 'up'):
    choice = 4
  elif dir == ('d', 'down'):
    choice = 5
  elif dir == 'grab':
    choice = 6
  elif dir == 'why':
    choice = 7
  elif dir == 'inventory':
    choice = 8
  elif dir == 'use':
    choice = 9
  elif dir == 'help':
    choice = 10
  elif dir == 'exits':
    choice = 11
  elif dir == 'friends':
    choice = 12
  elif dir in ('hi', 'hello'):
    choice = 13
  elif dir in ('e1337', 'E1337'):
    choice = 14
  else:
    return -1

  if choice in (0, 1, 2, 3, 4, 5):
    if room['directions'][choice] == 0:
      return -2
    else:
      return choice
  else:
    return choice

def exits(room):
  exits = []
  x = 0
  while x <= 5:
    if room['directions'][x] != 0 and room['directions'][x]:
      if x == 0:
        exits.append("north")
      if x == 1:
        exits.append("east")
      if x == 2:
        exits.append("south")
      if x == 3:
        exits.append("west")
      if x == 4:
        exits.append("up")
      if x == 5:
        exits.append("down")
      x += 1
    else:
      x += 1
  
  exits = sorted(exits)
  return print("Possible exits: " + ", ".join(exits))

def msg(room):
  if room['itemmsg'] != '' and room['obstaclesmsg'] != '':
    return print('\n' + room['msg'] + '\n' + room['itemmsg'] + '\n' + room['obstaclesmsg'] + '\n')
  elif room['itemmsg'] != '' and room['obstaclesmsg'] == '':
    return print('\n' + room['msg'] + '\n' + room['itemmsg'] + '\n' )
  elif room['itemmsg'] == '' and room['obstaclesmsg'] != '':
    return print('\n' + room['msg'] + '\n' + room['obstaclesmsg'] + '\n')
  elif room['itemmsg'] == '' and room['obstaclesmsg'] == '':
    return print('\n' + room['msg'] + '\n')
def movemsg(dir):
  print('\nYou move '+ dir)

def main():  
  room1 = {'name': '1', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room2 = {'name': '2', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room3 = {'name': '3', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room4 = {'name': '4', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room5 = {'name': '5', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room6 = {'name': '6', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room7 = {'name': '7', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room8 = {'name': '8', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room9 = {'name': '9', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room10 = {'name': '10', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room11 = {'name': '11', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room12 = {'name': '12', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room13 = {'name': '13', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''}
  room14 = {'name': '14', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room15 = {'name': '15', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room16 = {'name': '16', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room17 = {'name': '17', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room18 = {'name': '18', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room19 = {'name': '19', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room20 = {'name': '20', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room21 = {'name': '21', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room22 = {'name': '22', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room23 = {'name': '23', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room24 = {'name': '24', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room25 = {'name': '25', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room26 = {'name': '26', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room27 = {'name': '27', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room28 = {'name': '28', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room29 = {'name': '29', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room30 = {'name': '30', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room31 = {'name': '31', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room32 = {'name': '32', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room33 = {'name': '33', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room34 = {'name': '34', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room35 = {'name': '35', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room36 = {'name': '36', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  room37 = {'name': '37', 'directions': [], 'msg': '', 'items': [], 'itemmsg': '', 'obstacles': [], 'obstaclesmsg': '', 'solved': '', 'friends': ''} 
  
  room1['directions'] = [room2, 0, 0, 0, 0, 0]
  room2['directions'] = [room3, 0, room1, 0, 0, 0]
  room3['directions'] = [False, 0, room2, 0, 0, 0]
  room4['directions'] = [0, 0, room3, room5, 0, 0]
  room5['directions'] = [0, room4, room6, room7, 0, 0]
  room6['directions'] = [room5, 0, 0, room8, 0, 0]
  room7['directions'] = [0, room5, 0, room10, 0, 0]
  room8['directions'] = [0, room6, 0, False, 0, 0]
  room9['directions'] = [0, room8, 0, 0, 0, 0]
  room10['directions'] = [False, room7, room11, room12, 0, 0]
  room11['directions'] = [room10, 0, 0, 0, 0, 0]
  room12['directions'] = [0, room10, 0, room13, 0, 0,]
  room13['directions'] = [room18, room12, room17, room24, 0, 0]
  room14['directions'] = [0, room15, room10, 0, 0, 0]
  room15['directions'] = [0, room16, 0, room14, 0, 0]
  room16['directions'] = [0, 0, 0, room15, 0, 0]
  room17['directions'] = [room13, 0, 0, 0, room20, 0]
  room18['directions'] = [0, 0, room13, 0, room19, 0]
  room19['directions'] = [0, 0, 0, 0, room23, room18]
  room20['directions'] = [0, 0, 0, 0, room21, room17]
  room21['directions'] = [room23, 0, 0, 0, room20, room22]
  room22['directions'] = [0, 0, 0, 0, 0, room21]
  room23['directions'] = [0, 0, room21, 26, 0, room19]
  room24['directions'] = [0, room13, 0, room31, room25, 0]
  room25['directions'] = [0, 0, 0, 0, room26, room24]
  room26['directions'] = [0, room23, 0, 0, room27, room25]
  room27['directions'] = [0, 0, 0, 0, False, room26]
  room28['directions'] = [0, 0, 0, False, 0, room27]
  room29['directions'] = [0, room28, 0, room30, 0, 0]
  room30['directions'] = [0, room29, 0, 0, 0, 0]
  room31['directions'] = [0, room24, room32, 0, 0, 0]
  room32['directions'] = [room31, 0, room33, 0, 0, 0]
  room33['directions'] = [room32, 0, room36, room34, 0, 0]
  room34['directions'] = [0, room33, 0, False, 0, 0]
  room35['directions'] = [0, room34, 0, 0, 0, 0]
  room36['directions'] = [room33, 0, room37, 0, 0, 0]
  room37['directions'] = [room36, 0, False, 0, 0, 0]
  
  room1['msg'] = 'You see a statue of a metal man peeking out of a building.  A park is just across the street.'
  room2['msg'] = 'A sidewalk circles around a palm tree.'
  room3['msg'] = 'You see a large field with googlers playing ultimate frisbee and dodgeball.'
  room4['msg'] = 'A park opens up all around you with a small waterfall showing you a path west towards the campus.'
  room5['msg'] = 'The Google campus opens up before you. Colorful lawn chairs greet your passage, and a building on your left hosts an image of your likeness and all of your friends.'
  room6['msg'] = 'You are inside the Mercury building.  You spot a micro-kitchen and some open cubicles.'
  room7['msg'] = 'A T-rex skeleton towers over you and a beach volleyball court invites you to play.'
  room8['msg'] = 'You are greeted by a giant wall of jasmine.'
  room9['msg'] = 'You enter the Messenger cafe, the smell of sandwiches and popcorn in the air.'
  room10['msg'] = 'Two buildings hug the giant walkway and open up into a parking lot.'
  room11['msg'] = 'You find a small game room.'
  room12['msg'] = 'A bridge hovers over a shallow creek. A cute duck quacks at you.'
  room13['msg'] = 'Palm trees and corporate art occupy the concrete walkway between the 3 buildings.'
  room14['msg'] = 'You make your way into the Venus building.'
  room15['msg'] = 'A bridge allows you to cross from building to building. You see a gym lined with treadmills and weights.'
  room16['msg'] = "You've entered the Morning Star Cafe. A flurry of food choices inundates your senses and ability to make a choice."
  room17['msg'] = 'On your left you see a fake river comprised of rocks and on your right a piano. In fact, everything looks inviting except the elevators.'
  room18['msg'] = 'You enter the lobby of the Mars building and above you a slide slithers its way to your side.'
  room19['msg'] = 'You are on the 2nd floor. Exiting the elevator, you see the top of the slide. The temptation to ride it is very strong.'
  room20['msg'] = 'You are on the 2nd floor. Cubicles as far as the eye can see.'
  room21['msg'] = 'You are on the 3rd floor. You see a small micro-kitchen and a skybridge that will connect you to another building.'
  room22['msg'] = 'You are on the 4th floor. An empty room with a giant whale, whose belly serves as a couch, greets you.'
  room23['msg'] = 'You are on the 3rd floor of the Mars building. A graveyard of broken lava lamps sits in the middle of the floor.  A skybridge connects you to the other buildings.'
  room24['msg'] = 'You find a strange hallway with clean rooms and signs with drawings of hazmat suits on them.'
  room25['msg'] = 'The 2nd floor of the Saturn building.'
  room26['msg'] = 'You are on the 3rd floor of the Saturn building. You see a table with various jigsaw puzzles half finished. A skybridge connects you to a different building.'
  room27['msg'] = 'You are on the 4th floor. A mural of a violent green wave in the ocean greets your entrance.'
  room28['msg'] = 'You reach the top floor of the Saturn building.'
  room29['msg'] = 'You find a whiteboard filled with cartoonish drawings.'
  room30['msg'] = 'This is what you call the end of the hallway.'
  room31['msg'] = 'A beach volleyball court with a small sand castle in the middle grabs your attention.'
  room32['msg'] = 'You come upon a busy street full of self-driving cars zooming past you.'
  room33['msg'] = 'You enter a building to find a yet another gym on your right.'
  room34['msg'] = 'You see a sea of cubicles.'
  room35['msg'] = 'You find the massage room.'
  room36['msg'] = 'You enter a small cafeteria. People are standing around but no one is talking.'
  room37['msg'] = 'A boring, somewhat empty room.'
  
  room2['items'] = ['map']
  room6['items'] = ['banana peel']
  room11['items'] = ['fly swatter']
  room13['items'] = ['crocodile costume']
  room19['items'] = ["I'm Feeling Lucky sword"]
  room22['items'] = ['Shield of Android']
  room29['items'] = ['assortment of doodle stickers']
  
  room2['itemmsg'] = 'You see a map on a bench. Type "grab" to pick it up.'
  room6['itemmsg'] = 'You find a banana peel next to the compost bin. Clearly someone needs to work on their basketball skills.'
  room11['itemmsg'] = "You notice a fly swatter on someone's desk."
  room13['itemmsg'] = 'Laying in the middle of the path is a crocodile costume.'
  room19['itemmsg'] = "A ray of light reflects off a shiny metal object. You realize you have found the I'm Feeling Lucky sword."
  room22['itemmsg'] = 'The Shield of Android hangs on a wall.'
  room29['items'] = 'You find a bowl full of doodle stickers with a warning to take just one or two.'
  
  room3['obstacles'] = ['map']
  room8['obstacles'] = ['banana peel']
  room10['obstacles'] = ['crocodile costume']
  room27['obstacles'] = ["I'm Feeling Lucky sword"]
  room28['obstacles'] = ['Shield of Android']
  room34['obstacles'] = ['fly swatter']
  room36['obstacles'] = ['assortment of doodle stickers', 'banana', 'cup of quinoa', 'can of diet soda', 'latte']
  room37['obstacles'] = ['e1337']

  room3['obstaclesmsg'] = 'A horde of lost nooglers (new googlers) surrounds you and asks how to get around. Type "use" to give them your map to help them out.'
  room8['obstaclesmsg'] = 'A cute robot dog paces back and forth, clearly guarding a door.'
  room10['obstaclesmsg'] = 'An alligator blocks the building to the north.'
  room27['obstaclesmsg'] = 'You are greeted by one of the ferocious twin ghouls, Precision.'
  room28['obstaclesmsg'] = 'A sad, grieving spirit of Recall blocks your way as it mourns its twin.'
  room34['obstaclesmsg'] = 'You find a frustrated ground of engineers trying to solve a bug.'
  room36['obstaclesmsg'] = "You land on a over caffeinated googler with a glass of water, a grumpy engineer holding a latte, the vice president of some product you don't recognize with a diet coke in her hands, a happy noogler amazed that the micro-kitchen even offers quinoa, and an excited intern holding a banana."
  room37['obstaclesmsg'] = 'You come upon a giant lockbox with an alphanumeric keypad which could easily fit a missing letter.'

  room9['friends'] = 'red e'
  room16['friends'] = 'green l'
  room30['friends'] = 'yellow o'
  room35['friends'] = 'blue g'
  
  room = room1
  counter = 0
#---------------------------------------------------------  
  def use(room):
    if room['name'] == '3':
      room['directions'][0] = room4
      room['solved'] = '''\nYou give the map to the horde of nooglers.
They gratefully accept the map.  Now that they know where to go they immediately leave. You, on the other hand, feel a bit lost.

An exit appears towards the north.\n''' 
    elif room['name'] == '8':
      room['directions'][3] = room9
      room['solved'] = '''\nYou strategically drop the banana peel on the robot dog's path.
The robot dog walks unknowingly towards the banana peel.  Its foot slips and its circuitry shuts down in response.  It lays on its side, happily wagging its robot tail.

An exit appears towards the west.\n'''
    elif room['name'] == '10':
      room['directions'][0] = room14
      room['solved'] = '''\nYou put on the crocodile costume and say, "See you later alligator."
The alligator looks up at you and replies, "after a while crocodile" and walks away.

An exit appears towards the north.\n'''
    elif room['name'] == '27':
      room['directions'][4] = room28
      room['solved'] = '''\nYou strike Precision with the I'm Feeling Lucky sword.
The sword strikes Precision and the magical incantation for luck bursts like a grenade of light through the ghoul.

A ladder drops from the ceiling leading towards the top floor.\n'''
    elif room['name'] == '28':
      room['directions'][3] = room29
      room['solved'] = '''\nYou bash recall with the Shield of Android.
The broad side of the shield manages to hit most of the ghoul.  Its screeches in pain and vanishes before your eyes.
    
An exit appears towards the west.\n'''
    elif room['name'] == '34':
      room['directions'][3] = room35
      room['solved'] = '''\nYou smack the monitor with the fly swatter.
The screen shows static for a second and reverts back.  The distraction allows an engineer to see something they didn't before.  They fix the bug and answer your question about your missing buddy.

An exit appears towards the west.\n'''
    elif room['name'] == '36' and len(room['obstacles']) == 4:
      room['solved'] = '''\nYou ask to trade for your doodle stickers.
The intern is so excited about the stickers she immediately gives you her banana.  You wonder what you can trade for this?\n'''
      inventory.append('banana')
      room['obstaclesmsg'] = '''You land on a over caffeinated googler with a glass of water, a grumpy engineer holding a latte, the vice president of some product you don't recognize with a diet coke in her hands, and a happy noogler amazed that the micro-kitchen even offers quinoa.'''
    elif room['name'] == '36' and len(room['obstacles']) == 3:
      room['solved'] = '''\nYou ask to trade for your banana.
The noogler admits he doesn't even know what quinoa is and gratefully accepts your banana.\n'''
      inventory.append('cup of quinoa')
      room['obstaclesmsg'] = '''You land on a over caffeinated googler with a glass of water, a grumpy engineer holding a latte, and the vice president of some product you don't recognize with a diet coke in her hands.'''
    elif room['name'] == '36' and len(room['obstacles']) == 2:
      room['solved'] = '''\nYou suggest water and quinoa to the VP.  Her eyes clearly show you've taken away a moment of respite, but the truth of your statement convinces her to give up the diet soda.\n'''
      inventory.append('can of diet soda')
      room['obstaclesmsg'] = 'You land on a over caffeinated googler with a glass of water and a grumpy engineer holding a latte.'
    elif room['name'] == '36' and len(room['obstacles']) == 1:
      room['solved'] = '''\nYou ask to trade for your diet soda.
"You found the last one!", the grumpy engineer no longer looks so frustrated and puts down the latte with a beautiful flower made out of foam for the diet soda.\n'''
      inventory.append('latte')
      room['obstaclesmsg'] = 'You land on a over caffeinated googler with a glass of water.'
    elif room['name'] == '36' and len(room['obstacles']) == 0:
      room['solved'] = '''\nYou ask to trade for your latte.
The over caffeinated googler gladly accepts your latte. "Thank you for the latte, I hear you are looking for your friend.  I'll only tell you this once."\n'''
      inventory.append('sticky note with some clues on it')
      print(clues)
    return print(room['solved'])
#-------------------------------------------------
  time_start = time.time
  print("""
Type single word commands, no need to describe the subject. For example, "grab banana peel" should just be "grab" or "use banana peel" should just be "use".

Commands: north, south, east, west, up, down, grab, why, inventory, use, help, exits, and friends.

A strange tingle trickles across your skin. You feel lightheaded and sit down. Feeling better you stand up again and notice your reflection in a window. You are still the same big blue G you've always been and you can't help but smile.

But wait! Where are your friends \033[0;31mred o\033[0;0m, \033[0;37;43myellow o\033[0;0m, \033[0;34mblue g\033[0;0m, \033[0;32mgreen l\033[0;0m, and the always quirky \033[0;31mred e?\033[0;0m""")
  msg(room)
  exits(room)
#----------------------------------------------------
  while True:    
    if friends == ['\033[0;32mred o found', '\033[0;32myellow o found', '\033[0;32mblue g found', '\033[0;32mgreen l found', '\033[0;32mred e found\033[0;0m']:
      time_end = time.time
      print(f'''Congratulations on winning the game!
It took {counter} actions and {time_end - time_start} seconds.
You quacked 0 times.
Now get back to work.''')
      exit()
    deciding = True
    while deciding:
      dir = input()
      choice = get_choice(room, dir)
      if choice == -2:
        print(f"Failed to move {dir}")
      elif choice == -1:
        print('Invalid input')
      elif choice == 6:
        if room['items'] != []: 
          inventory.append(room['items'][0])
          room['items'] = []
          room['itemmsg'] = ''
        print("\nInventory: ")
        i = 0
        while i < len(inventory):
          print(inventory[i])
          i+=1
        print()
      elif choice == 7:
        print("why? one is the loneliest number")
      elif choice == 8:
        print("\nInventory: ")
        i = 0
        while i < len(inventory):
          print(inventory[i])
          i+=1
        print()
      elif choice == 9:
        if inventory != []:  
          for x in inventory:
            for y in room['obstacles']:
              if any(x) == any(y):
                inventory.remove(x)
                room['obstacles'].remove(x)
                room['obstaclesmsg'] = ''
                use(room)
                print("\nInventory: ")
                i = 0
                while i < len(inventory):
                  print(inventory[i])
                  i+=1
                print()
                exits(room)
              elif 'sticky note with some clues on it' in inventory:
                print(clues)
        else:
          print("\nYou are not sure that will do much right here.\n")    
      elif choice == 10:
        print("""Type single word commands, no need to describe the subject. For example, "grab banana peel" should just be "grab" or "use banana peel" should just be "use"
  Commands: north, south, east, west, up, down, grab, why, inventory, use, help, exits, and friends.
  """)
      elif choice == 11:
        exits(room)
      elif choice == 12:
        print('Friends:\n')
        i = 0
        while i < len(friends):
          print(friends[i])
          i += 1
        print()
      elif choice == 13:
        print('No one responds to your greeting.  You have a sinking feeling that you are not in control of your actions.')
      elif choice == 14:
        if room['name'] == '37':
          room['obstacles'] = []
          room['obstaclesmsg'] = ''
          room['solved'] = '''You finally google search all the clues and sure enough the lockbox opens.'''
          print(room['solved'])
        else:
          print("I get it, you're not a noob, but enough with the l33t speak.")
      else:
        counter += 1
        movemsg(dir)
        room = room['directions'][choice]
        msg(room)
        exits(room)
        deciding = False
#--------------------------------------------------------------------
    if room['friends'] != '' and room['obstacles'] == []:
      if room['friends'] == 'red o':
        friends[0] = '\033[0;32mred o found'
        room['friends'] = ''
        print('You found red o!')
      elif room['friends'] == 'yellow o':
        friends[1] = '\033[0;32myellow o found'
        room['friends'] = ''
        print('You found yellow o!')
      elif room['friends'] == 'blue g':
        friends[2] = '\033[0;32mblue g found'
        room['friends'] = ''
        print('You found blue g!')
      elif room['friends'] == 'green l':
        friends[3] = '\033[0;32mgreen l found'
        room['friends'] = ''
        print('You found green l!')
      elif room['friends'] == 'red e':
        friends[4] = '\033[0;32mred e found\033[0;0m'
        room['friends'] = ''
        print('You found red e!')
      print('Friends:\n')
      i = 0
      while i < len(friends):
        print(friends[i])
        i += 1
#----------------------------------------------
Menu()