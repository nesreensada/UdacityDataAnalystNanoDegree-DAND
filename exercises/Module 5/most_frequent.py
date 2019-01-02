"""Quiz: Most Frequent Word"""

def most_frequent(s):
    """Return the most frequently occuring word in s."""
    
    # HINT: Use the built-in split() function to transform the string s into an
    #       array
    
    # HINT: Sort the new array by using the built-in sorted() function or
    #       .sort() list method
    
    # HINT: Iterate through the array and count each occurance of every word
    #       using the .count() list method
    
    # HINT: Find the number of times the most common word appears using max()
    
    # HINT: Locate the index of the most frequently seen word
    
    # HINT: Return the most frequent word. Remember that if there is a tie,
    #       return the first (tied) word in alphabetical order.
    split_string = s.split()
    split_string.sort()
    max_word = split_string[0]
    max_count = 0
    for word in split_string:
        count = split_string.count(word)
        if(count > max_count or (count == max_count and max_word >= word) ):
            max_word = word
            max_count = count
    result = max_word
    return result


def test_run():
    """Test most_frequent() with some inputs."""
    print(most_frequent("cat bat mat cat bat cat")) # output: 'cat'
    print(most_frequent("betty bought a bit of butter but the butter was bitter")) # output: 'butter'


if __name__ == '__main__':
    test_run()

