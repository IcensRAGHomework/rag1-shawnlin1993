import json
import traceback
from pprint import pprint
from datetime import datetime  # 確保導入 datetime 模組

from model_configurations import get_model_configuration
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage


gpt_chat_version = 'gpt-4o'
gpt_config = get_model_configuration(gpt_chat_version)

def generate_hw01(question):
    llm = AzureChatOpenAI(
        model=gpt_config['model_name'],
        deployment_name=gpt_config['deployment_name'],
        openai_api_key=gpt_config['api_key'],
        openai_api_version=gpt_config['api_version'],
        azure_endpoint=gpt_config['api_base'],
        temperature=gpt_config['temperature'],          
    )
    message = HumanMessage(
        content=[
            {"type": "text", "text": question},
        ]
    )
    # 呼叫 OpenAI API
    response = llm.invoke([message])

  # 構建所需的 JSON 結構
    response_json = {
        "Result": [
            {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "name": response
            }
        ]
    }

    return response
    #pass
    
def generate_hw02(question):
    pass
    
def generate_hw03(question2, question3):
    pass
    
def generate_hw04(question):
    pass
    
def demo(question):
    llm = AzureChatOpenAI(
        model=gpt_config['model_name'],
        deployment_name=gpt_config['deployment_name'],
        openai_api_key=gpt_config['api_key'],
        openai_api_version=gpt_config['api_version'],
        azure_endpoint=gpt_config['api_base'],
        temperature=gpt_config['temperature']
    )
    message = HumanMessage(
        content=[
            {"type": "text", "text": question},
        ]
    )
    response = llm.invoke([message])
    
    return response

def demo1(question):
    llm = AzureChatOpenAI(
        model=gpt_config['model_name'],
        deployment_name=gpt_config['deployment_name'],
        openai_api_key=gpt_config['api_key'],
        openai_api_version=gpt_config['api_version'],
        azure_endpoint=gpt_config['api_base'],
        temperature=gpt_config['temperature'],          
    )
    message = HumanMessage(
        content=[
            {"type": "text", "text": question},
        ]
    )
    # 呼叫 OpenAI API
    response = llm.invoke([message])

  # 構建所需的 JSON 結構
    response_json = {
        "Result": [
            {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "name": response
            }
        ]
    }

    return response

if __name__ == '__main__':
    response = generate_hw01('2024年台灣10月紀念日有哪些?請根據json格式輸出')
    pprint(response.content)
  