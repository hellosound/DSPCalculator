import math

#DSP Calculator!

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

def bit_depth_to_dynamic_range():
    bit_depth = int(input("Enter the bit depth (e.g., 16, 24, 32): "))
    dynamic_range = round(20 * math.log10(2 ** bit_depth), 2)
    print(f"A bit depth of {bit_depth} provides a dynamic range of approximately {dynamic_range} dB.")

def reverb_pre_delay_calculator():
    bpm = float(input("Enter the tempo (BPM): "))
    beat_percentage = float(input("Enter the desired pre-delay as a percentage of a beat (e.g., 25 for quarter beat): "))
    pre_delay_ms = round((60 / bpm) * (beat_percentage / 100) * 1000, 2)
    print(f"At {bpm} BPM, a {beat_percentage}% pre-delay is {pre_delay_ms} milliseconds.")

def dsp_gain_calculation():
    developer_name = input("Enter your developer alias: ")
    plugin_name = input("Enter the name of your plugin: ")
    
    print(f"\nWelcome, {developer_name}! Initializing development tools for '{plugin_name}'.")
    
    # Simulating DSP parameter input
    input_signal_level = float(input("Enter the input signal level (dB): "))
    gain_adjustment = float(input("Enter the desired gain adjustment (dB): "))
    
    # Calculate the output signal level
    output_signal_level = input_signal_level + gain_adjustment
    
    # Round to 2 decimal places for precision
    rounded_output_level = round(output_signal_level, 2)
    
    print(f"\nInput Signal Level: {input_signal_level} dB")
    print(f"Gain Adjustment: {gain_adjustment} dB")
    print(f"Output Signal Level: {rounded_output_level} dB")
    
    # Debugging information
    print("\n--- Debugging Info ---")
    buffer_size = int(input("Enter the buffer size for processing (samples): "))
    sample_rate = int(input("Enter the sample rate (Hz): "))
    latency_ms = round((buffer_size / sample_rate) * 1000, 3)
    
    print(f"Buffer Size: {buffer_size} samples")
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Calculated Latency: {latency_ms} ms")
    
    # Testing filter parameters
    cutoff_frequency = float(input("\nEnter the cutoff frequency for the low-pass filter (Hz): "))
    if cutoff_frequency > sample_rate / 2:
        print(f"Warning: Cutoff frequency {cutoff_frequency} Hz exceeds Nyquist frequency ({sample_rate / 2} Hz).")
    else:
        print(f"Cutoff frequency {cutoff_frequency} Hz is valid for the given sample rate.")
    
    print(f"\nThank you, {developer_name}, for testing '{plugin_name}'!")

def main():
    print("Welcome to the DSP Development Tool!\n")
    print("Select a tool to use:")
    print("1. Frequency to MIDI Note Converter")
    print("2. Sample to Milliseconds Converter")
    print("3. Decibels to Linear Amplitude Converter")
    print("4. Delay Time Calculator")
    print("5. Nyquist Frequency Checker")
    print("6. Bit Depth to Dynamic Range Calculator")
    print("7. Reverb Pre-Delay Calculator")
    print("8. DSP Gain Calculation for VST Plugin")

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
    elif choice == 6:
        bit_depth_to_dynamic_range()
    elif choice == 7:
        reverb_pre_delay_calculator()
    elif choice == 8:
        dsp_gain_calculation()
    else:
        print("Invalid choice. Please select a valid tool.")

if __name__ == "__main__":
    main()

