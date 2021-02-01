from keitaro.api import API


class Report(API):

    def __init__(self, client, endpoint='report'):
        super(Report, self).__init__(client, endpoint)

    def labels(self, campaign_id, label_name, ref_name):
        """ref_name = ip/source/ad_campaign_id/creative_id/
        keyword/ad_campaign_idn/sub_id_1..10"""
        return super(Report, self).get('labels', campaign_id=campaign_id,
                label_name=label_name, ref_name=ref_name)
