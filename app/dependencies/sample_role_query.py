from typing import Union, Optional

from fastapi import Request, HTTPException, Depends
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer

get_bearer_token = HTTPBearer(auto_error=False)


class SampleRoleQuery(object):
    def __init__(self, roles: Union[list, str]):
        self.roles = [name.value.lower() for name in roles]

    def __call__(self, request: Request, auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token)):
        token = auth.credentials
        if not token:
            raise HTTPException(401, "Unauthorized")

        roles = set([role.lower() for role in get_roles(token)])
        if len(roles.intersection(set(self.roles))) == 0:
            raise HTTPException(403, "Forbidden")


def get_roles(token: str):
    # Sample token handling
    if token == "abcdef":
        return ["admin"]
