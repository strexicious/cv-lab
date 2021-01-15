import argparse
import os

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest="command")

	create_parser = subparsers.add_parser("create")
	create_parser.add_argument("fname")

	args = parser.parse_args()

	if args.command == "create":
		filenames = os.listdir()
		pred = lambda fname: len(fname) > 4 and fname[3] == "-" and fname[:3].isdecimal()
		next_num = max(map(lambda fname: int(fname[:3]), filter(pred, filenames))) + 1
		open(f"{next_num:03}-{args.fname}.py", "a").close()
