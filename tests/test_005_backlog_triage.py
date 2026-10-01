import unittest

from chargeback_evidence_builder.models import Record
from chargeback_evidence_builder.scoring import score_record


class DepthCheck5(unittest.TestCase):
    def test_005_backlog_triage(self):
        record = Record(id="dispute-005", exposure=22194, signal=0.593, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
