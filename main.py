from app import app
import views

if __name__ == '__main__':
    app.run(port=8965)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
