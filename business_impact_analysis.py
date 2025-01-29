class LossEstimation:
    """ Loss estimations to be used in a Business Impact Analysis """
    def __init__(self, aro, ef, val):
        self.aro = aro
        self.ef = ef
        self.val = val

    def single_loss_expectancy(self):
        """Cost of individual loss"""
        return self.val * self.ef

    def annualized_loss_expectancy(self):
        """Cost of a specific loss in a given year"""
        return self.single_loss_expectancy() * self.aro

if __name__ == "__main__":
    annualized_rate_occurance = float(input("Enter Annualized Rate of Occurance (ARO): "))
    exposure_factor = float(input("Enter Exposure Factor: "))
    asset_value = int(input("Enter value of asset at risk: "))

    loss_estimate = LossEstimation(annualized_rate_occurance, exposure_factor, asset_value)
    single_loss = loss_estimate.single_loss_expectancy()
    annualized_loss = loss_estimate.annualized_loss_expectancy()

    print(f"Single Loss Expectancy: {single_loss:,.0f}")
    print(f"Annualized Loss Expectancy: {annualized_loss:,.2f}")