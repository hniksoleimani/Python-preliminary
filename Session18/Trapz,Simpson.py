from scipy.integrate import trapz,simpson
x=[0,0.25,0.5,0.75,1]
y=[0,0.25,0.5,0.75,1]
t=trapz(y,x)
s=simpson(y,x)
print(s)
print("------------------------------")
print(t)
