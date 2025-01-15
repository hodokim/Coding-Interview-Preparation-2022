import sys
sys.stdin = open('testCase.txt', 'r')
input = sys.stdin.readline

first,second = map(int,input().split())

if first > second :
    print('>')
if first == second :
    print('==')
if(first < second):
    print('<')
    


