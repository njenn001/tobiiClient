import os 
from os import system, name
import argparse 
import random
import time
import threading
from turtle import clear 

# Project logo 
logo = (r''' 

 ___________________
|                   |
|___________________|             __
        |   |                    |  |   __
        |   |                    |  |  |__|                                __
        |   |     ____________   |  |   __    ___________    ___   __     |  |
        |   |    |            |  |  |  |  |  |    ____   |  |   \ |  |   _|  |_
        |   |    |   |--------   |  |  |  |  |   |____|  |  |    \|  |  |_    _|
        |   |    |   |           |  |  |  |  |    _______|  |  |\    |    |  |
        |   |    |   |--------|  |  |  |  |  |   |_______   |  | \   |    |  |
        |___|    |____________|  |__|  |__|  |___________|  |__|  \ _|    |__|
 -------------------------------------------------------------------------------
|                                                                               |
 -------------------------------------------------------------------------------

''')

# Clear terminal screen
def clearScreen():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

# Create virtual environment 
def virtmode(): 
    from scenario import Scenario
    print('Starting setup sequence...')
            
    # Run evaluation and resulting programs 
    scene = Scenario() 
    scene.virt_thread.start() 
    
    time.sleep(5) 
    scene.stop_threads()  

# Setup natural environment 
def natmode(): 
    from scenario import Scenario
    print('Starting setup sequence...')
            
    # Run evaluation and resulting programs 
    scene = Scenario() 
    scene.nat_thread.start()
    
    time.sleep(5) 
    scene.stop_threads()

# Clean repositories 
def cleanmode(): 
    from scenario import Scenario
    print('Cleaning...')
    
    scene = Scenario() 
    scene.clean_sequence() 
    
# Start con mode
def conmode(args): 
    from user import User 
    clearScreen()
    print('Starting strict consumption mode...')

    # Decode arguments
    you = User() 

    try: 
        you.strict_con(args) 
    except Exception as ex: 
        you.throw_exec('strict')    

# Start prod mode
def prodmode(args): 
    from user import User 
    print('Starting strict production mode...')

    # Decode arguments
    you = User() 

    try: 
        you.strict_prod(args) 
    except Exception as ex: 
        you.throw_exec('strict')    

# Start gui mode
def guimode(): 
    from user import User 
    print('Starting gui...')

    you = User()

    try: 
        you.gui()
    except Exception as ex: 
        you.throw_exec('gui')
        pass

# Display project info
def infomode(): 
    
    clearScreen() 
    print(logo) 

# Decode available arguments 
def args_decoder(args): 
        
    # Start virtual mode  
    if args.env: 
        virtmode()         

    # Start natural mode  
    if args.nat: 
        natmode()          

    # Start clean mode
    elif args.clean: 
        cleanmode() 

    # Start strict prod mode 
    elif args.prod: 
        prodmode(args) 

    # Start strict con mode 
    elif args.con: 
        conmode(args) 
        
    # Start gui mode
    elif args.gui: 
        guimode() 
        
    # Start info mode
    elif args.info: 
        infomode()

# Init command parser 
def init_parser(): 
    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=logo + 'Tobii tracker stream processing',
                epilog='For more help, see README.md')
        
    '''
    Specify different interface modes
    - env 
    - clean 
    - strict
    - gui 
    '''
    mode_group = parser.add_mutually_exclusive_group(required=True)

    # Virt Mode 
    mode_group.add_argument('-e', '--env', action='store_true',
                            help='Initialize environment setups.')

    # Nat mode 
    mode_group.add_argument('-n', '--nat', action='store_true',
                            help='Initialize natural setups.')

    # Clean Mode
    mode_group.add_argument('-c', '--clean', action='store_true',
                            help='Clean repository.')

    # Prod Mode
    mode_group.add_argument('-p', '--prod', action='store_true',
                            help='Auto tracking/production.')

    # Con Mode
    mode_group.add_argument('-co', '--con', action='store_true',
                            help='Auto reading/consumption.')

    # Gui Mode 
    mode_group.add_argument('-g', '--gui', action='store_true',
                            help='Start GUI.')

    # Info Mode 
    mode_group.add_argument('-i', '--info', action='store_true',
                            help='Show info.')        


    '''
    Specify different flags 
    - name
    - wait time (s)
    - broker id 
    - length 
    '''

    # Bootstrap server flag 
    parser.add_argument(
    '--bss', '--boostrap_servers', type=str, help="Specify broker IP address(es) and port number(s).", nargs='+')

   # Begin strict production
    parser.add_argument(
    '--topic', '--topic', type=str, help="Specify topic.", nargs='+')

    return parser 

# Main function 
def main(): 
        
    # Set and capture command line arguments     
    parser = init_parser()
    args, unknown = parser.parse_known_args() 

    # Decode available arguments 
    args_decoder(args) 

# Listen for main 
if __name__ == '__main__': 
    
    # Run main program    
    main() 