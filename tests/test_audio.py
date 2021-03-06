#!/usr/bin/env python
# -*- coding: utf-8 -*-

import librosa
from amen.audio import Audio
from amen.utils import example_audio_file

EXAMPLE_FILE = example_audio_file()
audio = Audio(EXAMPLE_FILE)
mono_audio = Audio(EXAMPLE_FILE, convert_to_mono=True, sample_rate=44100)

def test_default_sample_rate():
    assert isinstance(audio.sample_rate, float)
    assert(audio.sample_rate == 22050)

def test_default_channels():
    assert(audio.num_channels == 2)

def test_duration():
    duration = audio.raw_samples.shape[-1] / float(audio.sample_rate)
    assert(audio.duration == duration)

def test_file_path():
    assert(audio.file_path == EXAMPLE_FILE)

def test_sample_data():
    y, sr = librosa.load(EXAMPLE_FILE)
    assert(audio.raw_samples.all() == y.all())

def test_sample_rate():
    assert(mono_audio.sample_rate == 44100)

def test_channels():
    assert(mono_audio.num_channels == 1)

