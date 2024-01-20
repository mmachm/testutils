# Testutils

Those are little helper tools that I have developed in my free time to help me write quick tests.


## Expand Parameters

Expand parameters is an upgraded version of parameterize.expand(), which does not return None.
When one tries to run `parameterize.expand`decorated testcase, one gets an error along the lines of 
cannot create a test from None, because the return value of the original decorator is None. 
With the new decorator one can run the function directly with the little green arrow in Pycharm. 
And one can choose which parametrization case will be taken as default.

There are many interesting and non-trivial aspects one can run up against.
As I remark in `test_expand_parameters.py`, some of it is pretty cursed. But it is also extremely fun to think about. 

## Merge

When comparing nested structures of lists and dictionaries, one often uses objects like `unittests.mock.ANY`,
which is an object that compares as equal to anything. 
One might use this for timestamps in the tests or for any other object. 
When the expected object and the actual object do not compare as equal, their `__repr__` representation is taken,
formatted according to some pprint scheme, and compared - character for character. 


This means, that in the resulting diff, one sees a lot of irrelevant information like
```bash
ANY != '2024-01-20T12:30:45Z'
^^^    ^^^^^^^^^^^^^^^^^^^^^^
```
This leads to enormous diffs, in which it is really difficult to quickly spot what is actually wrong. 

The solution to that is call merge on the two objects prior to `assertEqual`.
```bash
self.assertEqual(*merge(expected_result, actual_result, message))
```
## Rex
This is an object, which compares as equal with strings (or other `Rex` objects), 
if the string matches a regex pattern for which the `Rex` object has been initiated. 
This is useful when using `factory_boy` factories, which do not reset between tests. 
Then the order of execution of tests will affect the numbers in the response, for example.

## SOME
Much like `ANY` for the purpose of writing quick tests, but it checks the type of the object to which it is being compared.
```bash
SOME(int) == 7    # True
SOME(int) == "7"  # False
```