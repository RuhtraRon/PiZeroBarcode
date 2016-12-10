import barcode
from barcode.writer import ImageWriter

#EAN = barcode.get_barcode_class('ean13')
#ean = EAN(u'5901234123457', writer=ImageWriter())
#fullname = ean.save('ean13_barcode')

#UPC = barcode.get_barcode_class('upc')
#upc = UPC(u'12345678901')
code = barcode.get('ean13', u'0400052525016', writer=ImageWriter())
#options = {'quiet_zone': 1.0, 'text_distance': 3, 'module_width': 0.4, 'module_height': 15, 'dpi': 111}
options = {'font_size': 5, 'text_distance': 3, 'dpi': 111}
fullname = code.save('marsh', options=options)

code2 = barcode.get('Code39', u'10034760902', writer=ImageWriter())
code2.save('planet_fitness',{'text_distance': 1, 'module_width': 0.1, 'font_size':5, 'dpi':111})
