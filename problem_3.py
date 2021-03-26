# Zack Gottesman, Will McCall, & Liam Prevelige
# Solution to problem 3 of voluntary coding assignment: "Reconstituting String with Anagrams"
# Calculates anagrams of strings up to length 9 under 60 sec

from itertools import permutations, product
import time

"""
For anagram string = "dynamic" - length 7
find_anagrams("dynamic"):
Number of anagrams, respective values:  (13, {'CYAN DIM', 'CID MANY', 'CANY DIM', 'CAD MINY', 'DAMN ICY', 'CANY MID', 'DYNAMIC', 'CAY MIND', 'CYAN MID', 'CYMA NID', 'CYMA DIN', 'MAND ICY', 'CID MYNA'})
Time taken (sec) for anagrams of "dynamic": 1.7335801124572754
"""
# --------------------------------------------------
"""
For anagram string = "dynamics" - length 8
find_anagrams("dynamics"):
Number of anagrams, respective values:  (32, {'DYNAMICS', 'CANDY SIM', 'CAY MINDS', 'CID MYNAS', 'CYAN DIMS', 'CANDY ISM', 'DISC MYNA', 'CYANS DIM', 'MIC SDAYN', 'CIDS MYNA', 'CANY MIDS', 'ADS MINCY', 'CYMA NIDS', 'DAMNS ICY', 'CAN MYSID', 'CYANS MID', 'CIDS MANY', 'DAS MINCY', 'CANY DIMS', 'CYMAS NID', 'MIC SANDY', 'CADS MINY', 'DISC MANY', 'CYMA SIND', 'CYMA DINS', 'CANDY MIS', 'CYAN MIDS', 'CAYS MIND', 'SCAD MINY', 'SAD MINCY', 'MICA SYND', 'CYMAS DIN'})
Time taken (sec) for anagrams of "dynamics": 3.2178375720977783
"""
# --------------------------------------------------
"""
For anagram string = "prevelige" - length 9
find_anagrams("prevelige"):
Number of anagrams, respective values:  (107, {'LEG PRIEVE', 'ERE PIG LEV', 'EVE LIG PRE', 'VERGE PLIE', 'LERP VEGIE', 'GIRL PEEVE', 'LIEGE PERV', 'ERE LEP VIG', 'EVE GEL PIR', 'GREVE LIPE', 'EVE LEG RIP', 'LEE REP VIG', 'GIE LEV PRE', 'VEE LEP RIG', 'LIE REP VEG', 'GIVE REPEL', 'REG LEP VIE', 'GIVER PEEL', 'LIG PEE REV', 'VEE LEG RIP', 'LEV PEE RIG', 'LEI REP VEG', 'ERE LIP VEG', 'GEE LEV RIP', 'GIVE LEPER', 'REI LEV PEG', 'GEE LIP REV', 'REI LEP VEG', 'LIE PER VEG', 'GREVE PILE', 'GEL PRIEVE', 'VEE GEL RIP', 'EVE LEP RIG', 'PIG RELEVE', 'GIE LEP REV', 'REG VEE LIP', 'EEL GIP REV', 'REE PIG LEV', 'GEL PRE VIE', 'LIE PRE VEG', 'EVE GRIPLE', 'LIGER VEEP', 'REE GIP LEV', 'REG EVE LIP', 'GEL PIE REV', 'LIE PEG REV', 'GIE LEV REP', 'EEL REP VIG', 'VEE GRIPLE', 'PEE VERLIG', 'VEE LEG PIR', 'ERG VEE LIP', 'ERG LEP VIE', 'GIP RELEVE', 'LEE PER VIG', 'GRIPE LEVE', 'GLEE VIPER', 'VERGE LIPE', 'ERE GIP LEV', 'VIRGE LEEP', 'REE LIP VEG', 'EVE LEG PIR', 'GREVE PLIE', 'REGIVE LEP', 'LEE GIP REV', 'EVE LIG REP', 'GIE LEV PER', 'VEE LIG PER', 'LEE RIP VEG', 'GLEI PREVE', 'GLEI PERVE', 'REE LEP VIG', 'LEG PRE VIE', 'LEE PIR VEG', 'LEE PIG REV', 'EVE GEL RIP', 'LEI PEG REV', 'EVE LIG PER', 'VERGE PILE', 'VIRGE PEEL', 'VEE LIG REP', 'VIRGE PELE', 'EEL PIG REV', 'EEL PER VIG', 'GEE LEV PIR', 'GEL REP VIE', 'EEL PRE VIG', 'EEL PIR VEG', 'GIVER PELE', 'REG LEV PIE', 'GRIEVE LEP', 'LEI PRE VEG', 'VEE GEL PIR', 'GEL PER VIE', 'LEG REP VIE', 'EEL RIP VEG', 'LEG PIE REV', 'GRIPE VELE', 'LEE PRE VIG', 'GIVER LEEP', 'ERG LEV PIE', 'LEG PER VIE', 'IRE LEP VEG', 'LEI PER VEG', 'IRE LEV PEG', 'ERG EVE LIP', 'VEE LIG PRE'})
Time taken (sec) for anagrams of "prevelige": 14.842000484466553
"""
# --------------------------------------------------
"""
For anagram string = "wownicealg" - length 10
find_anagrams("wownicealg"):
Number of anagrams, respective values:  (459, {'WAN CLEW GIO', 'NAW COLE WIG', 'AWN CIG LOWE', 'CAG WIEL WON', 'CAW LING OWE', 'ACE LING WOW', 'ICE LAWN WOG', 'ALOW CIG WEN', 'ANCE OWL WIG', 'GALENIC WOW', 'CLEW GON WAI', 'CINE GAL WOW', 'CAW GOLE WIN', 'CANE LIG WOW', 'COG LEW WAIN', 'WEAL COG WIN', 'COWAL WINGE', 'AWEING CLOW', 'COW GEN WALI', 'CION LEG WAW', 'WANE COW LIG', 'AWL COG WINE', 'NICE LAG WOW', 'NAW GLOW ICE', 'ECO GIN WAWL', 'AWL ECO WING', 'ACE LOW WING', 'CAGE LOW WIN', 'COW LENG WAI', 'NEG LAIC WOW', 'WANE COL WIG', 'COG WEN WALI', 'ANEW CIG LOW', 'ECO WAWLING', 'CON LWEI WAG', 'AWL COW GIEN', 'CLAW GIE WON', 'ALEC NOW WIG', 'CON LIG WAWE', 'NAW COG WIEL', 'COW GEN WAIL', 'LICE GON WAW', 'GEN LAIC WOW', 'CAW GOEL WIN', 'AWL CONE WIG', 'WANE CIG OWL', 'WENA COL WIG', 'ANGLICE WOW', 'NOG ICE WAWL', 'WALE CIG WON', 'CLAWING WOE', 'CAW GLEI NOW', 'WALE CON WIG', 'COG NIL WAWE', 'CAW GNOW LIE', 'CLAW ONE WIG', 'CONE LIG WAW', 'CLEG WON WAI', 'AWL ONCE WIG', 'CAG WILE NOW', 'COW NAG WILE', 'CIEL NOW WAG', 'COW NEG WALI', 'CAW LOG WINE', 'CON GLEI WAW', 'CIEL NAG WOW', 'ALEW CON WIG', 'ANE CLOW WIG', 'CLEG OWN WAI', 'CAG WIEL NOW', 'CAG LOWE WIN', 'CAN WILE WOG', 'COWL NEG WAI', 'WAN COG WIEL', 'CONI GEL WAW', 'ALEC WOWING', 'NAE CLOW WIG', 'WALE COWING', 'ANOW CIG LEW', 'LOCI NEW WAG', 'CLAW GIN WOE', 'CLAW GOE WIN', 'LOCI GEN WAW', 'CAW INGO LEW', 'COG NIE WAWL', 'CLAN GIE WOW', 'LAW GOWN ICE', 'AWN COG WIEL', 'CAW NOG WEIL', 'GAE COWL WIN', 'COL WAGE WIN', 'COG NEW WALI', 'CEIL NOW WAG', 'CAW ENOW LIG', 'COW GNAW LIE', 'NAW COW GLEI', 'CLOW NIE WAG', 'COG LINE WAW', 'GAE CLOW WIN', 'WEAN COW LIG', 'NAW COG WEIL', 'CEIL OWN WAG', 'WAE CLON WIG', 'CINE OWL WAG', 'ONCE LIG WAW', 'ENOW LAC WIG', 'COW GAL WINE', 'WAE CIG NOWL', 'CLAW GIO WEN', 'CAW GON WEIL', 'COLE WAG WIN', 'CLAW WIGEON', 'ALEW COG WIN', 'CEL WAIN WOG', 'AWN COG WILE', 'AWN COWL GIE', 'CINE LOG WAW', 'CIEL WON WAG', 'WEAL COW GIN', 'CLEG ION WAW', 'ICE LOWN WAG', 'CIG LAWN OWE', 'CLAN WOE WIG', 'CIEL NOG WAW', 'NAW LICE WOG', 'CAW GON WILE', 'AGE CLOW WIN', 'COIL NEW WAG', 'CEL INGO WAW', 'LACE NOW WIG', 'COW GAN WEIL', 'WAN GLOW ICE', 'ICE NOWL WAG', 'WAN LOG WICE', 'AWE COW LING', 'LICE OWN WAG', 'COW EGAL WIN', 'WEAL CON WIG', 'ANEW COL WIG', 'CIG LAWN WOE', 'COLE GIN WAW', 'CAW GEL WINO', 'ALEW CIG NOW', 'NAW CEIL WOG', 'ACE GOWL WIN', 'WEAL CIG WON', 'COW WANG LIE', 'COIL ENG WAW', 'WALE COW GIN', 'CLAW GIE OWN', 'COW NAG WIEL', 'CAW GLOW NIE', 'CLOG NIE WAW', 'COW ELAN WIG', 'NAG OWL WICE', 'CAW OGLE WIN', 'AWN LOG WICE', 'CLAW GEO WIN', 'CON WIEL WAG', 'COIN LEW WAG', 'COW LEAN WIG', 'GON ICE WAWL', 'LAW ONCE WIG', 'COW GAN WILE', 'CON WEIL WAG', 'CEIL GAN WOW', 'CAW GIE LOWN', 'CAG LIEN WOW', 'WANE CIG LOW', 'WALE CIG OWN', 'AWN LICE WOG', 'WEAL CIG NOW', 'CAIN LEW WOG', 'CLON GIE WAW', 'CLAW GIE NOW', 'CONI LEG WAW', 'NICE LOG WAW', 'GIEN LAC WOW', 'CAGE NIL WOW', 'CIG NEAL WOW', 'WAE CLOW GIN', 'COG LIEN WAW', 'LEW OCA WING', 'NAE COWL WIG', 'GAL OWN WICE', 'COW LANE WIG', 'COG LIN WAWE', 'AWN CLOW GIE', 'CIEL OWN WAG', 'WEAL CIG OWN', 'GOA CLEW WIN', 'ALOW CIG NEW', 'AWL NOG WICE', 'COW LAG WINE', 'NAW CIEL WOG', 'CAIN LEG WOW', 'WAN CIEL WOG', 'AWE CIG NOWL', 'COIN LEG WAW', 'ANOW CEL WIG', 'NICE OWL WAG', 'ICON LEG WAW', 'COG NEW WAIL', 'WEAN CIG LOW', 'LICE NAG WOW', 'CAGE OWL WIN', 'AWN COLE WIG', 'GAN LOW WICE', 'COW GEL WAIN', 'COG WEN WAIL', 'LAW NICE WOG', 'CION LEW WAG', 'CAG LINE WOW', 'WEAN COL WIG', 'CAG LOW WINE', 'CAW LING WOE', 'LICE WON WAG', 'CAW GOWN LIE', 'LAC OWE WING', 'LAW CIG ENOW', 'GNAW ICE OWL', 'AWL CINE WOG', 'WENA CIG OWL', 'CAG LEW WINO', 'LAW COG WINE', 'NAG LOW WICE', 'COW NEAL WIG', 'ACNE OWL WIG', 'ICE LANG WOW', 'ANEW COW LIG', 'CLOW NEG WAI', 'CAW OLE WING', 'WANG ICE LOW', 'COW GIE LAWN', 'LAG OWN WICE', 'NAW COG WILE', 'GOWLAN WICE', 'CIG LANE WOW', 'COIN GEL WAW', 'CEIL NAG WOW', 'AWE COWLING', 'ANE COWL WIG', 'ANGELIC WOW', 'WAE COW LING', 'CAWING LOWE', 'COW GALE WIN', 'ALEW COW GIN', 'AWN CEIL WOG', 'CEIL WON WAG', 'CAW LIEN WOG', 'CAN WIEL WOG', 'CIG ONE WAWL', 'COW GAN LWEI', 'LACE WON WIG', 'WAN COW GLEI', 'AWE COWL GIN', 'CAN WEIL WOG', 'ALE COW WING', 'CAW NOG WILE', 'CAW GIE NOWL', 'AWL GON WICE', 'CINE LAG WOW', 'ANEW CIG OWL', 'CAW LOGE WIN', 'ECO LAWN WIG', 'GAN OWL WICE', 'COW LIN WAGE', 'GNAW ICE LOW', 'CAW GOWN LEI', 'CLAW NIE WOG', 'LACE GIN WOW', 'CAW GON WIEL', 'LAW ECO WING', 'CLEW ION WAG', 'COWL NIE WAG', 'LAG WON WICE', 'NAW COG LWEI', 'LACE WIN WOG', 'GAL WON WICE', 'WAE COWLING', 'ACNE LIG WOW', 'ALEC WIN WOG', 'COL WAG WINE', 'LAG NOW WICE', 'LAW GNOW ICE', 'CON WILE WAG', 'AWL CIG ENOW', 'NAW CLOW GIE', 'CAG WILE OWN', 'AWL GOWN ICE', 'WAN COG LWEI', 'CONI LEW WAG', 'AWE CLOG WIN', 'ECO LING WAW', 'WAN CEIL WOG', 'CAG LWEI WON', 'CLEW NOG WAI', 'LOCI NEG WAW', 'AWN COW GLEI', 'COWAL GWINE', 'LOCI WEN WAG', 'COW NIL WAGE', 'CANG LIE WOW', 'CEL GOWN WAI', 'CEL GNOW WAI', 'COIL NEG WAW', 'LAW COW GIEN', 'AWN GLOW ICE', 'LICE NOW WAG', 'NICE GAL WOW', 'CAG WILE WON', 'LAIC WEN WOG', 'ALEC OWN WIG', 'CAW GIN LOWE', 'COIL WEN WAG', 'CLEG NOW WAI', 'ALEW CIG OWN', 'CLAW EON WIG', 'COL GIEN WAW', 'ACNE LOW WIG', 'CAW LEG WINO', 'AWL GNOW ICE', 'COW LINE WAG', 'CLAN OWE WIG', 'WEAN CIG OWL', 'EAN COWL WIG', 'ALEW COWING', 'CAW GIEN OWL', 'CAW NOG LWEI', 'CIG EON WAWL', 'AWN COG WEIL', 'CAW NOG WIEL', 'ACE GLOW WIN', 'COW GEAL WIN', 'COWL GEN WAI', 'CLAWING OWE', 'CAN LOWE WIG', 'NAW CIG LOWE', 'AWOL CIG WEN', 'NAW CLEW GIO', 'COW ENG WAIL', 'WENA COW LIG', 'CLAG NIE WOW', 'WAE CIG LOWN', 'CLAG WOE WIN', 'CAW GLEI OWN', 'ANCE LIG WOW', 'AWEING COWL', 'CAW GON LWEI', 'AWN CLEW GIO', 'GAL NOW WICE', 'WAN CIG LOWE', 'ANCE LOW WIG', 'CINE LOW WAG', 'CEIL NOG WAW', 'CLOW ENG WAI', 'NAW GOWL ICE', 'CANE LOW WIG', 'ICE LONG WAW', 'WAN COWL GIE', 'CIEL GON WAW', 'WENA CIG LOW', 'CON GIE WAWL', 'AWE CIG LOWN', 'COW LIEN WAG', 'LACE WOWING', 'WALE CIG NOW', 'CLOG NEW WAI', 'LAW NOG WICE', 'WAN COLE WIG', 'CANG LEI WOW', 'COW NAG WEIL', 'CLAG OWE WIN', 'CEIL GON WAW', 'CEL WAG WINO', 'CLOW GEN WAI', 'AWE CLON WIG', 'COW GAN WIEL', 'AWN CIEL WOG', 'ICON GEL WAW', 'AWOL CIG NEW', 'ALEC GIN WOW', 'CAG LWEI NOW', 'CAW LINE WOG', 'CAN GLEI WOW', 'AGLOW WINCE', 'ENG LAIC WOW', 'AWE CLOW GIN', 'COW NAG LWEI', 'COL GIN WAWE', 'COW GNAW LEI', 'CAN LWEI WOG', 'LICE NOG WAW', 'CIG ELAN WOW', 'CAG WEIL WON', 'ALEW CIG WON', 'CIG LEAN WOW', 'CAG WIEL OWN', 'NICE LOW WAG', 'WEAL COWING', 'CLAW GIO NEW', 'LAW CONE WIG', 'COIL GEN WAW', 'ICON LEW WAG', 'AWE COL WING', 'CAG OWL WINE', 'CAG WEIL NOW', 'COW ENG WALI', 'CLAW GIN OWE', 'LAW GON WICE', 'ACE NOWL WIG', 'CAGE LIN WOW', 'WAN COG WEIL', 'CAW GLEI WON', 'LAIC NEW WOG', 'LOCI ENG WAW', 'COW GLEN WAI', 'CAW GNOW LEI', 'WAE CLOG WIN', 'CION GEL WAW', 'AWL NICE WOG', 'CAW GOWL NIE', 'CLAW EGO WIN', 'ACE OWL WING', 'WAN LICE WOG', 'CAIN GEL WOW', 'CAG WEIL OWN', 'ACE LOWN WIG', 'WAE COL WING', 'NAW COWL GIE', 'CAW GIEN LOW', 'LICE GAN WOW', 'EAN CLOW WIG', 'COIGNE WAWL', 'LACE OWN WIG', 'LAC WINE WOG', 'LEA COW WING', 'AGE COWL WIN', 'LAW CINE WOG', 'COW WANG LEI', 'WAN GOWL ICE', 'COW LEG WAIN', 'AGO CLEW WIN', 'CAG LWEI OWN', 'LAC WOE WING', 'AWN COG LWEI', 'WALE COG WIN', 'ALEC WON WIG', 'WAN COG WILE', 'WAE COWL GIN', 'WANG ICE OWL', 'COW NEG WAIL', 'CIEL GAN WOW', 'AWN GOWL ICE', 'COWL ENG WAI', 'WAN CLOW GIE', 'CANE OWL WIG', 'CLOG WEN WAI', 'NAW LOG WICE'})
Time taken (sec) for anagrams of "wownicealg": 209.1041443347931
"""


