FROM tiangolo/uvicorn-gunicorn:python3.7

# 
WORKDIR /fastapi

# 
COPY ./requirements.txt /fastapi/requirements.txt

# 
RUN pip install --no-cache-dir -r /fastapi/requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

# 
COPY ./app /fastapi/app

# 
EXPOSE 8080