from keitaro.api import API


class Report(API):

    def __init__(self, client, endpoint='report'):
        super(Report, self).__init__(client, endpoint)

    def get_labels(self, campaign_id, label_name, ref_name):
        """Getting reports labels"""
        return super(Report, self).get(
            'labels', campaign_id=campaign_id,
            label_name=label_name, ref_name=ref_name)

    def build(self, interval, timezone,
              metrics=['clicks', 'campaign_unique_clicks',
                       'conversions', 'roi'], grouping=['campaign'],
              sort={'name': 'clicks', 'order': 'DESC'}):
        """Building custom keitaro report"""
        report_range = {'interval': interval, 'timezone': timezone}
        sort_by = [sort]
        return super(Report, self).post(
            'build', range=report_range, metrics=metrics,
            grouping=grouping, sort=sort_by)

    def update_labels(self, campaign_id, ref_name, items):
        """Update report labels"""
        return super(Report, self).post(
            'labels', campaign_id=campaign_id, ref_name=ref_name, items=items)
