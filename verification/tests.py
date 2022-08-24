"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [151],
            "answer": True
        },
        {
            "input": [212],
            "answer": True
        },
        {
            "input": [321],
            "answer": False
        }
    ],
    "Extra": [
        {
            "input": [222],
            "answer": True
        },
        {
            "input": [1212],
            "answer": False
        },
        {
            "input": [12121],
            "answer": True
        },
        {
            "input": [12345654321],
            "answer": True
        },
        {
            "input": [121235565532121],
            "answer": True
        },
        {
            "input": [110001],
            "answer": False
        }
    ]
}
