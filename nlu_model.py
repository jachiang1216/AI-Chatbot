from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)         # Load Training Examples stored in json file
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)            # Train using training data
    model_directory = trainer.persist(model_dir, fixed_model_name="BotNLU")    # Initialize Model Directory


def run_nlu():      # Run the Model and  Test it
   interpreter = Interpreter.load('./models/nlu/default/BotNLU')  # Load Model


# Before main is executed, it first defines __name__ variable and assigns it '__main__'
if __name__ == "__main__":
    train_nlu(data="./data/data.json", config_file="config_spacy.json", model_dir="./models/nlu")
    run_nlu()







