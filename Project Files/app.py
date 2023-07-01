from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'C:\Users\anany\Flask/model.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url


def login():
    a= request.form["mac"]
    b= request.form["ag"]
    c= request.form["ps"]
    if (c=="oh"):
        c1,c2,c3 = 1,0,0
    if (c=="il"):
        c1,c2,c3 = 0,1,0
    if (c=="in"):
        c1,c2,c3 = 0,0,1
 
    d= request.form["pd"]
    e= request.form["pap"]
    f= request.form["ul"]

    g= request.form["is"]
    if (g=="fe"):
        g1,g2 = 1,0
    if (g=="ma"):
        g1,g2 = 0,1

    h= request.form["iel"]
    if (h=="jd"):
        h1,h2,h3,h4,h5,h6,h7 = 1,0,0,0,0,0,0
    if (h=="hs"):
        h1,h2,h3,h4,h5,h6,h7 = 0,1,0,0,0,0,0
    if (h=="as"):
        h1,h2,h3,h4,h5,h6,h7 = 0,0,1,0,0,0,0
    if (h=="md"):
        h1,h2,h3,h4,h5,h6,h7 = 0,0,0,1,0,0,0
    if (h=="mas"):
        h1,h2,h3,h4,h5,h6,h7 = 0,0,0,0,1,0,0
    if (h=="phd"):
        h1,h2,h3,h4,h5,h6,h7 = 0,0,0,0,0,1,0
    if (h=="clg"):
        h1,h2,h3,h4,h5,h6,h7 = 0,0,0,0,0,0,1


    i= request.form["io"]
    if (i=="moi"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 1,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (i=="ps"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,1,0,0,0,0,0,0,0,0,0,0,0,0
    if (i=="ts"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,1,0,0,0,0,0,0,0,0,0,0,0
    if (i=="sal"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,1,0,0,0,0,0,0,0,0,0,0
    if (i=="em"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,1,0,0,0,0,0,0,0,0,0
    if (i=="cr"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,1,0,0,0,0,0,0,0,0
    if (i=="tm"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,1,0,0,0,0,0,0,0
    if (i=="os"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,0,1,0,0,0,0,0,0
    if (i=="phs"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,0,0,1,0,0,0,0,0
    if (i=="af"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,0,0,0,1,0,0,0,0
    if (i=="adc"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,0,0,0,0,1,0,0,0
    if (i=="ps"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,0,0,0,0,0,1,0,0
    if (i=="hac"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,0,0,0,0,0,0,1,0
    if (i=="ff"):
        i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14 = 0,0,0,0,0,0,0,0,0,0,0,0,0,1


    j= request.form["ih"]
    if (j=="re"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="ex"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="pai"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="bun"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="mov"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="go"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="camp"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="kaya"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0
    if (j=="ya"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
    if (j=="hi"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0
    if (j=="vg"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0
    if (j=="sk"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0
    if (j=="bj"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0
    if (j=="bg"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0
    if (j=="po"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0
    if (j=="ch"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0
    if (j=="dan"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0
    if (j=="sl"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0
    if (j=="cf"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0
    if (j=="bb"):
        j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16,j17,j18,j19,j20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1


    k= request.form["ir"]
    if (k=="owc"):
        k1,k2,k3,k4,k5,k6 = 1,0,0,0,0,0
    if (k=="otr"):
        k1,k2,k3,k4,k5,k6 = 0,1,0,0,0,0
    if (k=="nif"):
        k1,k2,k3,k4,k5,k6 = 0,0,1,0,0,0
    if (k=="hus"):
        k1,k2,k3,k4,k5,k6 = 0,0,0,1,0,0
    if (k=="wif"):
        k1,k2,k3,k4,k5,k6 = 0,0,0,0,1,0
    if (k=="unm"):
        k1,k2,k3,k4,k5,k6 = 0,0,0,0,0,1



    l= request.form["cg"]
    m= request.form["cl"]

    n= request.form["it"]
    if (n=="mvc"):
        n1,n2,n3,n4 = 1,0,0,0
    if (n=="svc"):
        n1,n2,n3,n4 = 0,1,0,0
    if (n=="vet"):
        n1,n2,n3,n4 = 0,0,1,0
    if (n=="pac"):
        n1,n2,n3,n4 = 0,0,0,1


    o= request.form["ct"]
    if (o=="rec"):
        o1,o2,o3,o4 = 1,0,0,0
    if (o=="sic"):
        o1,o2,o3,o4 = 0,1,0,0
    if (o=="fro"):
        o1,o2,o3,o4 = 0,0,1,0
    if (o=="que"):
        o1,o2,o3,o4 = 0,0,0,1


    p= request.form["ins"]
    if (p=="mid"):
        p1,p2,p3,p4 = 1,0,0,0
    if (p=="tol"):
        p1,p2,p3,p4 = 0,1,0,0
    if (p=="mad"):
        p1,p2,p3,p4 = 0,0,1,0
    if (p=="trid"):
        p1,p2,p3,p4 = 0,0,0,1

    q= request.form["ac"]
    if (q=="poli"):
        q1,q2,q3,q4,q5 = 1,0,0,0,0
    if (q=="fir"):
        q1,q2,q3,q4,q5 = 0,1,0,0,0
    if (q=="othe"):
        q1,q2,q3,q4,q5 = 0,0,1,0,0
    if (q=="amb"):
        q1,q2,q3,q4,q5 = 0,0,0,1,0
    if (q=="non"):
        q1,q2,q3,q4,q5 = 0,0,0,0,1
 

    r= request.form["ist"]
    if (r=="nys"):
        r1,r2,r3,r4,r5,r6,r7 = 1,0,0,0,0,0,0
    if (r=="scs"):
        r1,r2,r3,r4,r5,r6,r7 = 0,1,0,0,0,0,0
    if (r=="wvs"):
        r1,r2,r3,r4,r5,r6,r7 = 0,0,1,0,0,0,0
    if (r=="vas"):
        r1,r2,r3,r4,r5,r6,r7 = 0,0,0,1,0,0,0
    if (r=="ncs"):
        r1,r2,r3,r4,r5,r6,r7 = 0,0,0,0,1,0,0
    if (r=="pas"):
        r1,r2,r3,r4,r5,r6,r7 = 0,0,0,0,0,1,0
    if (r=="ohs"):
        r1,r2,r3,r4,r5,r6,r7 = 0,0,0,0,0,0,1


    s= request.form["ic"]
    if (s=="sprf"):
        s1,s2,s3,s4,s5,s6,s7 = 1,0,0,0,0,0,0
    if (s=="arl"):
        s1,s2,s3,s4,s5,s6,s7 = 0,1,0,0,0,0,0
    if (s=="colb"):
        s1,s2,s3,s4,s5,s6,s7 = 0,0,1,0,0,0,0
    if (s=="norb"):
        s1,s2,s3,s4,s5,s6,s7 = 0,0,0,1,0,0,0
    if (s=="hild"):
        s1,s2,s3,s4,s5,s6,s7 = 0,0,0,0,1,0,0
    if (s=="rivw"):
        s1,s2,s3,s4,s5,s6,s7 = 0,0,0,0,0,1,0
    if (s=="nork"):
        s1,s2,s3,s4,s5,s6,s7 = 0,0,0,0,0,0,1

    t= request.form["nv"]

    u= request.form["prd"]
    if (u=="quest"):
        u1,u2,u3 = 1,0,0
    if (u=="noda"):
        u1,u2,u3 = 0,1,0
    if (u=="yeda"):
        u1,u2,u3 = 0,0,1

    v= request.form["bi"]
    w= request.form["wi"]

    x= request.form["pra"]
    if (x=="questi"):
        x1,x2,x3 = 1,0,0
    if (x=="nore"):
        x1,x2,x3 = 0,1,0
    if (x=="yere"):
        x1,x2,x3 = 0,0,1

    y= request.form["tca"]
    z= request.form["inc"]
    az= request.form["pc"]
    by= request.form["vc"]

    cx= request.form["am"]
    if (cx=="saa"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 1,0,0,0,0,0,0,0,0,0,0,0,0,0
    if (cx=="dod"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,1,0,0,0,0,0,0,0,0,0,0,0,0
    if (cx=="subu"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,1,0,0,0,0,0,0,0,0,0,0,0
    if (cx=="niss"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,1,0,0,0,0,0,0,0,0,0,0
    if (cx=="chev"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,1,0,0,0,0,0,0,0,0,0
    if (cx=="ford"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,1,0,0,0,0,0,0,0,0
    if (cx=="bmw"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,1,0,0,0,0,0,0,0
    if (cx=="toyo"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,0,1,0,0,0,0,0,0
    if (cx=="aud"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,0,0,1,0,0,0,0,0
    if (cx=="accu"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,0,0,0,1,0,0,0,0
    if (cx=="volw"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,0,0,0,0,1,0,0,0
    if (cx=="jee"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,0,0,0,0,0,1,0,0
    if (cx=="merc"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,0,0,0,0,0,0,1,0
    if (cx=="hoda"):
        cx1,cx2,cx3,cx4,cx5,cx6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14 = 0,0,0,0,0,0,0,0,0,0,0,0,0,1
    
       

    t=[[int(a),int(b),int(c1),int(c2),int(c3),int(d),float(e),int(f),int(g1),int(g2),int(h1),int(h2),int(h3),int(h4),int(h5),int(h6),int(h7),int(i1),int(i2),int(i3),int(i4),int(i5),int(i6),int(i7),int(i8),int(i9),int(i10),int(i11),int(i12),int(i13),int(i14),int(j1),int(j2),int(j3),int(j4),int(j5),int(j6),int(j7),int(j8),int(j9),int(j10),int(j11),int(j12),int(j13),int(j14),int(j15),int(j16),int(j17),int(j18),int(j19),int(j20),int(k1),int(k2),int(k3),int(k4),int(k5),int(k6),int(l),int(m),int(n1),int(n2),int(n3),int(n4),int(o1),int(o2),int(o3),int(o4),int(p1),int(p2),int(p3),int(p4),int(q1),int(q2),int(q3),int(q4),int(q5),int(r1),int(r2),int(r3),int(r4),int(r5),int(r6),int(r7),int(s1),int(s2),int(s3),int(s4),int(s5),int(s6),int(s7),int(t),int(u1),int(u2),int(u3),int(v),int(w),int(x1),int(x2),int(x3),int(y),int(z),int(az),int(by),int(cx1),int(cx2),int(cx3),int(cx4),int(cx5),int(cx6),int(cx7),int(cx8),int(cx9),int(cx10),int(cx11),int(cx12),int(cx13),int(cx14)]]
    output= model.predict(t)
    print(output) 
    
    if(output==1):
        return render_template("index.html",y = "YES, it is a fraudulent claim")
    if(output==0):
        return render_template("index.html",y = "NO, it is not a fraudulent claim")

if __name__ == '__main__' :
    app.run(debug= False)
