"""Boilerplate Reasoner API with FastAPI."""
import logging

from fastapi import FastAPI

from reasoner_pydantic import Request, Message

LOGGER = logging.getLogger(__name__)

APP = FastAPI(
    title='Boilerplate Reasoner API',
    version='1.0.0',
)


@APP.post('/query', response_model=Message)
async def handle_query(
        request: Request,
) -> Message:
    """Handle /query request."""
    message = request.message.dict()
    LOGGER.info('Received request. Responding...')
    return message
