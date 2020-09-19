try:
    print(a)
except:
    print("error occurred")

#catch specific error
try:
    print(c)
except NameError:
    print("name error")
except:
    print("Error")
finally:
    print("will execute always")

#raise exception
try:
    raise Exception("Some error happened")
except:
    print("catching the above error")

#type error
try:
    x = "hello"
    if not type(x) is int:
      raise TypeError("Only integers are allowed")
except:
    print("type error")

#get error message
import traceback
try:
    x = 10/0
except Exception as e:
    tb = traceback.format_exc()
    print(tb)
    print(str(e))
