SMALL_DIRECTORY_THRESHOLD = 100000
UPDATE_SIZE = 30000000
TOTAL_MEMORY = 70000000

class File:
    def __init__(self, name, size, parentDirectory):
        self.parentDirectory = parentDirectory
        self.name = name
        self.size = size

class Directory:        
    def __init__(self, name, parentDirectory):
        self.name = name
        self.parentDirectory = parentDirectory  
        self.files = []
        self.subdirectories = []
        self.size = 0

    def updateFileSize(self, fileSize):
        self.size += fileSize
        if self.parentDirectory:
            self.parentDirectory.updateFileSize(fileSize)

    def addFile(self, fileName, fileSize):
        self.files.append(File(fileName, fileSize, self))
        self.updateFileSize(fileSize)
    
    def addDirectory(self, directoryName):
        self.subdirectories.append(Directory(directoryName, self))

    def getSubdirectory(self, subdirectoryName):
        return [directory for directory in self.subdirectories if directory.name == subdirectoryName][0]

def parseFileSystem(data):
    rootDirectory = Directory(data[0].replace('$ cd ', ''), None)
    currentDirectory = rootDirectory

    for line in data[1:]:
        if line.startswith('$ ls'):
            continue
        elif line.startswith('$ cd'):
            targetDirectoryName = line.replace('$ cd ', '')
            currentDirectory = currentDirectory.getSubdirectory(targetDirectoryName) if targetDirectoryName != '..' else currentDirectory.parentDirectory
        elif line.startswith('dir'):
            currentDirectory.addDirectory(line.replace('dir ', ''))
        else:
            fileSize, fileName = line.split(' ')
            currentDirectory.addFile(fileName, int(fileSize))

    return rootDirectory

def smallSubirectories(root):
    size = root.size if root.size <= SMALL_DIRECTORY_THRESHOLD else 0

    for subdirectory in root.subdirectories:
        size += smallSubirectories(subdirectory)

    return size

def directoryToDeleteSize(root, neededMemory, smallestSizeToDeleteFound):
    for subdirectory in root.subdirectories:
        if subdirectory.size < neededMemory:
            continue
        smallestSizeToDeleteFound = directoryToDeleteSize(subdirectory, neededMemory, min(subdirectory.size, smallestSizeToDeleteFound))

    return smallestSizeToDeleteFound

def part1(data):
    root = parseFileSystem(data)
    return smallSubirectories(root)

def part2(data):
    root = parseFileSystem(data)
    neededMemory =  root.size + UPDATE_SIZE - TOTAL_MEMORY
    return directoryToDeleteSize(root, neededMemory, TOTAL_MEMORY)