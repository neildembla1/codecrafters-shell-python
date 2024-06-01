import sys


def main():
	valid_commands = ["exit", "echo", "type"]

	while True:
		sys.stdout.write("$ ")
		sys.stdout.flush()

		# Wait for user input
		command = input()
		args = command.split(" ")
		cmd = args[0].lower()

		if cmd not in valid_commands:
			sys.stdout.write(f"{command}: command not found\n")
			continue

		if cmd == "exit": break
		if cmd == "echo":
			print(" ".join(args[1:]))
		if cmd == "type":
			if args[1].lower() in valid_commands: print(f"{args[1]} is a shell builtin")
			else:
				print(f"{args[1]} not found")
				continue


if __name__ == "__main__":
	main()
