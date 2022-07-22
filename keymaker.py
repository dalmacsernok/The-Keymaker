def shift_characters(word, shift):
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    word = word.lower()
    word_letters = [] 
    shifted_word_letters = []
    for character in word: 
        word_letters.append(character)
    for i in range(len(word_letters)):
        for j in range(len(list_of_letters)):
            if word_letters[i] == list_of_letters[j]:
                try:
                    shifted_word_letters.append(list_of_letters[j + shift])
                except IndexError:
                    shifted_word_letters.append(list_of_letters[j + shift - 26])
    shifted_word = "".join(shifted_word_letters) 
    return shifted_word
    

def pad_up_to(word, shift, n):
    result = word.lower()
    for i in range(n):
        shifted_word = shift_characters(word, shift)
        word = shifted_word
        result += word
    return result[:n]


def abc_mirror(word):
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    word = word.lower()
    mirrored_letters = []
    word_letters = []
    for character in word:
        word_letters.append(character)
    for i in range(len(word_letters)):
        for j in range(len(list_of_letters)):
            if word_letters[i] == list_of_letters[j]:
                mirrored_letters.append(list_of_letters[(26 - j) - 1])
    mirrored_word = "".join(mirrored_letters)
    return mirrored_word


def create_matrix(word1, word2):
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    matrix = [] 
    shifted_word = ""
    for i in word2:
        index = list_of_letters.index(i)
        shifted_word = shift_characters(word1, index)
        matrix.append(shifted_word)
    return matrix


def zig_zag_concatenate(matrix):
    word = ""
    for i in range(len(matrix[0])):
        if i % 2 == 0:
            for j in range(len(matrix)):
                word += matrix[j][i]
        else:
            for x in reversed(range(len(matrix))):
                word += matrix[x][i]
    return word


def rotate_right(word, n):
    result = word
    if n >= 0:
        for i in range(n):
            rotated = result[-1] + result[:-1]
            result = rotated
    else:
        for i in range (abs(n)):
            rotated = result[1:] + result[0]
            result = rotated
    return result


def get_square_index_chars(word):
    result = ""
    word_letters = []
    for character in word:
        word_letters.append(character)
    for i in range(len(word_letters)):
        for j in range(len(word_letters)):
            if i == j ** 2:
                result += word[i]
    return result


def remove_odd_blocks(word, block_length):
    word = word.lower()
    blocks = []
    for i in range(0, len(word), block_length):
        blocks.append(word[i:i+block_length]) 
    splitted_blocks = blocks[0::2]
    new_string = "".join(splitted_blocks)
    return new_string


def reduce_to_fixed(word, n):
    result = ""
    new_word = word[:n]
    n = n // 3
    result = rotate_right(new_word, -n)
    return result[::-1]


def hash_it(word):
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
