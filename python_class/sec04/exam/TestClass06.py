#생성자와 소멸자를 살펴보자.
# 생성자를 명시하지 않으면 자동으로 내부호출되어 생성되고 명시하게 되면 명시된 생성자가 호출된다.
# 생성자는 단 한번 객체를 생성할 때 자동 호출되며 해당클래스의 모든 멤버를 [동적 할당 메모리로 로드 __new__] 하게 된다.
# 생성자의 목적은 멤버변수 초기화 [객체초기화] 에 있다.

class MyDel:
    def __init__(self, a=100):  #생성자   b=200
        self.a=a
        print("__ init__",a)

    def __del__(self):  #소멸자 , 객체가 소멸되는 시점에서 호출 되면서 리소스 해제(db 연결 해제, 파일 닫기등)
        print("나 소거된다. 현재 클래스에서 호출되거나 참조한 다른클래스를 멤버로 가질때  소거한다.  ")

if __name__ == '__main__':
    a1 = MyDel(200)  #MyDel이라는 클래스를 생성자를 호출하면서 객체 생성한다.
    print(a1.a)
    MyDel.a=10000   #
    #del(a1)
    b= MyDel()
    print(MyDel.a, a1.a )





