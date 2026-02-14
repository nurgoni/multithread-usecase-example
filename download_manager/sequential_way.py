import time


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

# download satu per satu
start = time.time()

for url, filename in files:
    download_file(url, filename)

end = time.time()

print(f"Total time: {end - start} seconds")
