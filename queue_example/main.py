import time
import threading


class DownloadThread(threading.Thread):
    def __init__(self, url, filename):
        super().__init__()

        self.url = url
        self.filename = filename
    
    def run(self):
        """
        Code yang jalan di thread ini
        """
        self._download_file()

    def _download_file(self):
        """
        Simulate download file
        """
        print(f"⬇️  Downloading {self.filename}...")
        time.sleep(2)  # Simulate download time
        print(f"✅ {filename} selesai")


# list of file
files = [
    ("https://example.com/file1.pdf", "file1.pdf"),
    ("https://example.com/file2.pdf", "file2.pdf"),
    ("https://example.com/file3.pdf", "file3.pdf"),
    ("https://example.com/file4.pdf", "file4.pdf"),
    ("https://example.com/file5.pdf", "file5.pdf"),
]

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


import time

def download_file(url, filename):
    """Simulate download file"""
    print(f"⬇️  Downloading {filename}...")
    time.sleep(2)  # Simulate download time
    print(f"✅ {filename} selesai")

# List files to download
files = [
    ("https://example.com/file1.pdf", "file1.pdf"),
    ("https://example.com/file2.pdf", "file2.pdf"),
    ("https://example.com/file3.pdf", "file3.pdf"),
    ("https://example.com/file4.pdf", "file4.pdf"),
    ("https://example.com/file5.pdf", "file5.pdf"),
]

# Download satu per satu
start = time.time()

for url, filename in files:
    download_file(url, filename)

end = time.time()
print(f"Total waktu: {end - start:.2f} detik")