SEGMENTS = ((60, '0-1h'), (180, '1-3h'), (600, '3-10h'), (float('inf'), '10h+'))
SEGMENT_NAMES = [label for _, label in SEGMENTS] + ['unknown']


def segment(minutes):
    if minutes is None or minutes < 0:
        return 'unknown'
    return next(label for upper, label in SEGMENTS if minutes < upper)
