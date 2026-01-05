from fastapi import Header, HTTPException, status

REGULATOR_API_KEYS = {
    # Example only – replace with secure vault / env
    "regulator-demo-key-001": "REGULATOR"
}


def regulator_auth(x_api_key: str = Header(...)):
    role = REGULATOR_API_KEYS.get(x_api_key)
    if role != "REGULATOR":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized regulator access"
        )
    return True
