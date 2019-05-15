# Trains a simple dialogue management model
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent                               # Trains the Model
from rasa_core.policies.keras_policy import KerasPolicy         # Models used to train
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig


def run_online(interpreter, domain_file="domain.yml", training_data_file='data/stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    model_path = './models/dialogue'            # Where to save the model after its trained
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy(max_history=3, epochs=100, batch_size=50)],
                  interpreter=interpreter,
                  action_endpoint=action_endpoint)
    data = agent.load_data(training_data_file, augmentation_factor=50)
    agent.train(data)
    agent.persist(model_path)  # Save the Model
    interactive.run_interactive_learning(agent, training_data_file, skip_visualization=True)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/BotNLU')
    run_online(nlu_interpreter)

