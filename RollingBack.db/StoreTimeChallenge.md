# Store Time Challenge

The challenge is to store time information in the database so that the original time can be reconstructed. Whatever else you decide to store, you Must continue to store the UTC time = that's the only reliable way to store time so that they are all correct, relative to each other.

The extra column could be used to store either timezone information, or the original time's offset from UTC, or the tzinfo. It's up to you what you store.

Modify the code to store the correct information, then modify checkdb to retrieve the original time and display it along with the UTC time.

Remember to close any open tables and delete the database in the Project pane, before running your modified program for the first time.
