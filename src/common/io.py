import csv
import hashlib
import json
import os
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def read_jsonl(path):
    with Path(path).open(encoding='utf-8') as handle:
        return [json.loads(line) for line in handle if line.strip()]


def write_text(path, text, immutable=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if immutable and path.exists():
        if path.read_text(encoding='utf-8') != text:
            raise ValueError(f'Refusing to overwrite raw data: {path}')
        return
    temp = path.with_suffix(path.suffix + '.tmp')
    with temp.open('w', encoding='utf-8', newline='') as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    if immutable:
        # Hard linking atomically publishes the complete file without replacing it.
        os.link(temp, path)
        temp.unlink()
    else:
        temp.replace(path)


def write_json(path, value, immutable=False):
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', immutable)


def write_jsonl(path, rows, immutable=False):
    write_text(path, ''.join(json.dumps(r, ensure_ascii=False, allow_nan=False) + '\n' for r in rows), immutable)


def write_csv(path, rows, fields):
    import io
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    write_text(path, buffer.getvalue())


def sha256(path):
    # Git may check text files out with CRLF on Windows. Snapshot integrity
    # should depend on textual content, not the host OS line-ending convention.
    data = Path(path).read_bytes().replace(b'\r\n', b'\n').replace(b'\r', b'\n')
    return hashlib.sha256(data).hexdigest()
