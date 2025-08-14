
[     UTC     ] Logs for smart-pricing-app-6erzgsffm37bawk8z7btud.streamlit.app/
────────────────────────────────────────────────────────────────────────────────────────
[10:02:02] 🚀 Starting up repository: 'smart-pricing-app', branch: 'main', main module: 'app.py'
[10:02:02] 🐙 Cloning repository...
[10:02:03] 🐙 Cloning into '/mount/src/smart-pricing-app'...
[10:02:03] 🐙 Cloned repository!
[10:02:03] 🐙 Pulling code changes from Github...
[10:02:03] 📦 Processing dependencies...
Check if streamlit is installed
cat: /mount/admin/install_path: No such file or directory
──────────────────────────────── Installing Streamlit ──────────────────────────────────
Using uv pip install.
Using Python 3.13.5 environment at /home/adminuser/venv[2025-08-14 10:02:04.213686] 
Resolved 37 packages in 564ms
Prepared [2025-08-14 10:02:07.117691] 37 packages[2025-08-14 10:02:07.117927]  [2025-08-14 10:02:07.122146] in 2.33s[2025-08-14 10:02:07.122372] 
Installed 37 packages in 97ms
 + altair==5.5.0
 + attrs==25.3.0
 + blinker==1.9.0
 + cachetools==6.1.0
 + certifi==2025.8.3
 + charset-normalizer==3.4.3
 + click==8.2.1
 + gitdb==4.0.12
 + gitpython==3.1.45
 + idna==3.10
 + jinja2==3.1.6
 + jsonschema==4.25.0
 + jsonschema-specifications==2025.4.1
 + markupsafe==3.0.2
 + narwhals==2.1.1
 + numpy==2.3.2
 + packaging==25.0
 + pandas==2.3.1
 + pillow==11.3.0
 + protobuf==6.31.1
 + pyarrow==21.0.0
 + pydeck==0.9.1
 + python-dateutil==2.9.0.post0
 + pytz==2025.2
 + referencing==0.36.2
 + requests==2.32.4
 + rpds-py==0.27.0[2025-08-14 10:02:07.216940] 
 + six==1.17.0
 + smmap==5.0.2
 + streamlit==1.48.1
 + tenacity==9.1.2
 + toml==0.10.2
 + tornado==6.5.2
 + typing-extensions==4.14.1
 + tzdata==2025.2
 + urllib3==2.5.0
 + watchdog==6.0.0
