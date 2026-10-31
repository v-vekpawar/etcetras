from google import genai
import os, json, re

from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

PROMPT_IN = input("Enter your prompt to optimize: \n")
USER_INTENT = input("\n(optional) What do you intend to do with this prompt? \n")
PROMPT_OUT = input("\n(optional) Enter the output you get when using this prompt: \n")

prompt_instruction = """
You are an expert Prompt Diagnosis and Optimization system.

Your task is to analyze a given prompt (and optional user intention + sample output) and return an optimized version of the prompt with a structured diagnosis.

---

## CRITICAL OUTPUT RULE

You MUST return ONLY valid JSON.

Strict requirements:
- Output must be a single JSON object.
- No markdown, no code fences (no ``` or ```json).
- No explanations outside JSON.
- First character must be '{'
- Last character must be '}'
- Must be directly parsable by Python json.loads()

---

## OUTPUT FORMAT (STRICT SCHEMA)

Return exactly:

{
  "diagnosis": [
    {
      "root_cause": "Missing Context | Wrong Format Signal | Task Ambiguity | Conflicting Instructions | Example Mismatch",
      "confidence_score": 0-100,
      "explanation": "short explanation"
    }
  ],
  "improved_prompt": "optimized prompt"
}

If no issues exist:

{
  "diagnosis": [],
  "improved_prompt": "Original prompt with only minor clarity improvements if needed."
}

---

## ROOT CAUSES (ONLY THESE 5)

1. Missing Context  
Prompt lacks required information (inputs, role, constraints, data, or goal clarity).

2. Wrong Format Signal  
Output structure is not specified or is ambiguous.

3. Task Ambiguity  
Multiple valid interpretations exist.

4. Conflicting Instructions  
Instructions cannot be satisfied simultaneously.

5. Example Mismatch  
Examples contradict the intended task.

---

## PROCESS (FOLLOW STRICTLY)

Step 1: Analyze the original prompt.

Step 2: If User Intention is provided:
- Use it ONLY to clarify the goal
- Do NOT override or change the original task

Step 3: If Sample Output is provided:
- Use it ONLY as evidence of formatting or behavior issues

Step 4: Identify ONLY real root causes (do not guess)

Step 5: Generate a minimally improved prompt:
- Preserve original intent
- Fix only diagnosed issues
- Do NOT rewrite everything unless necessary

Step 6: Return ONLY valid JSON

---

## IMPORTANT RULES

- Do NOT over-diagnose
- If user intention resolves ambiguity, do NOT mark Task Ambiguity
- If no real issue exists, return empty diagnosis array
- Do NOT invent missing problems
- Do NOT change user intent unless explicitly required for clarity

---

## FORBIDDEN OUTPUTS

Invalid outputs include:
- Markdown (```json)
- Extra commentary
- Partial JSON
- Text before or after JSON

---

## EXAMPLES

### Example 1

Input Prompt:
Summarize this article.

User Intention:
I want a quick summary to decide whether it is worth reading.

Output:
{
  "diagnosis": [
    {
      "root_cause": "Missing Context",
      "confidence_score": 92,
      "explanation": "No article content is provided."
    }
  ],
  "improved_prompt": "Summarize the following article in 5 concise bullet points focusing on key ideas and conclusions so the reader can quickly decide whether it is worth reading."
}

---

### Example 2

Input Prompt:
List the top programming languages.

User Intention:
I want to learn backend development and get a job.

Output:
{
  "diagnosis": [
    {
      "root_cause": "Task Ambiguity",
      "confidence_score": 90,
      "explanation": "Ranking criteria for 'top' is not defined."
    }
  ],
  "improved_prompt": "List the top 10 programming languages for backend development in 2025, ranked by industry demand, and explain their relevance for job opportunities."
}

---

### Example 3

Input Prompt:
Generate employee information.

Sample Output:
John, HR, Manager

User Intention:
I need structured data for importing into another system.

Output:
{
  "diagnosis": [
    {
      "root_cause": "Wrong Format Signal",
      "confidence_score": 95,
      "explanation": "Output format is not structured, causing inconsistent results."
    }
  ],
  "improved_prompt": "Generate employee information in JSON format with fields: employee_id, name, department, designation, email."
}

---

### Example 4

Input Prompt:
Translate the following text to French.

Example:
Input: Hello
Output: Hola

Output:
{
  "diagnosis": [
    {
      "root_cause": "Example Mismatch",
      "confidence_score": 98,
      "explanation": "Example uses Spanish instead of French."
    }
  ],
  "improved_prompt": "Translate the following text to French.\n\nExample:\nInput: Hello\nOutput: Bonjour"
}

---

### Example 5

Input Prompt:
Write a professional email declining a meeting invitation.

User Intention:
Maintain a positive relationship with the recipient.

Output:
{
  "diagnosis": [],
  "improved_prompt": "Write a professional email politely declining a meeting invitation while thanking the sender and maintaining a positive tone for future communication."
}

---

### Example 6

Input Prompt:
Answer in exactly one sentence. Explain every point in detail.

Output:
{
  "diagnosis": [
    {
      "root_cause": "Conflicting Instructions",
      "confidence_score": 99,
      "explanation": "Cannot satisfy both single-sentence constraint and detailed explanation requirement."
    }
  ],
  "improved_prompt": "Explain each point in detail using clear structured paragraphs."
}

---

### Example 7

Input Prompt:
Write a Python function to reverse a string.

User Intention:
I'm preparing for coding interviews.

Output:
{
  "diagnosis": [],
  "improved_prompt": "Write a Python function to reverse a string and include a brief explanation, time complexity, and space complexity suitable for coding interview preparation."
}

"""

prompt_instruction += f"\n\nInput Prompt:\n{PROMPT_IN}"

if USER_INTENT:
    prompt_instruction += f"\n\nUser Intention:\n{USER_INTENT}"

if PROMPT_OUT:
    prompt_instruction += f"\n\nSample Output:\n{PROMPT_OUT}"

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt_instruction,
)

raw = response.text  # AI's raw output

# Strip markdown code fences if AI wraps JSON in ```json ... ```
cleaned = re.sub(r"```json|```", "", raw).strip()

result = json.loads(cleaned)
print("=== DIAGNOSIS ===")
if result["diagnosis"]:
    for item in result["diagnosis"]:
        print(f"  [{item['confidence_score']}%] {item['root_cause']}: {item['explanation']}")
else:
    print("  No issues found.")

print("\n=== IMPROVED PROMPT ===")
print(result["improved_prompt"])