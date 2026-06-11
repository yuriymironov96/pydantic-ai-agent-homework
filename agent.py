import os
from datetime import datetime
from dataclasses import dataclass

from dotenv import load_dotenv
from pydantic_ai import Agent, RunContext

load_dotenv()

# Set API key
os.environ['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY', '')


# Agent context — what is passed to tools
@dataclass
class AgentContext:
    user_name: str
    started_at: datetime


# Create agent with system prompt
agent = Agent(
    'google:gemini-2.5-flash',
    # 'ollama:qwen3:14b',
    deps_type=AgentContext,
    system_prompt=(
        "You are a useful AI assistant. Respond concisely and friendly. "
        "Address the user by name. "
        "If you need the current date or time, use tools."
    ),
)


@agent.tool
async def get_current_time(ctx: RunContext[AgentContext]) -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@agent.tool
async def get_user_info(ctx: RunContext[AgentContext]) -> dict:
    """Returns the user information — name and session start time."""
    return {
        "name": ctx.deps.user_name,
        "session_started": ctx.deps.started_at.isoformat(),
    }


@agent.tool
async def calculate(ctx: RunContext[AgentContext], expression: str) -> str:
    """
    Calculates the mathematical expression.
    
    Args:
        expression: mathematical expression, e.g. "2 + 2" or "(15 * 3) / 5"
    """
    try:
        # Limited eval for security — only numbers and basic operations
        allowed = set("0123456789+-*/.() ")
        if not all(c in allowed for c in expression):
            return "Expression contains forbidden symbols"
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {e}"