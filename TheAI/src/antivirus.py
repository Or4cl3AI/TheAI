```python
import os
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

API_KEY = 'YOUR_VIRUSTOTAL_API_KEY'
virus_database = VirusTotalPublicApi(API_KEY)

class Antivirus:
    def __init__(self):
        self.virus_database = virus_database

    def scan_for_virus(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")
        else:
            with open(file_path, 'rb') as file_to_check:
                # hash the file
                sha256_returned = hashlib.sha256(file_to_check.read()).hexdigest()

            response = self.virus_database.get_file_report(sha256_returned)
            if response['response_code'] == 200:
                if response['results']['positives'] > 0:
                    return VirusFound(file_path, response['results']['positives'])
                else:
                    return None

class VirusFound:
    def __init__(self, file_path, positives):
        self.file_path = file_path
        self.positives = positives

    def __str__(self):
        return f"Virus found in {self.file_path}. Detected by {self.positives} antivirus engines."

if __name__ == "__main__":
    antivirus = Antivirus()
    virus_found = antivirus.scan_for_virus('path_to_your_file')
    if virus_found:
        print(virus_found)
    else:
        print("No virus found.")
```
This code uses the VirusTotal API to scan files for viruses. You need to replace 'YOUR_VIRUSTOTAL_API_KEY' with your actual API key from VirusTotal. The `scan_for_virus` function takes a file path as input, hashes the file, and sends the hash to VirusTotal for scanning. If a virus is found, it returns a `VirusFound` object, otherwise it returns `None`. The `VirusFound` class is a simple data class that holds the file path and the number of antivirus engines that detected the virus.