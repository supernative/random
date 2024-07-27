import networkx as nx
import google.generativeai as genai

def upload_to_gemini(path, mime_type=None):
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def set_config(temperature, top_p, top_k, max_output_tokens, stop_sequences, response_mime_type):
    config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
        "stop_sequences": stop_sequences,
        "response_mime_type": response_mime_type
    }
    return config 

def prepare_model(model_name, generation_config, system_instruction):
    model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config, system_instruction=system_instruction)
    return model

def start_session(model, history=[]):
    chat = model.start_chat(history=history)
    return chat

def send_message(session, text):
    response = session.send_message(text)
    return response

def view_text(response):
    return response.text
    
class Group(nx.Graph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agents = {}
        self.tasks = {}

    def add_agent(self, agent):
        self.agents[agent.name] = agent
        self.add_node(agent.name)

    def add_task(self, task):
        self.tasks[task.name] = task
        self.add_node(task.name)

    def connect(self, agent_name, task_name):
        self.add_edge(agent_name, task_name)

    def run_task(self, task_name, agent_name):
        task = self.tasks[task_name]
        agent = self.agents[agent_name]
        return task.run(agent)

class Agent:
    def __init__(self, name, model_name, generation_config, system_instruction):
        self.name = name
        self.model = prepare_model(model_name, generation_config, system_instruction)
        self.session = start_session(self.model)

    def send_message(self, text):
        response = send_message(self.session, text)
        return view_text(response)

class Task:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def run(self, agent):
        return self.function(agent)

def close_loop(agent):
    while True:
        user_input = input(f"{agent.name}: ")
        response = agent.send_message(user_input)
        print(f"{agent.name}: {response}")
        if "end" in user_input.lower():
            break

# Example usage
group = Group()

# Create agents
agent1 = Agent("Agent 1", "models/text-bison@001", set_config(temperature=0.7, top_p=0.95, top_k=40, max_output_tokens=100, stop_sequences=["\n"], response_mime_type="text/plain"), "You are a helpful and polite chat assistant.")
agent2 = Agent("Agent 2", "models/text-bison@001", set_config(temperature=0.7, top_p=0.95, top_k=40, max_output_tokens=100, stop_sequences=["\n"], response_mime_type="text/plain"), "You are a helpful and polite chat assistant.")
group.add_agent(agent1)
group.add_agent(agent2)

# Create tasks
close_loop_task = Task("Close Loop", close_loop)
group.add_task(close_loop_task)

# Connect agents to tasks
group.connect("Agent 1", "Close Loop")
group.connect("Agent 2", "Close Loop")

# Run the tasks
group.run_task("Close Loop", "Agent 1")
group.run_task("Close Loop", "Agent 2")

print(group.nodes)
print(group.edges)
