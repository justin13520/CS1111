import re
import urllib.request
#Justin Liu, jl8wf

def name_to_url(name):
    """
    name_to_url function is to make a given name into a form that can be appended
    on to the end of a url that is findable.
    :param name: String that is a name for an employee of UVA
    :return: string in the form of first middle last name with a '-' between them
    """
    s = '-'
    lst = name.lower().split()
    for i in range(len(lst)):
        #gets rid of the period
        if '.' in lst[i]:
            lst[i] = lst[i].strip('.')
        #reorganizes the name if last name first by making it into a list,
        #then switching around the order by appending and removing
        if ',' in lst[i]:
            lst[i] = lst[i].strip(',')
            lst.append(lst[i])
            lst.remove(lst[i])
    #lst to string
    name = s.join(lst)
    return name

def report(name):
    """
    The report function accesses a url and finds the job, money earned, ad rank of an
    UVA employee. This is done by using regex that match their position in the html file.
    The results can then be altered to be more readable by using the replace function.
    If the URL does not exist, job is None and rank and money are 0.
    :param name: Name of Employee
    :return: job, money earned, and rank in UVA
    """
    s = ''
    url_name = name_to_url(name)
    try:
    #checks to see if url exists
    #adds the name converted onto the end to get the url page
        persons_page = urllib.request.urlopen('https://cs1110.cs.virginia.edu/files/uva2018/'+url_name)
        #decodes
        info = persons_page.read().decode("UTF-8")
        #job regex
        j = re.compile(r'Job title:(.*)<br />')
        match1 = j.search(info)
        job = match1.group(1)
        job = job.replace('amp;',"")
        job = job.replace('&#39;', "'")
        #salary regex
        m = re.compile(r'total gross pay: [$]?([0-9]+[,][0-9]+)')
        match2 = m.search(info)
        money = match2.group(1)
        if money is None:
            money = 0
        money = money.split(',')
        money = s.join(money)
        money = float(money)
        #rank regex
        r = re.compile(r'rank</td><td>([0-9]?[,]?[0-9]+)')
        match3 = r.search(info)
        #defaults to 0 if rank doesn't exist
        rank = 0
        if match3 is not None:
            rank = match3.group(1)
            rank = rank.split(',')
            rank = s.join(rank)
    except urllib.error.URLError:
        #if it doesn't exist
        job = None
        money = 0
        rank = 0
    return job, money, rank


