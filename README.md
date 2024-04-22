# RC Number DB Generator
Queries CAC API using RC Numbers to retrieve company information.

This works by running the shell script get_co_rc.sh and passing in 3 arguments
- The RC number at start of the range
- The RC number at the end of the range.
- The Number at which you want to increment your end range by.

  Example ./get_co_rc 100350 100400 100

  The above when run returns a csv file with entries for rc 100350 - rc 100400. After the initial execution subsequent files will contain 100 rc entries.

  
