import base64


# Function to decode Base64 strings
def decode_base64_string(base64_string):
    # Remove any trailing numbers or whitespace
    base64_string = base64_string.split()[0]
    # Decode the Base64 string
    decoded_bytes = base64.b64decode(base64_string)
    # Convert the decoded bytes into a string (assuming UTF-8 encoding)
    return (
        decoded_bytes.decode("utf-8", errors="replace")
        .replace("\n", " ")
        .replace("\r", "")
    )


input_file_path = "o200k_base.tiktoken"

output_file_path = "o200k_base.txt"

with open(input_file_path, "r") as input_file, open(
    output_file_path, "w"
) as output_file:
    for line in input_file:
        decoded_string = decode_base64_string(line)
        output_file.write(decoded_string + "\n")

print(f"Decoded file has been saved to {output_file_path}")
