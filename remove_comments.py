import tokenize
import io
import sys

def remove_comments(script):
    io_obj = io.StringIO(script)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    # Remove trailing whitespace
    return '\n'.join(line.rstrip() for line in out.splitlines())

if __name__ == '__main__':
    for file in sys.argv[1:]:
        try:
            with open(file, 'r') as f:
                content = f.read()
            new_content = remove_comments(content)
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Processed {file}")
        except Exception as e:
            print(f"Could not process {file}: {e}")
