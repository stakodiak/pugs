#!/usr/bin/python
"""Fetches scripts from script dir and adds them to path."""
import os
import textwrap

def main():
    cwd = os.getcwd()
    target_dir = "/usr/local/pugs"
    script_dir = "scripts"

    # create home (dog house?) for pugs scripts
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print("created target ({})".format(target_dir))

    # make sure pugs is in path
    if target_dir not in os.environ["PATH"]:
        path_script = """
        # pugs utilities
        export PATH=%s:$PATH
        """ % target_dir
        print("Warning:", target_dir, "not in path")
        print("Please add to bash config:")
        print(textwrap.dedent(path_script))

    # link to all pugs scripts
    script_names = os.listdir(script_dir)
    print("added:")
    for i, script_name in enumerate(script_names):
        link_name = script_name
        if link_name.startswith("."):
            continue
        suffixes = ["-command.py", ".py"]
        for suffix in suffixes:
            if link_name.endswith(suffix):
                link_name = link_name[:-1 * len(suffix)]
        source = os.path.join(cwd, script_dir, script_name)
        target = os.path.join(target_dir, link_name)
        print("'{}' -> {}".format(link_name, source))
        try:
            os.symlink(source, target)
            os.chmod(target, 0755)  # user can write, not user can r/x
        except OSError as e:
            if e.errno == 17:
                continue
            elif e.errno == 13:
                print("Can't write to {}!".format(target_dir))
                raise e
            else:  # pug down, pug down
                raise e


if __name__ == "__main__":
    main()
