#!/usr/bin/env python
import logging

# Define the logger
LOG = logging.getLogger(__name__)

def create_poem(name, start_index, stop_index, number_of_entries_per_line, separator):
    LOG.debug("%s %i %i"%(name, start_index, stop_index))

    word_count = 0
    line = ''
    for i in range(start_index, stop_index+1):
        line += "%s%s%s"%(name, separator, i)
        line += ", " if i != stop_index else "."
        word_count += 1
        if word_count%number_of_entries_per_line == 0:
            print line
            line = ""
    if line != "":
        print line

if __name__ == "__main__":
    try:
        import argparse
    except Exception, e:
        print ""
        print "Try running 'sudo apt-get install python-argparse' or 'sudo easy_install argparse'!!"
        print ""
        raise e

    parser = argparse.ArgumentParser(description='Create a poem with a name followed by a number. E.g.: Nimbus 1, Nimbus 2, Nimbus 3... Nimbus 2000.')
    parser.add_argument( 'name'
                         , type=str
                         , help='Name in the poem.'
                         )
    parser.add_argument( 'stop_index'
                         , type=int
                         , help='Where to stop, e.g. 2000 in the example above for Nimbus 2000.'
                         )
    parser.add_argument( '--start-index'
                         , type=int
                         , default=1
                         , help='Start index. Number at the first entry. If not set, starting from 1, e.g. Nimbus 1.'
                         )
    parser.add_argument( '--separator'
                         , type=str
                         , default=" "
                         , help='Separator between name and number. If not set, a space is inserted.'
                         )
    parser.add_argument( '--number-of-entries-per-line'
                         , type=int
                         , default=1
                         , help='Number of entries per line.'
                         )
    parser.add_argument( '-d', '--debug', action='store_true', help="Output debugging information." )
    parser.add_argument( '--log_filename', type=str, help="File used to output logging information." )

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig( filename=args.log_filename, level=logging.DEBUG )
    else:
        logging.basicConfig( filename=args.log_filename, level=logging.INFO )

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig( filename=args.log_filename, level=logging.DEBUG )
    else:
        logging.basicConfig( filename=args.log_filename, level=logging.INFO )

    # Output what is in the args variable.                                                                                                                                                                                                    
    LOG.debug(args)

    create_poem(args.name, args.start_index, args.stop_index, args.number_of_entries_per_line, args.separator)
