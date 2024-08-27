python -m vllm.entrypoints.openai.api_server \
    --model /home/app/llama-3-8b-instruct \
    --chat-template ./llama3_chat_template.jinja \
    --dtype float16 \
    --api-key EMPTY \
    --tensor-parallel-size 1 \
    --pipeline-parallel-size 1 \
    --seed 100 \
    > server.log &