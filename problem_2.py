from collections import Counter
import time

buckets = [[] for _ in range(15)]


def read_dictionary(words_file):
    global dictionary
    
    with open(words_file) as sowpods:
        dictionary = sowpods.readlines()

    dictionary = [word.strip() for word in dictionary] 

    # longest_words = []
    # max_len = 0
    # for word in dictionary:
    #     if len(word) > 15:
    #         max_len = len(word)
    #         longest_words.append(word)

    for word in dictionary:
        l = len(word)
        buckets[l-1].append(word)


def build_anagrams():
    global ana

    ana = {}
    for word in dictionary:
        s = "".join(sorted(word))
        if s not in ana:
            ana[s] = [word]
        else:
            ana[s].append(word)


def find_anagrams_faster(word, original_word):
    sorted_word = "".join(sorted(word))
    if sorted_word not in ana:
        return []
    possible_anagrams = ana[sorted_word]
    anagrams = []
    
    for possible_anagram in possible_anagrams:
        anagrams.append(possible_anagram)
        if possible_anagram in parent:
            if distance[original_word] > distance[parent[possible_anagram]]:
                parent[possible_anagram] = original_word
        else:
            parent[possible_anagram] = original_word
    return anagrams


def find_anagrams_faster_modified(word, original_word):
    sorted_word = "".join(sorted(word))
    if sorted_word not in ana:
        return []
    possible_anagrams = ana[sorted_word]
    anagrams = []
    for possible_anagram in possible_anagrams:
        anagrams.append(possible_anagram)
        if possible_anagram in parent2:
            if distance2[original_word] > distance2[parent2[possible_anagram]]:
                parent2[possible_anagram] = original_word
        else:
            parent2[possible_anagram] = original_word
    return anagrams


def find_word_pyramid():
    global parent, distance
    
    read_dictionary('sowpods.txt')
    build_anagrams()

    parent = {}
    distance = {}

    curr_bucket_num = len(buckets) - 1 # needs to be corrected to actual largest bucket
    curr_bucket = buckets[curr_bucket_num]
    longest_so_far = curr_bucket[0]
    largest_dist = 0

    while largest_dist <= curr_bucket_num:
        for word in curr_bucket:
            s = []
            if word not in distance:
                s.append(word)
                distance[word] = 1
            # print("-----------")
            while len(s) > 0:
                curr_word = s.pop()

                # for all combos of 1 less letter
                for j in range(len(curr_word)):
                    temp_s = curr_word[:j] + curr_word[j+1:]
                    anagrams = find_anagrams_faster(temp_s, curr_word)

                    for anagram in anagrams:
                        if anagram not in distance:
                            s.append(anagram)
                            distance[anagram] = distance[curr_word] + 1
                            if distance[curr_word] + 1 > largest_dist:
                                largest_dist = distance[curr_word] + 1
                                longest_so_far = anagram
                    

            # if largest_dist > curr_bucket_num:
            #     return longest_so_far, largest_dist
        
        curr_bucket_num -= 1
        curr_bucket = buckets[curr_bucket_num]

    return longest_so_far, largest_dist


def find_anagrams_faster2(word, original_word):
    sorted_word = "".join(sorted(word))
    if sorted_word not in ana:
        return []
    possible_anagrams = ana[sorted_word]
    anagrams = []
    for possible_anagram in possible_anagrams:
        anagrams.append(possible_anagram)
        if possible_anagram in parent2:
            if distance2[original_word] >= distance2[parent2[possible_anagram][0]]:
                parent2[possible_anagram].append(original_word)
        else:
            parent2[possible_anagram] = [original_word]
    
    return anagrams


def find_all_word_pyraminds(L):
    global parent2, distance2
    
    read_dictionary('sowpods.txt')
    build_anagrams()

    longest_bucket_num = len(buckets) - 1 # needs to be corrected to actual largest bucket
    longest_bucket = buckets[longest_bucket_num]
    largest_dist = 0
    tips = []

    
    for word in longest_bucket:
        parent2 = {}
        distance2 = {}
        distance2[word] = 1

        s = []
        s.append(word)
        longest_with_curr_tip = 0
        while len(s) > 0:
            curr_word = s.pop()

            # for all combos of 1 less letter
            for j in range(len(curr_word)):
                temp_s = curr_word[:j] + curr_word[j+1:]
                anagrams = find_anagrams_faster_modified(temp_s, curr_word)

                for anagram in anagrams:
                    if anagram not in distance2:
                        s.append(anagram)
                        distance2[anagram] = distance2[curr_word] + 1
                        if distance2[curr_word] + 1 > longest_with_curr_tip:
                            longest_with_curr_tip = distance2[curr_word] + 1
                            # longest_so_far = anagram
            if longest_with_curr_tip >=L:
                tips.append(word)
                break

    return tips


