from pydub import AudioSegment #pip install pydub
from pocketsphinx import AudioFile #Пока не получилось скачачать библиотеку #pip install pocketsphinx

# Открываем аудиофайл с помощью PyDub
audio_file = AudioSegment.from_mp3("audio.mp3") #Путь к моему файлу

# Конвертируем аудиофайл в временный wav-файл
wav_file = "audio.wav"
audio_file.export(wav_file, format="wav")

# Экземпляр класса распознавания речи
recognizer = AudioFile()

# Открываем временный wav-файл с помощью PocketSphinx
recognizer.open(wav_file)

# Создаем текстовый файл для записи распознанного текста
text_file = open("text.txt", "w")

# Цикл распознавания речи из аудио
for phrase in recognizer:
    # Записываем распознанный текст в файл
    text_file.write(phrase.hypothesis() + "\n")

# Закрываем файлы
text_file.close()
recognizer.close()
