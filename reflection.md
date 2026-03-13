# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Response: 
  - When I first ran the Streamlit app, the code execute without any issues. First, when I selected different difficulty levels, the range for different levels of bit off to me. Second, the most visible bug was the hints were backwards, that is, a guess that was too high told me to go higher, and a guess that was too low told me to go lower. I also found that some turns compared the guess against a string version of the secret number, which caused incorrect outcomes. Finally, I also noticed the New Game button did not fully reset the app state. 

  - In addition, I also observed that after a win or loss, clicking New Game leaves the app in “won” or “lost” state. It also ignores the difficulty range when generating the new secret. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Response:  
  - I used Claude for help with bug identification and fixing them 

  - Correct AI Suggestion - Hard mode is easier than Normal
    - Cause: “get_range_for_difficulty()” returns (1,100) for Normal and (1,50) for Hard.

  - Incorrect AI Suggestion
    - AI suggested issues with the Streamlit app resetting the secret. Since the app already shares the secret in session state, the bigger issues were reversed hint logic and incomplete reset behavior.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Response: 
  - I was able to decide that a bug was really fixed by reproducing the behavior of the code before and after the fix. For manual testing, I used Debug info panel on the app to compare my guesses to the actual secret number and confirm whether the hint matched the expected direction. Also, I used "iPython" to debug the code and run manual test cases to check if the behavior of the program is as expected. 

  - In addition to manual testing and debugging, I ran the automated tests using the pytest cases for valid and invalid inputs. It should be noted that the test_game_logic.py file needs some tweaks as our game does not just show "Win", "Too High", or "Too Low", it returns tuples of ("Win", "🎉 Correct!"), ("Too High", "📉 Go LOWER!"), or ("Too Low", "📈 Go HIGHER!") so the `test_game_logic.py` script should be updated accordingly. Further, for creating additional test for automated testing, I generated some test cases by my self, and prompted Claude to generate additional test cases for me. 

>> `conftest.py` was added as a "zero-config" tool for automated testing of the project.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Response: 
  - In normal Python script, we run it once and it is done with execution. In Streamlit, the moment we interact with the app, Streamlit refreshes the app. It starts at line 1 and executes the whole script again to make sure new changes are properly reflected. Since it restarts the script, it forgets everything. For example, our `score` variable will reset to `0` everything script reruns and causes problems as we cannot keep track of progress.

  - The session state gives a our app a memory and that makes our app keep track of secret number, sore and attempts between the reruns. Also, resetting the UI is necessary to keep the game logic in sync.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


Response:
  - I feel one habit I want to keep is writing down the expected behavior before changing the code, because it made debugging much more precise. While using AI, I would very each suggestion against the actual code sooner instead of assuming the first suggestion is correct. I have changed the way I think about AI-generated code or suggestions because the code looks well written and easy to read at first, however several bugs were identified in logic and state management.


> **Note:** For a detailed report with screenshots, please review the accompanying PDF for documentation (`report.pdf`) of the code issues, reproducibility evidence, and implemented fixes.


> **Note:** Every AI-generated code change, test case, and debugging suggestion included in this project was manually validated and tested before implementation to ensure correctness and avoid introducing new issues.