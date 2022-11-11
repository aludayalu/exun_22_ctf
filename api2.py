vit="""
https://github.com/Lumatozer/Vitality
vars: registered total used booted temp temptwo;
if (booted==None) (
    var booted=true;
    var registered=('test',);
    var total=100;
    var used=(10,);
);
if (txmsg=='withdraw') (
    var temp=0;
    var temptwo=0;
    if (txsender in registered)(
    .registered obj txsender $temp;
    .used $ temp $temptwo;
    );
    tx (total-temptwo) txsender 'LTZ';
);
if (txmsg=='register' and txsender not in registered) (
    .registered + txsender;
    .used + 5;
);
if (txmsg=='play' and txsender in registered)(
    var temp=0;
    var temptwo=0;
    .registered obj txsender $temp;
    .used $ temp $temptwo;
    if (temptwo>0) (
        .used insert temp (temptwo-10);
    );
);
Request query : txmsg
""".replace("\n","<br>").replace("    ","&nbsp;")

import flask
from flask import Flask,render_template_string,request
app=Flask(__name__)
app.config['key']="_hehe_"
@app.route("/")
def hack():
    try:
        if dict(request.args)=={}:
            return vit
        if dict(request.args)["txmsg"]=="withdraw":
            return "why_vI7a1I7y_7h0_Oof"
        else:
            return "Oof"
    except:
        return "Oof"
app.run(port=1235,host="0.0.0.0")
