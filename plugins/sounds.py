# -*- coding: utf-8 -*-
import json

class sounds:

    def __init__(self,SID,master):
        self.master=master
        self.SID=SID

    def help(self):
        return {"sounds": "All sound commands"}

    def hook_checkout(self,text):
        for r in self.master.receipt.receipt:
            if r['product']=='deposit':
                self.master.send_message(False,'sound','itsgone.wav')
                break;
        self.master.send_message(False,'sound','katsjing.wav')

    def hook_balance(self,(usr,had,has,transID)):
        if has < -13.37:
            self.master.send_message(False,'sound','sinterklaas.wav')

    def hook_undo(self,(transID,totals,receipt,beni)):
        pass

    def playsounds(self,text):
        if text=='ns':
            self.master.send_message(False,'sound','ns.wav')
        elif text=='deuron':
            pass
        elif text=='deuroff':
            pass
        elif text=='kassaon':
            pass
        elif text=='kassaoff':
            pass
        elif text=='killsounds':
            pass
        elif text=='abort':
            self.master.callhook('abort',None)
            return True
        else:
            return False
        self.showsounds()
        return True
        
    def showsounds(self):
        custom=[]
        custom.append({'text': 'abort','display': 'Abort'})
        custom.append({'text': 'ns','display': 'Ding Dong'})
        custom.append({'text': 'deuron','display': 'Deur on'})
        custom.append({'text': 'deuroff','display': 'Deur off'})
        custom.append({'text': 'kassaon','display': 'Kassa on'})
        custom.append({'text': 'kassaoff','display': 'Kassa off'})
        custom.append({'text': 'killsounds','display': 'Kill Music'})
        self.master.send_message(True,'buttons',json.dumps({'special':'custom','custom':custom}))
        self.master.send_message(True,'message','Please select a command')
        self.master.donext(self,'playsounds')

    def input(self,text):
        if text=="sounds":
            self.showsounds()
            return True

    def pre_input(self,text):
        self.master.send_message(False,'sound','KDE_Beep_ClassicBeep.wav')

    def hook_wrong(self,text):
        self.master.send_message(False,'sound','KDE_Beep_Beep.wav')

    def startup(self):
        pass
