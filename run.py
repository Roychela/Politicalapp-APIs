from app import politicoapp
import os

app = politicoapp()

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host ="0.0.0.0", port=port)
