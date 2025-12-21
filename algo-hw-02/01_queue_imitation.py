from queue import Queue

# Creating a task queue
task_queue: Queue = Queue()

# Counter for incoming tasks
tasks_counter: int = 0

def generate_request() -> None:
    global tasks_counter
    tasks_counter += 1
    task: str = f"Task #{tasks_counter}"
    task_queue.put(task)
    print(f"{task} was added to the queue.")

def show_queue_state() -> None:
    print(f"Current tasks in queue ({task_queue.qsize()}):")
    for item in list(task_queue.queue):
        print(f" - {item}")

def process_request() -> None:
    if not task_queue.empty():
        task: str = task_queue.get()
        print(f"Processing {task}")
    else:
        print("Nothing to process. The queue is empty!")

def main() -> None:
    print("Welcome to the Task Queue Processor! \nLet's start by adding some tasks.")
    for _ in range(3):
        generate_request()

    # main loop
    while True:
        action = input("\nWhat to do next? - add task (a), process task (p), or quit (q)?: ").strip().lower()

        if action == 'a':
            generate_request()
            show_queue_state()
        elif action == 'p':
            process_request()
            show_queue_state()
        elif action == 'q':
            print("Exiting the Task Queue Processor. Goodbye!")
            break
        else:
            print("Invalid action! Please choose 'a', 'p', or 'q'.")


if __name__ == "__main__":
    main()