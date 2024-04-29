def comparePokerFigure(f1, f2):
        compair_list = ["2","3",'4','5','6','7','8','9','10',"J", "Q", "K","A"]

        if compair_list.index(f1) > compair_list.index(f2):
            return True
        else:
              return False