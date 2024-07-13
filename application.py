from router_imp import RouterImp
def run():
    router= RouterImp()
    router.withRoute("bar", "result")
    router.withRoute("bar/abc","1")
    router.withRoute("bar/bc/*","2")
    router.withRoute("bar/c/abc","3")
    # print(router.route("/bar"))
    # print(router.route("/bar/abc"))
    # print(router.route("bar/bc"))
    print(router.route("bar/c/*"))
if __name__=="__main__":
    run()