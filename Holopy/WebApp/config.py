import os

def test(argv):

    settings = {
            '-i':'localhost',
            '-p':'8080',
            '-d':'/tmp/'}

    if '--help' in argv or len(argv)%2 == 0:
        print("""Running app:
            python3 __init.py <params>
                -i  ->  Listening adress    default: localhost
                -p  ->  Port                default: 8080
                -d  ->  Data folder         default:/tmp/holograms/""")
        quit()
    
    else:
        params = {}
        for param in argv[1::2]:
            params[param] = argv[argv.index(param)+1]
        
        settings.update(params)
        
        if not os.path.exists(settings['-d']+'Holopy_holo/'):
            os.mkdir(settings['-d']+'Holopy_holo/')
            os.mkdir(settings['-d']+'Holopy_holo/raw/')
            os.mkdir(settings['-d']+'Holopy_holo/holo/')
            os.mkdir(settings['-d']+'Holopy_holo/reholo/')



        return settings

