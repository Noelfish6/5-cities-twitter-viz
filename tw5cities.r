load('/Users/xshen/Documents/python_r/tw5cities.RDa')
ls()

str(tw5cities)
#write into a text file
write.table(tw5cities, file="tw5cities.txt", row.names = FALSE, quote = FALSE, sep="\t")