import google.generativeai as genai

# ADD YOUR API KEY
GOOGLE_API_KEY = "YOUR-API-KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# The folllowing are python dictionaries if you don't know
# Refer https://www.w3schools.com/python/python_dictionaries.asp
studentMap = {1:"Aadhilakshmi", 2:"Aaron", 3:"Aarunya", 4:"Abhinand"}
studentHobbyMap = {1:"Drawing", 2:"Singing", 3:"Dancing", 4:"Programming"}

# THE FOLLOWING FUNCTIONS MISS `RETURNS` TRY TO ADD IT
# REFER: https://www.w3schools.com/python/python_dictionaries.asp
def getStudentName(rollNumber: int):
    """
    Returns the name of the student based on the roll number
    """
    

def getStudentHobby(rollNumber: int):
    """
    Returns the hobby of the student based on the roll number
    """
    

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", tools=[getStudentName, getStudentHobby] # Note that we are passing the functions we created to help the model 😍
)

# print(model)

chat = model.start_chat(enable_automatic_function_calling=True)

# getting prompt from the user and passing it into the model
prompt = input("Enter the prompt: ")
response = chat.send_message(prompt)

print(response.text)

# To see how actually function call works uncomment the following
# There is a nice shortcut for that, select the code block, hold CTRL+/ (forward slash) together, you can use the same to comment as well!
# for content in chat.history:
#     print(content.role, "->", [type(part).to_dict(part) for part in content.parts])
#     print("-" * 80)