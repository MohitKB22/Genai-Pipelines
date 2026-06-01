class Generator:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template

    def generate_answer(self, question, context_chunks):
        prompt = self._create_prompt(question, context_chunks)
        response = self.llm.generate(prompt)
        return response

    def _create_prompt(self, question, context_chunks):
        context = "\n".join(context_chunks)
        return self.prompt_template.format(question=question, context=context)