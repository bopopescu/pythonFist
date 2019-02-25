
# import io
#
# output = io.StringIO()
# output.write('First line .\n')
# print('Second line.', file=output)
#
# contents = output.getvalue()
# output.close()


from time import gmtime, strftime
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))





























