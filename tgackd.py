import os

for ddstextures in os.listdir('input/'):
	
	with open('input/'+ddstextures,'rb') as f:
            data = f.read()

            header = b'\x00\x00\x00\x09\x54\x45\x58\x00\x00\x00\x00\x2C\x00\x00\x20\x80\x01\x00\x01\x00\x00\x01\x18\x00\x00\x00\x20\x80\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\xCC\xCC'
	
	dds=open('output_TGACKD/'+ckdtextures.replace('.dds','.tga.ckd'),'wb')
	print('making '+ckdtextures.replace('.dds','')+'...')
	dds.write(header+data)
	dds.close()