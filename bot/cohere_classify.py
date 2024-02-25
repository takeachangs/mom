import cohere
from utils.constants import PREAMBLE

class CohereGenerate:
    def __init__(self):
        """
        Initialize Cohere client
        """
        self.co = cohere.Client("6yJnofp1XcVL54HTVCh19zBlXnGLuDm9GdAqyQJi")
        self.model = "embed-english-v2.0"
        self.examples = PREAMBLE

        def classify_message(self, message):
            """
            Get response from Cohere API in dictionary format
            """
            response = self.co.generate(
                examples = self.examples,
                prompt = message
            )
            return response.classifications[0].prediction
            
