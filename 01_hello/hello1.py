from fastapi import FastAPI

app : FastAPI = FastAPI()

app.get("/h1")

#aking a function in that rount 
def welcom ():
    return"hello? Bro "

#so if i want to run this from right here we have to 
if __name__  == "__main__":
    import uvicorn
    uvicorn.run("hello1:app", reload=True)

