# Link to get the video
# "http://tvod-ptp8k.static.cdn.tvod.com.vn/tvcatchup/20190331/htv9sd/{number1}-htv9hd-{number2}.ts"
# video starts at number1 = 201903310740 and number2 = 52140
# it ends at 201903310759 and 52330
# for other videos, inspect the first and final .ts package sent by the server, input the approriate start and end


f = open("video.ts","wb")
number = 201903310740
for i in range(52140, 52331):
    url = lambda number,i : f"http://tvod-ptp8k.static.cdn.tvod.com.vn/tvcatchup/20190331/htv9sd/{number}-htv9hd-{i}.ts"
    r = requests.get(url(number,i))
    while str(r) != "<Response [200]>":
        number += 1
        r = requests.get(url(number,i))
        print(number)
    else:
        print(i)
        f.write(r.content)
        
f.close()
