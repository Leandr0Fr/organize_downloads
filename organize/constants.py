from os import path

DOWNLOADS_FOLDER = path.abspath(path.join(path.expanduser("~"), "Downloads"))


FOLDERS = {
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".bat", ".sh", ".msi"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".alac"],
    "Video": [".mp4", ".mov", ".wmv", ".avi", ".mkv", ".flv", ".webm", ".3gp", ".mpeg"],
    "Documents": [
        ".txt",
        ".rtf",
        ".md",
        ".doc",
        ".docx",
        ".odt",
        ".xls",
        ".xlsx",
        ".ods",
        ".ppt",
        ".pptx",
        ".odp",
        ".pdf",
    ],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
    "Others": [],
}
