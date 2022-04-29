# ABOUT CREDIT RISK (Under development...)
Credit risk can be defined as the risk that a debtor will not settle its commitments in a timely manner, also called default. In fact, every type of financial investment has its risks. Among them, credit risk is one of those that can generate the greatest problems for investors and cause severe losses. So, technically, credit risk is related to the ability of a borrower to return that amount, under the agreed conditions, to the creditor. It is a practice aimed not only at mitigating financial inconvenience, but also at providing a structure to deal with the situation.

## Risk rating
One way to assess risk is through rating, which in turn is a specific methodology developed by risk rating agencies. Standard & Poors, Moody's and Fitch Ratings are some of the best known. Institutions assess issues such as type of business, economic scenario and relationship of partnerships to categorize risk. The companies evaluated by the agencies are classified into:

Level A (AAA, AA+, A1, A2, Aa): low risk of default; <br />
Level B (BBB, BB+, B1, B2, Bb): average default risk; <br />
Level C and variations: high risk of default; <br />
Level D: in default situation.

## Research objectives 
The main objective of this study will be to develop a statistical model that makes it possible to make a prediction (not an exact prediction that is always right, that would be impossible, but a prediction that most of the time is right), through already known data about an individual, that demonstrates whether in the future that person will be able to pay their debts correctly. One or two defaults do not affect a company, however, a large number of defaults can cause a major disruption to cash flows, causing serious financial problems. In addition, a series of insights will be generated during the modeling process, on the available resources of the data, in order to assist in decision making related to other sectors.

# MODELING PROCESS
We cannot go directly to the model without first cleaning up the data and doing a pre-analysis. First, an analysis will be carried out and verification of missing data in the database, then a treatment and removal of outliers will be carried out and finally the generation of some graphs and insights.

## About missing data removed from the original database:      

| TOTALS                     | VALUES                         
|----------------------------|--------------------------------
| Number of observations     | 32581
| Number of missing data     | 3943
| Percentage of data removed | 12.10 %


## About outliers removed from the original database:      

| TOTALS                     | VALUES                         
|----------------------------|--------------------------------
| Number of observations     | 32581
| Number of outliers         | 10716
| Percentage of data removed | 32.89 %


## Table with a small sample of the data:

person_age|person_income|person_home_ownership|person_emp_length|loan_intent|loan_grade|loan_amnt|loan_int_rate|loan_status|loan_percent_income|cb_person_default_on_file|cb_person_cred_hist_length
|-|-|-|-|-|-|-|-|-|-|-|-
28|15000|RENT|1.0|PERSONAL|A|5000|7.4|1|0.33|N|9
25|69000|RENT|0.0|HOMEIMPROVEMENT|E|15000|16.7|1|0.22|Y|3
26|52800|RENT|4.0|VENTURE|B|8975|10.99|0|0.17|N|2
27|72996|MORTGAGE|12.0|EDUCATION|A|9200|6.03|0|0.13|N|8
26|26000|RENT|2.0|DEBTCONSOLIDATION|C|3825|14.27|0|0.15|N|4
24|75200|OWN|5.0|EDUCATION|A|6500|7.14|0|0.09|N|2
22|18000|RENT|0.0|MEDICAL|B|3600||1|0.2|N|3
24|60000|RENT|5.0|HOMEIMPROVEMENT|D|3400||0|0.06|N|2
25|90000|RENT|9.0|HOMEIMPROVEMENT|C|6000|13.49|0|0.07|N|4
23|34900|MORTGAGE|2.0|MEDICAL|F|4000||1|0.11|Y|4


## Selected attributes and a brief description:

Attribute|Description
|-|-
|person_age| Indicates the person's age in years.
|person_income| The person's anual income.
|person_home_ownership| The type of home that can be rented, owned, mortgaged and others.
|person_emp_length| The person's employment length in years.
|loan_intent| The person's intent for the loan.
|loan_grade| The loan grade, which can be A, B, C, D, E, F, G.
|loan_amnt| The loan amount.
|loan_int_rate| The loan interest rate.
|loan_status| Shows loan status (default and non-default).
|loan_percent_income| The committed percentage of income dedicated to the mortgage.
|cb_person_default_on_file| Person's default history.
|cb_person_cred_hist_length| The person's credit history.

<p float="left">
	<br />
	<img src="/1_results/3_hist_loan_amnt.jpg" width="600" />
	<br />
	<br />
</p>

## Descriptive analysis:

attributes|mean|median|std|variance|lower|higher
|-|-|-|-|-|-|-
person_age|27.73|26.00|6.35|40.30|20.00|144.00
person_income|66074.85|55000.00|61983.12|3841907061.81|4000.00|6000000.00
person_emp_length|4.79|4.00|4.14|17.16|0.00|123.00
loan_amnt|9589.37|8000.00|6322.09|39968779.56|500.00|35000.00
loan_int_rate|11.01|10.99|3.24|10.50|5.42|23.22
loan_status|0.22|0.00|0.41|0.17|0.00|1.00
loan_percent_income|0.17|0.15|0.11|0.01|0.00|0.83
cb_person_cred_hist_length|5.80|4.00|4.06|16.44|2.00|30.00



Under development...
