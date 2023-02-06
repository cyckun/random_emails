import  random

def getRandomSet(bits):
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    total_set = num_set + char_set

    value_set = "".join(random.sample(total_set, bits))

    return value_set

if __name__ == '__main__':
    alice_file = "../emails_alice.txt"
    bob_file = "../emails_bob.txt"
    filea = open(alice_file, 'w')
    fileb = open(bob_file, 'w')
    N  = 20000000
    count = 0
    while count < N - 1000:
        random_str = getRandomSet(20)
        random_str_bob = random_str + "bob"
        filea.write(random_str)
        filea.write("\n")
        fileb.write(random_str_bob)
        fileb.write("\n")
        count = count + 1
    for i in range(0, 1000):
        random_str = getRandomSet(20)
        filea.write(random_str)
        filea.write("\n")
        fileb.write(random_str)
        fileb.write("\n")

    print("random email ok.")
