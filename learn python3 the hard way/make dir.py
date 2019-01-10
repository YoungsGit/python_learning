import os

def newfile(s):
	for i in range(1,s+1):
		path = 'lesson {}'.format(i)
		filename = path + '\\' + path +'.py'
		f = open(filename,'ab')
		testnote = '#coding=utf-8'
		f.write(testnote.encode('utf-8'))
		f.close()

if __name__ == '__main__':
	s = int(input('请输入数字：'))
	newfile(s)
		
