
import sympy as sp

x = sp.symbols('x', positive=True)

tu = sp.sqrt(x)*(x**3-6*x**2+11*x-6)
mau = x**2-3*x+2

f = sp.factor(sp.cancel(tu/mau))

print("Ham rut gon:", f)

# Cau b: Do thi
# Dung hai khoang de tranh cac diem bi loai
# x = 1, 2 la diem khong thuoc tap xac dinh
sp.plot(f, (x, 0.001, 5))

# Cau c: Nghiem
print("Nghiem:", sp.solve(f, x))

# Cau d: Dao ham
df = sp.simplify(sp.diff(f, x))
print("Dao ham:", df)
print("Diem dung:", sp.solve(df, x))

# Cau e: Dien tich tren [3,5]
S = sp.integrate(f, (x, 3, 5))
print("Dien tich:", S)
