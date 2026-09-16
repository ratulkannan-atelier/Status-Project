# Uptime Monitor

## Decisions

### What counts as "up"?
1xx - Informational
2xx - Success
3xx - Redirection (a redirect means the server responded and is functioning, so it counts as up)
4xx - Client Error
5xx - Server Error
So my rule is that, Less than 400 is OK and More than 400 is not OK



### Timeout
5 seconds feels like a good middle ground. Not too short, since normal latency and connection delays need some buffer to avoid false negatives. Not too long either, since a slow response should still count as a problem.

### Failure types: no response vs. a bad response
Wrong URL - The program crashes
404 Error - The program runs as expected

### Timestamp: whose clock, and which timezone?
UTC is a standard, universal timezone, so it was used instead of local time. Target servers' times were never used at all, since different services could be in different timezones and that would break consistency across the history. Instead, the timestamp is recorded from my own machine's clock, converted to UTC, so it stays consistent no matter which machine or timezone runs the code.


### Storage (fill in during Step 3)
<!-- JSON file, append-only log, or SQLite — which, and why not the other two.
     What's the record shape? -->

### One process or two (fill in during Step 4)
<!-- Background thread inside the web app, or a separate process writing to shared
     storage the web app reads? Which did you pick, and why? -->

### Does history survive a restart? Should it? (fill in during Step 3/4)

### Why systemd rather than nohup or a cron job? (fill in during Step 7)

## Gotchas hit while building this
I was testing in a Jupyter Notebook (VS Code's Interactive Window), and it was running a different Python interpreter than my project's venv. Switching the notebook's interpreter to "3.14" wasn't enough on its own, since that matched the global Python 3.14 install, not the venv — a separate environment with its own installed packages. Running the script directly from the terminal with the venv's Python avoided the ambiguity entirely.