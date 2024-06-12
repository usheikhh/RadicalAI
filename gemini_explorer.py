import vertexai
import streamlit as st 
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

#my project name
project = "gemini-explorer-424819"
#enabling the project through vertexai.init, and passing in the project from there
vertexai.init(project = project) 

#setting up a config. generative_models object with GenerationConfig attribute 
#can access what to pass in at @ https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig
config = generative_models.GenerationConfig(
    temperature = 0.4
)

#creating the model:
#creating a new GenerativeModel object
model = GenerativeModel(
    #passing in model_name and generation_config
    "gemini-pro",
    generation_config= config
)

#creating the chat session
chat = model.start_chat(response_validation=False) #I ran into a bug when I asked the model who are you and this was the fix.
                                                    #I wonder what other implications this has 


#helper function to display and send streamlit messages. Will serve as a way to display and store the messages that will be incoming 
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query) #going to store the response and sending the query over to the chat session
    output = response.candidates[0].content.parts[0].text #from there we get the actual text output 


    with st.chat_message("model"):
        st.markdown(output) #model.markdown; telling the stream to create a chat message from this output and applying it to the chat session

#displaying and sending stream messages:
    st.session_state.messages.append( #going to append in the session memory that the user had made a query 
        {
            "role": "user",
            "content": query
        }
    )

    st.session_state.messages.append(#from there we are going to append the models output
        {
            "role": "model",
            "content": output
        }
    )

#setting the title 
st.title("Gemini Explorer")

#initialize chat history 
if "messages" not in st.session_state: #if messages empty, set messages to be an empty array 
    st.session_state.messages = []

#display and load  chat history
for index, message in enumerate(st.session_state.messages): #for every message that is in within the state memory, we're going to enumerate through them
    content = Content( #create content that has this content object/class with 2 parameters: role & parts
        role = message["role"], #this is role that we had set from earlier in 'messages.append'
        parts = [Part.from_text(message["content"])] #this is the content from earlier 
    )

    #we are creating this content object to pass into the chat history; this helps make it a multi-turn convo rather than a single-turn
    chat.history.append(content)

 #giving the user options to select a theme from 
def initialPrompt() -> str:
    option = st.selectbox( #setting a box to choose a theme from 
    'Please choose one of the following options:',
    ('','Standard', 'Pirate', 'GenZ')
    )

    initial_prompt_options = { 
        "Standard": "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive. Ask for the user's name",
        "Pirate": "Introduce yourself as ReX, an assistant powered by Google Gemini. You speak like a pirate and use emojis to be interactive. Ask for the user's name",
        "GenZ": "Introduce yourself as ReX, a cool assistant powered by Google Gemini. Vibe and chat with emojis! 😎✌️. Speak like someone from genZ. Ask for the user's name"
    }

    #setting the inital prompts to send based on input 
    if option == 'Standard':
        initial_prompt = initial_prompt_options["Standard"]
        return initial_prompt
    elif option == 'Pirate':
        initial_prompt = initial_prompt_options["Pirate"]
        return initial_prompt
    elif option == 'GenZ':
        initial_prompt = initial_prompt_options["Standard"]
        return initial_prompt

    

# For initial message startup 
if len(st.session_state.messages) == 0:
    #setting the theme before sending initial message 
    prompt = initialPrompt()
    if prompt:
        llm_function(chat, prompt)

#to capture user input:
query = st.chat_input("Gemini Explorer")

#if there is an input
if query:
    with st.chat_message("user"): #we're going to send the role 
        st.markdown(query) #and then add that to the actual session
    llm_function(chat,query) #and then call the helper function once again to actually add these messages into the chat model itslef
