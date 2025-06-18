 Echo Bridge is a reverb, tremolo, and delay pedal. The original goal of this pedal was to emulate the sound of the bridge by Tandem, but I got carried away and now it's more like a Strymon Flint + a delay lol. It can still do Echo Bridge -- as well as many other spaces -- and is an all around fun time-based multi-effect 🤝 see patch notes below.

### Controls (Normal Mode)

| CONTROL      | DESCRIPTION              | NOTES                                                                                                                                                                                                      |
| ------------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KNOB 1       | Reverb Dry/Wet Amount    |                                                                                                                                                                                                            |
| KNOB 2       | Tremolo Speed            |                                                                                                                                                                                                            |
| KNOB 3       | Tremolo Depth            |                                                                                                                                                                                                            |
| KNOB 4       | Delay Time               |                                                                                                                                                                                                            |
| KNOB 5       | Delay Feedback           |                                                                                                                                                                                                            |
| KNOB 6       | Delay Dry/Wet Amount     |                                                                                                                                                                                                            |
| SWITCH 1     | Reverb knob funcion      | **UP** - 0% Dry, 0-100% Wet<br/>**MIDDLE** - Dry/Wet Mix<br/>**DOWN** - 100% Dry, 0-100% Wet                                                                                                               |
| SWITCH 2     | Tremolo Waveform         | **UP** - Square<br/>**MIDDLE** - Triangle<br/>**DOWN** - Sine<br/>                                                                                                                                         |
| SWITCH 3     | Trem & Delay Makeup Gain | **UP** - Plus<br/>**MIDDLE** - Normal<br/>**DOWN** - None                                                                                                                                                  |
| FOOTSWITCH 1 | Reverb On/Off            | Normal press toggles reverb on/off.<br/>Double press toggles reverb edit mode (see below).<br/>Long press to reflash firmware, in case it's ever needed                                                    |
| FOOTSWITCH 2 | Delay/Tremolo On/Off     | Normal press toggles delay.<br/>Double press toggles tremolo.<br/><br/>**LED:**<br/>- 100% when only relay is active<br/>- 40% pulsing when only tremolo is active<br/>- 100% pulsing when both are active |

### Controls (Reverb Edit Mode)
*Both LEDs flash when in edit mode.*

| CONTROL      | DESCRIPTION                 | NOTES                                                                               |
| ------------ | --------------------------- | ----------------------------------------------------------------------------------- |
| KNOB 1       | Reverb Amount (Wet)         | Not saved. Just here for convenience.                                               |
| KNOB 2       | Pre Delay                   | 0 for Off, up to 0.25                                                               |
| KNOB 3       | Decay                       |                                                                                     |
| KNOB 4       | Tank Diffusion              |                                                                                     |
| KNOB 5       | Input High Cutoff Frequency |                                                                                     |
| KNOB 6       | Tank High Cutoff Frequency  |                                                                                     |
| SWITCH 1     | Tank Mod Speed              | **UP** - High<br/>**MIDDLE** - Medium<br/>**DOWN** - Low                            |
| SWITCH 2     | Tank Mod Depth              | **UP** - High<br/>**MIDDLE** - Medium<br/>**DOWN** - Low                            |
| SWITCH 3     | Tank Mod Shape              | **UP** - High<br/>**MIDDLE** - Medium<br/>**DOWN** - Low                            |
| FOOTSWITCH 1 | Save & Exit                 | Saves all parameters and exits Reverb Edit Mode.<br/>Long press to reflash firmware |
| FOOTSWITCH 2 | Save & Exit                 | Saves all parameters and exits Reverb Edit Mode.                                    |

### Factory Reset (Restore default reverb parameters)

To enter factory reset mode, **press and hold** **Footswitch #2** when powering the pedal. The LED lights will alternate blinking slowly.

1. Rotate Knob #1 to 100%. The LEDs will quickly flash simultaneously and start blinking faster.
2. Rotate Knob #1 to 0%. The LEDs will quickly flash simultaneously and start blinking faster.
3. Rotate Knob #1 to 100%. The LEDs will quickly flash simultaneously and start blinking faster.
4. Rotate Knob #1 to 0%. The LEDs will quickly flash simultaneously, defaults will be restored, and the pedal will resume normal pedal mode.

To exit factory reset mode without resetting. Power off the pedal and power it back on.

### Patches 

#### Echo Bridge

{to-do - what's the best way to show this?}

#### {TO-DO - more patches!}
### Acknowledgements

- The hardware is a Hothouse by [Cleveland Music Co](https://github.com/clevelandmusicco), which provided a base for development.
	- The algo and pedal is based on the Daisy Seed, which means that if you really wanted, you could reflash [a bunch of other effects](https://github.com/clevelandmusicco/HothouseExamples) onto this pedal! It's super fun and addicting
%%-  The software is a fork of [Flick](https://github.com/joulupukki/hothouse-effects/tree/main/src/Flick), with the Datorro reverb algo modified to be closer to the original Echo Bridge frequency curve. The controls work the same as the original, so feel free to try out the original effect to hear the difference! %%
- This software is licensed under the GNU General Public License (GPL) for open-source use.
