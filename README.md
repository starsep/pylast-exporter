# pylast-exporter
This script allows to export all scrobbles from Last.fm using [pylast](https://github.com/pylast/pylast/) library.
You need Last.fm API key to use it.
Visit https://www.last.fm/api/account/create to create a new one.
List of api keys: https://www.last.fm/api/accounts

# Config
To configure script use environment variables
- PYLAST_EXPORTER_API_KEY
- PYLAST_EXPORTER_API_SECRET
- PYLAST_EXPORTER_USERNAME

Output will be printed on standard output

# Example usage with Docker
```
docker build -t pylast-exporter .
docker run \
    --env PYLAST_EXPORTER_API_KEY=$PYLAST_EXPORTER_API_KEY \
    --env PYLAST_EXPORTER_API_SECRET=$PYLAST_EXPORTER_API_SECRET \
    --env PYLAST_EXPORTER_USERNAME=$PYLAST_EXPORTER_USERNAME \
    pylast-exporter
```
