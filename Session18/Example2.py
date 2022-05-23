from scipy.integrate import trapz,simpson,quad
def f(x):
    return x**7
x=np.linspace(1,3,50)
y=x**7
q=quad(f,1,3)
t=trapz(y,x)
s=simpson(y,x)
print(s)
print("------------------------------")
print(t)
print("-------------------------------")
print(q)
