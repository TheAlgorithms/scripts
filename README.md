# The Algorithms Scripts
  
Internal scripts used across all The Algorithms repositories

## build_directory_md.py
This script should be run by a workflow on every push and pr to update the `DIRECTORY.md` file. It takes the following arguments:
```
[0] - Language
[1] - Base path
[2] - Allowed filenames
[3] - Files or folders to ignore (optional)
[4] - Folders to ignore, but include children (optional)
```
For example, the command for the C++ repo would be:
```bash
python3 build_directory_md.py C-Plus-Plus . .cpp,.hpp,.h > DIRECTORY.md
```
Or more advanced, for the MATLAB / Octave repo:
```bash
python3 build_directory_md.py MATLAB-Octave . .m - algorithms > DIRECTORY.md
