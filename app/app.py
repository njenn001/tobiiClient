import os 
import argparse 
import random
import time
import threading 


# Main function 
def main(): 
          
    # Decode available arguments 
    def args_decoder(args): 
        
        if not args: 
            
            print('none')
        
        elif args.env: 
            from scenario import Scenario
            print('Starting setup sequence...')
                    
            # Run evaluation and resulting programs 
            scene = Scenario() 
            scene.inst_thread.start() 
            
            #time.sleep(5) 
            scene.stop_threads()             
                
        elif args.clean: 
            from scenario import Scenario
            print('Cleaning...')
            
            scene = Scenario() 
            scene.clean_sequence() 
        
        elif args.strict: 
            from user import User 
            print('Starting strict mode...')

            # Run GUI 
            you = User() 

            try: 
                you.run_strict() 
            except Exception as ex: 
                you.throw_exec('r')
            
        elif args.gui: 
            from user import User 
            print('Starting gui...')

            you = User()

            try: 
                you.gui()
            except Exception as ex: 
                you.throw_exec('gui')
            

    # Init command parser 
    def init_parser(): 
        parser = argparse.ArgumentParser(
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    description='Tobii Tracker stream processing')
            
        '''
        Specify different interface modes
        - env 
        - clean 
        - strict
        - gui 
        '''
        mode_group = parser.add_mutually_exclusive_group(required=True)

        # Setup Mode 
        mode_group.add_argument('-e', '--env', action='store_true',
                                help='Initialize environment setups.')

        # Test Mode
        mode_group.add_argument('-c', '--clean', action='store_true',
                                help='Clean directory.')

        # Strict Mode
        mode_group.add_argument('-s', '--strict', action='store_true',
                                help='Start tracking.')

        # Gui Mode 
        mode_group.add_argument('-g', '--gui', action='store_true',
                                help='Start GUI.')        


        '''
        Specify different flags 
        - name
        - wait time (s)
        - broker id 
        - length 
        '''
        
        return parser 
            
    # Set and capture command line arguments     
    parser = init_parser()
    args, unknown = parser.parse_known_args() 

    # Decode available arguments 
    args_decoder(args) 

# Listen for main 
if __name__ == '__main__': 
    
    # Run main program    
    main() 