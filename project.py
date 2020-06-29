
filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print (line.strip())
       line = fp.readline()
       cnt += 1