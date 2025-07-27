class FileSystemItem:
    def show(self):
        pass

class File(FileSystemItem):
    def __init__(self,name):
        self.name = name 
        
    def show(self, indent = 0):
        print("  "*indent + f"File: {self.name}")

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name 
        self.items = [] 
        
    def add(self, item: FileSystemItem):
        self.items.append(item)
    
    def show(self, indent=0):
        print("  "*indent +f"Folder: {self.name}")
        for item in self.items:
            item.show(indent+1)
            
if __name__ == "__main__":
    
    file1 = File("resume.pdf")
    file2 = File("report.docx")
    file3 = File("photo.jpg")
    
    folder1 = Folder("Document")
    folder2 = Folder("Pictures")
    folder3 = Folder("Main Folder")
    
    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)
    
    folder3.add(folder1)
    folder3.add(folder2)
    
    folder3.show()
    
    
    
    
    