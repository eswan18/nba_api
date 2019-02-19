def event_mgs_desc(row):
    if row['EVENTMSGDESC'] == 1:
        val = 'FIELD_GOAL_MADE'
    elif row['EVENTMSGDESC'] == 2:
        val = 'FIELD_GOAL_MISSED'
    elif row['EVENTMSGDESC'] == 3:
        val = 'FREE_THROWfree_throw_attempt'
    elif row['EVENTMSGDESC'] == 4:
        val = 'REBOUND'
    elif row['EVENTMSGDESC'] == 5:
        val = 'TURNOVER'
    elif row['EVENTMSGDESC'] == 6:
        val = 'FOUL'
    elif row['EVENTMSGDESC'] == 7:
        val = 'VIOLATION'
    elif row['EVENTMSGDESC'] == 8:
        val = 'SUBSTITUTION'
    elif row['EVENTMSGDESC'] == 9:
        val = 'TIMEOUT'
    elif row['EVENTMSGDESC'] == 10:
        val = 'JUMP_BALL'
    elif row['EVENTMSGDESC'] == 11:
        val = 'EJECTION'
    elif row['EVENTMSGDESC'] == 12:
        val = 'PERIOD_BEGIN'
    elif row['EVENTMSGDESC'] == 13:
        val = 'PERIOD_END'
    return(val)