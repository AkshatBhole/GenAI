from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.prompts import PromptTemplate
from secret_key import gemini_key
import os

os.environ["GOOGLE_API_KEY"] = gemini_key


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)




def generate_name_and_menu(cuisine):
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

    prompt_template_name= PromptTemplate(
        input_variables=[ "cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest only one fancy name for this."
    )

    prompt_template_name.format(cuisine="nagpur")

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # 2nd chain 

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

    prompt_template_name= PromptTemplate(
        input_variables=[ "restaurant_name"],
        template="suggest some menu items for {restaurant_name} food."
    )

    fooditem_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="menu_items")


    chain = SequentialChain(
        chains=[name_chain, fooditem_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )
    response = chain({"cuisine": cuisine})
    return response

if __name__ == "__main__":
    print(generate_name_and_menu("Indian"))
    