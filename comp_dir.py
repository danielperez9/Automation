import filecmp

# dir1='D:\Sampletext'
# dir2='D:\module'
res=filecmp.dircmp('D:\SampleText','D:\module')
res.report()

