from keitaro.api import API


class Click(API):

    def __init__(self, client, endpoint='clicks'):
        super(Click, self).__init__(client, endpoint)

    def clean_stats(
            self, *, start_date, end_date, campaign_id=None, timezone=None):
        """
        Cleans keitaro stats between start_date and end_date
        """
        return super(Click, self).post(
            'clean', start_date=start_date, end_date=end_date,
            campaign_id=campaign_id, timezone=timezone)
