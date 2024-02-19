# struct MyPair:
#     var f:Int
#     var s:Int
#     fn __init__(inout self, f: Int, s: Int):
#         self.f = f
#         self.s = s
    
#     fn dump(self):
#         print(self.f, self.s)

# trait SomeTrait:
#     fn req_trait(inout self, x:Int):
#         pass

# struct SomeStruct(SomeTrait):
#     fn req_trait(inout self, x:Int):
#         print(x)

# fn fun_with_traits[T: SomeTrait](x: T):
#     x.req_trait(2)

# # fn use_traits():
# #     var tr = SomeStruct()
# #     fun_with_traits(tr)

# def main():
#     let my = MyPair(9,9)
#     my.dump()
#     fun_with_traits(SomeStruct())

#This example should work but it doesnt bcuz mojo ig 

trait Quackable:
    fn quack(self):
        ...

@value
struct Duck(Quackable):
    fn quack(self):
        print("Quack")

@value
struct StealthCow(Quackable):
    fn quack(self):
        print("Moo!")

fn make_it_quack[T: Quackable](x:T):
    x.quack()


fn main():
    make_it_quack(Duck())
    make_it_quack(StealthCow())