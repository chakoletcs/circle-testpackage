class InsufficientException(Exception):
    pass
class MobileInventoty:
    def __init__(self,inventory=None):
        if inventory == None:
            self.balance_inventory={}
        elif not isinstance(inventory,dict):
            raise TypeError("Input inventory must be dictionary")
        elif not (set(map(type,inventory))=={str}):
            raise ValueError("Mobile model must be a string")
        elif [True for i in inventory.values() if(not isinstance(i,int) or i <1)]:
            raise ValueError("No. of mobiles must be a positive integer")
        else:
            self.balance_inventory=inventory
    def add_stock(self,new_stock):
        if not isinstance(new_stock,dict):
            raise TypeError("Input inventory must be dictionary")
        elif not (set(map(type,new_stock))=={str}):
            raise ValueError("Mobile model must be a string")
        elif [True for i in new_stock.values() if(not isinstance(i,int) or i <1)]:
            raise ValueError("No. of mobiles must be a positive integer")
        else:
            for i,c in new_stock.items():
                if i in self.balance_inventory.keys():
                    x=self.balance_inventory[i]+c
                    self.balance_inventory[i]=x
                else:
                    self.balance_inventory.update({i:c})

    def sell_stock(self,requested_stock):
        if not isinstance(requested_stock,dict):
            raise TypeError("Input inventory must be dictionary")
        elif not (set(map(type,requested_stock))=={str}):
            raise ValueError("Mobile model must be a string")
        elif [True for i in requested_stock.values() if(not isinstance(i,int) or i <1)]:
            raise ValueError("No. of mobiles must be a positive integer")
        else:
            for i,c in requested_stock.items():
                if not i in self.balance_inventory.keys():
                    raise InsufficientException("No Stock. New Model Request")
                elif c>self.balance_inventory[i]:
                    raise InsufficientException("Insufficient Stock")
                else:
                    self.balance_inventory[i]=self.balance_inventory[i]-c

