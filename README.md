# Beat Saber Map Utilities

These help solve the kinds of problems one may have while making Beat Saber maps.

Requires Python 3, and uses [`pipenv`](https://pipenv.readthedocs.io/en/latest/) for dependencies. Run `pipenv install` to install them.

* `build-package` - create a package zip using info.json (assumes git annotated tags)
* `copy-section` - copy a section of one file - such as `_bookmarks`, `_notes`, or `_obstacles` - to another
* `plot-note-rate` - plot notes per second of the given difficulty with a moving window 
* `pretty-print` - reformat the JSON files as pretty-printed for more readable diffs
  * The `pre-commit` git hook uses this to prevent committing changes to a map if its files are not pretty-printed.
