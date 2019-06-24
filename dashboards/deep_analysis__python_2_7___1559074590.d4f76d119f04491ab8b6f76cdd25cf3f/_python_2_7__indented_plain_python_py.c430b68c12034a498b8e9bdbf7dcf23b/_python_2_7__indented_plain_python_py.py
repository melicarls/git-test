def a(x):
  return x

def b(x):
  for i in range(2):
    if True:
      pass
    else:
      print('')
  print(a(x))
  print('bar')
  return 1

b('foo')

def c():
  print('baz')

c()

# expect-output-to-have: foo
# expect-output-to-have: bar
# expect-output-to-have: baz
