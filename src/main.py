import os
from argparse import ArgumentParser
from importlib import import_module


def main() -> None:
    parser = ArgumentParser(description="Just another generic programming exercises using Python.")
    parser.add_argument("exercise", choices=['project_euler'])
    parser.add_argument("problem_number", type=int)
    args = parser.parse_args()

    result = run(args.exercise, args.problem_number)
    if not result:
        print(f"No solution for {args.exercise} problem {args.problem_number} yet.")


def run(exercise: str, num: int) -> bool:
    print(f"Exercise:\t{exercise}")
    print(f"Problem:\t{num}")

    group_index = (num - 1) // 50
    group_start = (50 * group_index) + 1
    group_end = group_start + 50 - 1
    group_dir = f"problems_{group_start}_to_{group_end}"
    current_dir = os.path.dirname(__file__)

    module_dir = os.path.join(current_dir, exercise, group_dir)
    if not os.path.exists(os.path.join(module_dir, "__init__.py")):
        return False

    module_prefix = f"problem_{num}"
    module_name = None
    try:
        for filename in os.listdir(module_dir):
            if filename.startswith(module_prefix) and filename.endswith(".py"):
                module_name = filename[:-3]
                break
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    if module_name is None:
        return False

    try:
        module_path = f"{exercise}.{group_dir}.{module_name}"
        module = import_module(module_path)
        module.solution()
    except ImportError as e:
        print(f"Failed to import module: {e}")
        return False

    return True


if __name__ == '__main__':
    main()
