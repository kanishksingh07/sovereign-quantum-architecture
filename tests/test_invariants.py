from src.primitives.observation import Observation
from src.primitives.quantum_state import QuantumState
from src.engine.evolution import EvolutionEngine
import copy
# Last Updated: Cycle 3 Completion

def run_abuse_test():
    print("--- STARTING DAY 1 VALIDATION ---")
    
    engine = EvolutionEngine()
    universe = QuantumState()

    # 1. Test Deterministic Replay [cite: 45]
    print("\n[TEST] Normal Evolution...")
    obs1 = Observation(10, "sensor_1", "SYSTEM_STATUS", "CRITICAL")
    delta1 = engine.evolve(universe, obs1)
    universe.apply_delta(delta1, {"timestamp": 10, "hash": obs1.get_hash()})
    print(f"State: {universe.view}")

    # 2. Test Impossible Transition [cite: 40]
    print("\n[TEST] Attempting Illegal Transition (CRITICAL -> HEALTHY)...")
    obs2 = Observation(20, "sensor_1", "SYSTEM_STATUS", "HEALTHY")
    delta2 = engine.evolve(universe, obs2)
    universe.apply_delta(delta2, {"timestamp": 20, "hash": obs2.get_hash()})
    print(f"State: {universe.view} (Expect 'RECOVERY')")

    # 3. Test Retroactive Mutation [cite: 50]
    print("\n[TEST] Attempting Time Travel (timestamp 15 < 20)...")
    try:
        obs_past = Observation(15, "hacker", "INJECT", "MALWARE")
        engine.evolve(universe, obs_past)
    except ValueError as e:
        print(f"BLOCKED: {e}")

    # 4. Test No-Cloning 
    print("\n[TEST] Attempting to Clone Universe...")
    try:
        fake_universe = copy.copy(universe)
    except RuntimeError as e:
        print(f"BLOCKED: {e}")

    print("\n--- DAY 1 COMPLETE: SEALED ---")

if __name__ == "__main__":
    run_abuse_test()