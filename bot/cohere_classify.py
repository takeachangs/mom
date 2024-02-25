import cohere
from utils.constants import CLASSIFIER_EXAMPLES

class CohereClassify:
    def __init__(self):
        """
        Initialize Cohere client
        """
        self.co = cohere.Client("6yJnofp1XcVL54HTVCh19zBlXnGLuDm9GdAqyQJi")
        self.model = "embed-english-v2.0"
        self.examples = CLASSIFIER_EXAMPLES

    def classify_message(self, message):
        """
        Get response from Cohere API in dictionary format
        """
        response = self.co.classify(
            inputs=[message],
            examples = self.examples
        )
        return response.classifications[0].prediction
            
