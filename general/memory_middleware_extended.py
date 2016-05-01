# Orignal version taken from http://www.djangosnippets.org/snippets/186/
# Original author: udfalkso
# Modified by: Shwagroo Team

import sys
import re
import StringIO
from hotshot import Profile, stats
from tempfile import mktemp
from os import unlink

from django.conf import settings


words_re = re.compile(r'\s+')

group_prefix_re = [
    re.compile("^.*/django/[^/]+"),
    re.compile("^(.*)/[^/]+$"),  # extract module path
    re.compile(".*"),            # catch strange entries
]


class ProfileMiddleware(object):
    """
    Displays hotshot profiling for any view.
    http://yoursite.com/yourview/?prof

    Add the "prof" key to query string by appending ?prof (or &prof=)
    and you'll see the profiling results in your browser.
    It's set up to only be available in django's debug mode,
    is available for superuser otherwise, but you really shouldn't add this
    middleware to any production configuration.

    WARNING: It uses hotshot profiler which is not thread safe.
    """
    def __init__(self):
        self.tmpfile = None
        self.prof = None

    def process_request(self, request):
        if (settings.DEBUG or request.user.is_superuser) \
                and request.method == 'GET' and request.GET.get('prof', False):
            self.tmpfile = mktemp()
            self.prof = Profile(self.tmpfile)

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if (settings.DEBUG or request.user.is_superuser) \
                and request.method == 'GET' and request.GET.get('prof', False):
            return self.prof.runcall(callback, request, *callback_args,
                                     **callback_kwargs)

    @staticmethod
    def get_group(f):
        for g in group_prefix_re:
            name = g.findall(f)
            if name:
                return name[0]

    @staticmethod
    def get_summary(results_dict, sum_obj):
        group = [(item[1], item[0]) for item in results_dict.items()]
        group.sort(reverse=True)
        group = list[:40]

        res = "      tottime\n"
        for item in group:
            res += "%4.1f%% %7.3f %s\n" % \
                   (100 * item[0] / sum_obj if sum_obj else 0, item[0], item[1])
        return res

    def summary_for_files(self, stats_str):
        stats_str = stats_str.split("\n")[5:]

        mystats = {}
        mygroups = {}

        sum_obj = 0

        for s in stats_str:
            fields = words_re.split(s)
            if len(fields) == 7:
                time = float(fields[2])
                sum_obj += time
                file_name = fields[6].split(":")[0]

                if file_name not in mystats:
                    mystats[file_name] = 0
                mystats[file_name] += time

                group = self.get_group(file_name)
                if group not in mygroups:
                    mygroups[group] = 0
                mygroups[group] += time

        return '<pre> ---- By file ----\n\n{}\n ' \
               '---- By group ---\n\n{}</pre>'.\
            format(self.get_summary(mystats, sum_obj),
                   self.get_summary(mygroups, sum_obj))

    def process_response(self, request, response):
        if (settings.DEBUG or request.user.is_superuser) \
                and request.method == 'GET' and request.GET.get('prof', False):
            self.prof.close()

            out = StringIO.StringIO()
            old_stdout = sys.stdout
            sys.stdout = out

            obj_stats = stats.load(self.tmpfile)
            obj_stats.sort_stats('time', 'calls')
            obj_stats.print_stats()

            sys.stdout = old_stdout
            stats_str = out.getvalue()

            if response and response.content and stats_str:
                response.content = "<pre>" + stats_str + "</pre>"

            response.content = "\n".join(response.content.split("\n")[:40])

            response.content += self.summary_for_files(stats_str)

            unlink(self.tmpfile)

        return response
