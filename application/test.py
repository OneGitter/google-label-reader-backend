def generateFiles(input_file_name):
    try:
        with open(input_file_name, 'r') as file:
            lines = file.readlines()

        for index, line in enumerate(lines):
            output_file_name = f'output_file_{index + 1}.txt'
            with open(output_file_name, 'w') as output_file:
                output_file.write(line)

        print(f"Successfully generated {len(lines)} files.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "O_order_log00.csv"
    generateFiles(input_file)