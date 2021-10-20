class BinarySearch():

    def main(self, list, item):
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = int((low + high) / 2)
            guess = list[mid]

            if guess == item:
                return mid
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None




if __name__ == '__main__':
    bs = BinarySearch()

    list = [1,2,3,4,5,6,7,8,9]
    print(bs.main(list, 9))
