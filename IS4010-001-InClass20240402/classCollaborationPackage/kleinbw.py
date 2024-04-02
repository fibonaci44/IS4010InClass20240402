# Name : Ben Klein
# Email : kleinbw@mail.uc.edu
# Brief Description : Defines the kleinbw function


def kleinbw(n):
    """
    :type n: int
    :rtype: int
    Function prompt : Write a function that takes the binary representation of a positive integer and returns the number of 
    set bits
     it has (also known as the Hamming weight).
    Returns the number of bits for a given n int
    """
    
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

    if __name__ == "__main__":
        n = 3
        print(kleinbw(n))
