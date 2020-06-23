import os
import time
import fasttext

from utils.logging_util import Logger

LOGGER = Logger.get_instance()


class ClassifierTraining:
    """
    This class contains the code to train the model to be hosted in web service.

    :Author: Pranay Chandekar
    """

    @staticmethod
    def train_classifier():
        """
        This method loads the data, trains the model and saves the model in path "resources/model" for web service.
        """
        # Step 01: Set the data paths
        resources_path = "resources"

        data_path = os.path.join(resources_path, "data")
        train_file_path = os.path.join(data_path, "cooking.train")
        test_file_path = os.path.join(data_path, "cooking.valid")

        # Step 02: Train the model.
        model = fasttext.train_supervised(
            input=train_file_path,
            lr=1.0,
            epoch=100,
            wordNgrams=2,
            bucket=200000,
            dim=50,
            loss="hs",
        )

        # Step 03: Evaluate the model on validation data.
        LOGGER.logger.info(
            "Validation Metrics: " + str(model.test(test_file_path)) + "\n"
        )

        # Step 04: Save the model.
        model_directory = os.path.join(resources_path, "model")
        model_file_path = os.path.join(model_directory, "model.bin")
        model.save_model(model_file_path)


if __name__ == "__main__":
    tic = time.time()

    ClassifierTraining.train_classifier()

    toc = time.time()

    LOGGER.logger.info(
        "Total time taken to train the classifier: " + str(toc - tic) + " seconds.\n"
    )
