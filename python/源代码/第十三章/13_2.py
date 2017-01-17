def download(url,filename=""):
    def reporthook(block_count, block_size, file_size):
        if file_size == -1:
            print ("Can't determine the file size, now retrieved", block_count*block_size)
        else:
            percentage = int((block_count*block_size*100.0)/file_size)
            if percentage > 100:
                print ("100%")
            else:
                print ("%d%%" % (percentage))
    filehandler, m = urlretrieve(url,filename,reporthook=reporthook)
    print ("Done")
return filehandler
