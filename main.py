import random, time, sys

MAX_NUM_SNAILS = 10
MAX_LEN_NAME = 20
FINISH_LINE = 40

print(' ' * 34, 'Snails Run')
while True:
  print('How many snails want to run? Max:', MAX_NUM_SNAILS)
  response = input()
  if response.isdecimal():
    num_snails = int(response)
    if num_snails > 1 and num_snails <= MAX_NUM_SNAILS:
      break
  print('Please enter a number betwen 2 and', MAX_NUM_SNAILS)
snails_names = []
for i in range(num_snails):
  while True:
    print('Enter name for snail №', i + 1)
    name = input()

    if len(name) > MAX_LEN_NAME or len(name) == 0:
      print('Enter valid name:', '(Please)')
    elif name in snails_names:
      print('Name already taken')
    else:
      break
  snails_names.append(name)
clean_string = '\n' * 40
print(clean_string)
print('START' + ' ' * (FINISH_LINE - len('START')) + 'FINISH')
print('|' + ' ' * (FINISH_LINE - 1) + '|')
snail_progress = {}
for name in snails_names:
  print(name)
  print('@v')
  snail_progress[name] = 0

time.sleep(1.5)
sleeping_SNAIL = None
sleep_count = 3
while True:
  if sleeping_SNAIL == None:
    if random.randint(1, 3) == 3:
      sleeping_SNAIL = random.choice(snails_names)
  else:
    sleep_count -= 1
  if sleep_count == 0:
    sleeping_SNAIL = None
    sleep_count = 3
  for snail_name in snails_names:
    if snail_progress[snail_name] == FINISH_LINE:
      print(snail_name, 'has WON!')
      sys.exit()
  for i in range(random.randint(1, num_snails // 2)):
    random_snail_name = random.choice(snails_names)
    if random_snail_name != sleeping_SNAIL:
      snail_progress[random_snail_name] += 1
  if 'MOBIK_CHEAT' in snail_progress:
    snail_progress['MOBIK_CHEAT'] += 1
  time.sleep(0.5)
  print(clean_string)
  print('START' + ' ' * (FINISH_LINE - len('START')) + 'FINISH')
  print('|' + ' ' * (FINISH_LINE - 1) + '|')
  for name in snails_names:
    spaces = snail_progress[name]
    if name != sleeping_SNAIL:
      print(' ' * spaces + name)
    else:
      print(' ' * spaces + 'z' * sleep_count)
    print('.' * spaces + '@v')

#77 79 66 73 75 95 67 72 69 65 84
console = 'ASCII'
#qwerty
#MOBIK_CHEAT
