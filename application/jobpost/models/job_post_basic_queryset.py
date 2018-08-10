from django.db import models


class JobPostQuerySet(models.QuerySet):
    """
        Detail about job post query set
    """

    def job_title(self):
        """
            Get all job post
        """

        return self.defer('job_title','vacancy', 'deadline','id').filter(status=True)
