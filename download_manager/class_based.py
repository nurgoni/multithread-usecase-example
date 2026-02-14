import time
import threading


# method 1: pakai fungsi yang sudah ada
# thread = threading.Thread(
#     target=download_file,
#     args=(url, filename)
# )

def download_file(url, filename):
    print(f"Downloading {filename}...")
    time.sleep(2)
    print(f"Downloaded {filename}")

# list of file
files = [
    ("https://example.com/file1.pdf", "file1.pdf"),
    ("https://example.com/file2.pdf", "file2.pdf"),
    ("https://example.com/file3.pdf", "file3.pdf"),
    ("https://example.com/file4.pdf", "file4.pdf"),
    ("https://example.com/file5.pdf", "file5.pdf"),
]

# method 2: Buat class: (untuk yang lebih kompleks)
class DownloadThread(threading.Thread):
    def __init__(self, url, filename):
        super().__init__()

        self.url = url
        self.filename = filename

    def run(self):
        # code yang jalan di thread ini
        self.download_file()

    def download_file(self):
        print(f"Downloading {self.filename}...")
        time.sleep(2)
        print(f"Downloaded {self.filename}")

start = time.time()
threads = []

# create thread
for url, filename in files:
    thread = DownloadThread(url, filename)
    threads.append(thread)
    thread.start()

# join thread
for thread in threads:
    thread.join()

end = time.time()

print(f"Total time: {end - start} seconds")
