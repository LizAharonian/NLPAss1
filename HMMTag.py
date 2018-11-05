import sys
import MLETrain as mle


def get_top_tag(w,one_prev,two_prev):
    max_score = 0
    final_t = None
    for t in mle.singles:
        # calculate q
        temp_score = mle.getE(w,t) * mle.getQ(t,one_prev,two_prev)
        if temp_score > max_score:
            max_score = temp_score
            final_t = t
    return final_t

def greedy_algo():
    with open(input_file_name, 'r') as input_file:
        content = input_file.readlines()
        for line in content:
            one_prev = None
            two_prev = None
            words_list = line.strip('\n').strip().split(" ")
            for word in words_list:
                try:
                    tag = get_top_tag(word, one_prev, two_prev)
                    # swap and update params
                    temp = one_prev
                    one_prev = tag
                    two_prev = temp

                except Exception:
                    continue




argv = sys.argv[1:]
if (len(argv)!=5):
    exit(1)
input_file_name = argv[0]
q_file = argv[1]
e_file = argv[2]
out_file_name = argv[3]
extra_file_name = argv[4]


