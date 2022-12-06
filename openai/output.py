
# return success and JWT token

@app.post("/startrun")
def startrun(headers: Dict[str, str]):
    iem_key = headers.get("iem-key")
    if iem_key:
        # validate JWT token from header 'item-key' with JWKS service
        # return success
        return {"success": True}
    else:
        # create new JWT token
        jwt_token = generate_jwt_token()
        # add this token to JWKS service
        add_token_to_jwks(jwt_token)
        # cache request to JWKS service
        cache_request_to_jwks()
        # return success and JWT token
        return {"success": True, "token": jwt_token}