from typing import Annotated
import typer

app = typer.Typer()

@app.command() 
def userReg(#ister
    user: Annotated[str, typer.Argument()], #online name that the AI will call
    age: Annotated[int, typer.Option(min=18)],#with ai needs to be over 18
    ):
        if(age < 18):
            return 0 #add error
        print(f"User is {user}")
        print(f"--age is {age}")
    

@app.command()
def rpg(mode: str):
    if mode == "demo":
        print("demo mode")
        #make a rpg function that will set up 
    else:
        return 0 #add error for no mode set


if __name__ == "__main__":
    app()
