from __future__ import print_function

from vivid_schemer import __version__

from vivid_schemer.playbook.book import Book
from vivid_schemer.play import Play
from vivid_schemer.sexp import SExp, SAtom
from vivid_schemer.errors import VividError

import click
import readline

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode emacs')

_book = Book('the_little_schemer')
_tree = False

import cmd
import logging

FORMAT = '[%(levelname)s] [%(filename)s:%(lineno)d] %(message)s '
logging.basicConfig(level=logging.WARNING, format=FORMAT)


class Repl(cmd.Cmd):
    prompt = 'play>: '
    intro = 'Usage: [a]bort  [e]val  [s]tack  [t]op  [h]elp'

    def __init__(self, code):
        cmd.Cmd.__init__(self)
        self._play = Play()
        self._play.parse(code)

    def do_help(self, arg):
        print('The Vivid Schemer %s' % __version__)
        print('abort\tabort this session')
        print('eval\tevaluate current expression')
        print('stack\tprint the whole stack')
        print('top\tprint the expression on top of the stack')
        print('help\tprint this message')

    def do_abort(self, arg):
        print('goodbye!')
        return True

    def do_eval(self, arg):
        try:
            args = arg.strip().split()
            if len(args) > 0:
                self._play.next(args[0])
            else:
                self._play.next()
        except StopIteration:
            v = self._play.value
            if isinstance(v, int):
                print('(integer): %s' % v)
            elif isinstance(v, SAtom):
                print('(atom): %s' % str(v))
            elif isinstance(v, SExp):
                print('(list): %s' % v.as_list())
            else:
                raise TypeError('(unknown type): ' % v)
            return True

    def do_top(self, arg):
        args = arg.strip().split()
        if len(args) > 0:
            self._play.top(args[0])
        else:
            self._play.top()

    def do_stack(self, arg):
        args = arg.strip().split()
        if len(args) > 0:
            self._play.stack(args[0])
        else:
            self._play.stack()

    do_h = do_help
    do_t = do_top
    do_e = do_eval
    do_a = do_abort
    do_s = do_stack
    do_EOF = do_abort


@click.group()
@click.option('-v', '--verbose', count=True, help='verbosity: -v, -vv')
def cli(verbose):
    """A REPL for "The Little Schemer" built with love."""
    if verbose == 1:
        logging.getLogger().setLevel(logging.INFO)
    elif verbose == 2:
        logging.getLogger().setLevel(logging.DEBUG)


@cli.command(short_help='list the chapters')
def list():
    """List all the chapters in "The Little Schemer"."""
    for ch in _book.collect():
        click.echo(ch)


@cli.command(short_help='choose a chapter')
@click.argument('name')
def chapter(name):
    """Choose a chapter in "The Little Schemer" to play."""
    with open(_book.collect()[name]) as fd:
        s = ''.join(fd.readlines())
        cmd = Repl(s)
        cmd.cmdloop()


@cli.command(short_help='enter the playground')
@click.option('--code', '-s', prompt='scheme>', help='The code to play.')
def playground(code):
    """Try with any code in playground."""

    try:
        cmd = Repl(code)
        cmd.cmdloop()
    except VividError as e:
        print(e)


if __name__ == "__main__":
    cli()
