def test_function(filePath, targetString):
    try:
        with (open)(filePath, 'r') as file:
            output =0
            for line in file:
                helper= line.count(targetString)
                
                output+=helper
                if helper!=0:
                    print(output)
                
        return output
    except FileNotFoundError:
        return -1
def main():
    filePath = '/Users/dagafed/Desktop/gutenberg.org_cache_epub_10_pg10.txt'
    targetString=input("Input Target String:")

    occurrences=test_function(filePath, targetString)

    if occurrences==-1:
        print("File not found")
    else:
        print({occurrences})
if __name__ == '__main__':
    main()