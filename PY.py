#DAY1 
#출력과 변수
#출력은 priunt() 함수를 사용한다.
print("Hello World") #Hello World 출력

#변수는 데이터를 저장하는 공간이다.
name = "JAY" #문자열 변수 name에 "JAY" 저장
print(name) #변수 name의 값을 출력  

#변수 이름의 규칙
#1. 변수 이름은 문자, 숫자, 밑줄(_)로 구성될 수 있다.
#2. 변수 이름은 숫자로 시작할 수 없다.
#3. 변수 이름은 대소문자를 구분한다.
#4. 변수 이름은 예약어를 사용할 수 없다.

# 1example = "Hello" 숫자로 시작하는 변수 이름은 안된다.
example1 = "Hello" #올바른 변수 이름
print(example1) 

#기본 데이터 타입
#1. 정수형(int): 정수를 저장하는 데이터 타입
#2. 실수형(float): 소수를 저장하는 데이터 타입
#3. 문자열형(str): 문자를 저장하는 데이터 타입
#4. 불린형(bool): 참(True)과 거짓(False)을 저장하는 데이터

print(type(10)) #정수형
print(type(3.14)) #실수형
print(type("Hello")) #문자열형
print(type(True)) #불린형

#타입 변환
#1. int(): 정수형으로 변환
#2. float(): 실수형으로 변환
#3. str(): 문자열형으로 변환
A = 3.7
print(int(A)) #내림하여 정수형으로 변환

A = -1
print(bool(A)) #0이 아닌 모든 숫자는 참(True)으로 변환
A = 1
print(bool(A)) #0이 아닌 모든 숫자는 참(True)으로 변환
A = 0
print(bool(A)) #0은 거짓(False)으로 변환

#DAY2 
#리스트
list1 = [] #리스트 생성
print(list1) #빈 리스트 출력
list1 = list() #문자열을 리스트로 변환
print(list1) #빈 리스트 출력  

#리스트안에 리스트도 넣을 수 있다
list2 = [1, 2, 3, [4, 5]] #리스트 안에 리스트
print(list2) #리스트 출력

#.append() 메서드: 리스트에 요소 추가
list1 = [1, 2, 3] #리스트 생성
list1.append(4) #리스트에 요소 추가
print(list1) #리스트 출력

#sort() 메서드: 리스트를 오름차순으로 정렬
list1 = [3, 1, 2] #리스트 생성
list1.sort() #리스트 정렬
print(list1) #정렬된 리스트 출력

#sort(reverse=True) 메서드: 리스트를 내림차순으로 정렬
list1 = [3, 1, 2] #리스트 생성
list1.sort(reverse=True) #리스트 내림차순 정렬
print(list1) #내림차순으로 정렬된 리스트 출력

#sorted() 함수: 리스트를 정렬하여 새로운 리스트 반환
list1 = [3, 1, 2] #리스트 생성
print(sorted(list1)) #정렬된 새로운 리스트 출력
print(list1) #원래 리스트는 변경되지 않음
print(sorted(list1, reverse=True)) #내림차순으로 정렬된 새로운 리스트 출력

#reverse() 메서드: 리스트의 요소 순서를 반대로 뒤집음
list1 = [1, 2, 3] #리스트 생성
list1.reverse() #리스트 요소 순서 뒤집기
print(list1) #뒤집힌 리스트 출력

#len() 함수: 리스트의 길이(요소의 개수)를 반환
list1 = [1, 2, 3] #리스트 생성
print(len(list1)) #리스트의 길이 출력

#insert() 메서드: 리스트의 특정 위치에 요소 삽입
list1 = [1, 3] #리스트 생성
list1.insert(1, 2) #인덱스 1에 요소

#remove() 메서드: 리스트에서 특정 요소 제거
list1 = [1, 2, 3] #리스트 생성
list1.remove(2) #리스트에서 요소 2 제거
print(list1) #요소 2가 제거된 리스트 출력

#pop() 메서드: 리스트에서 마지막 요소 제거 및 반환
list1 = [1, 2, 3] #리스트 생성
list2 = list1.pop(2) #리스트에서 인덱스 2의 요소 제거
print(list1) #마지막 요소가 제거된 리스트 출력
print(list2) #제거된 요소 출력

#count() 메서드: 리스트에서 특정 요소의 개수 반환
list1 = [1, 2, 2, 3] #리스트 생성
print(list1.count(2)) #리스트에서 요소 2의 개수 출력

#extend() 메서드: 리스트에 다른 리스트의 요소 추가
list1 = [1, 2] #리스트 생성
list1.extend([3, 4]) #리스트에 다른 리스트의 요소 추가
print(list1) #확장된 리스트 출력
# + 연산자: 리스트를 연결하여 새로운 리스트 생성
list1 = [1, 2] #리스트 생성
print(list1 + [3, 4]) #리스트를 연결하여 새로운 리스트 출력
print(list1) #원래 리스트는 변경되지 않음





