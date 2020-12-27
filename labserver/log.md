# SERVER

## troubleshooting

SYMPTOMS: in uwsgi log:
```
!!! UNABLE to load uWSGI plugin: ./python_plugin.so: cannot open shared object file: No such file or directory !!!
...
invalid request block size: 21573 (max 4096)...skip
```
CAUSE: first line eludes me. last line is due to running uwsgi without `--http` or equivalent; in this case, it is necessary to start a web server in front of uwsgi, like nginx.


## log

### 2020 12 25

having a symlink in / called lab means i can write links as `/lab/...` and this works with both the html server and in vim.

i think the ini file was out of date. pulling everything except for the name of the python file.

i think the installation got weird. `which uwsgi` doesn't seem to refer to the installation via apt. will have to pay closer attention next time i build up a machine.

### 2020 10 18

TOFIX: markdown server cannot handle cyrillic characters in the filename.

### 2020 10 17

refs
- [subprocess](https://docs.python.org/3/library/subprocess.html#module-subprocess)

working python/pandoc poc. much more could be done with subprocess at a later date.

working demo of triggering conversion from request.

I just realized I should definitely be using absolute paths for everything. That makes my scripts much more robust to changing locations of lab/ and the actual uwsgi app.


Having taken a walk and having some time to think about it...

- uwsgi app takes input, parses it, generates absolute path(s), and passes it(them) to the appropriate parser.
	- for example, md and text files are passed to panserv.
	- directories (ending in /) are passed to dirserv.
- panserv blindly accepts a target file and an output file as absolute paths and attempts the generation.
	- panserv also handles knowing whether or not to generate (static is newer, i.e.), NOT the app.
- dirserv blindly accepts a target directory and an output file as absolute paths and attempts the generation.
- both panserv and dirserv (and similar future scripts) will do basic sanity checking but no sanitization.

- also: in markdown files, absolute paths can be written as /lab/... apparently this resolves to domain.tld/lab/... but definitely check asap

[vim](/lab/notes/vim.md)


### 2020-09-06

references
- [nginx uwsgi](https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-ubuntu-14-04)

apt prereqs: `python3-dev python3-pip nginx uwsgi uwsgi-plugin-python`
pip3 prereqs: `uwsgi`

`$ uwsgi --plugin python,http --http 0.0.0.0:9090 --wsgi-file app.py`
other options:
- `--processes <n>`
- `--threads <n>`
- `--stats 127.0.0.1:<port>`
  - telnet to specified ip

i have a working poc, nginx passing to uwsgi serving a binary string. next
step: python/pandoc poc, research of indexing options


