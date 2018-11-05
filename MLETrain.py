import sys
from collections import Counter

GAMA1 = 0.5
GAMA2 = 0.25
GAMA3 = 0.25


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
    if (singles[(t)]!=0):
        return e_mle[(w,t)]/singles[(t)]
    else:
        return 0

def getQ(t1,t2,t3):
    return 5
    #todo: q3 yoav
    return GAMA1 * (triplets[(t1,t2,t3)]/ pairs[(t1,t2)]) + GAMA2 * (pairs[(t2,t3)]/singles[(t2,)]) + GAMA3 * (singles[(t3,)]/counter_words)


def liz():
    print "kkk"

    print ""
argv = sys.argv[1:]
if (len(argv)!=3):
    exit(1)
input_file_name = argv[0]
q_file = argv[1]
e_file = argv[2]

e_mle = Counter()
singles = Counter()
pairs = Counter()
triplets = Counter()

one_prev = None
two_prev = None

with open(input_file_name, 'r') as input_file:
    content = input_file.readlines()
    counter_words = 0
    for line in content:
        token_list = line.strip('\n').strip().split(" ")
        for token in token_list:
            try:
                w , tag = get_word_and_tag(token)
                counter_words += 1
                # fill e_mle
                e_mle[(w,tag)] +=1
                # fill q_mle
                singles[(tag,)] += 1
                if one_prev != None:
                    pairs[(one_prev, tag)] += 1
                if two_prev != None:
                    triplets[(two_prev, one_prev, tag)] += 1
                # swap and update params
                temp = one_prev
                one_prev = tag
                two_prev = temp

            except Exception:
                continue
        one_prev = None
        two_prev = None

write_q_mle_to_file(singles,pairs,triplets,q_file)
write_e_mle_to_file(e_mle,e_file)

# if __name__ == "__main__":
# 	main(sys.argv[1:])


