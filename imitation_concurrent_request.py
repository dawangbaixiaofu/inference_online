import os
from openai import OpenAI
from time import time
from concurrent.futures import ThreadPoolExecutor


# 移除http_proxy
os.environ.pop('http_proxy', None)
# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://0.0.0.0:8000/v1"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

chat_completion = client.chat.completions.create(
    messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": "Who won the world series in 2020?"
    }, {
        "role":
        "assistant",
        "content":
        "The Los Angeles Dodgers won the World Series in 2020."
    }, {
        "role": "user",
        "content": "Where was it played?"
    }],
    model=model,
)

print("Chat completion results:")
print(chat_completion)


start = time()

messages=[{
        "role": "system",
        "content": "你是一个帮助人类的聊天助手."
    }, {
        "role": "user",
        "content": "介绍下你自己？"
    }]
kwargs = {"messages": messages, "model": model}


request_nums = 1000
with ThreadPoolExecutor(max_workers=request_nums) as executor:
    all_tasks = [executor.submit(lambda x: client.chat.completions.create(**x), kwargs) for _ in range(request_nums)]
    for task in all_tasks:
        result = task.result()
        print(result)

end = time() 
duration = end - start
print(f"total used time is: {duration/60} s.")