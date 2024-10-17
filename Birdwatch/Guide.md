# Instructions for Extracting JPEG Files from a Binary File

## 1. Located the Large File in the Case Tab
- Opened the analysis tool and navigated to the **Case** tab.
- Found and downloaded the largest .jpg file in the **C Drive** which was significantly larger than others.

## 2. Found the Indexes of Each FFD8 Occurrence
- Wrote a script (e.g., in Python) to read the binary file.
- Searched for all instances of `b'\xFF\xD8'` (the JPEG Start of Image marker).
- Recorded the positions (indexes) where they occur.

## 3. Saved the Data into Separate Files
- For each FFD8 index, stored the data in a new file with the extension `*.jpg`.

## Summary
By locating the **FFD8** (Start of Image) and **FFD9** (End of Image) markers, you can extract each JPEG file embedded within the large binary file.
