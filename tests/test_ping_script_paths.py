#!/usr/bin/env python3
"""Mock workspace tests for ping_script_paths.py.

These tests exercise the diagnostic against temporary workspaces so missing
critical dependencies and fully aligned workspaces are both demonstrated
without claiming anything about the user's actual local filesystem.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "ping_script_paths.py"

REQUIRED = [
    "archives/AI-LEGION-CREATIVE-CONVERGENCE",
    "verify_repo_states.py",
    "PROVENANCE-LOG-TEMPLATE.md",
    "SCHEMA-MACHINE-READABLE.yaml",
    "THREE_LAYER_FOUNDATION_SEALED.md",
    "RELEASE_v1.0.0_MANIFEST.json",
]


class PingScriptPathsTests(unittest.TestCase):
    def run_verifier(self, workspace: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VERIFIER)],
            cwd=workspace,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_missing_critical_dependency_returns_nonzero(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            result = self.run_verifier(workspace)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("MISALIGNED", result.stdout)
            self.assertIn("Independent Verification Performed: ❌ NO", result.stdout)

    def test_all_critical_paths_aligned_returns_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            (workspace / "archives/AI-LEGION-CREATIVE-CONVERGENCE").mkdir(parents=True)
            for relative in REQUIRED[1:]:
                path = workspace / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("test fixture\n", encoding="utf-8")

            result = self.run_verifier(workspace)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("All critical paths verified", result.stdout)
            self.assertIn("READY FOR EXECUTION", result.stdout)


if __name__ == "__main__":
    unittest.main()
