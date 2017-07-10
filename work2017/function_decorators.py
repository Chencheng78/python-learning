# def p_decorate(func):
#    def func_wrapper(name):
#        return "<p>{0}</p>".format(func(name))
#    return func_wrapper
#
# @p_decorate
# def get_text(name):
#    return "lorem ipsum, {0} dolor sit amet".format(name)
#
# print get_text("John")
#
# # Outputs <p>lorem ipsum, John dolor sit amet</p>

#
# def square(func):
#     def func_wrapper(num):
#         return func(num)*func(num)
#     return func_wrapper
#
#
# @square
# def add_1(num):
#     return num + 1
#
#
# print add_1(7)


# def p_decorate(func):
#     def func_wrapper(*args, **kwargs):
#         return "<p>{0}</p>".format(func(*args, **kwargs))
#     return func_wrapper
#
#
# class Person(object):
#     def __init__(self):
#         self.name = "John"
#         self.family = "Doe"
#
#     @p_decorate
#     def get_fullname(self):
#         return self.name+" "+self.family
#
# my_person = Person()
# print my_person.get_fullname()

from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name

print get_text("John")

print get_text.__name__ # get_text
print get_text.__doc__ # returns some text
print get_text.__module__ # __main__