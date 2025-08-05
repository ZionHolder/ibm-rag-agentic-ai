from model import llama3_response, granite_response, mixtral_response

def call_all_models(system_prompt, user_prompt):
    llama_result = llama3_response(system_prompt, user_prompt)
    granite_result = granite_response(system_prompt, user_prompt)
    mixtral_result = mixtral_response(system_prompt, user_prompt)

    print("Llama3 Response:\n", llama_result.content)
    print("\nGranite Response:\n", granite_result.content)
    print("\nMixtral Response:\n", mixtral_result.content)

# Example call to test all models
#call_all_models("You are a helpful assistant who provides concise and accurate answers", "I've been using the Galaxy S25 Edge for a couple of weeks now, and I have to say, it's super comfortable to hold. The design just feels right in my hand. It has all the same features as the higher-end models in the lineup, no compromises there. But the real standout is the battery life; thanks to Samsung's optimizations, it easily lasts me through a full day of heavy use without needing a charge. Totally recommend it!")


