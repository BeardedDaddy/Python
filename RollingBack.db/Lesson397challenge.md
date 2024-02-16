# Store time information in the database so that the original time can be reconstructed. You must continue to store the UTC time - that's the only reliable way to store time so that they are all correct, relative to each other

Read the documentation in SQLite to determine how to store time.

## Modify the rollback program so that it includes an extra column in the database. The extra column could be used to store either timezone information, or the original time's offset from UTC, or the tzinfo. It's up to you what you store

Find out how to add a column to the database.
Store the local time as a string.

### Modify the code store the correct information, then modify checkdb to retrieve the original time and display it along with the UTC time
