import os
from dotenv import load_dotenv
from bluequbit.bluequbit_client import BQClient
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

load_dotenv()
api_key = os.getenv("BLUEQ_API_KEY")

client = BQClient(api_token=api_key)

qasm_file_path = "P1_little_peak.qasm"
qc = QuantumCircuit.from_qasm_file(qasm_file_path)

job = client.run(qc)

raw_sv = job.get_statevector()

statevector = Statevector(raw_sv)

probs = statevector.probabilities_dict()
most_probable = max(probs, key=probs.get)
print(f"Most probable bitstring: {most_probable}")
print(f"Probability: {probs[most_probable]:.4f}")
