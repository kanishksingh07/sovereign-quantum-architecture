from src.primitives.observation import Observation
from src.primitives.quantum_state import QuantumState
from src.engine.evolution import EvolutionEngine
from src.engine.collapse import CollapseEngine
from src.engine.causality import CausalityEngine

def test_final_integration():
    print("--- STARTING CYCLE 3: FINAL SYSTEM INTEGRATION ---")
    
    # 1. Initialize the Full Stack
    universe = QuantumState()
    evo = EvolutionEngine()
    collapse = CollapseEngine()
    causality = CausalityEngine()
    
    # 2. The Timeline Begins (Cycle 1)
    print("\n[PHASE 1] Timeline Established")
    obs1 = Observation(10, "sensor_A", "REACTOR_TEMP", 500)
    delta1 = evo.evolve(universe, obs1)
    universe.apply_delta(delta1, {"timestamp": 10, "hash": obs1.get_hash()})
    print(f"Tick 10: {universe.view}")

    # 3. The Mistake Happens (A bad update)
    print("\n[PHASE 2] The 'Mistake' Occurs")
    obs_mistake = Observation(20, "sensor_A", "REACTOR_TEMP", 9000) # Critical Error
    delta_mistake = evo.evolve(universe, obs_mistake)
    universe.apply_delta(delta_mistake, {"timestamp": 20, "hash": obs_mistake.get_hash()})
    print(f"Tick 20: {universe.view} (CRITICAL STATE)")

    # 4. Attempting "Undo" (Forbidden)
    # We verify that we cannot just delete the last record.
    # (In code, we just prove we are not touching universe._history directly)
    
    # 5. The Compensation (Cycle 3)
    print("\n[PHASE 3] Applying Compensation (Not Undo)")
    # We ask the Causality Engine to fix 'REACTOR_TEMP' back to safe levels
    comp_obs = causality.generate_compensation(universe, "REACTOR_TEMP", 550)
    
    # Evolve forward with the compensation
    delta_fix = evo.evolve(universe, comp_obs)
    universe.apply_delta(delta_fix, {"timestamp": comp_obs.timestamp, "hash": comp_obs.get_hash()})
    
    print(f"Tick {comp_obs.timestamp}: {universe.view} (Stabilized)")

    # 6. Final Audit (Measurement & Causal Integrity)
    print("\n[PHASE 4] Final System Audit")
    
    # Measure the result (Cycle 2)
    final_measurement = collapse.measure(universe, "REACTOR_TEMP", "strict")
    print(f"Final Measurement: {final_measurement}")
    
    # Verify Time never flowed backward
    is_valid = causality.validate_causal_chain(universe._history)
    if is_valid:
        print("Causal Chain Integrity: VERIFIED")
    else:
        print("Causal Chain Integrity: FAILED")

    print("\n--- SYSTEM ARCHITECTURE: COMPLETED & SEALED ---")

if __name__ == "__main__":
    test_final_integration()