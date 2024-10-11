import tiktoken

enc = tiktoken.get_encoding("o200k_base")

k = 199998
output_file_path = "o200k_base.txt"


# Decodes the input key and returns the decoded string
# The \n and \r characters are replaced with spaces or empty strings
def decode(k):
    return (
        str(enc.decode_bytes([k]).decode("utf-8", errors="replace"))
        .replace("\n", " ")
        .replace("\r", "")
    )


# Write the decoded strings to the output file
with open(output_file_path, "w") as output_file:
    for i in range(k):
        decoded_string = decode(i)
        output_file.write(decoded_string + "\n")
