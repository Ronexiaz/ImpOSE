from waitress import serve
import app
import cred

serve(app.app, host=cred.ADDRESS, port=8080)