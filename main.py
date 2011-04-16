import time
import re
import cleverbot
from pyomegle import Omegle

def log(val):
  print val
  with open("log.txt", 'a') as f:
    f.write("%f: %s\n" % (time.time(), val))

while True:
  log("*****Conversation Start*****")
  cb = cleverbot.Session()
  om = Omegle()

  def debug(obj, ev):
    print "DEBUG: " + ev

  def recv(obj, ev):
    log("Stranger: " + ev)
    while True:
      try:
        resp = cb.Ask(ev)
        resp = re.sub("cleverbot", "Tim the Enchanter", resp, re.IGNORECASE)
        break
      except cleverbot.ServerFullError:
        continue
    log("Cleverbot: " + resp)
    if om.connected and len(resp) > 0:
        om.send_msg(resp)

  om.connect("message-received", recv)

  om.start(threaded = False)
  log("*****Conversation End*****")
