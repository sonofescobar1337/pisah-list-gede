def split_large_file(input_file, output_prefix, num_files):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        total_lines = len(lines)
        lines_per_file = total_lines // num_files

        for i in range(num_files):
            start_idx = i * lines_per_file
            end_idx = (i + 1) * lines_per_file if i < num_files - 1 else total_lines

            output_file = f"{output_prefix}_{i + 1}.txt"
            with open(output_file, 'w') as outfile:
                outfile.writelines(lines[start_idx:end_idx])

            print(f"File {output_file} created with {end_idx - start_idx} lines.")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = input("Masukkan nama file input: ")

    while True:
        try:
            num_files = int(input("Masukkan jumlah file output yang diinginkan: "))
            if num_files <= 0:
                print("Jumlah file output harus lebih dari 0.")
            else:
                break
        except ValueError:
            print("Masukkan angka yang valid untuk jumlah file output.")

    output_prefix = input("Masukkan awalan nama file output: ")

    split_large_file(input_file, output_prefix, num_files)
