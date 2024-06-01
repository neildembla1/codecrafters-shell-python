import sys


def main():
	valid_commands = ["exit"]

	while True:
		sys.stdout.write("$ ")
		sys.stdout.flush()

		# Wait for user input
		command = input()
		args = command.split(" ")
		if args[0].lower() not in valid_commands:
			sys.stdout.write(f"{command}: command not found\n")
			continue

		if args[0].lower() == "exit": break


if __name__ == "__main__":
	main()
