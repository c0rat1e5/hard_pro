def m():
  e = input
  a = ''
  for _ in[0] * int(e()):
    X, z = e(), []
    for y in e():
      s = i = 0
      for k in z:
        t = X.find(y, s) + 1
        if t < 1:
          break
        if t < k:
          z[i] = t
        s = k
        i += 1
      else:
        t = X.find(y, s) + 1
        if t:
          z += [t]
    a += f'\n{len(z)}'
  print(a[1:])
