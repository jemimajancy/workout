#!/usr/bin/python
import sys 

def main():
	if sys.argv[3]=="+":
		print int(sys.argv[1])+int(sys.argv[2])
	elif sys.argv[3]=="-":
		print int(sys.argv[1])-int(sys.argv[2])
	elif sys.argv[3]=="*":
		print int(sys.argv[1])*int(sys.argv[2])
	elif sys.argv[3]=="/":
		print int(sys.argv[1])/int(sys.argv[2])

if __name__=="__main__":
	main()
