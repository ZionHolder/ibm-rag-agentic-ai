from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

credentials = Credentials(
    url= "https://us-south.ml.cloud.ibm.com",
    # api_key = "<YOUR_API_KEY>" # Normally you'd put an API key here, but we've got you covered here    
)

params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 100
}

model = ModelInference(
    model_id='ibm/granite-13b-instruct-v2',
    params=params,
    credentials=credentials,
    project_id="skills-network"
)

text = """
<|system|>
You are an expert assistant who provides concise and accurate answers.<|eot_id|>

<|user|>
What is the capital of Canada?

<|assistant|>
Answer:
"""

print(model.generate(text)['results'][0]['generated_text'])