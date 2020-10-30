import random

filename = "./headass_quotes.txt"

def parse_command(invoke_message):
  tokens = invoke_message.content.split(' ', 2)
  if len(tokens) == 1:
    print('arg: none, get quote')
    return get_quote()
  elif tokens[1] == 'add' and len(tokens) > 2:
    print('arg: add new quote')
    save_quote(tokens[2])
    return ''


def save_quote(quote):
  with open(filename, 'a+') as f:
    f.write(quote + '\n')

def get_quote():
  with open(filename, 'r+') as f:
    content = f.readlines()
    if len(content) == 0:
      return 'No quotes added yet'
    else:
      return random.choice(content)


