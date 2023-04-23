from ECTools import Point,ECCurve,ECGroup,ECFactory

if __name__ == '__main__':

    factory = ECFactory()

    factory.print_all_groups(ECGroup(17),ECCurve(0,7))              # print all groups generated by ECCurve with valid origin 
    res = factory.print_group(ECGroup(17),ECCurve(0,7),Point(6,11))       # print generated group by ECCurve for a given origin (6,11)

    factory.plot_sequence(res)  # plot graph : blocking call (need to close window)

