import sys
import os


def main():
	valid_commands = ["exit", "echo", "type", "pwd", "cd"]
	PATH = os.environ.get("PATH")

	while True:
		sys.stdout.write("$ ")
		sys.stdout.flush()

		# Wait for user input
		command = input()
		args = command.split(" ")
		cmd = args[0].lower()

		if cmd not in valid_commands:
			if os.path.isfile(cmd):
				os.system(command)
			else:
				sys.stdout.write(f"{command}: command not found\n")
				continue

		if cmd == "exit": break
		if cmd == "echo":
			print(" ".join(args[1:]))
		if cmd == "type":
			if args[1].lower() in valid_commands: print(f"{args[1]} is a shell builtin")
			else:
				paths = PATH.split(":")
				for path in paths:
					if os.path.exists(f"{path}/{args[1]}"):
						sys.stdout.write(f"{args[1]} is {path}/{args[1]}\n")
						break
				else:
					print(f"{args[1]} not found")
					continue
		if cmd == "pwd":
			print(os.getcwd())
			continue
		if cmd == "cd":
			path = args[1]

			if path.startswith("./"): path = os.getcwd() + "/" + path.replace("./", "")

			# print(path)
			if os.path.exists(path): os.chdir(path)
			else: print(f"{path}: No such file or directory")



if __name__ == "__main__":
	main()
