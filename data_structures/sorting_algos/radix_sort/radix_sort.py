"""Radix sort algorithm."""


def radix_sort(input_list, base=10):
    """
    Radix sort algorithm.

    Function which takes in a list of positive integers
    and returns a list sorted in ascending order.
    """
    if len(input_list) < 2:
        return input_list
    try:
        if min(input_list) < 0:
            print('List must only contain position integers or 0')
            return None
    except TypeError:
        print('All data must be same type i.e. int, str, etc...')
        return None

    counter = 0

    def put_in_bucket(input_list, base, counter):
        """Place all numbers in list in bucket of integer."""
        buckets = [[] for x in range(base)]
        for num in input_list:
            digit = (num // (base ** counter)) % base
            buckets[digit].append(num)
        return buckets

    def repopulate_list(buckets_list):
        """Repopulate list with bucket values in order."""
        lst = []
        for bucket in buckets_list:
            if len(bucket) > 0:
                for num in bucket:
                    lst.append(num)
        return lst

    while max(input_list) > base ** (counter):
            input_list = repopulate_list(put_in_bucket(
                input_list, base, counter))
            counter = counter + 1

    return input_list
