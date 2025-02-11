# A=final amount
# i=principal(initial amount)
# r=interest rate
# n=number of times interest is compounded
# t=number of years

dimensions={
        "r":0.03,
        "n":3,
        "t":3,
        "p":4500
        }

def calculating_compound_interest(r,n,t,p):
        interest_rate_per_compounding_period=r / n
        number_of_times_interest_was_applied=n*t
        growth_factor_per_compounding_period=1+interest_rate_per_compounding_period
        total_growth_factor=growth_factor_per_compounding_period**number_of_times_interest_was_applied
        final_amount=p*total_growth_factor

        print(f"the total interest compounded in {n}years is ",round(final_amount)) if final_amount>0 else(0)
calculating_compound_interest(dimensions["r"],dimensions["n"],dimensions ["t"], dimensions["p"])