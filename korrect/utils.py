import asyncio
import os

import openai


class OpenAIEmbed():
    def __init__():
        openai.api_key = os.environ.get("OPENAI_API_KEY", None)
        assert openai.api_key is not None, "Please set the OPENAI_API_KEY environment variable."
        assert openai.api_key != '', "Please set the OPENAI_API_KEY environment variable."

    async def create_embedding(self, text, retry=3):
        for _ in range(retry):
            try:
                response = await openai.Embedding.acreate(input=text, model="text-embedding-ada-002")
                return response
            except openai.error.RateLimitError:
                print('Rate limit error, waiting for 1 second...')
                await asyncio.sleep(1)
            except openai.error.APIError:
                print('API error, waiting for 1 second...')
                await asyncio.sleep(1)
            except openai.error.Timeout:
                print('Timeout error, waiting for 1 second...')
                await asyncio.sleep(1)
        return None

    async def process_batch(self, batch, retry=3):
        tasks = [self.create_embedding(text, retry=retry) for text in batch]
        return await asyncio.gather(*tasks)