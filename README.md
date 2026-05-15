# RPG-CLI-Etrian-
Text based RPG using the Qwen
HF Transformers
Lora Fine Tunning
Requirements: Currently Built to work on a RTX 4070 Mobile


Tech Reference: 
https://mlflow.org/
Potential addition of TurboQuant

CLI Reefrences:
https://typer.tiangolo.com/reference/

CLI:
- [ ] create a simple cli
- [ ] possible "UI" needed for the cli for the entry of the program
WIP:
- [ ] Get RPG text data
- [ ] Fine tune on RPG text data and get LoRA files
- [ ] Limit scope, add system to enable restrict user input or diable for OP mode
- [ ] Create Drpg as demo (start with a dueogeon RPG)
- [x] Choose either Go (for cli built-ins) or python 
- [ ] Create API and design rpg system
- [ ] Support user created story frameworks (community matters)

Future:
- [ ] Possible addition of Chibi with visuals
- [ ] Possible addition of music or SFX
- [ ] User and community support of custom stories with vote system and search


Current Ideas:
Depending on users hardware, can have both a system and narritivare model, one can handle the in game logic and apis while other is pure dialoge 


Current "Docs": 
Actions are standered, however to conduct your dialouge we have a unique system. After writing the action you choose, use either * or ~ or both ~*. ~ indicates that the action is taken during the dialogue, * indicates that the action is taken after and ~* is during the dialouge.





!!!NEW!!!
Chaning the model to Qwen, will need short and long term memory + RAG for each new additional load to the game
