import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to split the file into 25MB sections
def split_file(file_path_str: str):
    if not file_path_str:
        raise FileNotFoundError(f"File {file_path_str} not found.")
    chunk_size = 25 * 512 * 512
    file_name = os.path.basename(file_path_str)
    file_size = os.path.getsize(file_path_str)

    with open(file_path_str, "rb") as file:
        part_num = 1
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            if file_size < chunk_size:
                data = data[:file_size]
            if file_size >= chunk_size:
                data = data[:chunk_size]
                file_size -= chunk_size

            output_file = f"./src/out/{file_name}_{part_num}.wav"
            # Send the chunk to the API
            send_chunk(data, file_name, part_num)

            part_num += 1


def send_chunk(data: bytes, file_name: str, part_num: int):
    subscript = openai.Audio.transcribe("whisper-1", data)
    with open(output_file, "a", encoding="utf-8") as file:
        sub_transcript = file.write(f"{subscript[0]['text']}\n")
    return sub_transcript


def process_file(file_path):
    if not os.path.isfile(file_path):
        print("File not found")
        return

    split_file(file_path)


if __name__ == "__main__":
    file_path = "docs/in/output.wav"
    process_file(file_path)
