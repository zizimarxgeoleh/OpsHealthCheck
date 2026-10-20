# Summary

This application checks service health across multiple rounds and generates a JSON
report. Investigate and repair inconsistent behavior in retries, incident handling,
scheduling, and reporting. Add regression tests that demonstrate your fixes.

## Expected behavior
Checks should respect configured retry limits and time budgets. Service state should
remain consistent across rounds, maintenance should suppress alerts, and results
should preserve service order. Reports should accurately reflect failures and
recoveries; unsuccessful exports should preserve existing files.

## Run
Install dependencies in a virtual environment, then run from the project root:

```bash
python -m pip install -r requirements.txt
python healthcheck.py --config services.yaml --output report.json
python -m unittest discover -s tests -v
```

Modify application code only; do not change the installed package or its pinned
version. Mock HTTP calls and use deterministic tests. Resolve setup issues
before starting the timed session.

## Submit
Return the modified project, at least eight new meaningful tests, and `NOTES.md`
summarizing your findings, decisions, verification, and unfinished work.
Documentation search and AI tools are allowed; disclose their use and be ready to
explain your solution. Evaluation considers correctness, testing, clarity, and
operational judgment. Partial solutions with clear reasoning are accepted.
