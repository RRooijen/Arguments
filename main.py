# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1

def greet(name, template_greetings = 'Hello, <name>!'):
    greetings = template_greetings.replace('<name>', name)
    return greetings

print(greet('Bob'))

# Part 2

def force(mass, body= 'earth'):
    surface_gravity={
        'sun':  274.0,
        'jupiter':  24.9,
        'neptune':  11.2,
        'saturn':  10.4,
        'earth':  9.8,
        'uranus':  8.9,
        'venus':  8.9,
        'mars':  3.7,
        'mercury':  3.7,
        'moon':  1.6,
        'pluto':  0.6
        }
    return mass * surface_gravity[body]
    
print(force(0.1, 'mars'))

# Part 3

def pull(m1,m2,d):

    f = 6.674*(10 ** -11)*((m1*m2)/d**2)

    return f

print(pull(800,1500,3))
    