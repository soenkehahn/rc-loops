# rc-loops

This is a for fun project where RCers can explore audio programming using [`looper`](https://github.com/soenkehahn/looper). `looper` is a tool that'll play back short (or longer) audio snippets in a loop. The little snippets are going to be created by scripts in this repo that we can write together.

## feedback

I'd appreciate any feedback for this readme, this repo or `looper`. So please, if you have any comments, questions or suggestions, get in touch. Either on zulip or by email (soenkehahn@gmail.com). Or you can open issues on the [issue tracker for this repo](https://github.com/soenkehahn/rc-loops/issues) or on the [issue tracker for `looper`](https://github.com/soenkehahn/looper/issues).

## how it works

### install `looper`

First you need to install `looper`. There's installation instructions here: https://github.com/soenkehahn/looper#installation

### running looper

Now you can run looper on `run.sh`:

```bash
looper run.sh
```

This should produce some audio output. I've added two example files (`sine.py` and `noise.js`) as inspiration. For the two example files you need python and node.

You can also listen to the files separately by doing `looper sine.py` or `looper noise.js`.

You can render the output into a wav file with:

```bash
looper run.sh --render output.wav
```

### what's happening

`looper` will run the given executable and read the output that it produces into a sound buffer. It will then play that sound buffer in a loop. It will also watch the executable for changes. When the executable file changes it'll rerun it, again read its output into a sound buffer and start playing that new sound buffer instead of the old one.

This allows a workflow where you can make changes to the sound generating scripts, save them and then just wait for `looper` to pick up the changes and play the new loop. That way you get a fast feedback cycle on your changes.

You can also specify additional files for `looper` to watch, for example:

```bash
looper run.sh --watch sine.py --watch noise.js
```

### contributing changes

Feel free to modify the example files, or add new files to `run.sh`. And submit those changes through github PRs.

And be careful about the sound volume when editing the audio scripts! It's easily possible to generate very loud noises that can be painful to listen to.
