from fastapi import FastAPI
from scraper import GettingDataFrom
app = FastAPI()

quotes = GettingDataFrom()

        
@app.get("/{cat}")
async def read_item(cat):
    return quotes.get_data(cat)