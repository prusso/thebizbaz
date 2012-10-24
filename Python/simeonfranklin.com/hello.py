from datetime import datetime

hour = datetime.now().hour

if hour > 23:
    time_of_day = 'midnight'
elif hour > 16:
    time_of_day = 'evening'
elif hour > 11:
    time_of_day = 'afternoon'
else:
    time_of_day = 'morning'
    
print 'Good %s, world!' % time_of_day
