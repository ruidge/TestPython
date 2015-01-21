# coding=utf-8
'''
Created on 2014-10-17

@author: zhangrui6
'''
"""Framework for getting filetype-specific metadata.

Instantiate appropriate class with filename.  Returned object acts like a
dictionary, with key-value pairs for each piece of metadata.
    import fileinfo
    info = fileinfo.MP3FileInfo("/music/ap/mahadeva.mp3")
    print "\\n".join(["%s=%s" % (k, v) for k, v in info.items()])

Or use listDirectory function to get info on all files in a directory.
    for info in fileinfo.listDirectory("/music/ap/", [".mp3"]):
        ...

Framework can be extended by adding classes for particular file types, e.g.
HTMLFileInfo, MPGFileInfo, DOCFileInfo.  Each class is completely responsible for
parsing its files appropriately; see MP3FileInfo for example.
"""
import os
import sys
from UserDict import UserDict

def stripnulls(data):
    "strip whitespace and nulls"
    return data.replace("\00", "").strip()

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename #这个时候其实是调用了__setitem__函数,MP3子类复写了这个方法加入了自定义解析

class MP3FileInfo(FileInfo):
    "store ID3v1.0 MP3 tags"
# 类属性,类似static;成员属性用self.XXX在不需要定义
# 类属性既可以通过直接对类的引用，也可以通过对类的任意实例的引用来使用。
# 在 Java 中，静态变量 (在 Python 中叫类属性) 和实例变量 (在 Python 中叫数据属性) 两者都是紧跟在类定义之后定义的 (一个有 static 关键字，一个没有)。
# 在 Python 中，只有类属性可以定义在这里，数据属性定义在 __init__ 方法中。
# 类属性可以作为类级别的常量来使用 (这就是为什么我们在 MP3FileInfo 中使用它们)，但是它们不是真正的常量。你也可以修改它们。
# 在 Python 中没有常量。如果你试图努力的话什么都可以改变。这一点满足 Python 的核心原则之一：坏的行为应该被克服而不是被取缔。
# 如果你真正想改变 None 的值，也可以做到，但当无法调试的时候别来找我。
    tagDataMap = {"title"   : (3, 33, stripnulls),
                  "artist"  : (33, 63, stripnulls),
                  "album"   : (63, 93, stripnulls),
                  "year"    : (93, 97, stripnulls),
                  "comment" : (97, 126, stripnulls),
                  "genre"   : (127, 128, ord)}

    def __parse(self, filename):
        "parse ID3v1.0 tags from MP3 file"
        self.clear()
        try:                               
            fsock = open(filename, "rb", 0)
            try:                           
                fsock.seek(-128, 2)        
                tagdata = fsock.read(128)  
            finally:                       
                fsock.close()              
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])               
        except IOError:                    
            pass                           

    def __setitem__(self, key, item):
        if key == "name" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)

def listDirectory(directory, fileExtList):                                        
    "get list of file info objects for files of particular extensions"
    fileList = [os.path.normcase(f)
                for f in os.listdir(directory)]           
    fileList = [os.path.join(directory, f) 
               for f in fileList
                if os.path.splitext(f)[1] in fileExtList] 
    def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):      
        "get file info class from filename extension"                             
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]       
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
    return [getFileInfoClass(f)(f) for f in fileList]                             

if __name__ == "__main__":
#     for info in listDirectory("/music/_singles/", [".mp3"]):
#         print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
#         print
    info = MP3FileInfo();
    print info
    info['name'] = 'C:\\Users\\zhangrui6\\Desktop\\test.mp3'
    print info

# 专用方法相关:
# 在 Java 中，通过使用 str1 == str2 可以确定两个字符串变量是否指向同一块物理内存位置。这叫做对象同一性，在 Python 中写为 str1 is str2。
# 在 Java 中要比较两个字符串值，你要使用 str1.equals(str2)；在 Python 中，你要使用 str1 == str2。

# 专用方法意味着任何类 可以像字典一样保存键-值对，只要定义 __setitem__ 方法。
# 任何类可以表现得像一个序列，只要定义 __getitem__ 方法。
# 任何定义了 __cmp__ 方法的类可以用 == 进行比较。
# 并且如果你的类表现为拥有类似长度的东西，不要定义 GetLength 方法，而定义 __len__ 方法，并使用 len(instance)。

# Python 存在许多其它的专用方法。有一整套的专用方法，可以让类表现得象数值一样，允许你在类实例上进行加、减，以及执行其它算数操作。
# (关于这一点典型的例子就是表示复数的类，数值带有实数和虚数部分。) 
# __call__ 方法让一个类表现得像一个函数，允许你直接调用一个类实例。并且存在其它的专用函数，允许类拥有只读或只写数据属性
