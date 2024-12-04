# E2EStack
End 2 End Stack for AI Automation and Integrations

## Develop Steps for E2EApp

```
cd E2EApp/E2EApp

./gradlew run
```

## Prerequisites

```
python3 -m venv venv

source venv/bin/activate

# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip using Python directly
python3 get-pip.py

# Clean up
rm get-pip.py

pip install langchain langchain-community python-dotenv openai

cd E2EStack

python main.py

```


## Prerequisites for E2EPydantic 
* Steps for getting started with PydanticAI

```
python3 -m venv venv

source venv/bin/activate

# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip using Python directly
python3 get-pip.py

# Clean up
rm get-pip.py

pip install pydantic-ai yfinance gradio python-dotenv
```


## Running E2EPydantic

```
cd E2EPydantic

python ui.py
```