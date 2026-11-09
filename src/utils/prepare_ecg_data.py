"""Reassemble the checked-in ECG archive and extract its MATLAB dataset."""

import shutil
import tempfile
import zipfile
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "ecg"
DEFAULT_TARGET = DATA_DIR / "cut_pub_4sec.mat"


def prepare_ecg_data(target=DEFAULT_TARGET):
    target = Path(target)
    if target.is_file():
        return target

    parts = [DATA_DIR / f"cut_pub_4sec.zip.{number:03d}" for number in (1, 2)]
    missing = [str(part) for part in parts if not part.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing ECG archive fragments: {', '.join(missing)}")

    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=target.parent) as temp_dir:
        temp_dir = Path(temp_dir)
        archive = temp_dir / "ecg.zip"
        with archive.open("wb") as combined:
            for part in parts:
                with part.open("rb") as source:
                    shutil.copyfileobj(source, combined)
        with zipfile.ZipFile(archive) as zipped:
            matches = [
                member for member in zipped.infolist()
                if not member.is_dir() and Path(member.filename).name == "cut_pub_4sec.mat"
            ]
            if len(matches) != 1:
                raise ValueError(f"Expected one cut_pub_4sec.mat in archive, found {len(matches)}")
            extracted = temp_dir / target.name
            with zipped.open(matches[0]) as source, extracted.open("wb") as destination:
                shutil.copyfileobj(source, destination)
        extracted.replace(target)
    return target


if __name__ == "__main__":
    print(f"ECG dataset ready: {prepare_ecg_data()}")
