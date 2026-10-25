# import constant
# from pathlib import Path
# import extract_files
# import normalize
# import parser

# def main():
#     extracted_texts = []
#     for file_path in list(Path(constant.DATA_PATH).rglob("*.*")):
#         print(f"Processing file: {file_path}")
#         if file_path.is_file():
#             try:
#                 raw_text = extract_files.extract_text_from_file(file_path)
#                 normalized_text = normalize.normalize_text(raw_text)
#                 extracted_texts.append(normalized_text)
#             except Exception as e:
#                 print(f"Error processing {file_path}: {e}")
#     print("Extracted and normalized texts from files:")
#     for i, text in enumerate(extracted_texts, start=1):
#         print(f"\nText {i}:")
#         print(text)

# if __name__ == "__main__":
#     main()
print("bựa")