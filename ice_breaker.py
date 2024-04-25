from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import os
import json

if __name__ == "__main__":
    load_dotenv()

    print("Hello Langchain")

    information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world; as of April 2024, Forbes estimates his net worth to be $178 billion.[4]
"""

    summary_template = """
    given the information {information} about a person I want you to create :
    1. A short summary
    2. two interesting facts about them
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables = ["information"],
        template = summary_template
    )

    llm = ChatOpenAI(temperature = 1, model_name = "gpt-3.5-turbo")
    chain = LLMChain(llm = llm, prompt = summary_prompt_template)
    res = chain.invoke(input = {"information" : information})
    
    response = json.dumps(res)

    with open("/Langchain/ICE_BREAKER/response.txt", "w") as f:
        f.write(response)


    
    