
import os
import os.path
import re

from api.lib.tmp_lib import generate_new_unnamed_tmp_file_name, generate_named_tmp_file


IP_ADDRESS_FILE_NAME = "prev-ipv4.txt"



def get_local_ipv4() -> str:
    tmp_file = generate_new_unnamed_tmp_file_name()
    os.system("hostname -I | awk '{ print $1 }' > " + tmp_file) # UNIX only.
    with open(tmp_file, "r") as f:
        address = f.read()
    os.remove(tmp_file)
    return re.sub(r'\n', '', address)


def get_updated_ipv4() -> str:
    """ Check if IPv4 has been updated. Returns None if no change.
    """
    tmp_file = generate_named_tmp_file(IP_ADDRESS_FILE_NAME)
    current_ipv4 = get_local_ipv4()

    if not os.path.exists(tmp_file):
        # No previous IP recorded.
        with open(tmp_file, "w") as f:
            f.write(current_ipv4)
        return current_ipv4

    else:
        # A previous IP was recorded.
        with open(tmp_file, "r") as f:
            previous_ipv4 = f.read()

        if previous_ipv4 == current_ipv4:
            return None
        else:
            with open(tmp_file, "w") as f:
                f.write(current_ipv4)
            return current_ipv4
