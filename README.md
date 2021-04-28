# MAT 412 Differential Geometry Final

## Running

Make sure `python3` is installed and on your path. 
Install `sympy` using `pip3` by running:
```sh
pip3 install sympy
```
**Note: `pip` might be needed instead of `pip3`**
Then run:
```sh
python3 ParallelTransport.py
```
or
```sh
python3 Mobius.py
```
**Note: `python` might be needed instead of `python3`**

It should print out the results of the calculations in your terminal.

`ParallelTransport.py` is for problem 1a and `Mobius` is for problem 2c

## License
ParallelTransport.py and Mobius.py
Copyright (C) 2021 Jeffrey Tucker
All rights reserved

## Example outputs

`ParallelTransport.py`
```
1a:

alpha': Matrix([[-sin(2*t)], [cos(2*t)], [cos(t)]])
alpha'': Matrix([[-2*cos(2*t)], [-2*sin(2*t)], [-sin(t)]])

T: Matrix([[-sqrt(2)*sin(2*t)/sqrt(cos(2*t) + 3)], [cos(2*t)/sqrt(cos(t)**2 + 1)], [cos(t)/sqrt(cos(t)**2 + 1)]])
k: 1/sqrt(cos(t)**2 + 1)

n: Matrix([[-sqrt(2)*sin(2*t)/sqrt(cos(2*t) + 3)], [cos(2*t)/sqrt(cos(t)**2 + 1)], [cos(t)/sqrt(cos(t)**2 + 1)]])

x_u: Matrix([[-sin(u)*sin(v)], [sin(v)*cos(u)], [0]])x_v: Matrix([[cos(u)*cos(v)], [sin(u)*cos(v)], [-sin(v)]])

N: Matrix([[-sqrt(sin(v)**2)*cos(u)], [-sqrt(sin(v)**2)*sin(u)], [-sqrt(2)*sin(2*v)/(2*sqrt(1 - cos(2*v)))]])

k_n: (-cos(t - v) - cos(t + v) + cos(-2*t + u + v) - cos(2*t - u + v))*sin(v)/(2*(cos(t)**2 + 1)*sqrt(sin(v)**2))

N x alpha': Matrix([[(-sin(u)*sin(v)*cos(t) + cos(2*t)*cos(v))*sin(v)/sqrt(sin(v)**2)], [(2*sin(t)*cos(v) + sin(v)*cos(u))*sin(v)*cos(t)/sqrt(sin(v)**2)], [-sqrt(1/2 - cos(2*v)/2)*cos(2*t - u)]])

k_g: (0.707106781186548*sqrt(1 - cos(2*t - 3.14159265358979))*cos(t)**2 - 2*(sin(t)**2 + 1)*sin(2*t)*cos(t)**2 + 2*sin(t)*cos(t)**2*cos(2*t) - 2*sin(t)*cos(2*t)**2)/cos(t)**3

k_g2: ((sqrt(2 - 2*cos(2*t - 3.14159265358979)) - 4*(sin(t)**2 + 1)*sin(2*t) + 4*sin(t)*cos(2*t))*cos(t)**2/2 - 2*sin(t)*cos(2*t)**2)/cos(t)**3

1c:

w: Matrix([[-sin(u)*sin(v)*cos(cos(t) - 1)/cos(t) - sin(cos(t) - 1)*cos(u)*cos(v)], [-sin(u)*sin(cos(t) - 1)*cos(v) + sin(v)*cos(u)*cos(cos(t) - 1)*sec(t)], [sin(v)*sin(cos(t) - 1)]])

w(0): Matrix([[0], [1.00000000000000], [0]])
w(pi/4): Matrix([[-0.532631185239781], [0.821354618873816], [-0.204158297810090]])
w(pi/2): Matrix([[-0.540302272784170], [0.841470984807897], [-8.41471053891216e-10]])
w(-pi/4): Matrix([[0.532631185045647], [0.821354619067951], [-0.204158297535542]])
w(-pi/2): Matrix([[0.540302338952110], [0.841470984807897], [-8.41471156941690e-10]])
```


