import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.load_ui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graphs.graphbuilder import GraphBuilder
def load_langgraph__agenticai_app():
    """
    Loads and runs the Agentic AI application with StreamlitUI.
    This fucntion initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while,
    implementing exception handling and robustness

    """

    ##LOAD UI

    ui =  LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error!! Failed to load user input from the UI")
        return
    
    user_message = st.chat_input("Enter your message")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input= user_input)
            model = obj_llm_config.get_llm_model()
            if not model:
                st.error("LLM MODEL COULD NOT BE INITIALIZED")
                return
            
            usecase = user_input.get("Selected_Usecase")
            if not usecase:
                st.error("NO USECASE SELECTED")
                return 
            
            graph_builder = GraphBuilder(model)
            try: 
                graph = graph_builder.setup_graph(usecase)
            except Exception as e:
                st.error(f"Error : graph set up Failed - {e}")

        except Exception as e:
            st.error(f" ERROR {e}")



