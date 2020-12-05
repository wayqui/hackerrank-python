import textwrap

def wrap(string, max_width):
    # This
    list = textwrap.wrap(string, max_width)
    result = "\n".join(list)
    # Is the same as
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)