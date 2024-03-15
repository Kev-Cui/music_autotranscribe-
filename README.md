### Ironhack DA Jan 2024 Final Project
# Musescribe - Audio to MIDI transcriber

A data pipeline that takes a mp3 file as input and gives a midi file recording sequence of notes corroponding to the input audio.
Complete pipeline in file: IO framework.ipnynb

Files Naming notice:
for .keras models, ones with 'mfccs' specified in file name takes audio mfccs as input, others take audio spectrograms.
All .pkl files are stored data, the two with 'X' and 'y' in name are a pair of mfccs+lable data
for direct excecution, use files without 'test and learn'
for code exploration, refer to files with 'test and learn'

## Data source:
Piano Pieces of Public Domain Classical Music:
piano-midi.de
sheetmusicinternational.com
musescore.com

## The project presentation (15.03.2024) was made using Google Sheets
Presentation url: https://docs.google.com/presentation/d/1rRmKU1n_km_07ffYkrLJpoh9A2yzz15ichzVTckgD88/edit?usp=sharing
