import sys
import random
from collections import Counter

lambda_1 = 0.5
lambda_2 = 0.25
lambda_3 = 0.25

e_mle = Counter()
singles = Counter()
pairs = Counter()
triplets = Counter()
words_counter = 0

def write_q_mle_to_file(singles, pairs, triplets,q_file):
    write_counter_to_file(q_file,singles,'w')
    write_counter_to_file(q_file,pairs,'a')
    write_counter_to_file(q_file,triplets,'a')

def write_e_mle_to_file(e_mle, e_file):
    write_counter_to_file(e_file,e_mle,'w')

def write_counter_to_file(file_name, counter,flag):
    with open(file_name, flag) as file:
        for key in counter:
            file.write(" ".join(key) + "\t" + str(counter[key]) + "\n")


def get_word_and_tag(token):
    k = token.rfind("/")
    return token[:k], token[k + 1:]

def getE(w,t):
    if (singles[(t,)]!=0):
        return float(e_mle[(w,t)])/singles[(t,)]
    else:
        #return 0
        return random.uniform(0, 1)

def getQ(t1,t2,t3):
    #t1 = a, t2 = b, t3 = c
    first_prob = 0
    sec_prob = 0
    third_prob = 0
    if pairs[(t1,t2)] > 0:
        first_prob = lambda_1 * (float(triplets[(t1, t2, t3)]) / pairs[(t1, t2)])

    if singles[(t2,)] > 0:
        sec_prob = lambda_2 * (float(pairs[(t2, t3)]) / singles[(t2,)])

    if words_counter > 0:
        third_prob = lambda_3 * (float(singles[(t3,)]) / words_counter)

    return  first_prob + sec_prob + third_prob



def initialize_dicts_from_file(e_mle_file, q_mle_file):
    global e_mle
    e_mle = Counter()
    global singles
    singles = Counter()
    global pairs
    pairs = Counter()
    global riplets
    triplets = Counter()
    global words_counter
    words_counter = 0
    # e_mle = Counter()
    # singles = Counter()
    # pairs = Counter()
    # triplets = Counter()

    with open(e_mle_file, 'r') as f:
        content = f.readlines()
        for line in content:
            line = line.strip("\n")
            if line == "":
                continue
            key, value = line.split("\t")
            value = int(value)
            words_counter += value
            word, tag = key.split(" ")
            e_mle[(word, tag)] = value

    with open(q_mle_file, 'r') as f:
        content = f.readlines()
        for line in content:
            line = line.strip("\n")
            if line == "":
                continue
            key, value = line.split("\t")
            value = int(value)
            tags = tuple(key.split(" "))
            if len(tags) == 1:
                singles[tags] = value
            elif len(tags) == 2:
                pairs[tags] = value
            elif len(tags) == 3:
                triplets[tags] = value

def main(argv):
    if (len(argv)!=3):
        exit(1)
    input_file_name = argv[0]
    q_file = argv[1]
    e_file = argv[2]

    global e_mle
    e_mle = Counter()
    global singles
    singles = Counter()
    global pairs
    pairs = Counter()
    global riplets
    triplets = Counter()


    with open(input_file_name, 'r') as input_file:
        content = input_file.readlines()
        global lala
        lala = 0
        for line in content:
            one_prev = 'STR'
            two_prev = 'STR'

            token_list = line.strip('\n').strip().split(" ")
            for token in token_list:
                try:
                    w , tag = get_word_and_tag(token)
                    lala += 1
                    # fill e_mle
                    e_mle[(w,tag)] +=1
                    # fill q_mle
                    singles[(tag,)] += 1
                    pairs[(one_prev, tag)] += 1
                    triplets[(two_prev, one_prev, tag)] += 1
                    # swap and update params
                    temp = one_prev
                    one_prev = tag
                    two_prev = temp

                except Exception:
                    continue

    write_q_mle_to_file(singles,pairs,triplets,q_file)
    write_e_mle_to_file(e_mle,e_file)

if __name__ == "__main__":
	main(sys.argv[1:])


