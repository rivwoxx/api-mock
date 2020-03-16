import connexion
from waitress import serve

app = connexion.App(__name__, specification_dir="./")
app.add_api("meh.yaml")
# app.run(debug=True)
serve(app, host='0.0.0.0', port=5000)
