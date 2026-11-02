def get_langchain_llm(llm_api:str):
  if llm_api == "openai":
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    return llm

  elif llm_api == "gemini":
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-4-argon", temperature=0)
    return llm

  elif llm_api == "ollama": #requires to run ollama local server, hence doesnt require API_KEY
    from langchain_ollama import ChatOllama
    llm = ChatOllama(model="gemma2:2b", temperature=0)
    return llm


  else: # "groq"
    from langchain_groq import ChatGroq
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)
    return llm