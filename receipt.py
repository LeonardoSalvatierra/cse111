
import csv

def main():

    key_index = 0

    products_dict = read_dictionary("products.csv", key_index)

    print("All products:")
    print(products_dict)
    print()

    request_list = []

    with open("request.csv", "rt") as request_file:

        reader = csv.reader(request_file)
        next(reader)

        print("Requested Items:")
        for row in reader:
            
            if len(row) != 0:

                request_list.append(row)
            
            if row[0] in products_dict:
                items = products_dict[row[0]]
                print(f"{items[1]}: {row[1]} $ {items[2]}")
                print()


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:

            product = row[0]
            product_name = row[1]
            price = row[2]

            dictionary[product] = [product, product_name, price]

    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()