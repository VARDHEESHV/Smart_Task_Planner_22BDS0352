import google.generativeai as genai
import os

def generate_plan(user_goal: str):
    """
    Generates a task plan using the Gemini API.

    Args:
        user_goal: The goal input by the user.

    Returns:
        A string containing the generated plan in Markdown format.
    """
    try:
        # SECURITY FIX: Load the API key from an environment variable.
        # This is the safest way to handle secrets in production apps.
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        
        genai.configure(api_key=api_key)

        # Model configuration
        generation_config = {
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        # API FIX: Use the widely supported and current 'gemini-2.5-flash' model name.
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            generation_config=generation_config
        )

        # The prompt is structured to guide the LLM to produce a detailed and well-formatted plan.
        prompt = f"""
        You are an expert project manager and strategic planner. Your task is to break down a high-level user goal into a detailed, actionable plan. The plan should be comprehensive, logical, and easy to follow.

        **User Goal:** "{user_goal}"

        Please generate a plan with the following structure in Markdown format:

        ### **Project Plan: [A concise and inspiring title for the goal]**

        **Overall Timeline:** [Provide a realistic estimated total duration for the goal]

        ---

        **Phase 1: [Name of the first phase, e.g., 'Foundation & Research']**
        * **Task:** [Task 1 Name]
            * **Description:** [A clear, one-sentence description of what this task involves.]
            * **Timeline:** [e.g., 'Week 1' or 'Day 1-3']
            * **Dependencies:** ['None' or specify the task it depends on]
        * **Task:** [Task 2 Name]
            * **Description:** [A clear, one-sentence description.]
            * **Timeline:** [e.g., 'Week 1']
            * **Dependencies:** ['Task 1']

        ---

        **Phase 2: [Name of the second phase, e.g., 'Execution & Development']**
        * **Task:** [Task 3 Name]
            * **Description:** [A clear, one-sentence description.]
            * **Timeline:** [e.g., 'Week 2-3']
            * **Dependencies:** ['Task 2']

        ---

        **(Add as many phases and tasks as necessary to comprehensively cover the goal. Be detailed.)**

        **Key Milestones:**
        * **Milestone 1:** [Description of a key milestone and when it should be achieved, e.g., 'Project Brief Finalized - End of Week 1']
        * **Milestone 2:** [Add another significant milestone]

        **Potential Risks & Mitigation:**
        * **Risk:** [Describe a potential challenge or roadblock.]
            * **Mitigation:** [Suggest a proactive strategy to mitigate this risk.]

        Provide a well-structured and logical breakdown. The timelines should be realistic and the dependencies clear.
        """

        # Generate content
        response = model.generate_content(prompt)

        # Return the text part of the response
        return response.text

    except Exception as e:
        print(f"An error occurred in the planner: {e}")
        # Re-raise the exception to be caught by the Streamlit app
        raise e