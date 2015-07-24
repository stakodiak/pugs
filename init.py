#!/usr/bin/python
import os
import textwrap

def main():
    cwd = os.getcwd()
    target_dir = '/usr/local/pugs'
    script_dir = 'barks'

    # create home for pugs scripts
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print "created target (%s)" % target_dir

    # make sure pugs is in path
    if target_dir not in os.environ['PATH']:
        path_script = """
        # pugs utilities
        export PATH=%s:$PATH
        """ % target_dir
        print "Warning:", target_dir, "not in path"
        print "Please add to bash config:"
        print textwrap.dedent(path_script)


    # link to all pugs scripts
    script_names = os.listdir(script_dir)
    print "Adding", len(script_names), "pugs."
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
            elif e.errno == 13:
                print "Can't write to %s!" % target_dir
                raise e
            else:  # pug down, pug down
                raise e

if __name__ == '__main__':
    main()
