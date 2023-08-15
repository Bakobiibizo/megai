import json
import datetime
from interfaces import Prompt, AIResponse

class PromptParser:
    @staticmethod
    def parse(prompt: Prompt):
        # Parsing the mode, model, prompts, imageUrl, base64Image, n, and size from the Prompt object
        mode = prompt.mode
        model = prompt.model
        prompts_list = prompt.prompts
        image_url = prompt.imageUrl
        base64_image = prompt.base64Image
        n = prompt.n  # Optional attribute
        size = prompt.size  # Optional attribute
        

# Defining the data parser functions

def serialize_ai_response(ai_response: AIResponse) -> str:
    """Serialize an AIResponse object to JSON string."""
    return json.dumps(ai_response.__dict__, default=str)  # Convert datetime to string if present

def deserialize_prompt(json_str: str) -> Prompt:
    """Deserialize a JSON string into a Prompt object."""
    prompt_data = json.loads(json_str)
    
    # Convert timestamp to datetime object if present
    if prompt_data.get("timestamp"):
        prompt_data["timestamp"] = datetime.fromisoformat(prompt_data["timestamp"])
    
    return Prompt(**prompt_data)

# These functions provide the necessary serialization and deserialization between the AIResponse and Prompt objects and JSON.


# Mocked version of the AIResponse class based on the provided requirements

class AIResponse:
    def __init__(self, id, mode, role, object, usage, viewer_content):
        self.id = id
        self.mode = mode
        self.role = role
        self.object = object
        self.usage = usage
        self.viewer_content = viewer_content

class AIResponseParser:
    @staticmethod
    def parse(ai_response: AIResponse):
        # Parsing the id, mode, role, object, usage, and viewer_content from the AIResponse object
        user_id = ai_response.id
        mode = ai_response.mode
        role = ai_response.role
        object_data = ai_response.object
        usage = ai_response.usage
        viewer_content = ai_response.viewer_content
        
        # Mock function to handle the parsed data (can be replaced with actual implementation)
        def mock_function(user_id, mode, role, object_data, usage, viewer_content):
            print("Handling AI response with mode:", mode)
            # Further processing logic can be added here
        
        # Calling the mock function with the parsed data
        mock_function(user_id, mode, role, object_data, usage, viewer_content)

# Example usage of the AIResponseParser
ai_response_example = AIResponse("user_id", "image", "assistant", {"created": 1589478378, "data": [{"url": "https://..."}]}, "usage_data", "viewer_content")
AIResponseParser.parse(ai_response_example)
