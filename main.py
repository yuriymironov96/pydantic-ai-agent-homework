from datetime import datetime
from agent import agent, AgentContext


def main():
    print("AI agent is ready. Enter 'exit' to exit.\n")
    
    name = input("What is your name? ").strip() or "Guest"
    
    context = AgentContext(
        user_name=name,
        started_at=datetime.now(),
    )
    
    # Save messages history to context
    message_history = []
    
    while True:
        user_input = input(f"\n{name}: ").strip()
        
        if user_input.lower() in ('exit', 'quit', 'вихід'):
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        result = agent.run_sync(
            user_input,
            deps=context,
            message_history=message_history,
        )
        
        print(f"\nAgent: {result.output}")
        
        # Save new messages to history
        message_history = result.all_messages()


if __name__ == "__main__":
    main()