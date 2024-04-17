import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

st.set_page_config(page_title="Gen4Edu Helper")

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


def getLLamaresponse(subject, clas, no_words,  chapter):
    
    llm = CTransformers(model=r'C:\Users\Acer\OneDrive\Desktop\model\model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 512,
                                'temperature': 1})
    template = """
        You are a very good {clas} {subject} school teacher and want to teach your students about {chapter}. Devise a lecture plan. 
            """

    prompt = PromptTemplate(input_variables=["chapter", "clas", 'no_words', 'subject'],
                            template=template)

    response = llm(prompt.format(chapter = chapter,
                    clas = clas, no_words=no_words, subject = subject))
    return response


with st.sidebar:
    st.title('Gen4Edu GPT')
    # st.subheader('Enter parameters')
    # language = st.sidebar.selectbox('Choose a language', ['English', 'Hindi', 'Punjabi', 'Marathi', 'Telugu'])
    # subject  = st.sidebar.selectbox('Choose a subject', ['Science', 'Maths', 'Social Science', 'English', 'Computer Science', 'Arts'])
    # style = st.sidebar.selectbox('You are a:', ['Student', 'Teacher', 'Researcher', 'You are just curious'])
    # no_words = st.sidebar.slider('No of words:', min_value=10, max_value=300, value=80, step=1)

def llm_write():
    st.write(getLLamaresponse(subject, clas, no_words,chapter))
    
st.title("Welcome back, Teacher")
st.subheader('Enter information to generate lesson plan')
language = st.selectbox('Choose a language', ['English', 'Hindi', 'Punjabi', 'Marathi', 'Telugu'])
subject  = st.selectbox('Choose a subject', ['Science', 'Maths', 'Social Science', 'English', 'Computer Science', 'Arts'])
clas = st.selectbox('Choose a class', ['VIII','VII','VI','V','IV','III','II','I'])
chapter = st.selectbox('Choose a chapter', ['Coal and Petroleum','Light','Some Natural Phenomena','Atoms and Molecules'])
# no_words = st.slider('No of words:', min_value=10, max_value=300, value=80, step=1)
submit = st.button('Generate', on_click=llm_write)
# # st.spinner('Generating...')
# response = 'Chutiye'
# response = getLLamaresponse(subject, clas, no_words,chapter)
# st.write(response)
# if st.button('Generate'):
#     # Code to execute when the button is pressed
#     st.spinner('Generating...')
#     response = getLLamaresponse(subject, clas, no_words,chapter)
#     st.write('generating')
#     st.write(response)
# else:
#     st.write('Sorry')
