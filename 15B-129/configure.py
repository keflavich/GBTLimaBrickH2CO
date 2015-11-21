with open("/users/aginsbur/GBT15B-129/H2CO_2cm_KUSetup_GC_15B-129.py",'r') as f:
    myconfig = f.read()

Configure(myconfig)
Balance()
