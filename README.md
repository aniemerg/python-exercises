# Python exercises

A small workspace for solving one coding exercise at a time. Requires Python 3;
there are no dependencies to install.

## Run

```sh
cd ~/dev6/python-exercises
python3 main.py          # Try the example input
python3 -m unittest -v  # Run all tests
```

You can also run the tests directly with `python3 test_main.py`.
If `python --version` reports Python 3 on your system, `python` works too.

## Work on an exercise

1. Define the expected behavior in `test_main.py`. Add methods whose names start
   with `test_`, using `self.assertEqual(solve(input_value), expected_value)`.
2. Run the tests to see the new test fail.
3. Write code in `main.py` until the tests pass.
4. Add edge cases and repeat.

The starter exercise reverses the order of words and normalizes whitespace.
Replace `solve` and its tests for your next exercise. Change the input at the
bottom of `main.py` for a quick manual run; importing it from tests does not run
that example.

To run a single test:

```sh
python3 -m unittest test_main.SolveTests.test_reverses_words -v
```
