import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]

def linear_search(sequence, number):
    count = sequence.count(number)
    position = []
    for n, i in enumerate(sequence):
        if i == number:
            position.append(n)

    output = dict()
    output["position"] = position
    output["count"] = count
    return output


# print(linear_search([-51, -12, -3, -3, -1, 2, 8, 13, 14, 14, 14, 21, 22, 23, 24, 25, 48, 63, 64, 70, 72, 78, 90, 102, 120], 14))

def pattern_search(sequence, vzor):

    dna_segmented = []
    segment_range = []
    start_index = 0
    seznam = []
    for index in range(0, len(sequence) - len(vzor) - 1):
        if sequence[index:index + len(vzor)] != vzor:
            continue
        else:
            dna_segmented.append(sequence[start_index:index])
            segment_range.append([start_index, index - 1])
            start_index = index + len(vzor)
            seznam.append(index)

    # print(dna_segmented)
    # print(segment_range)
    return set(seznam)




def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    data = read_data("sequential.json", "dna_sequence")
    # print(unordered_numbers)
    print(pattern_search(data, "ATA"))

if __name__ == '__main__':
    main()