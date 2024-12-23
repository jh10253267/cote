def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    arr = ["-", "_", "."]
    
    for i in new_id:
        if not (97 <= ord(i) <= 122 or 48 <= ord(i) <= 57 or i in arr):
            new_id = new_id.replace(i, "")
                
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    new_id = new_id.strip('.')
    
    if len(new_id) == 0:
        new_id += "a"
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    new_id = new_id.strip('.')
    
    if len(new_id) <= 2:
        val = new_id[-1]
        while len(new_id) < 3:
            new_id += val
    
    return new_id