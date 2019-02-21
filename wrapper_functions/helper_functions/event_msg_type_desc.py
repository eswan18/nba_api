def event_msg_type_desc(col):
    if col == 1:
        return 'FIELD_GOAL_MADE'
    elif col == 2:
        return 'FIELD_GOAL_MISSED'
    elif col == 3:
        return 'FREE_THROW_ATTEMPT'
    elif col == 4:
        return 'REBOUND'
    elif col == 5:
        return 'TURNOVER'
    elif col == 6:
        return 'FOUL'
    elif col == 7:
        return 'VIOLATION'
    elif col == 8:
        return 'SUBSTITUTION'
    elif col == 9:
        return 'TIMEOUT'
    elif col == 10:
        return 'JUMP_BALL'
    elif col == 11:
        return 'EJECTION'
    elif col == 12:
        return 'PERIOD_BEGIN'
    elif col == 13:
        return 'PERIOD_END'
    else:
        return None