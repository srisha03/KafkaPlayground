from flask import Flask, request, render_template_string, redirect, url_for
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search']
        producer.send('test-topic', key=b'search_term', value=bytes(search_term, 'utf-8'))
        return redirect(url_for('results'))
    return render_template_string(home_template)

@app.route('/results')
def results():
    return render_template_string(results_template)

home_template = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Simple Search</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">Search Something</h1>
      <form method="post">
        <div class="mb-3">
          <input type="text" class="form-control" name="search" placeholder="Enter search term" required>
        </div>
        <button type="submit" class="btn btn-primary">Search</button>
      </form>
    </div>
  </body>
</html>
'''

results_template = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>No Results</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">No Results</h1>
      <a href="/" class="btn btn-primary">Go Back</a>
    </div>
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
