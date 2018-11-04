import sys

def main(argv):
    if (len(argv)!=3):
        exit(1)
    input_file_name = argv[0]
    q_file = argv[1]
    e_file = argv[2]

    e_mle_dict = {}
    with open(input_file_name, 'r') as input_file:
        content = input_file.readlines()
        for line in content:
            words_list = line.strip('\n').strip().split(" ")
            for word in words_list:
                try:
                    k = word.rfind("/")
                    w , tag = word[:k], word[k+1:]
                    if (w,tag) in e_mle_dict:
                        e_mle_dict[(w,tag)] +=1
                    else:
                        e_mle_dict[(w,tag)] = 1
                except Exception:
                    continue
    write_e_dict_to_file(e_file, e_mle_dict)


def write_e_dict_to_file(e_file, e_mle_dict):
    with open(e_file, 'w') as file:
        for key, value in e_mle_dict.iteritems():
            word, tag = key
            file.write(word + " " + tag + "\t" + str(value) + "\n")




def getQ(t1,t2,t3):
    print "liz"

if __name__ == "__main__":
	main(sys.argv[1:])


