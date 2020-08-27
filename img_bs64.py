from PIL import Image
import os
import base64

# 获取文件大小:KB
def get_size(file):
    size = os.path.getsize(file)
    return size / 1024

# 拼接输出文件地址
def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile

    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
def compress_image(infile, outfile='', mb=130, step=10, quality=80):
    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)
    return outfile, get_size(outfile)

def img_bs64(infile,outfile='', savefile =''):
    compress_image(infile)
    outfile = get_outfile(infile, outfile)
    f=open(outfile,'rb')
    pbs64=base64.b64encode(f.read()) 
    f.close()
    dir, suffix = os.path.splitext(infile)
    savefile = '{}-out{}'.format(dir, '.txt')
    mf=open(savefile,"wb")
    mf.write(pbs64)
    mf.close
    os.remove(outfile)
    #print(pbs64) #This will make python shell stuck, so put it in a txt file
    
    
if __name__ == '__main__':
    picturepath= "luffy.jpg" 
    img_bs64(picturepath)
