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
            "input": [6, 2],
            "answer": False
        },
        {
            "input": [34, 2],
            "answer": False
        },
        {
            "input": [455, 2],
            "answer": True
        }
    ],
    "Extra": [
        {
            "input": [693, 2],
            "answer": True
        },
        {
            "input": [2409, 2],
            "answer": True
        },
        {
            "input": [20, 3],
            "answer": True
        },
        {
            "input": [44, 3],
            "answer": False
        },
        {
            "input": [84, 3],
            "answer": False
        },
        {
            "input": [88, 3],
            "answer": False
        },
        {
            "input": [4264, 3],
            "answer": True
        },
        {
            "input": [9841, 3],
            "answer": True
        },
        {
            "input": [20, 4],
            "answer": False
        },
        {
            "input": [100, 4],
            "answer": False
        },
        {
            "input": [8802, 4],
            "answer": True
        },
        {
            "input": [9286, 4],
            "answer": True
        },
        {
            "input": [40, 5],
            "answer": False
        },
        {
            "input": [961, 5],
            "answer": True
        },
        {
            "input": [96, 5],
            "answer": False
        },
        {
            "input": [24, 8],
            "answer": False
        },
        {
            "input": [89, 8],
            "answer": True
        },
        {
            "input": [16, 10],
            "answer": False
        },
        {
            "input": [404, 10],
            "answer": True
        },
        {
            "input": [1441, 10],
            "answer": True
        },
        {
            "input": [1442, 10],
            "answer": False
        },
        {
            "input": [1413, 16],
            "answer": True
        },
        {
            "input": [2056, 16],
            "answer": True
        },
        {
            "input": [3148, 16],
            "answer": True
        },
        {
            "input": [4, 100],
            "answer": True
        },
        {
            "input": [108, 100],
            "answer": False
        },
        {
            "input": [157, 100],
            "answer": False
        },
        {
            "input": [707, 100],
            "answer": True
        },
        {
            "input": [4545, 100],
            "answer": True
        }
    ]
}
