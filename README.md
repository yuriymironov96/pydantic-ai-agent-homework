# pydantic-ai-agent-homework

## Prerequisites

### Get access to free-tier Gemini

1. Log into https://aistudio.google.com;
2. Press "API keys" -> "Create API key";
3. Copy the key (it starts as `AIza...`);
4. Copy `.env.example` and rename it to `.env`;
5. Pase the key from p.3 into `.env` like this: `GEMINI_API_KEY=AIza...`;
6. NEVER COMMIT YOUR `.env`, or any other files that contain sensitive variables!


### Install python 3.14

https://www.python.org/downloads/


### Install `uv`

https://docs.astral.sh/uv/getting-started/installation/

Theoretically you can use pip+virtualenv, but I would lke to promote modern tools.


## Setup

- Fill `.env` file;
- Run `uv sync`;
- Run `uv run main.py`;

## Home assignment

1. Implement one of the agents below, or come up with your own;
2. Look into optional tasks if you want to;
3. Push the agent code to GitHub (!!!make sure you do not commit API keys or anything else sensitive);
4. Record a video of how your agent works.

## Agent ideas

### 1. Culinary Assistant

* `search_recipe(query: str)` - search for recipes (from JSON data or hardcoded recipes);
* `convert_measurements(amount: float, from_unit: str, to_unit: str)` - convert measurements between US and metric systems;
* `get_ingredient_info(name: str)` - get ingredient information (allergens, sugar content, nutritional facts, etc.).

### 2. Calendar Bot

* `add_event(title: str, date: str)` - add an event to the calendar (using a global variable or file for storage);
* `list_events(date: str = "today")` - view events for a specific date;
* `find_free_slot(duration_minutes: int)` - find an available time slot.

### 3. Language Learning Assistant

* `add_word(word: str, translation: str)` - add a word and its translation (using a global variable or file for storage);
* `quiz_me(count: int = 5)` - start a vocabulary quiz;
* `show_progress()` - view learning statistics and progress.

### 4. Note-Taking Assistant

* `save_note(title: str, content: str)` - save a note;
* `search_notes(query: str)` - search notes by content;
* `summarize_notes()` - generate a summary of all notes.

### 5. Habit Tracker Bot

* `mark_habit_done(habit_name: str)` - mark a habit as completed;
* `show_streak(habit_name: str)` - display the current streak;
* `add_new_habit(name: str)` - create a new habit.

### 6. Pomodoro Timer Assistant

* `start_pomodoro(minutes: int = 25)` - start a Pomodoro timer;
* `take_break()` - begin a break session;
* `show_stats()` - show daily productivity statistics.

### 7. Technical Terms Translator

* `translate_term(term: str, target_lang: str)` - translate a technical term with contextual explanation;
* `add_term(en: str, uk: str, context: str)` - add a new term to the glossary;
* `quiz_terms(domain: str)` - test knowledge of terms in a specific domain.

### 8. Team Assistant

* `create_standup_template()` - generate a daily standup template;
* `track_blocker(description: str)` - record a blocker or impediment;
* `summarize_week()` - generate a weekly summary.

### 9. DevOps Team Assistant

* `check_deployment_status(env: str)` - check deployment status (using a fake API);
* `get_recent_logs(service: str)` - retrieve recent service logs;
* `restart_service(name: str)` - restart a service (with confirmation).

## Optional

1. Install ollama locally: https://ollama.com. Ask ChatGPT which model would adequately run on your computer (main indicators are RAM and GPU). Try and switch agent from Gemini to Ollama;
2. Make your chat persistent by storing history into file and loading it back (https://pydantic.dev/docs/ai/core-concepts/message-history/#storing-and-loading-messages-to-json);
3. Add a web UI to your chat (https://pydantic.dev/docs/ai/guides/web/);
4. Add another agent that would summarize older messages, compressing history and saving you some tokens (https://pydantic.dev/docs/ai/core-concepts/message-history/#summarize-old-messages);
5. Look up https://pydantic.dev/docs/ai/examples/setup/ for more inspiration!