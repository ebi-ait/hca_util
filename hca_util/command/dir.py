from hca_util.local_state import get_local_state, set_local_state, LocalState


class CmdDir:
    """
    user: both wrangler and contributor
    aws resource or client used in command - none, all local operations.
    """

    @staticmethod
    def run():
        local_state = get_local_state()
        return True, str(local_state)

    @staticmethod
    def clear(a):
        if a:  # clear all
            local_state = LocalState()  # create a new empty local state obj
            set_local_state(local_state)
            return True, 'All cleared'
        else:
            local_state = get_local_state()
            local_state.unselect_dir()
            set_local_state(local_state)
            return True, 'Selection cleared'
