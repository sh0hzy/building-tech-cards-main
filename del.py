import os

# Папка, где лежат файлы (замени на свою)
root_dir = "C:/Users/Admin/Documents/building-tech-cards-main"

# Список строк, которые нужно удалить
lines_to_remove = [
    '<link rel="icon" type="image/png" sizes="32x32" href="https://static.tildacdn.com/tild6437-3666-4739-b130-336435396463/AppStore.png" media="(prefers-color-scheme: light)" />',
    '<link rel="icon" type="image/png" sizes="32x32" href="https://static.tildacdn.com/tild3337-3839-4137-a234-626466316435/AppStore.png" media="(prefers-color-scheme: dark)" />',
    '<link rel="icon" type="image/svg+xml" sizes="any" href="https://static.tildacdn.com/tild6665-3564-4464-a339-373331356533/AppStore.svg" />',
    '<link rel="apple-touch-icon" type="image/png" href="https://static.tildacdn.com/tild3831-3436-4762-b862-386439386431/Group_100.png" />',
    '<link rel="icon" type="image/png" sizes="192x192" href="https://static.tildacdn.com/tild3831-3436-4762-b862-386439386431/Group_100.png" />'
]

def clean_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Убираем ненужные строки
    new_lines = [line for line in lines if line.strip() not in lines_to_remove]

    # Перезаписываем файл, только если есть изменения
    if new_lines != lines:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"✔ Очищен: {file_path}")

# Проход по папке
for subdir, _, files in os.walk(root_dir):
    for filename in files:
        if filename.endswith(".html"):
            clean_file(os.path.join(subdir, filename))
