with open("randomparas.txt", encoding="utf-8", errors="ignore") as f:
    huge_text = f.read()

# with open("<>.txt") as file: (open a local scope)
#   huge_text f.read()

chunks = huge_text.split("\n")

# list = ["hey","hi","ti"] (implict indexing)

# enumerated_list = [[0,"hey"],[1,"hi"],[2,"ti"]] (explicit indexing)

for i,chunk in enumerate(chunks):
    # processing each chunk
    # 1. word length
    words = chunk.split()
    sentence = chunk.split(".")
    # other mining elements
    print(i+1,len(sentence))

f.close() # clearing memory leaks