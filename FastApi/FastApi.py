from fastapi import FastAPI

app=FastAPI()

@app.get("/kat")

def cat():
    cat={
        "name":"milly",
        "age":2,
        "color":"black",
        "race": "persian",
        "eye_color":"green"
    }
    return cat