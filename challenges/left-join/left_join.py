from hash_table import HashTable


def left_join(ht_syn, ht_ant):
    """
    Takes in two hash tables and returns a list of lists.
    Each nested list contains the word, its synonym and either
    its antonym or None if no antonym exists on the second hash table.
    """
    output_list = []
    print(ht_syn.buckets)
    print(ht_ant.buckets)
    for entry in ht_syn.buckets:
        # import pdb; pdb.set_trace()
        # print(ht_syn.buckets)
        # print(entry)
        if entry.head.val is not None:

            current_dict = entry.head.val
            
            word_key = list(current_dict.keys())[0]

            output_list.append([
                word_key,
                entry.head.val[word_key],
                ht_ant.get(word_key)
            ])
    
    return output_list
