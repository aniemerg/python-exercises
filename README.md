# Python exercises

A small template for solving one coding exercise at a time, starting with tests.
Requires Python 3; no dependencies or environment setup needed.

## Start an exercise

```sh
cd ~/dev6
git clone git@github.com:aniemerg/python-exercises.git exercise-2
cd exercise-2
```

Choose a new folder name for each exercise.

## Work on an exercise

1. Paste the exercise into the triple-quoted area at the top of `test_main.py`.
2. Copy or uncomment the entire example test class. Change the inputs and expected
   outputs to match your exercise, and add methods named `test_...` for more cases.
   Keep the methods inside the class and the assertions inside their methods.
3. Run `python3 -m unittest -v`. Confirm your tests are listed and fail because
   `solve` raises `NotImplementedError`. **"Ran 0 tests" means you haven't enabled
   any tests yet**, even if the command prints `OK`.
4. Implement `solve` in `main.py`, replacing `*args, **kwargs` with the arguments
   your exercise needs, such as `nums, target`.
5. Run the tests again. Read any failures, update your solution, and repeat until
   all tests pass. Add edge cases as you go.

Use `self.assertEqual(actual, expected)` for exact results. When the exercise
allows a list in any order (such as Two Sum indices), use
`self.assertCountEqual(actual, expected)` instead.

## Commands

```sh
python3 -m unittest -v  # Run all tests
python3 test_main.py -v  # Same tests, directly
python3 -m unittest test_main.SolveTests.test_case_1 -v  # Run one test
```

Adjust the class and method names in the last command if you renamed them.
To try inputs manually, edit the `print(solve(...))` call at the bottom of
`main.py`, then run `python3 main.py`. The initial stub intentionally raises
`NotImplementedError`; importing it from tests does not run the manual example.

If `python --version` reports Python 3 on your system, `python` works too.
