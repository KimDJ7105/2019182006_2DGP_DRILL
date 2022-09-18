#파이썬에서 문자는 없다. 전부 문자열이다.
name = "Kim'dong"

#True와 False의 첫글자는 대문자로 써야한다.
a = True
b = False

#파이썬은 문자열 간의 합이 가능하다.
first = 'DongJae'
last = 'Kim'

name = first + '.' + last

#문자열과 상수의 곱도 가능하다.
#print(first * 3)

#문자열에 인덱스를 넣으면 해당 자리의 문자를 알 수 있다.
name[0]
name[3]

print(name[-1]) #인덱스가 음수이면 뒤에서 부터 확인한다.

#슬라이스 기능 name[start : stop : step]
name[0:3] #인덱스 0부터 3미만을 의미
name[-3:] #뒤에서 3번째부터 끝까지를 의미
name[3:] #3번째부터 끝까지를 의미
name[:] #문자열 전체를 의미
name[::2] #처음부터 끝까지 2간격에 있는 문자열을 의미
name[::-1] #문자열 전체를 반대로 출력

#파이썬의 자료형은 동적이다. 프로그램 실행중 실시간으로 변수형이 바뀔수 있다.
#hour = input("Enter Hour :")
hour = '154'
print(hour)
print(type(hour))

hour = int(hour)

print(hour)
print(type(hour))

#파이썬에서의 비교의 리턴값은 BOOL 타입이다. 연산자의 형태는 c언어와 같다.
#파이썬은 비교 연산을 문자열로도 사용 가능하다.

print("korea" == 'korea')

print("aa" > "ab")

#복합자료형
#list : 순서가 있는, 중복을 허용하는 데이터의 집합
[3,4,5,6,2,3,4,5,1,2,3,4]
name = ['kim','hyun','ho','lee']
node = ['holl', 'namd', 'level']
#type = list, len()을 통해 원소의 개수를 알 수 있다.
#리스트 이름. 하면 다양한 기능을 사용할 수 있다.
name.sort()
name.append('holy') #name 리스트에 holy 추가
name.remove('ho') #name 리스트에서 ho 제거
#리스트 + 리스트를 통해 두 리스트의 원소를 모두 가진 리스트를 만들수 있다.
plus = name + node
#리스트도 슬라이스 가능
trio = plus[:3]
del plus[-1] #제일 뒤의 원소를 삭제
#dictionary(map) : 검색을 위한 키를 갖는 데이터의 집합 즉, 키와 벨류의 쌍으로 이루어진 집합 벨류는 중복될 수 있지만 키는 중복될 수 없음.
#dictionary는 순서가 없는 자료구조이다.
dic = {'s' : 6, 'o' : 1, 't' : 2, 'f' : 4}
dic['s'] #6을 의미
dic['t'] #2를 의미
#원소의 추가 / 삭제도 가능
dic['se'] = 7 #se : 7을 추기
del dic['s'] #키 s를 갖는 원소를 삭제
#순서가 없기 때문에 정렬하려면 리스트 사용해야 한다.

#tuple 여러개의 값을 동시에 관리, 순서가 있고 중복이 가능하지만 한번 정해진 맴버 데이터를 바꿀수 없다.
#선언할 때는 소괄호를 사용하고 숫자원소 하나만 있을때는 int와 구분하기 위해 뒤에 ,를 붙인다. 괄호 생략 가능
t1 = (1,2,3)
t2 = (1, )
t3 = 1,2,3,4
#tuple간에 더하기와 상수의 곱은 가능하다. 슬라이스도 당연 가능
t1 + t2
t3 * 3
