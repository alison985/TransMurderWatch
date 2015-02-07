from flask import Flask, render_template
import webhose
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
    
webhose.config(token='46e002b6-73c5-4281-8bde-c1791802ff5f')


query = '(transgender OR "trans woman" OR "trans man") AND (killed OR murdered)'

def runQuery():
  queryResults = webhose.search(str(query))
  return queryResults

def find_most_recent(results):
    recent_time = datetime.strptime(results[0].published[0:10], "%Y-%m-%d")
    recent_post = results[0]
  
    for r in results:
	    r_date = datetime.strptime(r.published[0:10], "%Y-%m-%d")
	    if (r_date > recent_time):
	      recent_time = r_date
	      recent_post = r
	    
    return recent_post