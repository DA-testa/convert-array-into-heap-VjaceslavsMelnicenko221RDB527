# python3 

def build_heap(data):
    swaps = []
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    for i in range (n, -1, -1):
        c = i
        while True:
            d = (c * 2) + 1
            if d >= n:
                break
            if d+1 < n and data[d+1] < data[d]:
                d = d+1
            if data[c] > data[d]:
                swaps.append((c, d))
                data[c], data[d] = data[d], data[c]
                c = d
            else:
                break
    return swaps

def main():

    
    tt = input("Input or File: ")
    if "I" in tt:
        n = int(input())
        data = list(map(int, input().split()))
    
    elif "F" in tt:
        s = input()
        if "a" not in s:
            with open("tests/" + s, 'r', encoding='utf-8') as w:
                n = int(w.readline())
                data = list(map(int, w.readline().split()))
    else:
        print("Error")
        return 

    assert data is not None and len(data) == n
    

    swaps = build_heap(data)
    
    assert len(swaps) <= n*4
    

    print(len(swaps))
    
    for i, j in swaps:
        print(i, j)
       
if __name__ == "__main__":
    main()
