import json
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

class Processor:
    
    data_transform_prompt_template = PromptTemplate.from_template(
        """
        Convert this value from {source} to {target} type: \n{data}. Return as a plain text, without any code formatting.
        Respond with the converted data only, and do not include any other information.
        
        Validation Criteria: If the input data does not appear to be valid CSV or JSON Array based on the source type, 
        simple respond with an error message: "FORMAT_INVALID"
        
        Convert any spaced words in the source CSV headers to camel case keys in JSON, and camel case keys in JSON to 
        title case headers in CSV 
        """
    )
    
    def __init__(self) -> None:
        load_dotenv()
        self.model = init_chat_model(
            model="gemini-2.0-flash", 
            model_provider="google_genai"
        )
    
    async def csv_to_json(self, csv_data_bytes: bytes) -> list[dict[str, object]]:
        """
        Transforms the source CSV file to a list of dictionary
        
        Args:
            csv_data_types (bytes): The content of the csv file in the form of bytes
        
        Returns:
            str: A list of dictionaries representing the JSON transformed from the CSV
        csv
        """
        data_text = csv_data_bytes.decode()
        result_text = await self._send_llm_message('csv', 'json', data_text)
        if (result_text == 'FORMAT_INVALID'):
            raise ValueError("The provided data for CSV is invalid")
        return json.loads(result_text)
    
    async def _send_llm_message(self, source: str, target: str, data: str) -> str:
        """
        Sends the message to the LLM and retrieves the text from the LLM's response. The
        validations and rules that the transformation must adhere to are all delegated to
        the LLM, and none are actually processed locally
        
        Args:
            source (str): The source format of the data (CSV/JSON)
            target (str): The target format of the data (JSON/CSV)
            data (str): The data that is expected to be transformed

        Returns:
            str: The textual content from the LLM's response
        """
        prompt_value = self.data_transform_prompt_template.invoke(
            {
                "source": source,
                "target": target,
                "data": data
            }
        )
        result_message = await self.model.ainvoke(input=prompt_value)
        return result_message.text()
