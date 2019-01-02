import datetime 
def which_date(start_date,time):
    """
    This function takes as input a string depicting a date in YYYY/mm/dd
    format and a string stating a time period in the form of "X day(s)" or
    "Y week(s)". Output should be a string in form YYYY/mm/dd with the date
    that is X days or Y weeks after the initial date.
    """
    new_date = datetime.datetime.strptime(start_date, "%Y/%m/%d")
    if "day" in time :
        new_date = new_date+ datetime.timedelta(days = int(time.split(' ')[0]))
    if 'week' in time:
        new_date = new_date+ datetime.timedelta(weeks = int(time.split(' ')[0]))
    end_date = new_date.strftime("%Y/%m/%d")
    # Replace this with your code!
    
    return end_date
    
def test():
    """
    Here are a few tests to check if your code is working correctly! This
    function will be run when the Test Run button is selected. Additional
    tests that are not part of this function will also be run when the Submit
    Answer button is selected.
    """
    assert which_date('2016/02/10','35 days') == '2016/03/16'
    assert which_date('2016/12/21','3 weeks') == '2017/01/11'
    assert which_date('2015/01/17','1 week') == '2015/01/24'
    print("All tests completed.")


if __name__ == "__main__":
    test()
