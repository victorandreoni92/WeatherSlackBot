# Base AWS Lambda image for Python 3.8
FROM public.ecr.aws/lambda/python:3.8

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY bot/ .

# Define command to run upon container start
CMD ["bot.handler"]