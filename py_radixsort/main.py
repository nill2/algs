import os
import sys

def to_txt_array(array):
    return_txt = ''
    j = 0
    for i in array:
        if j > 0 :
            return_txt = return_txt + ', '
        return_txt = return_txt + str(i)
        j = j + 1
    return return_txt
        

def print_phase(buckets, phase):
    return_txt = '**********\n'
    #print(f'Phase {phase}')
    return_txt = return_txt + 'Phase ' +str(phase) + '\n'
    for i in range(10):
        bucket_i_len = len(buckets[i]) 
        bucket_txt=''
        if bucket_i_len > 0:
            for j in range(bucket_i_len):
                if j != 0 :
                    bucket_txt = bucket_txt + ', '
                bucket_txt = bucket_txt + buckets[i][j]
        else:
            bucket_txt = 'empty'
        
        return_txt = return_txt + 'Bucket ' + str(i) + ': ' + bucket_txt + '\n'
        #print(f'Bucket {i}: {bucket_txt}')
    return return_txt
        
            
    

def radixsort( unsorted_list, list_len, num_len):
    wip_list = []
    wip_list = unsorted_list
    cur_buckets = []
    return_txt = ''
    for i in range(num_len):
        cur_buckets.clear()
        cur_buckets = [[] for _ in range(10)]
        for j in range(list_len):
            cur_buckets[int(wip_list[j][num_len-i-1])].append(wip_list[j])
            #print(cur_buckets)
        wip_list.clear()
        for j in range(10):
            wip_list.extend(cur_buckets[j])
        return_txt = return_txt + print_phase(cur_buckets,i+1)
        
    return wip_list , return_txt
        

def main():
################################################################
#main function 
    # Get the current working directory that gets input data from input .txt file from 
    current_directory = os.getcwd()
    # Specify the subdirectory name
    subdirectory = 'example'
    if len(sys.argv) < 2:
        # If no argument is provided, use a default value
        input_file = os.path.join(current_directory, 'input.txt')
    else:
        # Access the first command-line argument (after the script name)
        input_file = os.path.join(current_directory, sys.argv[1])

    # Create a path to a file in the 'example' subdirectory
    output_file = os.path.join(current_directory, subdirectory, 'output.txt')
    array_length = 0
    numbers = []
    current_line = 0
    initial_array = ''
    num_len = 0
    try:
        with open(input_file, 'r') as file:
            for line in file:
                try:
                    if current_line == 0:
                        array_length = int(line.strip())
                        current_line = current_line + 1
                    else: 
                        number = line.strip()
                        numbers.append(number)
                        cur_num_len = len(number)
                        current_line = current_line + 1
                        if len(initial_array) > 0:
                            initial_array = initial_array + ', '
                        initial_array = initial_array + number
                        if num_len > 0 and cur_num_len!=num_len:
                            raise ValueError("Numbers  of different lengths") 
                            break
                        num_len = cur_num_len    
                except ValueError:
                    print(f"faced non-numeric line: {line.strip()}")
                    sys.exit("Exiting due to an exception")
        if current_line> array_length+1 :
            print(f"The file {input_file} is longer: {current_line} than it was indicated in its first line: {array_length}")
            sys.exit("Exiting due to an exception")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
        sys.exit("Exiting due to file not found.")
    else:
        try:
            with open(output_file, 'w+') as file: 
                file.write('Initial array:'+'\n') 
                file.write(initial_array+'\n')
                sorted_array, phases_txt = radixsort(numbers, array_length, num_len)
                file.write(phases_txt+'\n')
                file.write('**********\n') 
                file.write('Sorted array:'+'\n')
                file.write(to_txt_array(sorted_array)+'\n')
        except IOError as e:
            print(f"Error writing to file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()