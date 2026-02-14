import time
import threading


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

# download dengan threads
start = time.time()

threads = []

# buat thread untuk setiap file
for url, filename in files:
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()  # mulai thread

# tunggu semua threada selesai
for thread in threads:
    thread.join()

end = time.time()

print(f"Total time: {end - start} seconds")

