import time

def cp(word, ws, m=None):
    if m is None:
        m = {}
    
    if word in m:
        return m[word]
    
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        
        if prefix in ws:
            if suffix in ws or cp(suffix, ws, m):
                m[word] = True
                return True
    
    m[word] = False
    return False

def f2(filename):
    ws = set()
    words_list = []
    
    try:
        with open(r"C:\Users\admin\Documents\Downloads\Input_02.txt", 'r') as file:
            for line in file:
                word = line.strip()
                if word:
                    ws.add(word)
                    words_list.append(word)
    except FileNotFoundError:
        return "File not found!"
    
    words_list.sort(key=len, reverse=True)

    memo = {}
    largest_compound = ""
    second_largest_compound = ""
    
    start_time = time.time()  
    for word in words_list:
        ws.remove(word)
        
        if cp(word, ws, memo):
            if not largest_compound:
                largest_compound = word
            else:
                second_largest_compound = word
                break
        
        ws.add(word)
    end_time = time.time()  
    
    print(f"Time taken: {end_time - start_time:.3f} seconds")
    result = {
        "largest_compound": largest_compound if largest_compound else "No compound word found!",
        "second_largest_compound": second_largest_compound if second_largest_compound else "No second compound word found!"
    }
    return result

filename = "C:\\Users\\admin\\Documents\\Downloads\\Input_02.txt"
result = f2(filename)
print(f"Largest compound word: {result['largest_compound']}")
print(f"Second largest compound word: {result['second_largest_compound']}")
