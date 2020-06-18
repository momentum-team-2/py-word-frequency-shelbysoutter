import string 

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def clean_clean(text):
    text = text.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word_container = ""
    for character in text:
        if character in letters:
            word_container += character
    return word_container


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open(file)
    text = file.read()
    line_break = text.replace("\n", " ")
    space_fix = line_break.replace("  ", " ")
    dubdub_dash = space_fix.replace("--", " ")
    cleaned_text = clean_clean(dubdub_dash)
    
    split_text = cleaned_text.split()
    word_list = []
    for word in split_text:
        if not word in STOP_WORDS:
            word_list.append(word)
    
    organized_words = sorted(word_list, key = str)
    #   print(split_text)
    word_count_list = dict()
    for word in organized_words:
        if word in word_count_list:
            word_count_list[word] += 1
        else:
            word_count_list[word] = 1
    word_count_list = {key:value for key, value in word_count_list.items() if value >=1}
    sorted_words = sorted(word_count_list.items(), key = lambda seq: seq[1], reverse=True)

    
    for key, value in sorted_words:
        print(key.rjust(20), " | ", value, value * ("*"))

    # opened_file = open(file)
    # text = opened_file.read()
    # words = clean_clean(text).split()
    # word_list = remove_from_list(words, STOP_WORDS)
    # word_dict = get_word_dict(word_list)
    # alpha_dict = dict(sorted(word_dict.items()))
    # sorted_dict = dict(sorted(alpha_dict.items(), key=get_second_value, reverse=True))
    # output_list = get_output_list(sorted_dict)
    # output_word_list =  get_output_word_list(output_list)
    # longest_word = get_longest_word(output_word_list)
    # for item in output_list:
    #     print(f"{get_first_value(item).rjust(len(longest_word) + 2)} | {str(get_second_value(item)).ljust(3)}{get_second_value(item) * '*'}")



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

