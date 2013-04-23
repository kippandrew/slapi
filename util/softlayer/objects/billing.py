from util.softlayer.objects.core import *

class SoftLayerBillingOrder(BaseSoftLayerObject):
    """SoftLayer_Billing_Order"""

    def __init__(self, obj):
        super(SoftLayerBillingOrder, self).__init__(obj)

    @softlayer_property_format(label=False)
    def id(self):
        return self.get_data('id')

    @softlayer_property
    def status(self):
        return self.get_data('status')

    @softlayer_property
    def create_date(self):
        return self.get_data('createDate')

class SoftLayerBillingOrderQuote(BaseSoftLayerObject):
    """SoftLayer_Billing_Order_Quote"""

    def __init__(self, obj):
        super(SoftLayerBillingOrderQuote, self).__init__(obj)

    @softlayer_property_format(label=False)
    def id(self):
        return self.get_data('id')

    @softlayer_property
    def name(self):
        return self.get_data('name')

    @softlayer_property
    def status(self):
        return self.get_data('status')

    @softlayer_property
    def key(self):
        return self.get_data('quoteKey')

    @softlayer_property
    def create_date(self):
        return self.get_data('createDate')

class SoftLayerContainerProductOrder(BaseSoftLayerObject):
    """SoftLayer_Container_Product_Order"""

    def __init__(self, obj):
        super(SoftLayerContainerProductOrder, self).__init__(obj)

    @softlayer_property_format("Recurring Cost")
    def post_tax_recurring_charge(self):
        return self.get_data('postTaxRecurring')

    @softlayer_property_format(label=False)
    def pre_tax_recurring_charge(self):
        return self.get_data('preTaxRecurring')

    @softlayer_property_format("Setup Cost")
    def post_tax_setup_charge(self):
        return self.get_data('postTaxSetup')

    @softlayer_property_format(label=False)
    def pre_tax_setup_charge(self):
        return self.get_data('preTaxSetup')

    @softlayer_property_format("Prorated Order Charge")
    def prorated_order_charge(self):
        return self.get_data('proratedOrderTotal')
