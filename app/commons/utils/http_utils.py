from fastapi import Request
from fastapi import HTTPException
from starlette.concurrency import iterate_in_threadpool


async def get_body(request: Request) -> bytes:
    return await request.body()


async def _log_response_to_logger(response, body, request: Request, callback):
    response_body = [chunk async for chunk in response.body_iterator]
    response.body_iterator = iterate_in_threadpool(iter(response_body))
    response_data = []

    if len(response_body) > 0:
        response_data = response_body[0].decode()

    if len(response_data) > 0:
        try:
            payload = body if body else str(request.query_params)
        except HTTPException as e:
            payload = {
                'decodeError': True, 'msg': e.detail
            }
        log_body = {
            'route': request.url.path,
            'payload': payload,
            'response': response_data,
            'status_code': response.status_code,
            'original': response_data
        }
        callback(log_body)
