from fastapi import FastAPI, status
from hashlib import sha256
from fastapi.responses import RedirectResponse

from ebay_scraping.config import settings
from ebay_scraping.schema import EbayChallengeResponse

app = FastAPI()


@app.get("/ebay/callback", response_model=EbayChallengeResponse)
async def get_ebay_challenge_code(challenge_code: str):
    endcoded = f"{challenge_code}{settings.EBAY_VERIFICATION_TOKEN}{settings.BASE_URL}".encode()
    challenge_response = sha256(endcoded, usedforsecurity=True).hexdigest()

    return {"challengeResponse": challenge_response}


@app.get("/")
async def get_root():
    return {
        "message": "Welcome!"
    }
