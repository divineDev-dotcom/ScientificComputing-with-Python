def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    separator_line = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        top_line += operand1.rjust(width) + "    "
        bottom_line += operator + " " + operand2.rjust(width - 2) + "    "
        separator_line += "-" * width + "    "

    arranged_problems += top_line.rstrip() + "\n"
    arranged_problems += bottom_line.rstrip() + "\n"
    arranged_problems += separator_line.rstrip()

    return arranged_problems
