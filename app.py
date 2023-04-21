from flask import Flask, render_template,request
import keras
from keras.models import load_model
import tensorflow_cloud as tfc
app = flask(__name__)  
model = load_model("telecom_churn.h5") 
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/')
def helloworld():
    return render_template("base.html")
@app.route('/assesmment')
def prediction():
    return render_template("index.html")
@app.route('/predict',methods = ['post'])
def admin():
    a=request.form["gender"]
    if(a=='f'):
       a=0
    if(a=='m'):
       a=1
    b=request.form["srcitizen"]
    if(b=='n'):
       b=0
    if(b=='y'):
       b=1
    c=request.form["partner"]
    if(c=='n'):
       c=0
    if(c=='y'):
       c=1
    d=request.form["dependents"]
    if(d=='n'):
       d=0
    if(d=='y'):
       d=1
    e=request.form["tenure"]
    f=request.form["phservices"]
    if(f=='n'):
       f=0
    if(f=='y'):
       f=1
    g=request.form["multi"]
    if(g=='n'): 
        g1,g2,g3=1,0,0
    if(g == 'nps'):
        g1,g2,g3=0,1,0
    if(g == 'y'):
        g1,g2,g3=0,0,1
    h= request.form["is"]
    if(h == 'dsl'):
        h1,h2,h3=1,0,0
    if(h == 'fo'):
        h1,h2,h3=0,1,0
    if(h == 'n'):
        h1,h2,h3=0,0,1
    i= request.form["os"]
    if(i=="n"):
        i1,i2,i3=1,0,0
    if(i=='nis'):
        i1,i2,i3=0,1,0
    if(i=='y'):
        i1,i2,i3=0,0,1
    j= request.form["ob"]
    if(j=='n'):
        j1,j2,j3=1,0,0
    if(j == 'nis'):
        j1,j2,j3=0,1,0
    if(j == 'y'):
        j1,j2,j3=0,0,1
    k= request.form["dp"]
    if(k == 'n'):
        k1,k2,k3=1,0,0
    if(k == 'nis'):
        k1,k2,k3=0,1,0
    if(k == 'y'):
        k1,k2,k3=0,0,1
    l= request.form["ts"]
    if(l == 'n'):
        l1,l2,l3=1,0,0
    if(1 == 'nis'):
       l1,l2,l3=0,1,0
    l1,l2,l3=0,1,0
    if(1=='y'):
        l1,l2,l3=0,0,1
    m=request.form["stv"]
    if(m=='n'):
        m1,m2,m3=1,0,0
    if(m=='nis'):
        m1,m2,m3=0,1,0
    if(m=='y'):
     n=request.form["smv"] 
    if(n=='n'):
        n1,n2,n3=1,0,0
    if(n=='nis'):
        n1,n2,n3=0,1,0
    if(n=='y'):
        n1,n2,n3=0,0,1
    o=request.form ["contract"] 
    if(o=='mtm'):
         o1,o2,o3=1,0,0
    if(o=='oyr'):
        o1,o2,o3=0,1,0
    if(0=='tyrs'):
        o1,o2,o3=0,0,1
    p = request.form["pmt"] 
    if(p=='ec'):
        p1,p2,p3,p4=1,0,0,0
    if(p=='mail'):
        p1,p2,p3,p4=0,1,0,0
    if(p=='bt'):
        p1,p2,p3,p4=0,0,1,0
    if(p=='cc'):    
        p1,p2,p3,p4=0,0,0,1
    q= request.form["plb"]
    if(q=='n'):                                            
     q= request.form["plb"]
    if(q=='n'): 
      q=0
    if(q=='y'): 
      q=1
r= request.form["plb"]
s= request.form["tcharges"]
t=[[int('g1'),int('g2'),int('g3'),int('h1'),int('h2'),int('h3'),int('i1'),int('i2'),int('i3'),int('j1'),int('j2'),int('j3')]]
print(t) 
x = model.predict(t) 
print(x[0])  
if (x[[0]] <=0.5): 
    y="No" 
    render_template("predno.html", z = y) 
if(x[[0]] <=0.5):   
    y="yes" 
    render_template("predyes.html",z=y)