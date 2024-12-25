def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    word_c = word_count(file_contents)
    chr_dic = character_counting(file_contents)
    generate_report(file_path, word_c, chr_dic)

def read_file(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(master_string):
    return len(master_string.split())

def character_counting(master_string):
    char_dic = {}
    char_a_code = ord('a')
    char_z_code = ord('z')
    lmstr = master_string.lower()

    for c in range(char_a_code, char_z_code + 1):
        char_dic[chr(c)] = 0

    for i in range(0, len(master_string)):
        if(ord(lmstr[i]) >= char_a_code and ord(lmstr[i]) <= char_z_code):
            char_dic[lmstr[i]] += 1
    
    return char_dic

def generate_report(file_path, word_count, chr_count_dic):
    ordered_dic = reverse_sort_dic(chr_count_dic)
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for c in ordered_dic:
        print(f"The \'{c}\' character was found {ordered_dic[c]} times")
    print("--- End report ---")

def reverse_sort_dic(dic):
    return dict(sorted(dic.items(), key = lambda item: item[1], reverse = True))

main()