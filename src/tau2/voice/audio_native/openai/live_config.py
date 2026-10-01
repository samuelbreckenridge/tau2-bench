"""Re-export of the OpenAI Live config, which lives in ``tau2.data_model``.

The model is defined outside this package so that core (non-voice) code can
import it without pulling in the OpenAI realtime provider and its voice-only
dependencies (e.g. ``websockets``).
"""

from tau2.data_model.live_config import (  # noqa: F401
    DEFAULT_LIVE_BACKEND_PROMPT_TEMPLATE,
    DEFAULT_LIVE_FRONTEND_PROMPT_TEMPLATE,
    LiveConfig,
)
