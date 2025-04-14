import os
from dotenv import load_dotenv
from bluequbit.bluequbit_client import BQClient
from qiskit import QuantumCircuit

load_dotenv()
api_key = os.getenv("BLUEQ_API_KEY")

client = BQClient(api_token=api_key)

qasm_file_path = "P2_swift_rise.qasm"
qc = QuantumCircuit.from_qasm_file(qasm_file_path)

if qc.num_clbits == 0:
    qc.measure_all()

job = client.run(qc, shots=2048)
counts = job.get_counts()

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
most_probable, count = sorted_counts[0]

print(f"\nMost frequently measured bitstring: {most_probable}")
print(f"Count: {count} / {sum(counts.values())}")
print("\nTop 5 measured bitstrings:")
for bitstring, count in sorted_counts[:5]:
    print(f"{bitstring}: {count}")
