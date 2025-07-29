### Graded Quiz 2 Debrief

✅ Confirmed:
- The CommaSeparatedOutputParser is used to convert an LLM's response into CSV format in LangChain
- The FewShotPromptTemplate in LangChain provides specific examples or shots from LLMs, guiding the model to generate the requested output.
- LCEL uses the pipe (|) operator to connect components in a chain, allowing for a more intuitive and functional programming approach.

🧠 Clarified:
- The proper sequence for creating an LCEL pattern is Defining a template with variables -> Creating a PromptTemplate -> Build a chain using the pipe operator -> Invoke with input values
- Agents use the LLM to determine actions and then integrate with tools such as databases or websites to fulfil requests.
- The primary purpose of tect splitting is to divide long documents into smaller chunks that can fit within the limited context window of language models.
- LangChain uses memory to read adnd write historical data, ensuring continuity and context preservation across interactions.

🔄 Still need:
- Nothing to revisit
