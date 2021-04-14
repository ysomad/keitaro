from keitaro.api import API


class Report(API):

    def __init__(self, client, endpoint='report'):
        super(Report, self).__init__(client, endpoint)

    def get_labels(self, campaign_id, label_name, ref_name):
        """
        Gets reports labels
        """
        return super(Report, self).prepare_request(
            'GET', 'labels', campaign_id=campaign_id,
            label_name=label_name, ref_name=ref_name)

    def build(
            self, interval, timezone,
            metrics=['clicks', 'campaign_unique_clicks', 'conversions', 'roi'],
            grouping=['campaign'], sort={'name': 'clicks', 'order': 'DESC'}):
        """
        Builds custom keitaro report
        """
        return super(Report, self).prepare_request(
            'POST', 'build', range={'interval': interval, 'timezone': timezone},
            metrics=metrics, grouping=grouping, sort=[sort])

    def update_labels(self, campaign_id, ref_name, items):
        """
        Updates report labels
        """
        return super(Report, self).prepare_request(
            'POST', 'labels', campaign_id=campaign_id,
            ref_name=ref_name, items={'value': items})
