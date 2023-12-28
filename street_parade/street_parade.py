import sys


# Loading instance
inputs = sys.stdin.readlines()


def iterate_on_problems(inputs):
    inputs = inputs[::-1]
    while inputs:
        line = inputs.pop()
        # print("LINE", line, end="")
        try:
            if int(line) != 0:
                next_line = inputs.pop()
                input_stack = [int(x) for x in next_line.split()]
                # reverse the stack
                input_stack = input_stack[::-1]
                yield input_stack
        except:
            pass


size = int(inputs[0])
input_stack = [int(x) for x in inputs[1].split()]
# reverse the stack
input_stack = input_stack[::-1]

# print(input_stack)
# test =  [4, 1, 2, 5, 3]
# test = [3, 2, 1, 3]
# input_stack = test[::-1]


def test_street_parade(input_stack):
    side_stack = []
    output_value = 0

    while input_stack:
        # print(input_stack, side_stack, output_value)
        # (1) Regarde file d'attente
        if side_stack and side_stack[-1] == (output_value + 1):
            output_value = side_stack.pop()
        # (2) Regarde pile d'entrée
        else:
            current_value = input_stack.pop()
            # (A) Try to put in final list
            if current_value == (output_value + 1):
                output_value = current_value
            # (B) Try to put in side stack
            else:
                # Validation test
                if (not side_stack) or (current_value < side_stack[-1]):
                    side_stack.append(current_value)
                else:
                    return False
    return True


# print(" size", size, "input_stack", input_stack)
responses = []
for instance in iterate_on_problems(inputs):
    if test_street_parade(instance):
        responses.append("yes")
        # print("yes")
    else:
        responses.append("no")
        # print("no")
print("\n".join(responses), end="")