def recover_word_pyramid():     
    w, longest_pyramid = find_word_pyramid()
    print(":::::::::::::::::::")
    print("Length: " + str(longest_pyramid))
    print(":::::::::::::::::::")
    print("       PATH")
    print(":::::::::::::::::::")

    while w in parent:
        print(w)
        w = parent[w]
    print(w)


def recover_all_pyramids():
    tips = find_all_word_pyraminds(15)
    print(":::::::::::::::::::")
    print(":::::::::::::::::::")
    print(len(tips))
    print(tips)


def find_anagrams_faster3(word, original_word):
    sorted_word = "".join(sorted(word))
    if sorted_word not in ana:
        return []
    possible_anagrams = ana[sorted_word]
    anagrams = []
    
    for possible_anagram in possible_anagrams:
        anagrams.append(possible_anagram)
        if possible_anagram in parent3:
            if distance3[original_word] > distance3[parent3[possible_anagram]]:
                parent3[possible_anagram] = original_word
        else:
            parent3[possible_anagram] = original_word
    return anagrams


def longest_pyramid_with_word_down(given_word):
    # find longest shorter path
    global parent3, distance3
    
    read_dictionary('sowpods.txt')
    build_anagrams()

    parent3 = {}
    distance3 = {}

    distance3[given_word] = 1

    l = len(given_word)
    longest_so_far = ""
    largest_dist = 0

    s = []
    s.append(given_word)
    
    while len(s) > 0:
        curr_word = s.pop()

        # for all combos of 1 less letter
        for j in range(len(curr_word)):
            temp_s = curr_word[:j] + curr_word[j+1:]
            anagrams = find_anagrams_faster3(temp_s, curr_word)

            for anagram in anagrams:
                if anagram not in distance3:
                    s.append(anagram)
                    distance3[anagram] = distance3[curr_word] + 1
                    if distance3[curr_word] + 1 > largest_dist:
                        largest_dist = distance3[curr_word] + 1
                        longest_so_far = anagram
                    
            if largest_dist >= l:
                return longest_so_far, largest_dist

    return longest_so_far, largest_dist


def find_anagrams_faster_up(word, original_word):
    sorted_word = "".join(sorted(word))
    if sorted_word not in ana:
        return []
    possible_anagrams = ana[sorted_word]
    anagrams = []
    
    for possible_anagram in possible_anagrams:
        anagrams.append(possible_anagram)
        if possible_anagram in predecessor:
            if distance4[original_word] > distance4[predecessor[possible_anagram]]:
                predecessor[possible_anagram] = original_word
        else:
            predecessor[possible_anagram] = original_word
    return anagrams

def longest_pyramid_with_word_up(given_word):
    # find longest shorter path
    global predecessor, distance4
    
    read_dictionary('sowpods.txt')
    build_anagrams()

    predecessor = {}
    distance4 = {}

    distance4[given_word] = 1

    l = len(buckets) - 1
    longest_so_far = ""
    largest_dist = 0

    s = []
    s.append(given_word)
    
    while len(s) > 0:
        curr_word = s.pop()

        # for all combos of adding 1 more letter
        for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            temp_s = curr_word + let
            anagrams = find_anagrams_faster_up(temp_s, curr_word)

            for anagram in anagrams:
                if anagram not in distance4:
                    s.append(anagram)
                    distance4[anagram] = distance4[curr_word] + 1
                    if distance4[curr_word] + 1 > largest_dist:
                        largest_dist = distance4[curr_word] + 1
                        longest_so_far = anagram
                    
            if largest_dist >= l:
                return longest_so_far, largest_dist

    return longest_so_far, largest_dist

def recover_specific_word_path(word):
    longest_word_down, dist = longest_pyramid_with_word_down(word)
    print("::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::")
    print("       DOWN PATH" + " of Length: " + str(dist))
    print("::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::")

    path = []
    if longest_word_down != "":
        while longest_word_down in parent3:
            print(longest_word_down)
            path.append(longest_word_down)
            longest_word_down = parent3[longest_word_down]
        print(longest_word_down)
        path.append(longest_word_down)
    else:
        path.append(word)
        dist += 1

    longest_word2, dist2 = longest_pyramid_with_word_up(word)
    print()
    print("::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::")
    print("       UP PATH" + " of Length: " + str(dist2))
    print("::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::")
    if longest_word2 != "":
        while longest_word2 in predecessor:
            print(longest_word2)
            path.insert(dist, longest_word2)
            longest_word2 = predecessor[longest_word2]
        print(longest_word2)

    print("::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::")
    print("       FULL PATH" + " of Length: " + str(dist + dist2 - 1))
    print("::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::")
    for w in path:
        print(w)

s = time.time()
recover_specific_word_path("SOLIVAGANT")
e = time.time()
print(e-s)