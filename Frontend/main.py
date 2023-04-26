import json
import sqlite3
import jsonify
import  json
from flask import Flask , render_template ,request

app = Flask(__name__ , template_folder='views')
@app.route('/bse', methods = ['GET'])
def index():

    page = 0
    connection1 = sqlite3.Connection('Bse.db')
    curser1 = connection1.cursor()
    curser1.execute('select * from quotes')
    heading = ("equity_id" , "price" , "eps","ceps" ,"pe","pb","roe","grp","industry")
    data = curser1.fetchall()
    data = data[0:5]
    return render_template('quotes.html', heading=heading , data = data , page = page  )


@app.route('/bse/<id>', methods = ['GET'])
def page(id):
    id = int(id)
    if id <= 0:
        id = 0
    page = id
    page1 = id*5
    page2 = page1 + 5
    connection1 = sqlite3.Connection('Bse.db')
    curser1 = connection1.cursor()
    curser1.execute('select * from quotes')
    heading = ("equity_id" , "price" , "eps","ceps" ,"pe","pb","roe","grp","industry")
    data = curser1.fetchall()
    data = data[page1:page2]
    return render_template('quotes.html', heading=heading , data = data , page = page  )
@app.route('/update',methods=["POST"])
def update ():
    #conn = sqlite3.Connection('Bse.db')
    #curser = conn.cursor()
    x = request.get_json()
    g = json.loads(x)
    for y in g:
        conn = sqlite3.Connection('Bse.db')
        curser = conn.cursor()
        curser.execute("select * from Quotes where equity_id ='"+str(y[0])+"';")
        output =curser.fetchall()
        print(output)
        if len(output) == 0:
            comm3 = "insert into Quotes values('"+str(y[0])+"','"+str(y[1])+"','"+str(y[2])+"','"+str(y[3])+"','"+str(y[4])+"','"+str(y[5])+"','"+str(y[6])+"','"+str(y[7])+"','"+str(y[8])+"');"
            print(comm3)
            curser.execute(comm3)
            conn.commit()

        else:
            comm3 = "Update Quotes set equity_id ='"+str(y[0])+"',price ='"+str(y[1])+"',eps ='"+str(y[2])+"',ceps ='"+str(y[3])+"',pe ='"+str(y[4])+"',pb ='"+str(y[5])+"',roe ='"+str(y[6])+"',grp ='"+str(y[7])+"',industry ='"+str(y[8])+"' where equity_id ='" + str(y[0])+"';"
            print(comm3)
            curser.execute(comm3)
            conn.commit()

        
        print(y)


@app.route('/bse/quotes/<id>' , methods = ['GET'])
def getquote(id):
    connection1 = sqlite3.Connection('Bse.db')
    curser1 = connection1.cursor()
    curser1.execute("select * from quotes where equity_id = '"+str(id)+"';")
    heading = ("equity_id" , "price" , "eps","ceps" ,"pe","pb","roe","grp","industry")
    data = curser1.fetchall()
    return render_template('quotes.html', heading=heading , data = data )

@app.route('/' , methods = ['GET'])
def home():

    return render_template('home.html'
                           )

if __name__ == '__main__':
    app.run(debug=True)


