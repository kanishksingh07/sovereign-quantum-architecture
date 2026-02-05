from dataclasses import dataclass
from typing import Any, Optional, Dict
from src.primitives.quantum_state import QuantumState

# --- 1. THE OUTPUT ARTIFACT ---
@dataclass(frozen=True)
class CollapseResult:
    """
    The outcome of a measurement event.
    Satisfies: Produces observed value, confidence, and declared information loss.
    """
    observed_value: Any      # The 'Fact' extracted
    confidence: float        # 0.0 to 1.0 (How sure are we?)
    information_loss: float  # 0.0 to 1.0 (Did we discard nuance?)
    policy_used: str         # The rule that forced this result

# --- 2. THE MEASUREMENT POLICIES ---
class MeasurementPolicy:
    """
    Defines how we resolve uncertainty.
    Satisfies: Applies explicit measurement policies.
    """
    @staticmethod
    def strict(value: Any, entropy: float) -> CollapseResult:
        """High stakes: If uncertain, fail safe."""
        if entropy > 0.1:
            return CollapseResult("INDETERMINATE", 0.0, 1.0, "STRICT")
        return CollapseResult(value, 1.0, 0.0, "STRICT")

    @staticmethod
    def optimistic(value: Any, entropy: float) -> CollapseResult:
        """Low stakes: Return best guess but flag the risk."""
        confidence = max(0.0, 1.0 - entropy)
        return CollapseResult(value, confidence, entropy, "OPTIMISTIC")

# --- 3. THE COLLAPSE ENGINE ---
class CollapseEngine:
    """
    Deterministically extracts values from the Sovereign State.
    Satisfies: Deterministic collapse with replay guarantees.
    """
    def measure(self, state: QuantumState, observable: str, policy_name: str = "strict") -> CollapseResult:
        # 1. READ RAW STATE
        view = state.view
        raw_val = view.get(observable)
        
        # Simulate "Entropy" (In a real system, this comes from conflicting signals)
        # Here, we derive it from system health or specific 'entropy' fields
        current_entropy = view.get("entropy", 0.0) 
        
        # 2. APPLY POLICY [cite: 67]
        # We select the strategy for resolving this value.
        if policy_name == "optimistic":
            return MeasurementPolicy.optimistic(raw_val, current_entropy)
        else:
            # Default to STRICT (Safety first)
            return MeasurementPolicy.strict(raw_val, current_entropy)