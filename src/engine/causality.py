from typing import List, Dict, Any, Optional
from src.primitives.quantum_state import QuantumState
from src.primitives.observation import Observation
# Last Updated: Cycle 3 Completion

class CausalityEngine:
    """
    Enforces strict time ordering and manages irreversible history.
    Satisfies: Append-only timelines.
    Satisfies: Compensation over undo.
    """
    
    def validate_causal_chain(self, history: List[Dict[str, Any]]) -> bool:
        """
        Audits the history to ensure time never moved backward.
        """
        if not history:
            return True
            
        last_tick = -1
        for record in history:
            tick = record['tick']
            if tick <= last_tick:
                return False # CAUSALITY VIOLATION FOUND
            last_tick = tick
        return True

    def generate_compensation(self, state: QuantumState, target_observable: str, correction_value: Any) -> Observation:
        """
        Instead of 'undoing' a bad state, we create a new observation 
        that forces the state to the correct value moving forward.
        """
        # We must move time FORWARD.
        # If the last tick was 100, the compensation must happen at 101+.
        new_tick = state.last_tick + 1
        
        return Observation(
            timestamp=new_tick,
            observer_id="SYSTEM_COMPENSATOR",
            observable=target_observable,
            value=correction_value
        )