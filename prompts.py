from langchain_core.prompts import PromptTemplate

data = PromptTemplate(template="""this is the main prompt what is your name{name} what is your age {age}""", input_variables= ['name', 'age'],
                      validate_template= True)

data.save('template.json')