────────────────────────────────────────────────────────────────────────────────────────
[10:02:08] 📦 Processed dependencies!
cat: /mount/admin/install_path: No such file or directory
2025-08-14 10:02:16.547 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:02:18.632 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
[10:05:06] 🐙 Pulling code changes from Github...
[10:05:07] 📦 Processing dependencies...
[10:05:07] 📦 Processed dependencies!
[10:05:08] 🔄 Updated app!
2025-08-14 10:06:00.974 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:06:01.061 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:03.163 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:03.169 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:03.436 503 GET /script-health-check (127.0.0.1) 273.22ms
[10:07:03] ❗️ 
2025-08-14 10:07:08.213 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:08.226 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:08.508 503 GET /script-health-check (127.0.0.1) 295.79ms
2025-08-14 10:07:13.140 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:13.146 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:13.418 503 GET /script-health-check (127.0.0.1) 278.04ms
2025-08-14 10:07:18.183 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:18.188 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:18.496 503 GET /script-health-check (127.0.0.1) 313.66ms
2025-08-14 10:07:23.197 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:23.203 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:23.488 503 GET /script-health-check (127.0.0.1) 291.50ms
2025-08-14 10:07:28.192 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:28.199 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:28.494 503 GET /script-health-check (127.0.0.1) 302.64ms
2025-08-14 10:07:33.154 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:33.161 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:33.426 503 GET /script-health-check (127.0.0.1) 272.99ms
2025-08-14 10:07:38.195 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:38.201 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:38.504 503 GET /script-health-check (127.0.0.1) 309.64ms
2025-08-14 10:07:43.152 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:43.158 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:43.428 503 GET /script-health-check (127.0.0.1) 276.61ms
2025-08-14 10:07:48.230 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:48.236 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:48.519 503 GET /script-health-check (127.0.0.1) 289.04ms
2025-08-14 10:07:53.176 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:53.184 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:53.480 503 GET /script-health-check (127.0.0.1) 305.11ms
2025-08-14 10:07:58.155 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:07:58.160 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:07:58.388 503 GET /script-health-check (127.0.0.1) 233.57ms
2025-08-14 10:08:03.189 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:03.196 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:03.436 503 GET /script-health-check (127.0.0.1) 247.00ms
2025-08-14 10:08:08.157 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:08.162 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:08.395 503 GET /script-health-check (127.0.0.1) 238.86ms
2025-08-14 10:08:13.164 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:13.171 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:13.435 503 GET /script-health-check (127.0.0.1) 271.16ms
2025-08-14 10:08:18.162 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:18.168 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:18.468 503 GET /script-health-check (127.0.0.1) 305.73ms
2025-08-14 10:08:23.188 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:23.194 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:23.490 503 GET /script-health-check (127.0.0.1) 302.32ms
2025-08-14 10:08:28.145 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:28.151 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:28.387 503 GET /script-health-check (127.0.0.1) 242.67ms
2025-08-14 10:08:33.161 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:33.167 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:33.441 503 GET /script-health-check (127.0.0.1) 280.54ms
2025-08-14 10:08:38.164 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:38.171 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:38.427 503 GET /script-health-check (127.0.0.1) 263.91ms
2025-08-14 10:08:43.188 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:43.194 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:43.460 503 GET /script-health-check (127.0.0.1) 273.27ms
2025-08-14 10:08:48.153 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:48.158 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:48.440 503 GET /script-health-check (127.0.0.1) 287.42ms
2025-08-14 10:08:53.185 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:53.192 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:53.492 503 GET /script-health-check (127.0.0.1) 307.58ms
2025-08-14 10:08:58.187 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:08:58.194 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:08:58.443 503 GET /script-health-check (127.0.0.1) 256.53ms
2025-08-14 10:09:03.193 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:03.199 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:03.502 503 GET /script-health-check (127.0.0.1) 309.72ms
2025-08-14 10:09:08.184 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:08.190 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:08.499 503 GET /script-health-check (127.0.0.1) 315.83ms
2025-08-14 10:09:13.170 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:13.177 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:13.442 503 GET /script-health-check (127.0.0.1) 272.34ms
2025-08-14 10:09:18.162 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:18.168 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:18.464 503 GET /script-health-check (127.0.0.1) 303.26ms
2025-08-14 10:09:23.175 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:23.182 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:23.448 503 GET /script-health-check (127.0.0.1) 274.07ms
2025-08-14 10:09:28.179 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:28.185 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:28.490 503 GET /script-health-check (127.0.0.1) 311.29ms
2025-08-14 10:09:33.179 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:33.185 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:33.488 503 GET /script-health-check (127.0.0.1) 309.16ms
2025-08-14 10:09:38.203 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:38.209 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:38.504 503 GET /script-health-check (127.0.0.1) 300.64ms
2025-08-14 10:09:43.156 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:43.161 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:43.428 503 GET /script-health-check (127.0.0.1) 273.04ms
2025-08-14 10:09:48.171 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:48.178 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:48.412 503 GET /script-health-check (127.0.0.1) 240.78ms
2025-08-14 10:09:53.175 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:53.180 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:53.447 503 GET /script-health-check (127.0.0.1) 273.05ms
2025-08-14 10:09:58.177 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:09:58.184 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:09:58.463 503 GET /script-health-check (127.0.0.1) 286.19ms
2025-08-14 10:10:03.226 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:03.233 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:03.588 503 GET /script-health-check (127.0.0.1) 363.18ms
2025-08-14 10:10:08.180 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:08.186 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:08.482 503 GET /script-health-check (127.0.0.1) 302.41ms
2025-08-14 10:10:13.162 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:13.168 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:13.410 503 GET /script-health-check (127.0.0.1) 248.48ms
2025-08-14 10:10:18.167 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:18.172 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:18.418 503 GET /script-health-check (127.0.0.1) 251.17ms
2025-08-14 10:10:23.150 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:23.157 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:23.450 503 GET /script-health-check (127.0.0.1) 300.17ms
2025-08-14 10:10:28.170 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:28.176 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:28.415 503 GET /script-health-check (127.0.0.1) 245.04ms
2025-08-14 10:10:33.167 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:33.173 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:33.440 503 GET /script-health-check (127.0.0.1) 274.15ms
2025-08-14 10:10:38.161 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:38.168 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:38.407 503 GET /script-health-check (127.0.0.1) 246.61ms
2025-08-14 10:10:43.170 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:43.176 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:43.500 503 GET /script-health-check (127.0.0.1) 330.16ms
2025-08-14 10:10:48.154 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:48.160 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:48.389 503 GET /script-health-check (127.0.0.1) 235.63ms
2025-08-14 10:10:53.187 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:53.193 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:53.457 503 GET /script-health-check (127.0.0.1) 270.64ms
2025-08-14 10:10:58.182 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:10:58.188 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:10:58.455 503 GET /script-health-check (127.0.0.1) 272.80ms
2025-08-14 10:11:03.189 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:03.195 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:03.481 503 GET /script-health-check (127.0.0.1) 292.67ms
2025-08-14 10:11:08.167 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:08.172 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:08.417 503 GET /script-health-check (127.0.0.1) 250.47ms
2025-08-14 10:11:13.187 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:13.193 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:13.454 503 GET /script-health-check (127.0.0.1) 267.92ms
2025-08-14 10:11:18.189 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:18.195 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:18.472 503 GET /script-health-check (127.0.0.1) 283.30ms
2025-08-14 10:11:23.150 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:23.157 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:23.422 503 GET /script-health-check (127.0.0.1) 272.22ms
2025-08-14 10:11:28.172 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:28.178 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:28.484 503 GET /script-health-check (127.0.0.1) 313.02ms
2025-08-14 10:11:33.149 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:33.155 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:33.432 503 GET /script-health-check (127.0.0.1) 283.98ms
2025-08-14 10:11:38.166 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:38.172 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:38.468 503 GET /script-health-check (127.0.0.1) 302.18ms
2025-08-14 10:11:43.182 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:43.189 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:43.452 503 GET /script-health-check (127.0.0.1) 270.30ms
2025-08-14 10:11:48.170 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:48.176 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:48.471 503 GET /script-health-check (127.0.0.1) 302.00ms
2025-08-14 10:11:53.193 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:53.199 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:53.501 503 GET /script-health-check (127.0.0.1) 308.63ms
2025-08-14 10:11:58.165 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:11:58.171 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:11:58.412 503 GET /script-health-check (127.0.0.1) 247.77ms
2025-08-14 10:12:03.187 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:03.196 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:03.477 503 GET /script-health-check (127.0.0.1) 290.47ms
2025-08-14 10:12:08.172 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:08.178 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:08.471 503 GET /script-health-check (127.0.0.1) 299.50ms
2025-08-14 10:12:13.187 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:13.194 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:13.505 503 GET /script-health-check (127.0.0.1) 319.20ms
2025-08-14 10:12:18.146 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:18.153 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:18.439 503 GET /script-health-check (127.0.0.1) 293.64ms
2025-08-14 10:12:23.194 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:23.199 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:23.437 503 GET /script-health-check (127.0.0.1) 243.52ms
2025-08-14 10:12:28.235 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:28.243 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:28.577 503 GET /script-health-check (127.0.0.1) 342.37ms
2025-08-14 10:12:33.185 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:33.191 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:33.464 503 GET /script-health-check (127.0.0.1) 280.02ms
2025-08-14 10:12:38.192 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:38.197 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:38.473 503 GET /script-health-check (127.0.0.1) 281.60ms
2025-08-14 10:12:43.164 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:43.170 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:43.467 503 GET /script-health-check (127.0.0.1) 303.40ms
2025-08-14 10:12:48.170 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:48.177 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:48.425 503 GET /script-health-check (127.0.0.1) 255.21ms
2025-08-14 10:12:53.185 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:53.192 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:53.464 503 GET /script-health-check (127.0.0.1) 279.66ms
2025-08-14 10:12:58.181 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:12:58.187 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:12:58.469 503 GET /script-health-check (127.0.0.1) 288.87ms
2025-08-14 10:13:03.192 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:03.199 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:03.470 503 GET /script-health-check (127.0.0.1) 278.88ms
2025-08-14 10:13:08.202 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:08.207 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:08.475 503 GET /script-health-check (127.0.0.1) 273.41ms
2025-08-14 10:13:13.167 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:13.173 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:13.471 503 GET /script-health-check (127.0.0.1) 303.72ms
2025-08-14 10:13:18.175 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:18.182 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:18.468 503 GET /script-health-check (127.0.0.1) 292.67ms
2025-08-14 10:13:23.165 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:23.171 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:23.450 503 GET /script-health-check (127.0.0.1) 284.70ms
2025-08-14 10:13:28.167 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:28.173 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:28.435 503 GET /script-health-check (127.0.0.1) 268.53ms
2025-08-14 10:13:33.194 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:33.200 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:33.441 503 GET /script-health-check (127.0.0.1) 247.85ms
2025-08-14 10:13:38.157 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:38.163 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:38.406 503 GET /script-health-check (127.0.0.1) 249.74ms
2025-08-14 10:13:43.172 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:43.179 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:43.479 503 GET /script-health-check (127.0.0.1) 307.19ms
2025-08-14 10:13:48.251 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:48.260 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:48.579 503 GET /script-health-check (127.0.0.1) 329.18ms
2025-08-14 10:13:53.227 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:53.233 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:53.522 503 GET /script-health-check (127.0.0.1) 295.46ms
2025-08-14 10:13:58.164 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:13:58.170 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:13:58.449 503 GET /script-health-check (127.0.0.1) 285.86ms
2025-08-14 10:14:03.199 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:14:03.204 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:14:03.445 503 GET /script-health-check (127.0.0.1) 247.29ms
2025-08-14 10:14:08.160 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:14:08.166 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:14:08.448 503 GET /script-health-check (127.0.0.1) 289.30ms
2025-08-14 10:14:13.179 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:14:13.184 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:14:13.482 503 GET /script-health-check (127.0.0.1) 303.76ms
2025-08-14 10:14:18.159 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:14:18.165 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:14:18.446 503 GET /script-health-check (127.0.0.1) 288.25ms
2025-08-14 10:14:23.174 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:14:23.180 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:14:23.462 503 GET /script-health-check (127.0.0.1) 288.69ms
2025-08-14 10:14:28.181 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:14:28.189 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:14:28.447 503 GET /script-health-check (127.0.0.1) 266.18ms
2025-08-14 10:14:33.236 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:14:33.244 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 23, in <module>
    calendar = load_calendar()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 227, in __call__
    return self._get_or_create_cached_value(args, kwargs, spinner_message)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 269, in _get_or_create_cached_value
    return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 328, in _handle_cache_miss
    computed_value = self._info.func(*func_args, **func_kwargs)
  File "/mount/src/smart-pricing-app/app.py", line 22, in load_calendar
    return pd.read_csv("occasion_calendar.csv")
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ~~~~~~~~~~^
        f,
        ^^
    ...<6 lines>...
        storage_options=self.options.get("storage_options", None),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
        handle,
    ...<3 lines>...
        newline="",
    )
