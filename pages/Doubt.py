import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

st.set_page_config(page_title="GenAI4Edu Helper")

# Set page configuration
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)
# Streamlit app content


def getLLamaresponse(subject, input_text, style):
    
    llm = CTransformers(model=r'C:\Users\Acer\OneDrive\Desktop\model\model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 512,
                                'temperature': 1})
    template = """
        You are a very good {subject} school teacher, a {style} is asking you a doubt. Answer the question {input_text}. 
            """

    prompt = PromptTemplate(input_variables=["style", "input_text",  'subject'],
                            template=template)

    response = llm(prompt.format(style=style,
                    input_text=input_text, subject = subject))
    return response


with st.sidebar:
    st.title('GenAI4Edu GPT')
    st.subheader('Enter parameters')
    language = st.sidebar.selectbox('Choose a language', ['English', 'Hindi', 'Punjabi', 'Marathi', 'Telugu'])
    subject  = st.sidebar.selectbox('Choose a subject', ['Science', 'Maths', 'Social Science', 'English', 'Computer Science', 'Arts'])
    style = st.sidebar.selectbox('You are a:', ['Student', 'Teacher', 'Researcher', 'You are just curious'])
    # no_words = st.sidebar.slider('No of words:', min_value=10, max_value=300, value=80, step=1)
    # print(subject, style, no_words)

st.write("# Welcome back, Aditya!")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    print(prompt)
    response = getLLamaresponse(subject, prompt,style)
    print(response)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)