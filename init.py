#!/usr/bin/python
import os

def main():
    cwd = os.getcwd()
    target_dir = '/usr/local/pugs'
    script_dir = 'bin'

    # create home for pugs scripts
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print "created target (%s)" % target_dir

    # make sure pugs is in path
    if target_dir not in os.environ['PATH']:
        path_script = """
        # pugs utilities
        export PATH=%s:$PATH
        """.rstrip() % target_dir
        print "warning:", target_dir, "not in path"

        # add it to bash config?
        bash_config = os.path.expanduser('~/.bash_profile')
        if os.path.exists(bash_config):
            choice = raw_input("add it to %s? [y/n] " % bash_config)
            if choice.lower() in ['y', 'yes', 'yeah', 'mhm', 'ruff ruff']:
                with open(bash_config, 'a') as bash_profile:
                    bash_profile.write(path_script)
                os.popen('. %s' % bash_config)

    # link to all pugs scripts
    script_names = os.listdir(script_dir)
    print "adding", len(script_names), "pugs"
    for i, script_name in enumerate(script_names):
        link_name = script_name.rstrip('.py')
        source = os.path.join(cwd, script_dir, script_name)
        target = os.path.join(target_dir, link_name)
        print i + 1, '-', link_name,
        try:
            os.symlink(source, target)
            os.chmod(target, 0755)  # user can write, not user can r/x
            print "(added)"
        except OSError as e:
            if e.errno == 17:
                print "(exists)"
            else:  # pug down, pug down
                raise e

if __name__ == '__main__':
    main()
