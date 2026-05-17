import os
from database import RoadDatabase
from engine import OpenRoadBot

def main():
    print("Initializing Open Road AI...")
    
    # Path to the mock database
    db_path = os.path.join(os.path.dirname(__file__), 'data', 'roads.json')
    
    # Initialize the Database layer
    db = RoadDatabase(db_path)
    
    if not db.roads:
        print("Warning: Database is empty. Ensure 'data/roads.json' exists and contains data.")
    else:
        print(f"Loaded {len(db.roads)} road segments successfully.")

    # Initialize the Chatbot Engine
    bot = OpenRoadBot(db)
    
    print("\n" + "="*50)
    print("Welcome to Open Road AI!")
    print("You can ask me about road details or report issues.")
    print("Try: 'details about MG Road' or 'report pothole on High Street Link'")
    print("Type 'exit' or 'quit' to close.")
    print("="*50 + "\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("Open Road AI: Goodbye! Stay safe on the roads.")
                break
                
            response = bot.process_query(user_input)
            print(f"\nOpen Road AI:\n{response}\n")
            
        except KeyboardInterrupt:
            print("\nOpen Road AI: Goodbye! Stay safe on the roads.")
            break
        except Exception as e:
            print(f"\nOpen Road AI: Oops, something went wrong. ({e})\n")

if __name__ == "__main__":
    main()
