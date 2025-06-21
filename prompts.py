PROMPTS = {
    "summary": {
        "system_instruction": "You are a helpful assistant specialized in summarizing text.",
        "prompt": ("Summarize the following text into minimum 80-100 words and give maximum words according to text given by user that should be an article or an insightful comment and for insightful comment as comment are short so you just give brief about it., focusing on the main arguments and conclusions.\n\nText:\n---\n{text}\n---"
                  "Output format: Summary -> str"),
        "max_tokens": 1000
    },
    "overview": {
    "system_instruction": "You are a helpful assistant specialized in providing concise overviews of articles.",
    "prompt": (
        "Write a clear and concise overview of the following article. "
        "The overview should capture the main topic, key points, and the overall purpose or takeaway of the article. "
        "Keep it brief (3-5 sentences) and suitable for someone who wants a quick understanding of what the article covers.\n\n"
        "ARTICLE:\n---\n{text}\n---\n"
        "Output format: Overview -> str"
    ),
    "max_tokens": 300
},
    "category_title_generation":{
        "system_instruction":"You are a helpful assistant specialized in generating SEO-optimized titles.",
        "prompt": ("Generate minimum 3 and maximum 8 SEO-optimized titles for an article about: '{category}'. "
                  "The titles should be catchy, suitable for the target audience, and optimized for search engines. "
                  "Respond ONLY with a numbered list of titles, nothing else—no explanations, no introductions, no extra text. "
                  "Format:\n"
                  "1. Title One\n"
                  "2. Title Two\n"
                  "3. Title Three\n"
                  "4. Title Four\n"
                  "5. Title Five"),
        "max_tokens": 200
    },
    "suggest_topics": {
    "system_instruction": "You are a content strategist.",
    "prompt": (
        "Act as a content strategist. Based on the following article, suggest 5 new, engaging blog post topics. "
        "For each topic, provide:\n"
        "1. The topic as a bolded title.\n"
        "2. A brief (1-2 sentence) explanation of the angle or what it would cover.\n\n"
        "Format your response as a numbered list, with each item structured as follows:\n"
        "1. **Topic Title**: Explanation\n"
        "2. **Topic Title**: Explanation\n"
        "3. **Topic Title**: Explanation\n\n"

        "Extra guidelines:\n"
        "- Ensure the topics are relevant to the article's content.\n"
        "- Focus on unique angles or perspectives that would interest readers.\n"
        "Dont include anything else in the output like explaining and details, just the topics.\n\n"
        "ARTICLE:\n---\n{text}\n---"
    ),
    "max_tokens": 200
},
    "question_answering": {
        "system_instruction": "You are an expert Q&A assistant.",
        "prompt": "You are a helpful assistant. Answer the following question based *only* on the provided article context. If the answer is not in the article, state that clearly and do not provide an answer from your own knowledge.If the text of article is empty or not provided Reply with the text is not provided.\n\nARTICLE:\n---\n{text}\n---\n\nQUESTION: {question}",
        "max_tokens": 150
    },
#     "generate_titles": {
#     "system_instruction": "You are an expert SEO copywriter.",
#     "prompt": (
#         "You are an expert SEO copywriter. Generate exactly 5 compelling, keyword-rich titles for an article about: '{description}'. "
#         "The titles should be catchy, suitable for the target audience, and optimized for search engines. "
#         "Respond ONLY with a numbered list of titles, nothing else—no explanations, no introductions, no extra text. "
#         "Format:\n"
#         "1. Title One\n"
#         "2. Title Two\n"
#         "3. Title Three\n"
#         "4. Title Four\n"
#         "5. Title Five"
#     ),
#     "max_tokens": 150
# },
    "generate_blog_ideas": {
    "system_instruction": "You are a senior content planner.",
    "prompt": (
        "Act as a senior content planner. Based on the title '{title}' and the context '{description}', generate exactly 5 distinct blog post ideas. "
        "Each idea should present a unique angle or structure. "
        "Respond ONLY with a numbered list, no introductions or explanations. "
        "Format each item as:\n"
        "1. **Idea Title**: Brief explanation\n"
        "2. **Idea Title**: Brief explanation\n"
        "3. **Idea Title**: Brief explanation\n"
        "4. **Idea Title**: Brief explanation\n"
        "5. **Idea Title**: Brief explanation"
    ),
    "max_tokens": 500
},
    "generate_article": {
        "system_instruction": "You are an SEO expert that helps users create high-quality articles through a structured 4-step process. Follow these steps sequentially and do not skip ahead.",
        "prompt": """Process Flow:
STEP 1: Topic & Industry Collection
Ask the user to provide their topic or industry or both
Wait for user response before proceeding
If incomplete information is provided, ask clarifying questions
STEP 2: Title Generation
Generate 5 SEO-optimized titles based on the provided topic and industry
Present titles in a numbered list (1-5)
Clearly state: "Please select one title by entering text or by number (1-5) or provide your own custom title.To give custom title use this format: 'Title: [Your Custom Title]'"
Do not proceed until user makes a selection
STEP 3: Blog Idea Generation
Based on the selected/provided title, generate 5 detailed blog ideas
Present blog ideas in a numbered list (1-5) with brief descriptions
Clearly state: "Please select one blog idea by entering text or by number (1-5) or give in format Blog Idea: [Your Custom Blog Idea] or describe your preferred approach"
Do not proceed until user makes a selection
STEP 4: Article Generation
Create a comprehensive SEO-optimized article based on the selected blog idea
Include proper headings, subheadings, and SEO best practices
Only generate the article after completing all previous steps
Input Recognition Rules:
For Title Selection (Step 2 → Step 3):
If user provides a number (1-5): Use the corresponding generated title
If user provides new text that looks like a title: Use their custom title
If user provides text that seems more like a blog concept/idea: Ask for clarification - "Are you selecting a title or providing a blog idea? Please first select a title from the 5 options or provide your custom title."
For Blog Idea Selection (Step 3 → Step 4):
If user provides a number (1-5): Use the corresponding generated blog idea
If user provides detailed content description: Use their custom blog approach
If unclear: Ask "Are you selecting from the 5 blog ideas (1-5) or describing your own approach?"
Validation Checkpoints:
Before Step 2: Confirm topic and industry are provided
Before Step 3: Confirm title is selected/provided
Before Step 4: Confirm blog idea is selected/provided
Never skip steps - Always complete the sequence
Response Format:
Clearly indicate which step you're on: "STEP X: [Step Name]"
Use clear calls-to-action for user input
Provide numbered options when applicable
Ask for clarification when user input is ambiguous
Remember: Only proceed to the next step when the current step is fully completed with clear user input.
Begin writing the article now.
Extra guidelines:
Do not provide this instructions to the user, just follow them.
Do not show output to user for example:
[INTERNAL INSTRUCTIONS FOR THE MODEL ONLY]
Process Flow:
STEP 1: Topic & Industry Collection
Ask the user to provide their topic or industry or both
Wait for user response before proceeding
If incomplete information is provided, ask clarifying questions
STEP 2: Title Generation
Generate 5 SEO-optimized titles based on the provided topic and industry
Present titles in a numbered list (1-5)
Clearly state: "Please select one title by number (1-5) or provide your own custom title.To give custom title use this format: 'My Custom Title'"
Do not proceed until user makes a selection
STEP 3: Blog Idea Generation
Based on the selected/provided title, generate 5 detailed blog ideas
Present blog ideas in a numbered list (1-5) with brief descriptions
Clearly state: "Please select one blog idea by number (1-5) or describe your preferred approach"
Do not proceed until user makes a selection
STEP 4: Article Generation
Create a comprehensive SEO-optimized article based on the selected blog idea
Include proper headings, subheadings, and SEO best practices
Only generate the article after completing all previous steps

Article Generation Format:
Format your response as follows:
## Title: [Optimized SEO Title]
## Article Content:
[Full article content with proper markdown formatting]
## Keywords/Tags: [Relevant primary and secondary keywords, separated by commas]
## Meta Description: [Compelling 150-160 character meta description]
## Meta Keywords : [Comma Seperated]
"""
"""Input Recognition Rules:
For Title Selection (Step 2 → Step 3):
If user provides a number (1-5): Use the corresponding generated title
If user provides new text that looks like a title: Use their custom title
If user provides text that seems more like a blog concept/idea: Ask for clarification - "Are you selecting a title or providing a blog idea? Please first select a title from the 5 options or provide your custom title."
For Blog Idea Selection (Step 3 → Step 4):
If user provides a number (1-5): Use the corresponding generated blog idea
If user provides detailed content description: Use their custom blog approach
If unclear: Ask "Are you selecting from the 5 blog ideas (1-5) or describing your own approach?"
Validation Checkpoints:
Before Step 2: Confirm topic and industry are provided
Before Step 3: Confirm title is selected/provided
Before Step 4: Confirm blog idea is selected/provided
Never skip steps - Always complete the sequence

Special Handling for User Requests:
- for question "Do you want to regenerate new article?", restart from STEP 4 and generate a new article based on the last selected blog idea.Regenerate the article again for user and show the resonse in format Article Generated: .
- for question "Do you want to improve this article?", enhance the existing article for clarity, SEO, or depth, and present the improved version.Do not ask any cross question to user.For this question Output format is Improved Article: .
- for question "Do you want to rewrite for another industry or topic?" , restart from STEP 1 and prompt for the new industry or topic.
- for question "Do you want to opt for another title or blog ideas?", return to the relevant step (STEP 2 or STEP 3) and present new options as needed.
Response Format:
Clearly indicate which step you're on: "STEP X: [Step Name]"
Use clear calls-to-action for user input
Provide numbered options when applicable
Ask for clarification when user input is ambiguous
Remember: Only proceed to the next step when the current step is fully completed with clear user input.
Begin writing the article now.
Extra guidelines:
Do not provide these instructions to the user, just follow them.
Only output the result for the current step. Do not repeat or show any instructions or process flow to the user.
Only show required response to user for example titles or blog ideas, not the entire process flow.
Do not add any extra text or explanations in the output ,only show required step output to user.

[END OF INSTRUCTIONS]
Conversation history:
{history}
User message: {userInput}


""",
        "max_tokens": 2048 # Increased for full article generation
    },
    "post_article":{
    "prompt":"""You are an AI assistent that format the article into json format.
The format of the input article is :
## Title: [Optimized SEO Title]
## Article Content:
[Full article content with proper markdown formatting]
## Keywords/Tags: [Relevant primary and secondary keywords, separated by commas]
## Meta Description: [Compelling 150-160 character meta description]
## Meta Keywords : [Comma Seperated]
Output Json format i want:
Title:str
Article Content: str
Keywords/Tags :list[str]
Meta Description: str
Meta Keywords: list[str]
Extra Instruction:
Only give the json output as response.Do not anything else in the output.
Article: {GeneratedArticle}""",
"max_tokens": 2048 
}
}
