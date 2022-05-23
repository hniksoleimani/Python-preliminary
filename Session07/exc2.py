import random
import math
sp,su,sw=[0,0,0]
deviation_p,deviation_w,deviation_u=[0,0,0]
list_p=[]
list_w=[]
list_u=[]
diff_square_w=[]
diff_square_u=[]
diff_square_p=[]
n=int(input("n="))
phase1_worst=float(input("phase1_worst="))
phase1_best=float(input("phase1_best="))

phase2_worst=float(input("phase2_worst="))
phase2_best=float(input("phase2_best="))

phase3_worst=float(input("phase3_worst="))
phase3_best=float(input("phase3_best="))

for i in range(n):
    p=random.random()
    p1=((phase1_worst-phase1_best)*p)+phase1_best
    sp=sp+p1          #Mu=sp/n
    list_p=list_p+[p1]
      
    w=random.random()
    w1=((phase2_worst-phase2_best)*w)+phase2_best
    sw+=w1
    list_w=list_w+[w1]
    
    u=random.random()
    u1=((phase3_worst-phase3_best)*u)+phase3_best
    su+=u1
    list_u=list_u+[u1]
    
diff_square_p= [(i-(sp/n))**2 for i in list_p]               #morabae ekhtelaf khata
diff_square_w= [(i-(sw/n))**2 for i in list_w]
diff_square_u= [(i-(su/n))**2 for i in list_u]
for i in range(n):
    deviaton_p=deviation_p+diff_square_p[i]
    deviaton_w=deviation_w+diff_square_w[i]
    deviaton_u=deviation_u+diff_square_u[i]
sigma_p=math.sqrt(deviation_p/n)
sigma_w=math.sqrt(deviation_w/n)
sigma_u=math.sqrt(deviation_w/n)

mu_p=sp/n
mu_w=sw/n
mu_u=su/n

gauss_p=random.gauss(mu_p,sigma_p)
gauss_w=random.gauss(mu_w,sigma_w)
gauss_u=random.gauss(mu_u,sigma_u)


print("Expected cost of phase 1:",gauss_p)
print("Expected cost of phase 2:",gauss_w)
print("Expected cost of phase 3:",gauss_u)
print("Total expected cost of project:",gauss_p+gauss_w+gauss_u)
