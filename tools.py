import progressbar


def get_progressbar(N, name=""):
    return progressbar.ProgressBar(
        maxval=N,
        widgets=[progressbar.Bar('#', '[', ']'),
                 name,
                 progressbar.Percentage()])

def groupBy(_list, f =lambda x: x):
    d = {}

    for x in _list:
        try: d[f(x)].append(x)
        except: d[f(x)] = [x]
    
    return d