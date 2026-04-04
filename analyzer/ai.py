from langchain_ollama import ChatOllama
import scraper


JSON = """
{
    "overview": "(Descrione generale del ruolo lavorativo scelta come input)",
    "skills": [
        {"skill": "(nome skill1)", "desc": "(Descrizione della skill)","relevance":(quanto è richiesta da 1 a 10, 10= molto richiesta),"difficulty":(quanto è difficile, da 1 a 10, 10= molto difficile)},
        {"skill": "(nome skill2)","desc": "(Descrizione della skill)","relevance":(quanto è richiesta da 1 a 10, 10= molto richiesta),"difficulty":(quanto è difficile, da 1 a 10, 10= molto difficile)}
    ]
}
"""

class ai():
    def __init__(self):
        lcmodel =ChatOllama(model="gemma3:1b",temperature=0,reasoning =False)
        context =[('system',f"Take the following text and respond only with a json in the following format: {JSON}")]
        
    def ask(self, input):
        context.append(("human","Come faccio  ad essere promosso?"))

        response =lcmodel.invoke(context)