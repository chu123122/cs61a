def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    i = 1
    while i <= n:
        number_3,number_5=i%3==0,i%5==0
        if number_3 and number_5:
            print('fizzbuzz')
        elif  number_3:
            print('fizz')
        elif  number_5:
            print('buzz')
        else:
            print(i)
        i += 1
##################
def is_prime(n):
    """check a number whether is prime number
    >>> is_prime(3)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n==1:
        return False
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True

##################
def has_dight(n,k):
    while n>0:
        if n%10==k:
            return True
        n//=10
    return False

def current_number_right(n,k):
    """
    check current number whether is k
    """
    if n%10==k:
        return True
    else:
        return False

def unique_dights(n):
    """ check a number whether has unqiue dights
    >>> unique_dights(121)
    1
    >>> unique_dights(2984)
    4
    """
    i,unique=0,0
    while i<10:
        amount,number=0,n
        while has_dight(number,i):
            if current_number_right(number,i):
                amount+=1
            number//=10
        if amount==1:
            unique+=1
        i+=1
    return unique