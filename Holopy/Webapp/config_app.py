import os

def test(argv):
    settings = {
        '-i': 'localhost',
        '-p': '8080',
        '-d': '/tmp/'}

    if '--help' in argv or len(argv) % 2 == 0:
        print("""Running app:
            python3 __init.py <params>
                -i  ->  Listening adress    default: localhost
                -p  ->  Port                default: 8080
                -d  ->  Data folder         default:/tmp/Holopy_holo/""")
        quit()

    else:
        params = {}
        for param in argv[1::2]:
            params[param] = argv[argv.index(param) + 1]

        settings.update(params)
        server_path = argv[0][:-11] + 'static/'

        if not os.path.exists(server_path + 'Holopy_holo/'):
            print('\n * Creating symbolic link in {} to {}/Holopy_holo'.format(server_path, settings['-d']))
            os.system('ln -s {}/Holopy_holo {}'.format(settings['-d'], server_path))
            print('   * Done\n')

        print(' * Starting for parameters:')
        print('   * ip    : {}'.format(settings['-i']))
        print('   * port  : {}'.format(settings['-p']))
        print('   * folder: {}\n'.format(settings['-d']))

        if not os.path.exists(settings['-d'] + 'Holopy_holo/'):
            os.system('rm -rf {}/Holopy_holo'.format(server_path))
            print(''' * Database doesn't exist''')
            print('   * Creating folders...')
            print('     * Holopy_holo')
            os.mkdir(settings['-d'] + 'Holopy_holo/')
            print('     * Holopy_holo/raw/')
            os.mkdir(settings['-d'] + 'Holopy_holo/raw/')
            print('     * Holopy_holo/holo')
            os.mkdir(settings['-d'] + 'Holopy_holo/holo/')
            print('     * Holopy_holo/reholo')
            os.mkdir(settings['-d'] + 'Holopy_holo/reholo/')
            print('   * Done\n')

        return settings
    return None

