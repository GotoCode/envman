# envman

`envman` (short for ".**env** **man**ager") is a command-line utility for creating and managing multiple `.env` files.

## Installation

To install `envman`, simply run the following commands in your favorite shell (`bash`, `zsh`, etc.):

```
$ git clone git@github.com:GotoCode/envman.git
$ cd envman
$ ./install.sh
```

Now, you should be able to directly call the `envman` program from the command line, like so:

```
$ envman
```

If you wish to **un-install** the `envman` program, simply run the included `uninstall.sh` script as follows:

```
$ cd envman
$ ./uninstall.sh
```

## Usage

* `envman create <name>` - Create and save a file called `<name>.env`, based on the `.env` file in the current directory
* `envman load <name>` -  Load the file `<name>.env` into the `.env` file in the current directory
* `envman show <name>` - Print out the contents of the file `<name>.env`

## Data Storage

By default, `envman` stores any saved `.env` files under the `~/envs` directory, where `~` refers to the current user's home directory.
