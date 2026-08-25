import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import technocore_agent


class VerifyProofCommandTests(unittest.TestCase):
    def test_invalid_utf8_is_reported_without_a_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            proof_path = Path(directory) / "proof.json"
            proof_path.write_bytes(b"\xff")
            stderr = io.StringIO()

            with contextlib.redirect_stderr(stderr):
                exit_code = technocore_agent.main(
                    ["verify-proof", str(proof_path)]
                )

        self.assertEqual(exit_code, 1)
        self.assertIn("error: cannot read proof JSON:", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
