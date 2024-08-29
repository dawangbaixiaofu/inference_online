import asyncio
import os
from openai import AsyncOpenAI

# 移除http_proxy
os.environ.pop('http_proxy', None)
# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://0.0.0.0:8000/v1"

async def request(model):
    chat_completion = await client.chat.completions.create(
        messages = [{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": "Who won the world series in 2020?"
    }
    ],
        model = model
    )
    return chat_completion

async def main(request_nums=100):
    models = await client.models.list()
    model = models.data[0].id

    tasks = (asyncio.create_task(request(model)) for i in range(request_nums))
    ret = await asyncio.gather(*tasks)
    for e in ret:
        print(e)


from time import time 
start = time()

asyncio.run(main(request_nums=1000))

end = time() 
duration = end - start
print(f"total used time is: {duration/60} s.")
