from dataclasses import dataclass
from typing import Any
# Last Updated: Cycle 3 Completion

@dataclass(frozen=True)
class Observation:
    """
    An immutable record of an external event.
    Constraints:
    - Accepts inputs strictly as observations.
    - Never executes actions[cite: 36].
    """
    timestamp: int       # Logical time (Tick)
    observer_id: str     # Who saw it? (Sensor/Actor ID)
    observable: str      # What property was measured?
    value: Any           # The raw data payload

    def get_hash(self) -> str:
        """Generates a cryptographic signature of the observation."""
        content = f"{self.timestamp}:{self.observer_id}:{self.observable}:{self.value}"
        return hashlib.sha256(content.encode()).hexdigest()