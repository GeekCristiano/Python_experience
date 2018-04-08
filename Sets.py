# Study sets in python

def main():
    set1 = {1, 19, 45, 78}
    numbers = [5, 78, 9, 6, 19]
    set2 = set(numbers)
    print("Difference between first and second set:", set1.difference(set2))
    print("Difference another way:", set1 - set2)
    print("Difference another way:", set2 - set1)
    print("Difference between second and first set:", set2.difference(set1))

    print("Union:", set2.union(set1))
    print("Intersections:", set2.intersection(set1))


if __name__ == "__main__":
    main()
