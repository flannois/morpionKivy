from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

class MonMorpion(BoxLayout):
    def __init__(self,**kwargs):
        super(MonMorpion,self).__init__(**kwargs)
        self.plateauVierge()
        self.joueurActuel = "X"
        self.scoreX = 0
        self.scoreO = 0
        
        
    def appuiBouton(self,case):
        self.initListeBouton()

        self.posePion(case)
        
    def posePion(self,case):
        print('Clic en {}'.format(case))
        if self.caseEstVierge(case):
            print("Case jouable")
            self.plateau[case] = self.joueurActuel
            self.listeBouton[case].text = self.joueurActuel
            self.aGagne()
        else:
            print("case non jouable")

    def changementJoueur(self):
        if self.joueurActuel == "X":
            self.joueurActuel = "O"
        elif self.joueurActuel == "O":
            self.joueurActuel = "X"
        self.label_joueur.text = str("Tour de : "+self.joueurActuel)

    def caseEstVierge(self,case):
        if self.plateau[case] == "O" or self.plateau[case] == "X":
            return False
        else:
            return True

    def aGagne(self):
        print(self.plateau)
        
        # Si in joueur à gagné
        if self.plateau[0] == self.plateau[1] == self.plateau[2] or \
            self.plateau[0] == self.plateau[3] == self.plateau[6] or \
            self.plateau[0] == self.plateau[4] == self.plateau[8] or \
            self.plateau[1] == self.plateau[4] == self.plateau[7] or \
            self.plateau[2] == self.plateau[5] == self.plateau[8] or \
            self.plateau[2] == self.plateau[4] == self.plateau[6] or \
            self.plateau[3] == self.plateau[4] == self.plateau[5] or \
            self.plateau[6] == self.plateau[7] == self.plateau[8]:
                print(self.joueurActuel)  
                self.ajoutPoint()
                self.plateauVierge()
                  

       
        else:
            #Encore des chiffres ?
            if "0" in self.plateau or\
                "1" in self.plateau or\
                "2" in self.plateau or\
                "3" in self.plateau or\
                "4" in self.plateau or\
                "5" in self.plateau or\
                "6" in self.plateau or\
                "7" in self.plateau or\
                "8" in self.plateau:
                self.changementJoueur()

            else:
                self.plateauVierge()
                
            
            
            

    def plateauVierge(self):
        self.plateau = ["0","1","2","3","4","5","6","7","8"]
        

    
    
    def ajoutPoint(self):
        if self.joueurActuel == "X":
            print("X gagne")
            self.scoreX += 1
            self.label_scoreX.text = str(self.scoreX)
            
        elif self.joueurActuel == "O":
            print("O gagne")
            self.scoreO += 1
            self.label_scoreO.text = str(self.scoreO)


    def initListeBouton(self):
        self.listeBouton = [self.label_bouton0,self.label_bouton1,self.label_bouton2,
                    self.label_bouton3,self.label_bouton4,self.label_bouton5,
                    self.label_bouton6,self.label_bouton7,self.label_bouton8
                ]
        for i in range(len(self.plateau)):
            if not self.plateau[i] in "012345678":
                self.listeBouton[i].text=str(self.plateau[i])
            else:
                self.listeBouton[i].text=str(" ")





class MorpionApp(App,MonMorpion):

    def build(self):
        
        return MonMorpion()

if __name__ == '__main__':

    MorpionApp().run()