`Mobius.py`
```
2c:

x_u: Matrix([[-v*sin(u)*cos(u/2)/2 + (-v*sin(u/2) + 2)*cos(u)], [-v*cos(u/2)*cos(u)/2 - (-v*sin(u/2) + 2)*sin(u)], [-v*sin(u/2)/2]])
x_v: Matrix([[-sin(u/2)*sin(u)], [-sin(u/2)*cos(u)], [cos(u/2)]])
x_uu: Matrix([[v*sin(u/2)*sin(u)/4 - v*cos(u/2)*cos(u) - (-v*sin(u/2) + 2)*sin(u)], [v*sin(u/2)*cos(u)/4 + v*sin(u)*cos(u/2) + (v*sin(u/2) - 2)*cos(u)], [-v*cos(u/2)/4]])
x_uv: Matrix([[-sin(u/2)*cos(u) - sin(u)*cos(u/2)/2], [sin(u/2)*sin(u) - cos(u/2)*cos(u)/2], [-sin(u/2)/2]])
x_vv: Matrix([[0], [0], [0]])

N: Matrix([[(-v*cos(u) - v*cos(2*u)/2 + v/2 - 2*sin(u/2) - 2*sin(3*u/2))/sqrt((v*sin(u) + v*sin(2*u)/2 - 2*cos(u/2) - 2*cos(3*u/2))**2 + (-v*sin(u)**2 + v*cos(u) + 2*sin(u/2) + 2*sin(3*u/2))**2 + (-2*v*sin(u/2)*sin(u)**2 - v*sin(u/2) + v*sin(3*u/2)/4 - 3*v*sin(5*u/2)/4 + v*sin(u)*sin(2*u)/(4*sin(u/2)) + 4)**2*sin(u/2)**2)], [(v*sin(u) + v*sin(2*u)/2 - 2*cos(u/2) - 2*cos(3*u/2))/sqrt((v*sin(u) + v*sin(2*u)/2 - 2*cos(u/2) - 2*cos(3*u/2))**2 + (-v*sin(u)**2 + v*cos(u) + 2*sin(u/2) + 2*sin(3*u/2))**2 + (-2*v*sin(u/2)*sin(u)**2 - v*sin(u/2) + v*sin(3*u/2)/4 - 3*v*sin(5*u/2)/4 + v*sin(u)*sin(2*u)/(4*sin(u/2)) + 4)**2*sin(u/2)**2)], [8*sqrt(2)*(-v*cos(u) + v - 4*sin(u/2))/sqrt(32*v**2*cos(u)**2*cos(2*u)**2 - 128*v**2*cos(u)**2*cos(2*u) + 128*v**2*cos(u)**2 - 96*v**2*cos(u)*cos(2*u)**2 + 320*v**2*cos(u)*cos(2*u) - 368*v**2*cos(u) + 20*v**2*cos(2*u)**3 + 12*v**2*cos(2*u)**2 - 27*v**2*cos(2*u) - 136*v**2*cos(3*u) + 18*v**2*cos(4*u) + 24*v**2*cos(5*u) - 9*v**2*cos(6*u) + 338*v**2 - 2048*v*sin(u/2) + 2048)]])

E: v**2*sin(u/2)**2 + v**2/4 - 4*v*sin(u/2) + 4
F: 0
G: 1

e: (4*v**2*cos(u/2) - 3*v**2*cos(3*u/2) - v**2*cos(5*u/2) + v**2*sin(u)/(2*sin(u/2)) + v**2*sin(3*u)/(2*sin(u/2)) - 18*v*sin(u) - 2*v*sin(2*u) - 2*v*sin(3*u) + v/tan(u/2) - v*cos(7*u/2)/sin(u/2) + 32*cos(u/2))/(4*sqrt((v*sin(u) + v*sin(2*u)/2 - 2*cos(u/2) - 2*cos(3*u/2))**2 + (-v*sin(u)**2 + v*cos(u) + 2*sin(u/2) + 2*sin(3*u/2))**2 + (2*v*sin(u/2)*sin(u)**2 + v*sin(u/2) - v*sin(3*u/2)/4 + 3*v*sin(5*u/2)/4 - v*sin(u)*sin(2*u)/(4*sin(u/2)) - 4)**2*sin(u/2)**2))
f: 16*sqrt(2)/sqrt(32*v**2*cos(u)**2*cos(2*u)**2 - 128*v**2*cos(u)**2*cos(2*u) + 128*v**2*cos(u)**2 - 96*v**2*cos(u)*cos(2*u)**2 + 320*v**2*cos(u)*cos(2*u) - 368*v**2*cos(u) + 20*v**2*cos(2*u)**3 + 12*v**2*cos(2*u)**2 - 27*v**2*cos(2*u) - 136*v**2*cos(3*u) + 18*v**2*cos(4*u) + 24*v**2*cos(5*u) - 9*v**2*cos(6*u) + 338*v**2 - 2048*v*sin(u/2) + 2048)
g: 0

K: -16/(((v*sin(u) + v*sin(2*u)/2 - 2*cos(u/2) - 2*cos(3*u/2))**2 + (-v*sin(u)**2 + v*cos(u) + 2*sin(u/2) + 2*sin(3*u/2))**2 + (2*v*sin(u/2)*sin(u)**2 + v*sin(u/2) - v*sin(3*u/2)/4 + 3*v*sin(5*u/2)/4 - v*sin(u)*sin(2*u)/(4*sin(u/2)) - 4)**2*sin(u/2)**2)*(4*v**2*sin(u/2)**2 + v**2 - 16*v*sin(u/2) + 16))

H: (8*v*sin(u)**4 - 8*v*sin(u)**2 + 4*(-4*v**2*sin(u/2)**4*sin(u)**2 + 16*v**2*sin(u/2)**4 + 4*v**2*sin(u/2)**2*sin(u)**2 - 8*v**2*sin(u/2)**2 - v**2*sin(u)**4 + 4*v**2*sin(u)**2 + 4*v**2 + 8*v*sin(u/2)**3*sin(u)**2 - 8*v*sin(u/2)**3 - 8*v*sin(u/2)*sin(u)**2 - 24*v*sin(u/2) + 32)*sin(u/2))/(4*(12*v**2*sin(u/2)**4 - 4*v**2*sin(u/2)**2 + 3*v**2*sin(u)**2 + 2*v**2 - 32*v*sin(u/2) + 32)*sqrt(8*v**2*sin(u/2)**4*sin(u)**4 - 14*v**2*sin(u/2)**4*sin(u)**2 + 6*v**2*sin(u/2)**4 + 6*v**2*sin(u/2)**2*sin(u)**2 - 2*v**2*sin(u/2)**2 + 2*v**2*sin(u)**6 + 4*v**2*sin(u)**4*cos(u) - 15*v**2*sin(u)**4/2 - 4*v**2*sin(u)**2*cos(u) + 11*v**2*sin(u)**2/2 + v**2 + 16*v*sin(u/2)**3*sin(u)**2 - 16*v*sin(u/2)**3 - 16*v*sin(u/2)*sin(u)**2 + 4*v*sin(u)**4/sin(u/2) - 4*v*sin(u)**2/sin(u/2) + 16)*tan(u/2))
```
