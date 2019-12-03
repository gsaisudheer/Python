import sys
import random

def main():
	num=input("Enter the number of elements")
	print("The numbers will be selected randomly between 1 and 250 and then sorted")
	inputArray=[]
	for i in range(num):
		inputArray.append(random.randint(1,250))
	print("The input array generated is: ")
	print(inputArray)
	stoogeSort(inputArray,0,len(inputArray)-1)
	print("The sorted array is: ")
	print(inputArray)

def stoogeSort(l,i,j):
	if l[j] < l[i]:
		temp=l[j]
		l[j]=l[i]
		l[i]=temp
	if (j-i+1) >=3:
		t=(j-i+1)/3
		stoogeSort(l,i,j-t)
		stoogeSort(l,i+t,j)
		stoogeSort(l,i,j-t)
		print(l)

if __name__=='__main__': main()
