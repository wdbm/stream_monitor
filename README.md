# stream_monitor

This program monitors a specified set of data streams (files) for changes. If a file is not changed in a specified time, an alert is sent using [scalar](https://github.com/wdbm/scalar).

# setup

```Bash
pip install stream_monitor
```

Set up scalar, as described [here](https://github.com/wdbm/scalar).

# configuration and usage

A JSON configuration file (by default `stream_monitor_configuration.json`) guides the program on the streams to monitor and their required update times. Its contents are of the following form:

```Python
{
    "streams": {
        "./recording.csv": {"update_time"}: 30
    }
}
```

In this example configuration, `recording.csv` is a filepath to monitor for changes and `30` is the time in seconds within which the filepath should change.

When the program `stream_monitor` is executed, it imports the configuration and runs in a continuous loop, sending an alert whenever it detects that a stream is not being updated in its expected update time. The script has options for the configuration filepath, alarms, checking interval and verbosity (see `stream_monitor --help`).
