#!/usr/bin/python3

def main():
    buffersize = 500
    word = "What"
    infile = open('tiger.bmp', 'rb')
    outfile = open('tiger2.bmp', 'wb')
    buffer = infile.read(buffersize)
    i = 0
    while len(buffer):
        outfile.write(buffer)
        if(i < len(word)):
            outfile.write(bytearray(word[i], 'utf-8'))
            print("Writing " + word[i])
            i += 1
        print('.', end='')
        buffer = infile.read(buffersize)

    print()
    print('Done.')

if __name__ == "__main__": main()
