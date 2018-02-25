password=hello.password
userid= hello.userid
url=hello.url
namespace=hello.namespace

#process args
p=optparse.OptionParser()
#add options
p.add_option("-b",action="store_true",dest="b64")
p.add_option("-d",action="store_true",dest="getDate")