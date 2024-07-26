# PianoRoll Class Documentation

The `PianoRoll` class represents a configurable piano roll for managing MIDI note events and control vectors. This class allows you to add note events, apply control vectors (velocity, pan, X and Y modulation), and add markers for different sections. It also supports saving and loading state checkpoints.

## Initialization

### `__init__(self, resolution: int, length: int)`

Creates a new instance of the `PianoRoll` class.

- `resolution` (int): Number of ticks per bar.
- `length` (int): Length of the piano roll in bars.

```python
piano_roll = PianoRoll(resolution=480, length=4)  # 4 bars with 480 ticks per bar
```

## Methods

### `add_event(self, note: int, start: int, duration: int, velocity: int, pan: int, modulation: Tuple[int, int])`

Adds a note event to the piano roll.

- `note` (int): MIDI note number (0-127).
- `start` (int): Start tick of the note event.
- `duration` (int): Duration of the note event in ticks.
- `velocity` (int): Velocity of the note event.
- `pan` (int): Pan position of the note event.
- `modulation` (Tuple[int, int]): X and Y modulation values.

```python
piano_roll.add_event(note=60, start=0, duration=480, velocity=100, pan=64, modulation=(0, 1))
```

### `add_marker(self, position: int, label: str)`

Adds a marker at a specified position.

- `position` (int): Tick position of the marker.
- `label` (str): Label for the marker.

```python
piano_roll.add_marker(position=480, label="Chorus")
```

### `apply_slide(self, start: int, end: int, amount: float)`

Applies a slide effect to a range of columns.

- `start` (int): Start tick of the slide effect.
- `end` (int): End tick of the slide effect.
- `amount` (float): Amount of the slide effect.

```python
piano_roll.apply_slide(start=480, end=960, amount=0.5)
```

### `apply_porta(self, start: int, end: int, target_note: int)`

Applies a portamento effect to a range of columns.

- `start` (int): Start tick of the portamento effect.
- `end` (int): End tick of the portamento effect.
- `target_note` (int): Target MIDI note number for the portamento.

```python
piano_roll.apply_porta(start=960, end=1440, target_note=65)
```

### `modify_event(self, event_index: int, new_data: Tuple[int, int, int, int, int, Tuple[int, int]])`

Modifies an existing event.

- `event_index` (int): Index of the event to modify.
- `new_data` (Tuple): New event data (note, start, duration, velocity, pan, modulation).

```python
new_data = (62, 0, 480, 110, 70, (2, 3))
piano_roll.modify_event(event_index=0, new_data=new_data)
```

### `load_checkpoint(self, checkpoint: Dict[str, Any])`

Loads a pre-trained checkpoint.

- `checkpoint` (Dict[str, Any]): Checkpoint data.

```python
checkpoint = {
    'grid': np.zeros((128, 1920)),
    'control_vector': np.zeros((1920, 4)),
    'events': [(60, 0, 480, 100, 64, (0, 1))],
    'markers': {480: "Chorus"}
}
piano_roll.load_checkpoint(checkpoint)
```

### `save_checkpoint(self) -> Dict[str, Any]`

Saves the current state as a checkpoint.

- Returns: Checkpoint data (Dict[str, Any]).

```python
checkpoint = piano_roll.save_checkpoint()
```

## Example Usage

```python
# Initialize a new PianoRoll
piano_roll = PianoRoll(resolution=480, length=4)

# Add a note event
piano_roll.add_event(note=60, start=0, duration=480, velocity=100, pan=64, modulation=(0, 1))

# Add a marker
piano_roll.add_marker(position=480, label="Chorus")

# Apply a slide effect
piano_roll.apply_slide(start=480, end=960, amount=0.5)

# Apply a portamento effect
piano_roll.apply_porta(start=960, end=1440, target_note=65)

# Modify an event
new_data = (62, 0, 480, 110, 70, (2, 3))
piano_roll.modify_event(event_index=0, new_data=new_data)

# Save the current state
checkpoint = piano_roll.save_checkpoint()

# Load a checkpoint
piano_roll.load_checkpoint(checkpoint)
