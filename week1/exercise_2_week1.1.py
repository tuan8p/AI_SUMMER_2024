def find(arr):
    arr.sort()
    aver = sum(arr) / len(arr)
    print("Highest score: " + str(arr[-1]))
    print("Lowest score: " + str(arr[0]))
    print("Average score: " + str(aver))
    print("Second largest number: " + str(arr[-2]))
    arr.remove(arr[0])
    arr.remove(arr[0])
    aver = sum(arr) / len(arr)
    print("Average of the rest of them: " + str(aver))

def input1():
    arr = []
    for _ in range(10):
        temp = int(input());
        while(temp > 100):
            print("This value is over 100");
            temp = int(input());
        arr.append(temp);
    return arr

def main():
    arr = input1()
    find(arr)

main()
        

