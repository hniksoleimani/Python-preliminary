class convert_t:
    def __init__(self,t):
        self.t=t
    def f_c(self):
        f=self.t
        c=(f-32)*(5/9)
        return c
    def c_f(self):
        c=self.t
        f=(c*(9/5))+32
        return f
    def f_k(self):
        f=self.t
        k=(f+459.67)*(5/9)
        return k
    def k_f(self):
        k=self.t
        f=(k*(9/5))-459.67
        return f
    def k_c(self):
        k=self.t
        c=k-273.15
        return c
    def c_k(self):
        c=self.t
        k=c+273.15
        return k
class convert_l:
    def __init__(self,l):
        self.l=l
    def m_cm(self):
        m=self.l
        cm=m*100
        return cm
    def m_mm(self):
        m=self.l
        mm=m*1000
        return mm
    def cm_m(self):
        cm=self.l
        m=cm/100
        return m
    def cm_mm(self):
        cm=self.l
        mm=cm*10
        return mm
    def mm_m(self):
        mm=self.l
        m=mm/1000
        return m
    def mm_cm(self):
        mm=self.l
        cm=mm/10
        return cm
class convert_m:
    def __init__(self,m):
        self.m=m
    def kg_gr(self):
        kg=self.m
        gr=1000*kg
        return gr
    def kg_mgr(self):
        kg=self.m
        mgr=1000000*kg
        return mgr
    def gr_kg(self):
        gr=self.m
        kg=gr/1000
        return kg
    def gr_mgr(self):
        gr=self.m
        mgr=1000*gr
        return mgr
    def mgr_kg(self):
        mgr=self.m
        kg=mgr/1000000
        return kg
    def mgr_gr(self):
        mgr=self.m
        gr=mgr/1000
        return gr
        
    
k=int(input("convert_temperature(1),convert_length(2),convert_mass(3):"))
if k==1:
    t=float(input("Temperature="))
    m=int(input("f_c:1,c_f:2,:f_k:3k_f:4,k_c:5,,c_k:6="))
    convert=convert_t(t)
    if m==1:
        print(convert.f_c())
    elif m==2:
        print(convert.c_f())
    elif m==3:
        print(convert.f_k())
    elif m==4:
        print(convert.k_f())
    elif m==5:
        print(convert.k_c())
    elif m==6:
        print(convert.c_k())
    else:
        print("m value out of range.")


elif k==2:
    l=float(input("l="))
    m=int(input("m_cm:1,m_mm:2,cm_m:3,cm_mm:4,mm_m:5,mm_cm:6="))
    convert=convert_l(l)
    if m==1:
        print(convert.m_cm())
    elif m==2:
        print(convert.m_mm())
    elif m==3:
        print(convert.cm_m())
    elif m==4:
        print(convert.cm_mm())
    elif m==5:
        print(conver.mm_m())
    elif m==6:
        print(convert.mm_cm())
    else:
        print("Out of range.")
        

        
elif k==3:
    m=float(input("Enter mass:"))
    m1=int(input("kg_gr:1,kg_mgr:2,gr_kg:3,gr_mgr:4,mgr_kg:5,mgr_gr:6="))
    convert=convert_m(m)
    if m1==1:
        print(convert.kg_gr())
    elif m1==2:
        print(convert.kg_mgr())
    elif m1==3:
        print(convert.gr_kg())
    elif m1==4:
        print(convert.gr_mgr())
    elif m1==5:
        print(convert.mgr_kg())
    elif m1==6:
        print(convert.mgr_gr())
    else:
        print("Out of range.")
else:
    print("Value out of range.")
