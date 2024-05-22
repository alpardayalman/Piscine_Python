def give_bmi(
            height: list[int | float],
            weight: list[int | float]) -> list[int | float]:
    """
    This function calculates the BMI for a list of
    heights and weights.
    The formula for BMI is weight / height^2.
    Arguments are two lists of the same length,
    one for height and one for weight.
    Returns a list of BMI values.
    """
    try:
        assert len(height) == len(weight), \
            "Height and weight lists must be of the same length"
    except AssertionError as e:
        print(e)
        exit(1)
    bmi = []
    for i in range(len(height)):
        try:
            assert isinstance(height[i], (int, float)) and \
                isinstance(weight[i], (int, float)), \
                "Height and weight must be numbers"
            assert height[i] > 0 and weight[i] > 0, \
                "Height and weight must be positive numbers"
        except AssertionError as e:
            print(e)
            exit(1)
        bmi.append(weight[i] / (height[i] ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function takes a list of BMI values and a limit.
    It returns a list of booleans,
    True if the BMI is above the limit, False otherwise.
    """
    try:
        assert isinstance(limit, int) and limit >= 0, \
            "Limit must be a positive integer"
        for i in bmi:
            assert isinstance(i, (int, float)), \
                "BMI must be a number"
    except AssertionError as e:
        print(e)
        exit(1)
    return [b > limit for b in bmi]
