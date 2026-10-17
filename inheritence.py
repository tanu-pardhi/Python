class M :
    def fun(self):
        print("i am tanu")
class N :
    def fun2(self):
        print("i am mrunali")
class H(M,N):
    def fun3(self):
            print("i am aastha")

m=M()
n=N()
h=H()
m.fun()
n.fun2()
h.fun3()
h.fun2()
h.fun()
    