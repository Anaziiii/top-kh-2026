def print_success_message(text):
    print("Success: " + text)

def process_data(data, callback_function):
    print("processing data: " + data)
    callback_function("Successfully processed data")

process_data("Example of some file", print_success_message)