DSP Calculator Tool

The DSP Calculator Tool is a Python-based command-line program designed to help users perform common calculations related to digital signal processing (DSP) and music production. 
This tool includes functions for converting frequencies to MIDI notes, calculating delay times, converting decibels to linear amplitude, and more.

Features

Frequency to MIDI Note Converter
Converts a given frequency (in Hz) to the corresponding MIDI note.
Sample to Milliseconds Converter
Calculates the duration (in milliseconds) of a given number of samples at a specified sample rate.
Decibels to Linear Amplitude Converter
Converts a value in decibels (dB) to its corresponding linear amplitude.

Delay Time Calculator

Calculates the delay time (in milliseconds) for a specific tempo (BPM) and note duration.

Nyquist Frequency Checker

Checks if a test frequency exceeds the Nyquist frequency for a given sample rate.
-------------------------------------------------------------------------------------------------------------------------------
Usage

Clone or download the repository.
Make sure Python is installed on your system (Python 3.6 or later is recommended).

Run the script using: python DSPCalculator.py

Follow the prompts to select and use one of the tools.
-------------------------------------------------------------------------------------------------------------------------------
Menu Options

1. Frequency to MIDI Note Converter
Input a frequency (in Hz) to get the corresponding MIDI note.

2. Sample to Milliseconds Converter
Input buffer size (samples) and sample rate (Hz) to calculate the duration in milliseconds.

3. Decibels to Linear Amplitude Converter
Input a decibel value to get the equivalent linear amplitude.

4. Delay Time Calculator
Input tempo (BPM) and note duration (e.g., 0.25 for quarter note) to calculate delay time in milliseconds.

5. Nyquist Frequency Checker
Input a sample rate and test frequency to check if it exceeds the Nyquist frequency.

0. Exit
Exit the program.

Example

Welcome to the DSP Calculator Tool!

Select a tool to use:
1. Frequency to MIDI Note Converter
2. Sample to Milliseconds Converter
3. Decibels to Linear Amplitude Converter
4. Delay Time Calculator
5. Nyquist Frequency Checker
0. Exit

Enter the number of the tool you want to use: 1

Enter a frequency (Hz): 440
The frequency 440 Hz corresponds to MIDI note 69.0.
-------------------------------------------------------------------------------------------------------------------------------
Requirements
Python 3.6 or later

-------------------------------------------------------------------------------------------------------------------------------
Installation
Clone the repository:

git clone https://github.com/yourusername/DSPCalculator.git

Navigate to the project folder:
cd DSPCalculator

Run the script:
python DSPCalculator.py
-------------------------------------------------------------------------------------------------------------------------------
Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Inspired by the needs of digital signal processing and music production enthusiasts.

Built with Python.