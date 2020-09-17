import sys
print(sys.argv)

if (sys.argv[1] == 'runserver'):
    print('서버 구동')
else:
    print('끝')