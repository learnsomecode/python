# python

alright so you wanna learn python. sweet. let's jump in

## variables
we can start with variable declaration

```python
name = "josh"
age = 16
rad = True
```

variables can be defined with `name = value`. variable names can't be shit like `$123$$YOYOFUCk` so don't try making it that. just use letters (and numbers if need be but don't start a variable with a number)

variable names that work:

- `name`
- `grade`
- `isSet` (use camelcase if you want more than one word in a variable)
- `func1`

variable names that don't work:

- ``!!!HEY`
- `8888888`
- ``~ffffffffffff`

there are different data types but right now there's 3 main ones we'll worry about:

1. strings (just a collection of characters. "josh" is a string, for example. numbers CAN be strings but we'll get into that later. strings are always surrounded by double quotes (""))
2. integers (a fucking integer. what did you think? 1 is an integer. integers are not surrounded by quotes or anything at all quite frankly)
3. booleans (a true or false value. `True` or `False`. There's no Maybe. don't surround booleans in quotes unless you want a string like "True" or some shit)

anyways hopefully you understand basic variable declaration. it's pretty simple to be quite honest

## basic functions
say you wanna log some text or whatnot

there are functions for this kind of thing and they're built into Python so you can EASILy use them!! functions are just words with ()  after them, so they're pretty easy to use. each function does something different and your job is to know what the functions you're using mean. `print()` is the function you'll use in python to log text. a **string** goes inside the () there. everything inside those () are called parameters. they're ways to pass extra information to a function. let's try it


```python
print("learning python!")
```

this will log "learning python!" how cool

you can also use variables with functions, if you hadn't already figured that out

```python
name = "josh"
print(name)
```

which will print out "josh"

this is super cool and we can now make complex python scripts


next how about if we want to print a string like "my name is josh and i am 16 years old"? we need string interpolation. what this means is just making a string and inserting variables into it.

you can do this a few ways

1. ugly way and don't do this. use `+` to concatenate strings
```python
name = "josh"
age = 16
print("my name is " + name + " and I am " + age + " years old")

that method sucks so some cool dudes over at python thought of some other ways

2. `.format()`
```python
name = "josh"
age = 16
println("my name is {} and i am {} years old".format(name, age))
```

as you can see we're using the format  function/method on our string. it takes two parameters (you can separate parameters with a comma). use `{}` as placeholders in your string and the format command will replace them accordingly. as you can see we're now using functions inside functions. you can really do this as deep as you'd like


alright so what you may have realized is the above code doesn't work. it'll throw an error because age is an integer. this is a problem because we're trying to add a number inside a string, which logically makes 0 sense. to fix this we have to manually convert our number into a string if we want to make it all a string with the `str()` method, which just takes an input and makes it a string

```python
name = "josh"
age = 16
println("my name is {} and i am {} years old".format(name, str(age)))
```

some languages do this for us but python does not. shrug


okay take a deep breath i've been rambling and i apologize . hopefully you understand what I've just explained. if not, email me angry passive aggressive shit

go get a glass of water and come back


## defining our own functions!!!

`print()` suck ass  and we want our own functions/methods now. in some languages you can create your own function with a `function` key. python uses the `def` key because they like to be difficult and different. actually `def` is for "define". defining a function is fairly easy. syntax is nice. `def` followed by a function name (same rules apply with this as with variables names (no names that start with dollar signs and shit)) followed by `():`

below this things get kinda weird. most languages use `{}` for nesting but python uses white space and indentation. i'll show you what i mean

```python
def runAroundInCircles():
  ## THIS IS CODE INSIDE THE FUNCTION

## THIS IS CODE OUTSIDE OF THE FUNCTION

```

see what i Mean? also, anything that has a pound sign (`#`) before it is a comment, meaning none of it is actually used, it's just for your own instructions.

anyways, inside a function you can define any other code you want and it'l be run when the function is run. say I wanted to greet someone a ton. we could make a function for that

```python
name = "josh"
age = 16
def greet():
  print("my name is {} and i am {} years old".format(name, age))

greet()
```

this'll output exactly what you think. you can call a function with the function's name followed by `()`, by the way. even if the function doesn't take parameters, you must define a function with brackets, as well as call it with brackets. kinda weird but it'll make sense later.

but say we wanted to run greeting like 5 times and each time we wanted the name and age to be different. would we make 5 different functions? that would be a waste of time. so just define the function with parameters and you're set

```python
def greeting(name, age):
  print("my name is {} and i am {} years old".format(name, age))

greeting("josh", 16)
```

see how that works? meaning you can define the skeleton of the function and get the values later and use them when calling the function. pretty sick i kno. :snowboarder: :100: ill af

yeah so that's the basics of functions.


## classes

THIS IS WHERE PROGRAMMING GETS GOOD. it's 12:40am right now and i'm tired so I'll add this later

SNEAK PEEK!!!

```python
class Person():
    def __init__(self, name, age):
      self.name = name
      self.age  = age
    def greeting(self):
      print("my name's {} and i'm {} years old".format(self.name, self.age))

josh = Person("Josh", 16)
josh.greeting() # my name's Josh and i'm 16 years old
```
