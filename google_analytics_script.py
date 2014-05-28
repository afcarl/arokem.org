#!/usr/bin/env python
"""

"""
import os

# This should be inserted in every html page before the closing </head> tag:
google_analytics_txt = """

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-25254402-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

"""

def insert_g_analytics(fname):
    """

    Open a file, find the closing </head> tag and insert the google analytics
    text in there. 
    
    """
    ff = file(fname, 'r')
    # Get the text in there:
    ll = ff.readlines()
    ff.close()

    this_idx = None
    for idx, l in enumerate(ll):
        if '</head>' in l:
            this_idx = idx

    # Only if this is possible: 
    if this_idx:
        ll = ll[:this_idx] + [google_analytics_txt] + ll[this_idx:]
        ff = file(fname, 'w')
        ff.writelines(ll)
        ff.close()

def main():
    root_dir = './_build/html'
    for w in os.walk(root_dir):
        for ff in w[-1]:
            if ff.endswith('.html'):
                insert_g_analytics(os.path.join(w[0],ff))

if __name__ == '__main__':
    main()

