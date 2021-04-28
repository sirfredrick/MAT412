import sympy as sp

u, v = sp.symbols("u v")
# Paramterization of Mobius strip Do Carmo Differential Geometry of Curves and
# Surfaces 2-6 p. 109
x = (2-v*sp.sin((u/2)))*sp.sin(u)
y = (2-v*sp.sin((u/2)))*sp.cos(u)
z = (v*sp.cos((u/2)))

# Partial derivatives in terms of u and v
x_u = sp.diff(x, u)
y_u = sp.diff(y, u)
z_u = sp.diff(z, u)
x_v = sp.diff(x, v)
y_v = sp.diff(y, v)
z_v = sp.diff(z, v)
x_uu = sp.diff(x_u, u)
x_uv = sp.diff(x_u, v)
x_vv = sp.diff(x_v, v)
y_uu = sp.diff(y_u, u)
y_uv = sp.diff(y_u, v)
y_vv = sp.diff(y_v, v)
z_uu = sp.diff(z_u, u)
z_uv = sp.diff(z_u, v)
z_vv = sp.diff(z_v, v)

# Combine partials into R^3 vectors
P_u = sp.Matrix([x_u, y_u, z_u])
P_v = sp.Matrix([x_v, y_v, z_v])
P_uu = sp.Matrix([x_uu, y_uu, z_uu])
P_uv = sp.Matrix([x_uv, y_uv, z_uv])
P_vv = sp.Matrix([x_vv, y_vv, z_vv])

# Find surface normal vector
cross = P_u.cross(P_v)
N = cross/sp.sqrt(cross.dot(cross))

# Find first fundamental form
E = P_u.dot(P_u)
F = P_u.dot(P_v)
G = P_v.dot(P_v)

# Find second fundamental form
e = N.dot(P_uu)
f = N.dot(P_uv)
g = N.dot(P_vv)

# Find mean and Gaussian curvatures
K = (e*g-f**2)/(E*G-F**2)
H = (e*G-2*f*F+g*E)/(2*(E*G-F**2))

# Print results
print("2c:")
print()
print("x_u: " + str(P_u))
print("x_v: " + str(P_v))
print("x_uu: " + str(P_uu))
print("x_uv: " + str(P_uv))
print("x_vv: " + str(P_vv))
print()
print("N: " + str(sp.simplify(N)))
print()
print("E: " + str(sp.simplify(E)))
print("F: " + str(sp.simplify(F)))
print("G: " + str(sp.simplify(G)))
print()
print("e: " + str(sp.simplify(e)))
print("f: " + str(sp.simplify(f)))
print("g: " + str(sp.simplify(g)))
print()
print("K: " + str(sp.simplify(K)))
print()
print("H: " + str(sp.simplify(H)))
