# djangocms delete example project

## Requirements

You will need `docker-compose` to run this example project.

## main commands

To get this project up and running, run

`make`

from the project root.

To start the dev server, run 

`make migrate`

`make superuser`

`make runserver` --> will start the server at `localhost:8000`


## Reproduce problem:

1. Open a browser window at `localhost:8000` and log in.
2. Add an 'Artikel' from the toolbar via 'Artikel hinzufügen...'
3. Try to delete that 'Artikel' via the toolbar: 'Artikel' --> 'Artikel...' --> select instance to delete --> confirm delete.

The modal should go blank, and in the Javascript console, you'll find

```
bundle.toolbar.min.js:1 Uncaught TypeError: e.match is not a function
    at HTMLAnchorElement.<anonymous> (bundle.toolbar.min.js:1)
    at HTMLAnchorElement.dispatch (bundle.toolbar.min.js:1)
    at HTMLAnchorElement.g.handle (bundle.toolbar.min.js:1)

```
