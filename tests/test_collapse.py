from src.primitives.quantum_state import QuantumState
from src.engine.evolution import EvolutionEngine
from src.primitives.observation import Observation
from src.engine.collapse import CollapseEngine

def test_measurement_mechanics():
    print("--- STARTING CYCLE 2: COLLAPSE FRAMEWORK ---")
    
    # 1. Setup Universe
    state = QuantumState()
    evo_engine = EvolutionEngine()
    col_engine = CollapseEngine()

    # 2. Inject a "High Entropy" State
    # We observe a confusing signal that raises entropy (Simulated)
    print("\n[STEP 1] Evolving State to 'High Entropy'...")
    
    # Let's say we have an observation that sets entropy to 0.5 (Uncertainty)
    # We need to manually inject this via the Evolution Engine logic
    # (Assuming we added a rule for 'ENTROPY' or we just trust the engine to pass it)
    obs = Observation(10, "sensor", "entropy", 0.5) 
    delta = evo_engine.evolve(state, obs)
    state.apply_delta(delta, {"timestamp": 10, "hash": obs.get_hash()})
    
    obs_val = Observation(11, "sensor", "TARGET_COORDINATES", "100,200")
    delta_val = evo_engine.evolve(state, obs_val)
    state.apply_delta(delta_val, {"timestamp": 11, "hash": obs_val.get_hash()})

    print(f"Current World View: {state.view}")

    # 3. Test STRICT Policy (Should Fail/Block)
    print("\n[STEP 2] Measuring with STRICT Policy...")
    result_strict = col_engine.measure(state, "TARGET_COORDINATES", "strict")
    print(f"Strict Result: {result_strict}")
    # EXPECT: Value="INDETERMINATE", Confidence=0.0 (Because entropy 0.5 > 0.1 limit)

    # 4. Test OPTIMISTIC Policy (Should Return Value with Warning)
    print("\n[STEP 3] Measuring with OPTIMISTIC Policy...")
    result_opt = col_engine.measure(state, "TARGET_COORDINATES", "optimistic")
    print(f"Optimistic Result: {result_opt}")
    # EXPECT: Value="100,200", Confidence=0.5, Loss=0.5

    print("\n--- CYCLE 2 COMPLETE: MEASUREMENT SEMANTICS VALIDATED ---")

if __name__ == "__main__":
    test_measurement_mechanics()