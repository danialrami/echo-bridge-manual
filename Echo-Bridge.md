Echo Bridge is a reverb, tremolo, and delay pedal. The original goal of this pedal was to emulate the sound of the bridge by Tandem, but I got carried away and now it's more like a Strymon Flint + a delay lol. It can still do Echo Bridge -- as well as many other spaces -- and is an all around fun time-based multi-effect 🤝 see patch notes below.

## Controls (Normal Mode)

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

## Controls (Reverb Edit Mode)
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

## Reset (Restore default reverb parameters)

To enter reset mode, **press and hold** **Footswitch #2** when powering the pedal. The LED lights will alternate, blinking slowly.

1. Rotate Knob #1 to 100% -- the LEDs will quickly flash simultaneously and start blinking faster.
2. Rotate Knob #1 to 0% -- the LEDs will quickly flash simultaneously and start blinking faster.
3. Rotate Knob #1 to 100% -- the LEDs will quickly flash simultaneously and start blinking faster.
4. Rotate Knob #1 to 0% -- the LEDs will quickly flash simultaneously, defaults will be restored, and the pedal will resume normal pedal mode.

To exit reset mode without resetting, power off the pedal and power it back on.

## Patches 

this part of my website is kinda broken lmfao -- it's supposed to render a patch diagram with these settings. but trust its gonna look soooo sick when i figure this out. use your imagination! and if you find a setting that you like, let me know and i'll add it here!

### Echo Bridge

The classic Echo Bridge sound - warm reverb with extra subtle tremolo and a touch of delay to create THAT ambience.

```json
{
"name": "Echo Bridge",
"knobs": [0.35, 0.45, 0.25, 0.6, 0.4, 0.3],
"switches": [0.5, 0.0, 0.5]
}
```

**Settings:**
- **Reverb**: 35% for warm, present reverb
- **Tremolo**: Slow sine wave (45% speed, 25% depth) for gentle movement
- **Delay**: Medium time (60%) with moderate feedback (40%) and subtle mix (30%)
- **Switches**: Dry/wet mix, sine wave, normal gain

### Spring Reverb Tank

Classic spring reverb emulation - perfect for surf, rockabilly, or any vintage tone.

```json
{
"name": "Spring Reverb Tank",
"knobs": [0.7, 0.0, 0.0, 0.0, 0.0, 0.0],
"switches": [1.0, 0.5, 0.5]
}
```

**Settings:**
- **Reverb**: 70% wet signal for that classic dripping spring sound
- **Tremolo & Delay**: Off - pure reverb tone
- **Switches**: 100% wet mode for maximum spring character

### Tremolo Delay

Rhythmic tremolo paired with a synced delay for complex, pulsing textures.

```json
{
"name": "Tremolo Delay",
"knobs": [0.15, 0.7, 0.6, 0.5, 0.45, 0.4],
"switches": [0.5, 1.0, 1.0]
}
```

**Settings:**
- **Reverb**: Minimal (15%) to keep things tight
- **Tremolo**: Fast square wave (70% speed, 60% depth) for choppy rhythm
- **Delay**: Medium time with moderate feedback, balanced mix
- **Switches**: Dry/wet mix, square wave, plus gain to compensate for tremolo

### Ambient Wash

Lush, atmospheric reverb with slow tremolo and long delay for ambient soundscapes.

```json
{
"name": "Ambient Wash",
"knobs": [0.8, 0.2, 0.3, 0.85, 0.7, 0.5],
"switches": [0.0, 0.5, 0.0]
}
```

**Settings:**
- **Reverb**: High (80%) for maximum space
- **Tremolo**: Very slow triangle wave for gentle movement
- **Delay**: Long time (85%) with high feedback (70%) for cascading echoes
- **Switches**: Wet-only reverb, triangle wave, no makeup gain

### Slapback Echo

Quick, punchy slapback delay with minimal reverb - perfect for rockabilly and country.

```json
{
"name": "Slapback Echo",
"knobs": [0.2, 0.0, 0.0, 0.25, 0.15, 0.6],
"switches": [0.5, 0.5, 0.5]
}
```

**Settings:**
- **Reverb**: Subtle (20%) room sound
- **Tremolo**: Off for clean attack
- **Delay**: Short time (25%) with minimal feedback (15%) and present mix (60%)
- **Switches**: All middle positions for balanced tone

## Acknowledgements

- The hardware is a Hothouse by [Cleveland Music Co](https://github.com/clevelandmusicco), which provided a base for development.
	- The algo and pedal is based on the Daisy Seed, which means that if you really wanted, you could reflash [a bunch of other effects](https://github.com/clevelandmusicco/HothouseExamples) onto this pedal! It's super fun and addicting
- The software is a fork of [Flick](https://github.com/joulupukki/hothouse-effects/tree/main/src/Flick), with the Datorro reverb algo modified to be closer to the original Echo Bridge frequency curve. The controls work the same as the original, so feel free to try out the original effect to hear the difference!
- This software is licensed under the GNU General Public License (GPL) for open-source use. This means that this effect is never going to be put up for sale  --  just hit me up and i'll make you one if you can get me the parts.
	- The code for this website is also open source! Check out the repo on [Github](https://github.com/danialrami/echo-bridge-manual).