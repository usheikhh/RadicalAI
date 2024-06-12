# Gemini Explorer

![Gemini]

## Mission Scenario
Create a user-friendly chat interface using Streamlit that connects with Google's state-of-the-art large language model, Gemini. The goal is to provide an accessible platform for exploring and showcasing the capabilities of advanced language models. This project aims to serve as an educational and practical introduction to integrating large language models with intuitive interfaces.

## Mission Workflow:
- Task 1: 🌐 Enable Google Cloud
- Task 2: 🧬 Google Cloud Initialization
- Task 3: ☁️ Setting up Google Gemini
- Task 4: 📊 Streamlit Integration
- Task 5: 🗣️ Adding Initial System Messages
- Task 6: 📄 Preparing Submission

## Requirments:

- Python version 3.9x or above [Python](https://www.python.org/downloads/)
- Streamlit [Streamlit Documentation](https://docs.streamlit.io/)
- Gcloud account
- Vertexai [Vertexai Documentation](https://cloud.google.com/vertex-ai)

## Task 1: 🌐 Enabling Google Cloud

- Go to the [Google Cloud Platform](https://cloud.google.com/free/?utm_source=google&utm_medium=cpc&utm_campaign=japac-IN-all-en-dr-BKWS-all-core-trial-EXA-dr-1605216&utm_content=text-ad-none-none-DEV_c-CRE_644159077391-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt+~+GCP_General_core+brand_main-KWID_43700074766895886-aud-970366092687:kwd-6458750523&userloc_9062223-network_g&utm_term=KW_google%20cloud&gad_source=1&gclid=CjwKCAjw48-vBhBbEiwAzqrZVFHOq76jh9J0dgd2lwSHL3oF20yQX_sP4TvFoe6Nw7ofMguovMUk3BoChZ4QAvD_BwE&gclsrc=aw.ds) and Select "Get Started for free".
- Sign in using your Google Account and then provide the necessary details and complete the billing requirments.
- Accept the terms and conditions.
- Complete the payment process to initialize your Google Cloud Account.
- Create a new project (for instance "RadicalAI - Gemini Explorer").
- Access the Google Cloud Console.
- Navigation -> Artificial Intelligence -> Vertex AI -> Enable All Recommended APIs

![Task 1 - Gemini Explorer]

## Task 2: 🧬 Google Cloud Initialization

- Install the Google SDK using this [Link](https://cloud.google.com/sdk/docs/install).
- Run the following command to initialize the SDK:
  ```
  gcloud init
- Sign in using your Google Account credentials.
- Select an existing project or Create a new project
- Set default compute region and zone (Optional Step)

![Task 2]

## Task 3: ☁️ Setting up Google Gemini

- Install the streamlit framework
  ```
  pip install streamlit
- Refer the Streamlit Documentation to see an [Implementation using OpenAI's ChatGPT](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)
- In the project, we are using Google's Gemini Pro LLM.
- Use the project ID instead of the project name, like this: `project = "project_id"`. This helps avoid encountering a 403 permission denied error.

![Task 3 - Gemini Explorer]

## Task 4: 📊 Streamlit Integration
- Implement the steps given in the mission.
- Run the python file `streamlit run filename.py`.

![Task 4 - Gemini Explorer]

## Task 5: 🗣️ Adding Initial System Messages

![Task 5 - Gemini Explorer]

## Task 6: 📄 Preparing Submission

 - A GitHub repository for the project containing all the project files.
 - Loom Video representing the overall approach. [Loom Link]()

##  Issues Faced
 - When testing the app for bugs, I would ask 'who are you' which would lead to the app crashing. Based on some recommendations, I changed the response_validation to 'False' when creating the chat session 

