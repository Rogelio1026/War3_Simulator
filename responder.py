print(
"""I'm Yuhao Zheng
This is my first program
""")
x=input('Please Enter:')
try:
 if int(x)!=x:
  print ('This is a float')
 elif [int(x)==x]:
  print ('This is an integer')
except:
 print ('This is a string')
