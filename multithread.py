import threading
import spider
import time
# def single():
#     for i in spider.urls:
#         spider.craw(i)
#     for i in spider.li:
#         print(i)
def multi():
    spiders = []
    for i in spider.urls:
        spiders.append(
            threading.Thread(target=spider.craw,args=(i,))
        )
    for i in spiders:
        i.start()
    for i in spiders:
        i.join()

if __name__ == "__main__":
    # s1=time.time()
    # single()
    # e1=time.time()
    # print(e1-s1)

    s2=time.time()
    multi()
    e2=time.time()
    print(e2-s2)
    t=0
    for i in spider.li:
        print(i)
        t+=1
    print(t)

