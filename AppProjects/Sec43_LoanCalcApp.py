'''Mortgage Loan App'''
from mortgage import Loan
from matplotlib import pyplot
loan = Loan(principal=380000,interest=0.0267,term=30)

totalpaid = loan.total_paid
totalinterest = loan.total_interest
totalprincipal = loan.total_principal
# pyplot.plot(34,70)
print(totalpaid)
print(totalinterest)
print(totalprincipal)
def plot_loan(value,**kwargs):
    pyplot.yscale(str(totalpaid),**kwargs=linear)
    pyplot.xscale(str(loan.term), **kwargs=linear)
    pyplot.show
def create_graph(data, loan):
    x_values = []
    y_values = []

    