import math

def frequency_to_midi():
    frequency = float(input("Enter a frequency (Hz): "))
    if frequency <= 0:
        print("Frequency must be greater than 0 Hz.")
    else:
        midi_note = round(69 + 12 * (math.log2(frequency / 440.0)), 2)
        print(f"The frequency {frequency} Hz corresponds to MIDI note {midi_note}.")

def sample_to_milliseconds():
    buffer_size = int(input("Enter the buffer size (samples): "))
    sample_rate = int(input("Enter the sample rate (Hz): "))
    duration_ms = round((buffer_size / sample_rate) * 1000, 2)
    print(f"The duration of {buffer_size} samples at {sample_rate} Hz is {duration_ms} milliseconds.")

def decibels_to_linear():
    db_value = float(input("Enter a value in decibels (dB): "))
    linear_amplitude = round(10 ** (db_value / 20), 4)
    print(f"{db_value} dB corresponds to a linear amplitude of {linear_amplitude}.")

def delay_time_calculator():
    bpm = float(input("Enter the tempo (BPM): "))
    note_duration = float(input("Enter the note duration (e.g., 1 for whole note, 0.25 for quarter note): "))
    delay_time_ms = round((60 / bpm) * note_duration * 1000, 2)
    print(f"At {bpm} BPM, a {note_duration}-note duration is {delay_time_ms} milliseconds.")

def nyquist_frequency():
    sample_rate = int(input("Enter the sample rate (Hz): "))
    test_frequency = float(input("Enter a test frequency (Hz): "))
    nyquist_frequency = sample_rate / 2
    if test_frequency > nyquist_frequency:
        print(f"The frequency {test_frequency} Hz exceeds the Nyquist frequency ({nyquist_frequency} Hz).")
    else:
        print(f"The frequency {test_frequency} Hz is valid under the Nyquist frequency.")


def main():
    while True: 

        print("\nWelcome to the DSP Calculator Tool!\n")
        print("Select a tool to use:")
        print("1. Frequency to MIDI Note Converter")
        print("2. Sample to Milliseconds Converter")
        print("3. Decibels to Linear Amplitude Converter")
        print("4. Delay Time Calculator")
        print("5. Nyquist Frequency Checker")
        print("0. Exit")

        choice = int(input("\nEnter the number of the tool you want to use: "))

        if choice == 1:
            frequency_to_midi()
        elif choice == 2:
            sample_to_milliseconds()
        elif choice == 3:
            decibels_to_linear()
        elif choice == 4:
            delay_time_calculator()
        elif choice == 5:
            nyquist_frequency()
        elif choice == 0:
            print("Thank you for using the DSP Calculator Tool!")
            break

    else:
        print("Invalid choice. Please select a valid tool.")


#Check if script is being run as a module or directly
if __name__ == "__main__":
    main()

