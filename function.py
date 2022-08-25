def say_hi():
    print("hello")

say_hi()

def pack(clothes):
    for x in clothes:
        print(x)
clothes = ["Hat", "Shirt", "Pants"]

pack()

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

eat_lunch(["sandwich", "chips"])
eat_lunch([])