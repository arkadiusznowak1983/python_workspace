import shutil

from algorithm.print_as_log_writter import print
from pathlib import Path

class CopyNonRedundandFile:
    def copy(self, existing_path, new_path, destination_path):
        # calculate existing files hashes
        hashmap = {}
        for path in list(Path(existing_path).rglob("*")):
            hashmap[hash("{}.{}".format( path.stat().st_mtime, path.stat().st_mtime ))] = path.name

        # copy new files
        for path in list(Path(new_path).rglob("*")):
            if path.is_file() and hashmap.get(hash("{}.{}".format( path.stat().st_mtime, path.stat().st_mtime ))) is None:
                newPath = Path(shutil.copy(path.absolute(), destination_path))
                hashmap[hash("{}.{}".format(newPath.stat().st_mtime, newPath.stat().st_mtime))] = newPath.name
        return True
