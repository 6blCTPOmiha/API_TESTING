from data.test_data import FileData


class FileHelper:

    @staticmethod
    def generate_data_txt(path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(FileData.DATA_TXT_CONTENT)

    @staticmethod
    def read_file(path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def normalize_text(text: str) -> str:
        return text.replace("\r\n", "\n").strip()
