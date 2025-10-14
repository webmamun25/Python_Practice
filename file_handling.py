with open('sample_Test.txt','r') as file:
    line=file.readlines()
    # remove new line 
    total_line=list(map(lambda x:len(x.split()),line))
    # total lines 
    print(len(total_line))
    # total word 
    total_words=list(map(lambda x:len(x.split()),line))
    print(sum(total_words))
    # total characters 
    
    total_characters=list(map(lambda x:x.strip().replace(' ',''),line))
    total_characters=list(map(lambda x:len(x),total_characters))
    
    print(sum(total_characters))
    
    # sum important method of file handling
    strings=file.tell()
    print(strings)
    
    
    
    with open('sample_Test.txt', 'r') as file:
        print(f"file_tell:{file.tell()}") # আউটপুট: 0

        # whence=0 (ডিফল্ট): ফাইলের শুরু থেকে ৭ নম্বর বাইটে কার্সর সেট করা
        file.seek(6)
        
        print(f"seek(6) : {file.tell()}") # আউটপুট: 6
       
        # এখন যদি ফাইল পড়া হয়, তবে ৬ নম্বর পজিশন থেকে পড়া শুরু হবে
        content = file.read()
        print(f"'{content}'") # আউটপুট: 'Python'

        # whence=0: আবার ফাইলের শুরুতে ফিরে যাওয়া
        file.seek(0)
        print(f"seek(0) : {file.tell()}") # আউটপুট: 0
        
        
with open('sample_Test.txt', 'r+') as file: # 'r+' মোড মানে রিড এবং রাইট দুটোই করা যাবে
    print(f"Truncate করার আগে ফাইল: '{file.read()}'")

    # ফাইলটিকে প্রথম 10 বাইটে ছোট করা হলো
    file.truncate(10)

    # কার্সরটিকে আবার শুরুতে নিয়ে আসা হলো পড়ার জন্য
    file.seek(0)
    
    print(f"Truncate করার পরে ফাইল: '{file.read()}'")