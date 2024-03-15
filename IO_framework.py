def iScribe(model_path = 'piano_mfccs_RNN-LSTM.keras',mp3_file_path = 'piano_lanternrite2022.mp3'):
    from tensorflow.keras.models import load_model
    import librosa
    import numpy as np
    from sklearn.preprocessing import StandardScaler
    import mido
    from mido import Message, MidiFile, MidiTrack
    model = load_model(model_path)
    y, sr = librosa.load(mp3_file_path)
    n_mfcc=13
    hop_length=512
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, hop_length=hop_length)
    mfccs_t = np.transpose(mfccs)
    num_chunks = mfccs_t.shape[0] // 50
    chunks = np.array_split(mfccs_t[:num_chunks*50], num_chunks)
    if mfccs_t.shape[0] % 50 != 0:
        last_chunk = np.pad(mfccs_t[num_chunks*50:], ((0, 50 - mfccs_t.shape[0] % 50), (0, 0)), mode='constant')
        chunks.append(last_chunk)
    X = np.array([np.transpose(chunk) for chunk in chunks])
    scaler = StandardScaler()
    for i, note in enumerate(X):
        X[i] = scaler.fit_transform(note)
    predictions = model.predict(X)
    rounded_predictions = np.round(predictions).astype(int)
    predictions_list = rounded_predictions.tolist()
    pred_notes=[]
    for note in predictions_list:
        pred_notes.append(note[0])
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    tempo = mido.bpm2tempo(120)  # Set tempo to 120 beats per minute
    track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))

    # Add notes to the track
    time = 0
    for note in pred_notes:
        # Note on
        track.append(Message('note_on', note=note, velocity=64, time=time))
        # Note off after 1 second (480 ticks)
        track.append(Message('note_off', note=note, velocity=64, time=480))
        # Add delay before next note
        time = 240

    # Save the MIDI file
    outputname = 'output_'+mp3_file_path.split('/')[-1].split('.')[0]+'.mid'
    
    return mid