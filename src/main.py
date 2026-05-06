from logger import write_log


def start_input_logging():
    print("=== Input Logging Demo (Safe Mode) ===")
    print("Type something and press Enter. Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("> ")

            if user_input.lower() == "exit":
                print("Exiting...")
                break

            write_log(user_input)

        except KeyboardInterrupt:
            print("\nInterrupted. Exiting...")
            break


if __name__ == "__main__":
    start_input_logging()