"""
Helper method for creating a set of valid words using sowpods.txt
"""
def create_sowpods_dict():
    dict_file = open("sowpods.txt", "r")
    sowpods = dict()    # key is tuple of character frequency, value is list of corresponding words from sowpods.txt
    for line in dict_file:
        original_word = line.strip("\n")

        stripped_word = original_word.strip()
        # Anagrams have same number of characters - iterate through all characters of current string to find frequency
        char_freq = dict()  # key is character, value is frequency
        for char in stripped_word:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # To use key-value pairs as dictionary key, cast to tuple
        # https://stackoverflow.com/questions/39800762/adding-a-sorted-tuple-to-a-dictionary-as-a-key
        char_freq_tuple = str(tuple(sorted(char_freq.items())))

        # Multiple different words can have same key -- don't override
        if char_freq_tuple in sowpods:
            sowpods[char_freq_tuple].append(original_word)
        else:
            words_for_tuple_set = [original_word]
            sowpods[char_freq_tuple] = words_for_tuple_set

    dict_file.close()

    return sowpods


"""
Given a string input, return the number of and strings for all anagrams 
"""
def find_anagrams(anagram_word):
    # Get sowpods.txt dictionary using helper - key is character frequency, value is list of words w/ this frequency
    sowpods = create_sowpods_dict()
    n = len(anagram_word)
    anagrams_list = set()   # returned set will contain all anagrams for substrings of anagram_word
    sub_char_freq_dict = dict()  # key is the substring of anagram_word, value is character frequency

    # Checking permutations ensures all subsets of characters are considered -- efficiency could likely be improved here
    # Itertools documentation used: https://docs.python.org/3/library/itertools.html
    x = (permutations(anagram_word))

    try:    # Use try/catch block so when next(x) no longer exists, returns the list of anagrams
        while True:     # breaks when next(x) returns error
            anagram_word = ''.join(next(x))
            anagram_word = "_" + anagram_word       # filler character, ignore index 0
            anagram_word = anagram_word.strip().upper()     # mimic style of sowpods.txt
            F = [0 for x in range(n + 1)]
            F[0] = 1
            # Use pset4 approach of dynamically iterating over string, checking whether valid anagram using sowpods dict
            for m in range(1, n+1):
                b = 0
                for k in range(m):
                    # construct frequency count of letters for indexing into dict
                    curr_word = anagram_word[k+1:m+1]

                    if curr_word not in sub_char_freq_dict:
                        char_freq = dict()
                        for char in curr_word:
                            if char in char_freq:
                                char_freq[char] += 1
                            else:
                                char_freq[char] = 1
                        char_freq_tuple = str(tuple(sorted(char_freq.items())))
                        sub_char_freq_dict[curr_word] = char_freq_tuple     # for later retrieval, avoid repetition
                    else:
                        char_freq_tuple = sub_char_freq_dict[curr_word]
                    # If frequency of characters is matched in dictionary, anagram by definition
                    b = max(b, min(F[k], int(char_freq_tuple in sowpods)))
                F[m] = b

            # Modified version of pset4, starting recovery of the anagrams
            if F[n] != 0:
                m = n
                W = set()
                while m > 0:
                    k = m-1
                    flag = 0
                    while flag == 0:
                        # retrieve frequency count of letters for indexing into dict
                        curr_word = anagram_word[k+1:m+1]
                        char_freq_tuple = sub_char_freq_dict[curr_word]

                        if F[k] == 1 and char_freq_tuple in sowpods:
                            W.add(char_freq_tuple)
                            m = k
                            flag = 1
                        else:
                            k -= 1
                curr_anagrams = []

                # 'add' used to track anagram length > 3 and number < 4 (doesn't take advantage of improved efficiency)
                add = True

                for curr_char_freq_tup in W:
                    same_chars_anagram_list = []    # multiple words may have same frequency count -- all are anagrams
                    for same_chars_anagram in sowpods[curr_char_freq_tup]:
                        if len(same_chars_anagram) < 3 or len(same_chars_anagram_list) > 3:
                            add = False  # doesn't satisfy given requirements
                            break
                        else:
                            same_chars_anagram_list.append(same_chars_anagram)
                    curr_anagrams.append(same_chars_anagram_list)  # store all anagrams with same char frequency
                if add:  # if the anagram has length > 3 and anagrams total count < 4, then add to returned list
                    # every word with duplicate char frequency needs to be counted as new anagram
                    # Itertools documentation used: https://docs.python.org/3/library/itertools.html
                    distributed_anagrams = {' '.join(l) for l in product(*sorted(curr_anagrams))}   # sorting prevents duplicates
                    for anagram in distributed_anagrams:
                        anagrams_list.add(anagram)
    except Exception as e:  # if exception is called, then all permutations of anagram_word have been checked
        return len(anagrams_list), anagrams_list


anagram_string = "dynamic"

start_time = time.time()    # track running time to ensure < 1 min
print("Number of anagrams, respective values: ", find_anagrams(anagram_string))
print("Time taken (sec) for anagrams of \"" + anagram_string + "\": " + str(time.time() - start_time))
