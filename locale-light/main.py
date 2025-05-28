import ollama
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print("=" * 40)
    print("             Locale Light")
    print("=" * 40)

def help_menu():
    print("\nCommands:")
    print("  start <model_name>  - Start a chat with the specified model. e.g., 'start llama3'.")
    print("  help                - Show this help menu.")
    print("  install help        - Show installation help.")
    print("  exit                - Exit the application or chat.\n")

def install_help():
    print("\nInstallation Help:")
    print("1. Ensure you have Ollama installed and running.")
    print("2. Use the command 'ollama list' to see available models.")
    print("3. Use 'ollama pull <model_name>' to download a model if not already available.")
    print("4. Start the application and use 'start <model_name>' to begin chatting.\n")

def send_message():
    return input("You: ")

def get_response(model, message):
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": message}])
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

def chat_loop(model_name):
    clear_screen()
    header()
    print(f"Chatting with model: {model_name}\n(Type 'exit' to leave chat)\n")
    conversation = []  # Store the conversation history
    while True:
        msg = send_message()
        if msg.lower() == "exit":
            print("Exiting chat...")
            input("Press Enter to return to main menu...")
            break
        conversation.append({"role": "user", "content": msg})
        try:
            response = ollama.chat(model=model_name, messages=conversation)
            ai_reply = response['message']['content']
        except Exception as e:
            ai_reply = f"Error: {e}"
        conversation.append({"role": "assistant", "content": ai_reply})
        print(f"{model_name}: {ai_reply}\n")

def main():
    while True:
        clear_screen()
        header()
        print("Type 'help' for a list of commands.\n")
        user_input = input("> ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower().startswith("start "):
            parts = user_input.split(maxsplit=1)
            model_name = parts[1].strip()
            if model_name:
                chat_loop(model_name)
            else:
                print("Please specify a model name after 'start'.")
                input("Press Enter to continue...")
        elif user_input.lower() == "help":
            help_menu()
            input("Press Enter to continue...")
        elif user_input.lower() == "install help":
            install_help()
            input("Press Enter to continue...")
        else:
            print("Unknown command. Type 'help' for a list of commands.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
