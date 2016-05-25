"a demo module"

def print_b():
  "prints b"
  print('b')

def print_a():
  "prints a"
  print('I will print a')

#print_b() runs on import
print_b()


c = 2
d = 2


if __name__ == '__main__':
  #print_a() only executes when the module is run directly
  print_a()