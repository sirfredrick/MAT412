import sympy as sp
import math

# Function to find the norm of a R^3 vector
def norm(vector):
    return sp.sqrt(vector[0]**2+vector[1]**2+vector[2]**2)

# 1a normal and geodesic curvatures
t = sp.symbols("t")

# alpha(t) from question 1
print("1a:")
print()
alpha_x = sp.cos(t)*sp.cos(t)
alpha_y = sp.cos(t)*sp.sin(t)
alpha_z = sp.sin(t)

# Calculate derivatives of alpha(t) in terms of t
alpha_prime = sp.Matrix([sp.diff(alpha_x), sp.diff(alpha_y), sp.diff(alpha_z)])
print("alpha': " + str(sp.simplify(alpha_prime)))
alpha_2_prime = sp.diff(alpha_prime)
print("alpha'': " + str(sp.simplify(alpha_2_prime)))
print()

# Find unit tangent vector of alpha(t), T(t)
T = alpha_prime/norm(alpha_prime)
print("T: " + str(sp.simplify(T)))
# Find the curvature of alpha(t)
k = norm(T)/norm(alpha_prime)
print("k: " + str(sp.simplify(k)))
print()

# Find the unit normal vector of alpha(t), n(t)
n = T/norm(T)
print("n: " + str(sp.simplify(n)))
print()

u, v = sp.symbols("u v")

# Parameterization of the sphere
x = sp.Matrix([sp.sin(v)*sp.cos(u),sp.sin(v)*sp.sin(u),sp.cos(v)])

# Partials of the parameterization in terms of u and v
x_u = sp.diff(x, u)
x_v = sp.diff(x, v)
print("x_u: " + str(sp.simplify(x_u)) + "x_v: " + str(sp.simplify(x_v)))
print()

# Find the surface normal vector N(t)
cross = x_u.cross(x_v)
N = cross/norm(cross)
print("N: " + str(sp.simplify(N)))
print()

# Calculate the normal curvature
k_n = (k*n).dot(N)
print("k_n: " + str(sp.simplify(k_n)))
print()

# Find N(t) x alpha'(t) used to calculate the geodesic curvature
# Equation from http://www.math.wisc.edu/~angenent/561/kgsolutions.pdf
cross2 = N.cross(alpha_prime)
print("N x alpha': " + str(sp.simplify(cross2)))
print()

# Plug in k_g calculation to simplify
k_g = (2*sp.cos(2*t)*sp.sin(t)*sp.cos(t)**2-2*(sp.cos(2*t)**2)*sp.sin(t)+(-4*sp.sin(t)**2-2*sp.cos(t)**2)*sp.sin(2*t)*sp.cos(t)**2+(sp.cos(t)**2)*sp.sqrt(0.5-0.5*sp.cos(math.pi-2*t)))/(sp.cos(t)**3)
print("k_g: " + str(sp.simplify(k_g)))
print()

# Plug in k_g calculation again to simplify
k_g2 = (((sp.sqrt(2)/2)*sp.sqrt(1-sp.cos(2*t-math.pi))-2*((sp.sin(t)**2)+1)*sp.sin(2*t)+2*sp.sin(t)*sp.cos(2*t))/(sp.cos(t)))+((-2*sp.sin(t)*(sp.cos(2*t)**2))/(sp.cos(t)**3))
print("k_g2: " + str(sp.simplify(k_g2)))
print()

# 1c parallel transport
print("1c:")
print()

# Plug in a(t) and b(t) into w(t)
w=sp.cos(1-sp.cos(t))*sp.sec(t)*x_u+sp.sin(1-sp.cos(t))*x_v
print("w: " + str(sp.simplify(w)))
print()

# Calculate w(t) for various t

# t=0
e = 0.000000001
t_0 = 0
u_0 = t
v_0 = (math.pi)/2 - t
print("w(0): " + str(w.subs({u:u_0, v:v_0}).subs({t:t_0})))

# t=(pi/4)
t_1 = (math.pi/4)
u_1 = t
v_1 = (math.pi)/2 - t
print("w(pi/4): " + str(w.subs({u:u_1, v:v_1}).subs({t:t_1})))

# t=(pi/2)
t_2 = (math.pi/2) - e
u_2 = t
v_2 = (math.pi)/2 - t
print("w(pi/2): " + str(w.subs({u:u_2, v:v_2}).subs({t:t_2})))

# t=-(pi/4)
t_3 = -(math.pi/4) + e
u_3 = t
v_3 = (math.pi)/2 - t
print("w(-pi/4): " + str(w.subs({u:u_3, v:v_3}).subs({t:t_3})))

# t=-(pi/2)
t_4 = -(math.pi/2) + e
u_4 = t
v_4 = (math.pi)/2 - t
print("w(-pi/2): " + str(w.subs({u:u_4, v:v_4}).subs({t:t_4})))
