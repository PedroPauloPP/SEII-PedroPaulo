message = "Hello World"
 print(message)
 print(message[6:])
 
 print(message.lower())
 print(message.upper())
 print(message.count("Hello"))
 
 print(message.find('World')) 
 
 newMessage = message.replace('World', 'Universe')
 
 greeting="Hello"
 name="Raquel"
 
 message = '{}, {}. Welcome!'.format(greeting, name)
 message = f'{greeting}, {name.upper()}. Welcome!'

print(dir(name)) 
print(help(str))