"""Execute the report in a fresh kernel and check saved outputs."""
from pathlib import Path
import json, sys, tempfile
import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager

root = Path(__file__).resolve().parents[1]
path = root / "Assignment1_Data_Profiling.ipynb"
nb = nbformat.read(path, as_version=4)
nbformat.validate(nb)
# Bind exactly this Python environment without requiring a global kernel installation.
with tempfile.TemporaryDirectory() as temp:
    spec = Path(temp)/"python3"
    spec.mkdir()
    (spec/"kernel.json").write_text(json.dumps({"argv":[sys.executable,"-m","ipykernel_launcher","-f","{connection_file}"],
        "display_name":"Assignment 1 verification","language":"python"}),encoding="utf-8")
    manager = KernelSpecManager(kernel_dirs=[temp])
    client = NotebookClient(nb, timeout=180, kernel_name="python3", resources={"metadata":{"path":str(root)}},
                            record_timing=True)
    from jupyter_client import AsyncKernelManager
    client.km = AsyncKernelManager(kernel_name="python3", kernel_spec_manager=manager)
    client.execute()
nbformat.write(nb,path)
codes = [c for c in nb.cells if c.cell_type=="code"]
assert all(c.execution_count is not None for c in codes)
assert not [o for c in codes for o in c.outputs if o.output_type=="error"]
figs = sorted((root/"reports/figures").glob("*.png"))
assert len(figs)>=3 and all(p.stat().st_size>5000 for p in figs)
summary = json.loads((root/"reports/quality_summary.json").read_text(encoding="utf-8"))
assert summary["raw_reviews"]==327 and summary["source_titles"]==39
assert all(summary["checks"].values())
result = {"status":"passed","executed_code_cells":len(codes),"figures":len(figs),
          "quality_contracts_passed":len(summary["checks"]),"fresh_kernel":True,
          "python_executable":Path(sys.executable).name}
(root/"reports/execution_check.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
