def easy():
    return 1


def medium(nums):

    total = 0

    for i in nums:
        if i > 0:
            total += i

    return total


def hard(nums):

    total = 0

    for i in nums:

        if i > 0:

            for j in nums:

                if j % 2 == 0:

                    for k in nums:

                        total += k

    return total