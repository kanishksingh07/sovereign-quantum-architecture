import copy
from typing import Dict, Any, List
# Last Updated: Cycle 3 Completion

class QuantumState:
    """
    The isolated state container.
    Constraints:
    - No hidden global state[cite: 46].
    - Never mutates history[cite: 35].
    """
    def __init__(self):
        # The Ledger: An append-only log of all accepted state transitions
        self._history: List[Dict[str, Any]] = []
        
        # The Collapse: The current computed view of reality
        self._current_view: Dict[str, Any] = {"status": "INIT", "entropy": 0}
        
        # The Clock: Tracks the latest valid time seen
        self._last_tick: int = 0

    @property
    def view(self) -> Dict[str, Any]:
        """Returns a copy of the current view (read-only snapshot)."""
        return self._current_view.copy()

    @property
    def last_tick(self) -> int:
        return self._last_tick

    def apply_delta(self, delta: Dict[str, Any], meta: Dict[str, Any]):
        """
        The ONLY entry point for state change. 
        Strictly append-only.
        """
        if not delta:
            return

        record = {
            "tick": meta['timestamp'],
            "hash": meta['hash'],
            "delta": delta,
            "prev_hash": self._history[-1]['hash'] if self._history else "GENESIS"
        }
        
        # 1. Commit to History
        self._history.append(record)
        
        # 2. Update View (The Collapse)
        self._current_view.update(delta)
        
        # 3. Advance Time
        self._last_tick = meta['timestamp']

    # --- INVARIANT: NO CLONING ---
    def __copy__(self):
        raise RuntimeError("VIOLATION: QuantumState cannot be cloned.")

    def __deepcopy__(self, memo):
        raise RuntimeError("VIOLATION: QuantumState cannot be cloned.")