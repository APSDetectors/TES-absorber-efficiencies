
### TES-absorber-efficiencies

These python scripts just calculate x-ray absorption efficiencies for some commonly used x-ray TES absorber materials (and Germanium). It uses xraylib (https://github.com/tschoonj/xraylib/wiki) libraries. At least, these scripts give you an idea of how to use xraylib. 

Here are some notes on how to install xraylib on a Mac (without root):

* Install brew: 
```sh
$ mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
```
* Install xraylib with brew:
```sh
$ homebrew/bin/brew install homebrew/science/xraylib
$ cd homebrew/bin
$ ./brew info homebrew/science/xraylib
$ mkdir -p /Users/amiceli/.local/lib/python2.7/site-packages
$ echo 'import site; site.addsitedir("/Users/amiceli/homebrew/lib/python2.7/site-packages")' >> /Users/amiceli/.local/lib/python2.7/site-packages/homebrew.pth
```