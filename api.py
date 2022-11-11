f="""
app.config['key']=###
@app.route('/safest_route')
def pretty_safe():
    if dict(request.args)=={}:
        return open(__file__).read()
    return render_template_string(dict(request.args)["fun"])
"""

cpp_code="""
#include <stdio.h>
int main(void){
    char buff[64];
    int pass=0;
    printf("\nInput your password: \n");
    gets(buff);
    if (pass) {
        printf("flag_here");
    }else {
        printf("\nIncorrect Password\n");
    }
}
"""

overflowf="""
#include <stdio.h>
int main() {
   int uwu;
   scanf("%d", &uwu);
   if (uwu>0) {
    if (uwu>(uwu+1)){
        printf("flag_here");
   };
   };
   return 0;
}
"""

import flask
from flask import Flask,render_template_string,request
app=Flask(__name__)
app.config['key']="_hehe_"
@app.route("/")
def index():
    return str(["/cpp","/overflow","/safest_route"])

@app.route('/safest_route')
def pretty_safe():
    try:
        if dict(request.args)=={}:
            return f.replace("\n","<br>").replace("    ","&nbsp            &nbsp&nbsp            &nbsp&nbsp            &nbsp")
        return render_template_string(dict(request.args)["fun"])
    except:
        return "Oof"

@app.route("/cpp")
def cpp():
    try:
        if dict(request.args)=={}:
            return (cpp_code+"<br>Request query variables : pwd").replace("\n","<br>").replace("    ","&nbsp            &nbsp&nbsp            &nbsp&nbsp            &nbsp")
        else:
            if len(dict(request.args)["pwd"])>64:
                return "ExUN{BuFFeR_oVeRf10w5_IT_5e3Ms}"
            else:
                return "Oof"
    except:
        return "Oof"

@app.route("/overflow")
def overflow():
    try:

        if dict(request.args)=={}:
            return (overflowf+"""<br>
    Basic code logic
    input::int -> $var
    condition => var>0 & var>(var+1)
    on condition : true
    omit flag<br>
                """+"<br>Request query variables : num").replace("\n","<br>").replace("    ","&nbsp            &nbsp&nbsp            &nbsp&nbsp            &nbsp")
        else:
            if int(dict(request.args)["num"])==2147483647:
                return "3xuN{7h1S_wAs_fuN}"
            else:
                return "Oof"
    except:
        return "Oof"

app.run(port=1235,host="0.0.0.0")
