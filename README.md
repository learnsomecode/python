# python

tutorials
---------

http://www.learnpython.org/

my tutorial
-----------

alright so you wanna learn python. sweet. let's jump in

## quick terminology (I'll add more as I go)
- mutable: editable/changeable
- immutable: not editable/not changeable

## variables
we can start with variable declaration

```python
name = "josh" # strings
age = 16 # numbers
rad = True # booleans
things = (1, 2, 3) # tuples
groceries = ['eggs', 'milk', 'bread', 'the stolen dead souls of those whom I encapsulate'] # lists
b = {'thing': 1, 'thinnnn': 'k'} # dictionaries
```

variables can be defined with `name = value`. variable names can't be shit like `$123$$YOYOFUCk` so don't try making it that. just use letters (and numbers if need be but don't start a variable with a number)

variable names that work:

- `name`
- `grade`
- `isSet` (use camelcase if you want more than one word in a variable)
- `func1`

variable names that don't work:

- `!!!HEY`
- `8888888`
- `~ffffffffffff`

there are different data types

1. strings (just a collection of characters. "josh" is a string, for example. numbers CAN be strings but we'll get into that later. strings are always surrounded by double quotes ("")). strings are mutable.
2. integers (a fucking integer. what did you think? 1 is an integer. integers are not surrounded by quotes or anything at all quite frankly). integers are mutable.
3. booleans (a true or false value. `True` or `False`. There's no Maybe. don't surround booleans in quotes unless you want a string like "True" or some shit). booleans are mutable.
4. arrays are just a box filled with things. strings, numbers, booleans. whatever, it can be anything (in python!!). everything you add gets a number as a sort of label, and it's sort of like a lineup. numbers start at 0 (not 1!!). the first object is #0, then #1, then #2, and so on. this is how pretty much every language does things. indexing af. arrays are mutable.
5. tuples are, for the most part, just immutable arrays. just think of them like that. tuples are immutable.
6. dictionaries are just arrays with strings as labels instead of numbers. this makes things easier in some cases.

### using variables
```python
name = "josh" # strings (you can comment something out with the # sign)
name = "joe" # we can reassign strings too. they're mutable
age  = 16 # assigning variables to numbers works good ((:
isTired = True # variables can be assigned to booleans (True/False)
things = ['bbbbb', 11111, False] # Defining a list
things[0] = 'aaaahahaha' # Changes the first ([0]) object to string "aaaahahaha"
josh = {'name':name, 'age':age, 'tired':isTired, 'location': 'Vancouver, BC'} # Assigning dictionaries which use key values
josh['age'] = 10 # I'm 10 now, and this works because dictionaries are mutable
pants = ('straight', 'skinny', 'boot cut') # Defining a tuple (you can use () if you want)
pants[0] = 'funky' # Returns error: TypeError: 'tuple' object does not support item assignment
```

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
```

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
greeting("adam", 72)
```

see how that works? meaning you can define the skeleton of the function and get the values later and use them when calling the function. pretty sick i kno. :snowboarder: :100: ill af

yeah so that's the basics of functions.


## classes

THIS IS WHERE PROGRAMMING GETS GOOD.

alright so think over how functions work and how they could be useful. you can use them to do a set of tasks pretty quickly, but what if we wanted to make something like a character that has a list of functions (walk, run, jump) and we wanted that character to have different traits (speed, jumpHeight) etc. and say we had 5 characters. this means we have to create separate functions for 5 characters. that's cumbersome. so we have classes and objects instead.

think of classes like a blueprint. most programming tutorials say that so I'll do with it.

once you've defined a class you want to create a variable that has those attributes and functions (methods), so we can assign it like any other variable in python.

defining a class is pretty simple. it goes by the same syntax as defining a function except use `class` instead of `def`. inside the class definition we can define things like variables and functions that our object will get. let me make an example.

```python
class Person():
  name = "josh"
  age = 16
  def info(self):
    print("{} is {} years old".format(self.name, str(self.age)))
  def jump(self):
    print("{} jumped!".format(self.name))

josh = Person()
josh.jump()
```

when we assign `josh = Person()` (remember the `()`) we're creating what's called an instance of the class. `josh` is now our object to work with.

you're probably wondering what the `self` thing is though. it's gonna be weird explaining this (it always is the first time) but hopefully you get the hang of it.

### self
`self` is essentially what refers to the object. `self.name` in a class refers to the name variable of itself. not the class, but the instance. hopefully this is making sense. python automatically throws `self` into each parameter inside a class' functions/methods (call them methods if they're inside a class, functions if they're not). we still have to explicitly add `self` to our parameters anyways, though. don't ask me why.

also when you use a function from a class you use the dot notation (`instance.method()`) (always remember `()` on functions/methods!)

hopefully you understand the block of code above now. let's get into shit like `__init__()`

### __init__()

`__init__()` is one hell of a method. it's defined already in python. you throw it in any class and it automatically runs when an instance is created. meaning if we defined a print statement inside `__init__()`, it would run once we go `josh = Person()`, or whatever the variable and class are. printing text on instantiating (creating an instance) isn't too helpful, though. what we want to do here is usually throw parameters into variables we can use in the class.

so say you wanted to define a Person class but you don't want to define the name of the person yet (because that's like hardcoding the blueprint, we want to leave it as definable at instantiation as possible). we can use the `__init__()` method for this to define variables in self. init takes the parameters you want to give `Person()`.  kinda weird to explain that.

if we wanted our instantiation (in this case, josh) to have a name attribute, we would write `self.name = name`. this assigns the instance's variable "name" to the variable supplied when declared. hopefully that makes more sense with this example:

```python
class Person():
	def __init__(self, name, age):
		self.name = name
		self.age  = age
	def greeting(self):
		print("my name is {} and i am {} years old".format(self.name, self.age))

josh = Person('josh', 16)
josh.greeting() # my name is josh and i am 16 years old
```

also a nice way to clean this up (I personally like doing this) is to use `*` or `**` when using variables in parameters. what these do is allow an arbitrary number of arguments to functions. `*` gives back a tuple and `**` gives back a dictionary. we can use this in this case to clean things up


```python
class Person():
	def __init__(self, name, age):
		self.name = name
		self.age  = age
	def greeting(self):
		vars = {'name': self.name, 'age': self.age}
		print("my name is {name} and i am {age} years old".format(**vars))

josh = Person('josh', 16)
josh.greeting() # my name is josh and i am 16 years old
```

in this case the `**` operator is essentially unpacking our dictionary for us and using it with the `.format` function. with this function we can include variable names in the `{}`, meaning that if we include a variable name specified in a dictionary and then use that dictionary with the `**` operator, we can unpack and use it.
