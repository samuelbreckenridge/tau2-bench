"""Core install must import without the optional ``voice`` extra."""

import subprocess
import sys

import pytest

# Imports that only the `voice` extra provides.
VOICE_ONLY_MODULES = ["websockets", "elevenlabs", "deepgram", "pyaudio", "google.genai"]


@pytest.mark.parametrize("module", ["tau2", "tau2.cli", "tau2.data_model.simulation"])
def test_core_import_without_voice_deps(module):
    # Setting sys.modules[name] = None makes `import name` raise ImportError,
    # simulating a core-only install even when the voice extra is present.
    code = (
        "import sys\n"
        f"for m in {VOICE_ONLY_MODULES!r}:\n"
        "    sys.modules[m] = None\n"
        f"import {module}\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, timeout=120
    )
    assert result.returncode == 0, result.stderr[-2000:]
