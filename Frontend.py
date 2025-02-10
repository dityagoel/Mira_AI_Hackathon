import yaml
import streamlit as st
from mira_sdk import MiraClient,Flow

def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def main():   
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #EDFFD5; /* App background */
        }
        
        .stButton>button {
            background-color: #502203; /* Change button color */
            color: white;
            border-radius: 10px;
        }
        
        
        .stTextInput>div>div>input {
        background-color: #FFFFFF !important;
        color: black !important;
        padding: 10px !important;
        }

        .stTextArea>div>div>textarea {
        background-color: #FFFFFF !important;
        color: black !important;
        padding: 10px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("BEWELLBOT :herb:")
    Markdown= '''
    ## Health bot at your rescue! :wink:
    '''
    st.write(Markdown)
    st.markdown("<p style='font-size:20px;'> Crafted with 💡 by Ditya Goel. </p>", unsafe_allow_html=True)

    # Sidebar for API key
    api_key = st.sidebar.text_input("Enter Mira AI API Key", type="password")
    instructions = st.sidebar.write("Here’s a quick setup guide for the Mira API:")
    instructions1 = st.sidebar.write("1. Open https://flows.mira.network/ and Sign Up")
    instructions2 = st.sidebar.write("2. Navigate to your account settings or dashboard")
    instructions3 = st.sidebar.write("3. Locate the section labeled 'API Keys.' and generate a new API key")
    instructions4 = st.sidebar.write("4. Copy and securely store your API key, as you'll just get to see it one. Paste that here.")

    if not api_key:
        st.warning("Please enter your Mira AI API key in the sidebar to continue.")
        return

    try:
        client = MiraClient(config={"API_KEY": api_key})
    except Exception as e:
        st.error(f"Error initializing Mira AI client: {str(e)}")
        return

    # Main Code

    st.markdown("<p style='font-size:20px;font-weight: bold;'> Hello! I am your personal health bot! </p>", unsafe_allow_html=True)
    choice = st.selectbox('Which issue would you like me to assist you with?',["Self-Checkup", "Fitness Advice", "Vaccinations for you"])

    if choice == "Self-Checkup":
        config = load_yaml("test_flow.yaml")
        flow = Flow(source=config)  # Load flow configuration
        input_dict = {}  # Prepare test input
        st.markdown("<p style='font-size:20px;'> Enter details for Self Checkup: </p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:18px;'> Note: This is a general health checkup bot, for minor issues. </p>", unsafe_allow_html=True)
        age = st.text_input("Enter age:")
        input_dict["age"] = age
        weight = st.text_input("Enter Weight(in kg):")
        input_dict["weight"] = weight
        gender = st.text_input("Enter gender(Male/Female):")
        input_dict["gender"] = gender
        symptoms= st.text_input("Enter symptoms:")
        input_dict["symptoms"] = symptoms
        if st.button("Go"):
            response = client.flow.test(flow, input_dict)  # Test flow
            st.text_area("Result:",response['result'],height=500)


    elif choice == "Fitness Advice":
        flow = Flow(source="test_flow_2.yaml")  # Load flow configuration
        input_dict = {}  # Prepare test input
        st.markdown("<p style='font-size:20px;'> Enter details for Fitness Advice: </p>", unsafe_allow_html=True)
        age = st.text_input("Enter age:")
        input_dict["age"] = age
        weight = st.text_input("Enter Weight(in kg):")
        input_dict["weight"] = weight
        gender = st.text_input("Enter gender(Male/Female):")
        input_dict["gender"] = gender
        history = st.text_input("Enter Medical History:")
        input_dict["history"] = history
        if st.button("Go"):
            response = client.flow.test(flow, input_dict)  # Test flow
            st.text_area("Result:",response['result'],height=500)

    elif choice == "Vaccinations for you":
        flow = Flow(source="test_flow_3.yaml")  # Load flow configuration
        input_dict = {}  # Prepare test input
        st.markdown("<p style='font-size:20px;'> Enter details to find list of vaccinations: </p>", unsafe_allow_html=True)
        age = st.text_input("Enter age:")
        input_dict["age"] = age
        gender = st.text_input("Enter gender(Male/Female):")
        input_dict["gender"] = gender
        history = st.text_input("Enter Medical History:")
        input_dict["history"] = history
        if st.button("Go"):
            response = client.flow.test(flow, input_dict)  # Test flow
            st.text_area("Result:",response['result'],height=500)

    else:
        pass


main()
