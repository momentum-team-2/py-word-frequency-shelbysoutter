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
            word_container += ' ' + character
    return word_container


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open(file)
    text = file.read()
    
    line_break = text.replace("\n", " ")
    split_text = line_break.split(' ')
    space_fix = line_break.replace("  ", " ")
    dubdub_dash = space_fix.replace("--", " ")
    cleaned_text = clean_clean(dubdub_dash)
    
    word_list = []
    for word in split_text:
        if not word in STOP_WORDS:
            word_list.append(word)
    
    organized_words = sorted(word_list, key = str)

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

#python word_frequency.py one-today.txt