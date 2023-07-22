
import csv

def main():

    key_index = 0
    try:
        products_dict = read_dictionary("products.csv", key_index)
        

        print("Inkon Emporium")
        # print(products_dict)
        print()

        request_list = []

        with open("request.csv", "rt") as request_file:

            reader = csv.reader(request_file)
            next(reader)

            print("Requested Items:")
            print()

            quantities = 0
            subtotal_price = 0.00
            tax_amount = 0.00
            total_price = 0.00
            prices_quantity = 0.00

            

            for row in reader:
                
                if len(row) != 0:

                    request_list.append(row)
                
                # if row[0] in products_dict:
                items = products_dict[row[0]]
                print(f"{items[1]}: {row[1]} $ {items[2]}")
                quantities = quantities + int(row[1])
                prices_quantity = float(row[1]) * float(items[2])
                subtotal_price = subtotal_price + prices_quantity
                tax_amount = subtotal_price * 0.06
                total_price = tax_amount + subtotal_price

    except KeyError as key_err:

        print(f"unknown product ID in the request.csv file {key_err}")

    except FileNotFoundError as file_err:
            
        print(f"Error: missing file {file_err}")    

    except PermissionError as per_err:
        print(f"{per_err}")


    finally:
        print("")

    print()
    print(f"Number of Items: {quantities}")
    print(f"Subtotal: {subtotal_price:.2f}")
    print(f"Sales Tax: {tax_amount:.2f}")
    print(f"Total: {total_price:.2f}")
    print()
    print("Thank you for shopping at the Inkom Emporium.")
    
    # Import the datetime class from the datetime
    # module so that it can be used in this program.
    from datetime import datetime

    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

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