FileNotFoundError: [Errno 2] No such file or directory: 'occasion_calendar.csv'
2025-08-14 10:14:33.521 503 GET /script-health-check (127.0.0.1) 284.99ms
[10:14:36] 🐙 Pulling code changes from Github...
[10:14:36] 📦 Processing dependencies...
[10:14:36] 📦 Processed dependencies!
2025-08-14 10:14:38.166 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
[10:14:38] 🔄 Updated app!
2025-08-14 10:14:43.211 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:17:03.159 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:19:42.892 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 185, in __init__
    self._add_dir_watch(path, event_mask, recursive=recursive)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 404, in _add_dir_watch
    self._add_watch(path, mask)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 424, in _add_watch
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 435, in _raise_error
    raise OSError(errno.ENOSPC, "inotify watch limit reached")
OSError: [Errno 28] inotify watch limit reached
2025-08-14 10:22:03.161 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 185, in __init__
    self._add_dir_watch(path, event_mask, recursive=recursive)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 404, in _add_dir_watch
    self._add_watch(path, mask)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 424, in _add_watch
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 435, in _raise_error
    raise OSError(errno.ENOSPC, "inotify watch limit reached")
OSError: [Errno 28] inotify watch limit reached
2025-08-14 10:23:21.220 The `use_column_width` parameter has been deprecated and will be removed in a future release. Please utilize the `use_container_width` parameter instead.
[10:24:30] 🐙 Pulling code changes from Github...
[10:24:30] 📦 Processing dependencies...
[10:24:30] 📦 Processed dependencies!
[10:24:34] 🔄 Updated app!
2025-08-14 10:25:39.609 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:27:03.170 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:30:08.863 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:30:45.046 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:32:03.185 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:32:17.333 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:36:01.539 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:37:03.157 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
[10:39:44] 🐙 Pulling code changes from Github...
[10:39:44] 📦 Processing dependencies...
[10:39:44] 📦 Processed dependencies!
[10:39:46] 🔄 Updated app!
2025-08-14 10:39:58.355 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:39:58.429 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 20, in <module>
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 377, in __call__
    return self._decorator(
           ~~~~~~~~~~~~~~~^
        func,
        ^^^^^
    ...<6 lines>...
        hash_funcs=hash_funcs,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/metrics_util.py", line 443, in wrapped_func
    result = non_optional_func(*args, **kwargs)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 612, in _decorator
    return make_cached_func_wrapper(
        CachedDataFuncInfo(
    ...<7 lines>...
        )
    )
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 169, in make_cached_func_wrapper
    cached_func = CachedFunc(info)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 202, in __init__
    self._function_key = _make_function_key(info.cache_type, info.func)
                         ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 508, in _make_function_key
    source_code = inspect.getsource(func)
  File "/usr/local/lib/python3.13/inspect.py", line 1258, in getsource
    lines, lnum = getsourcelines(object)
                  ~~~~~~~~~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1250, in getsourcelines
    return getblock(lines[lnum:]), lnum + 1
           ~~~~~~~~^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1217, in getblock
    for _token in tokens:
                  ^^^^^^
  File "/usr/local/lib/python3.13/tokenize.py", line 588, in _generate_tokens_from_c_tokenizer
    raise TokenError(msg, (e.lineno, e.offset)) from None
tokenize.TokenError: ('EOF in multi-line string', (71, 1))
2025-08-14 10:42:03.197 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:42:03.203 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 20, in <module>
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 377, in __call__
    return self._decorator(
           ~~~~~~~~~~~~~~~^
        func,
        ^^^^^
    ...<6 lines>...
        hash_funcs=hash_funcs,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/metrics_util.py", line 443, in wrapped_func
    result = non_optional_func(*args, **kwargs)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 612, in _decorator
    return make_cached_func_wrapper(
        CachedDataFuncInfo(
    ...<7 lines>...
        )
    )
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 169, in make_cached_func_wrapper
    cached_func = CachedFunc(info)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 202, in __init__
    self._function_key = _make_function_key(info.cache_type, info.func)
                         ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 508, in _make_function_key
    source_code = inspect.getsource(func)
  File "/usr/local/lib/python3.13/inspect.py", line 1258, in getsource
    lines, lnum = getsourcelines(object)
                  ~~~~~~~~~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1250, in getsourcelines
    return getblock(lines[lnum:]), lnum + 1
           ~~~~~~~~^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1217, in getblock
    for _token in tokens:
                  ^^^^^^
  File "/usr/local/lib/python3.13/tokenize.py", line 588, in _generate_tokens_from_c_tokenizer
    raise TokenError(msg, (e.lineno, e.offset)) from None
tokenize.TokenError: ('EOF in multi-line string', (71, 1))
[10:42:03] ❗️ 
2025-08-14 10:42:03.477 503 GET /script-health-check (127.0.0.1) 281.48ms
2025-08-14 10:42:08.210 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:42:08.216 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 20, in <module>
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 377, in __call__
    return self._decorator(
           ~~~~~~~~~~~~~~~^
        func,
        ^^^^^
    ...<6 lines>...
        hash_funcs=hash_funcs,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/metrics_util.py", line 443, in wrapped_func
    result = non_optional_func(*args, **kwargs)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 612, in _decorator
    return make_cached_func_wrapper(
        CachedDataFuncInfo(
    ...<7 lines>...
        )
    )
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 169, in make_cached_func_wrapper
    cached_func = CachedFunc(info)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 202, in __init__
    self._function_key = _make_function_key(info.cache_type, info.func)
                         ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 508, in _make_function_key
    source_code = inspect.getsource(func)
  File "/usr/local/lib/python3.13/inspect.py", line 1258, in getsource
    lines, lnum = getsourcelines(object)
                  ~~~~~~~~~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1250, in getsourcelines
    return getblock(lines[lnum:]), lnum + 1
           ~~~~~~~~^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1217, in getblock
    for _token in tokens:
                  ^^^^^^
  File "/usr/local/lib/python3.13/tokenize.py", line 588, in _generate_tokens_from_c_tokenizer
    raise TokenError(msg, (e.lineno, e.offset)) from None
tokenize.TokenError: ('EOF in multi-line string', (71, 1))
2025-08-14 10:42:08.469 503 GET /script-health-check (127.0.0.1) 260.04ms
2025-08-14 10:42:13.223 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:42:13.230 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 20, in <module>
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 377, in __call__
    return self._decorator(
           ~~~~~~~~~~~~~~~^
        func,
        ^^^^^
    ...<6 lines>...
        hash_funcs=hash_funcs,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/metrics_util.py", line 443, in wrapped_func
    result = non_optional_func(*args, **kwargs)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 612, in _decorator
    return make_cached_func_wrapper(
        CachedDataFuncInfo(
    ...<7 lines>...
        )
    )
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 169, in make_cached_func_wrapper
    cached_func = CachedFunc(info)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 202, in __init__
    self._function_key = _make_function_key(info.cache_type, info.func)
                         ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 508, in _make_function_key
    source_code = inspect.getsource(func)
  File "/usr/local/lib/python3.13/inspect.py", line 1258, in getsource
    lines, lnum = getsourcelines(object)
                  ~~~~~~~~~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1250, in getsourcelines
    return getblock(lines[lnum:]), lnum + 1
           ~~~~~~~~^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1217, in getblock
    for _token in tokens:
                  ^^^^^^
  File "/usr/local/lib/python3.13/tokenize.py", line 588, in _generate_tokens_from_c_tokenizer
    raise TokenError(msg, (e.lineno, e.offset)) from None
tokenize.TokenError: ('EOF in multi-line string', (71, 1))
2025-08-14 10:42:13.528 503 GET /script-health-check (127.0.0.1) 305.67ms
2025-08-14 10:42:18.208 Failed to schedule watch observer for path /mount/src/smart-pricing-app
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/watcher/event_based_path_watcher.py", line 186, in watch_path
    folder_handler.watch = self._observer.schedule(
                           ~~~~~~~~~~~~~~~~~~~~~~~^
        folder_handler, folder_path, recursive=True
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/api.py", line 312, in schedule
    emitter.start()
    ~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/utils/__init__.py", line 75, in start
    self.on_thread_start()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start
    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)
                    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__
    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)
                    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 149, in __init__
    Inotify._raise_error()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/watchdog/observers/inotify_c.py", line 438, in _raise_error
    raise OSError(errno.EMFILE, "inotify instance limit reached")
OSError: [Errno 24] inotify instance limit reached
2025-08-14 10:42:18.214 Uncaught app execution
Traceback (most recent call last):
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mount/src/smart-pricing-app/app.py", line 20, in <module>
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 377, in __call__
    return self._decorator(
           ~~~~~~~~~~~~~~~^
        func,
        ^^^^^
    ...<6 lines>...
        hash_funcs=hash_funcs,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/metrics_util.py", line 443, in wrapped_func
    result = non_optional_func(*args, **kwargs)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_data_api.py", line 612, in _decorator
    return make_cached_func_wrapper(
        CachedDataFuncInfo(
    ...<7 lines>...
        )
    )
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 169, in make_cached_func_wrapper
    cached_func = CachedFunc(info)
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 202, in __init__
    self._function_key = _make_function_key(info.cache_type, info.func)
                         ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/cache_utils.py", line 508, in _make_function_key
    source_code = inspect.getsource(func)
  File "/usr/local/lib/python3.13/inspect.py", line 1258, in getsource
    lines, lnum = getsourcelines(object)
                  ~~~~~~~~~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1250, in getsourcelines
    return getblock(lines[lnum:]), lnum + 1
           ~~~~~~~~^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/inspect.py", line 1217, in getblock
    for _token in tokens:
                  ^^^^^^
  File "/usr/local/lib/python3.13/tokenize.py", line 588, in _generate_tokens_from_c_tokenizer
    raise TokenError(msg, (e.lineno, e.offset)) from None
tokenize.TokenError: ('EOF in multi-line string', (71, 1))
2025-08-14 10:42:18.477 503 GET /script-health-check (127.0.0.1) 268.89ms
main
elliebell857/smart-pricing-app/main/app.py


