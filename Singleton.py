class AplicationState:
    instance = None
    
    def __init__(self):
        self.isLoggedIn = False
        print('Created Aplication instance ')

    @staticmethod
    def getAppState():
        if not AplicationState.instance:
            AplicationState.instance = AplicationState()
        return AplicationState.instance

appState1 = AplicationState.getAppState();
print(appState1.isLoggedIn)

appState2 = AplicationState.getAppState()
appState2.isLoggedIn = True 

print(appState1.isLoggedIn , appState2.isLoggedIn)
