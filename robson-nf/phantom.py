import os

invoice_id = 1
htmlfile = 'http://127.0.0.1:8080/invoice/detail/' + str(invoice_id)
pdffile = 'invoice.pdf'
#pdffile = '/home/hobbit/azion-nf/static/pdf/invoice.pdf'
cmd = '/home/hobbit/Robson_Projects/azion-nf/phantomjs/bin/phantomjs /home/hobbit/Robson_Projects/azion-nf/phantomjs/examples/rasterize.js %s %s %s'

document_size = 'A4'

os.system(cmd % (htmlfile, pdffile, document_size))
