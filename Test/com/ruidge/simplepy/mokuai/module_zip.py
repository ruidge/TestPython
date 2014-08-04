# coding=utf-8
'''
Created on 2014-8-1

@author: zhangrui6
'''
import os
import zipfile

if __name__ == "__main__":
    zipFile = zipfile.ZipFile('E:\\test.zip')
    zipInfo = zipFile.getinfo(r'test_rename')
    print 'filename:', zipInfo.filename
    print 'date_time:', zipInfo.date_time
    print 'compress_type:', zipInfo.compress_type
    print 'comment:', zipInfo.comment
    print 'extra:', zipInfo.extra
    print 'create_system:', zipInfo.create_system
    print 'create_version:', zipInfo.create_version
    print 'extract_version:', zipInfo.extract_version
    print 'extract_version:', zipInfo.reserved
    print 'flag_bits:', zipInfo.flag_bits
    print 'volume:', zipInfo.volume
    print 'internal_attr:', zipInfo.internal_attr
    print 'external_attr:', zipInfo.external_attr
    print 'header_offset:', zipInfo.header_offset
    print 'CRC:', zipInfo.CRC
    print 'compress_size:', zipInfo.compress_size
    print 'file_size:', zipInfo.file_size
    zipFile.close()
