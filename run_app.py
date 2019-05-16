from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/BotNLU')
action_endpoint = EndpointConfig(url='http://localhost:5055/webhook')
agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter, action_endpoint=action_endpoint)

input_channel = SlackInput('xoxb-628393460407-620232368865-HEJRms7SMQKDdXYbNetbO2sX')

agent.handle_channels([input_channel], 5004, serve_forever=True)

