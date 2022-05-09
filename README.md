# ABOUT CREDIT RISK (Under development...)
Credit risk can be defined as the risk that a debtor will not settle its commitments in a timely manner, also called default. In fact, every type of financial investment has its risks. Among them, credit risk is one of those that can generate the greatest problems for investors and cause severe losses. So, technically, credit risk is related to the ability of a borrower to return that amount, under the agreed conditions, to the creditor. It is a practice aimed not only at mitigating financial inconvenience, but also at providing a structure to deal with the situation.

## Risk rating
One way to assess risk is through rating, which in turn is a specific methodology developed by risk rating agencies. Standard & Poors, Moody's and Fitch Ratings are some of the best known. Institutions assess issues such as type of business, economic scenario and relationship of partnerships to categorize risk. The companies evaluated by the agencies are classified into:

Level A (AAA, AA+, A1, A2, Aa): low risk of default; <br />
Level B (BBB, BB+, B1, B2, Bb): average default risk; <br />
Level C and variations: high risk of default; <br />
Level D (in default situation).

## Research problem
How to reduce the losses incurred by providing cash loans?

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


>To maintain the model's performance in terms of data integrity, rows with missing data will be deleted and not replaced with averages.

## About outliers removed from the original database: 

<p align="left">
	<br />
	<img src="/1_results/0_outliers_1.jpeg">
	<img src="/1_results/0_outliers_2.jpeg">
 	<img src="/1_results/0_outliers.jpeg">
	<br />
	<br />
</p>

| TOTALS                     | VALUES                         
|----------------------------|--------------------------------
| Number of observations     | 28638                 
| Number of outliers         | 9782            
| Percentage of data removed | 34.16 %

>* Following the same logic performed for the missing data, the outliers will also be removed.
>* At the end of this process, the total remaining observations were 19k. This is still a good amount to generate a model.

## Table with a small sample of the data:

person_age|person_income|person_home_ownership|person_emp_length|loan_intent|loan_grade|loan_amnt|loan_int_rate|loan_status|loan_percent_income|cb_person_default_on_file|cb_person_cred_hist_length
|-|-|-|-|-|-|-|-|-|-|-|-
22|30000|MORTGAGE|0|VENTURE|B|5000|11.48|0|0.17|N|4
35|66000|MORTGAGE|4|VENTURE|A|3000|6.03|0|0.05|N|7
27|58800|MORTGAGE|0|EDUCATION|C|9800|13.22|0|0.17|Y|9
25|26004|RENT|8|DEBTCONSOLIDATION|A|7000|6.92|0|0.27|N|3
23|69996|MORTGAGE|4|VENTURE|A|4000|8.0|0|0.06|N|2
23|71000|MORTGAGE|7|EDUCATION|A|9600|7.51|0|0.14|N|4
26|30000|RENT|9|VENTURE|B|2000|11.49|0|0.07|N|3
31|60682|RENT|3|PERSONAL|A|8650|8.49|0|0.14|N|8
33|75000|MORTGAGE|13|VENTURE|D|4000|14.11|0|0.05|N|7
22|63000|MORTGAGE|6|EDUCATION|A|3700|5.42|0|0.06|N|4


## Selected attributes and a brief description:

Attribute|Description
|-|-
|person_age| Indicates the person's age in years
|person_income| The person's anual income
|person_home_ownership| The type of home that can be rented, owned, mortgaged and others
|person_emp_length| The person's employment length in years
|loan_intent| The person's intent for the loan
|loan_grade| The loan grade, which can be A, B, C, D, E, F, G
|loan_amnt| The loan amount
|loan_int_rate| The loan interest rate
|loan_status| Shows loan status (default and non-default)
|loan_percent_income| The committed percentage of income dedicated to the mortgage
|cb_person_default_on_file| Person's default history
|cb_person_cred_hist_length| The person's credit history

## Loan Amount
<p align="center">
	<br />
 	<img src="/1_results/3_hist_loan_amnt.jpg" width="600" />
	<br />
	<br />
</p>

## Descriptive analysis:

attributes|mean|median|std|variance|lower|higher
|-|-|-|-|-|-|-
person_age|26.44|25.00|4.21|17.72|20.00|40.00
person_income|61494.52|57000.00|26449.17|699558669.53|7200.00|140304.00
person_emp_length|4.51|4.00|3.39|11.49|0.00|14.00
loan_amnt|8305.20|7500.00|4744.66|22511825.60|500.00|23750.00
loan_int_rate|10.40|10.59|2.95|8.70|5.42|21.74
loan_status|0.00|0.00|0.00|0.00|0.00|0.00
loan_percent_income|0.15|0.13|0.08|0.01|0.01|0.44
cb_person_cred_hist_length|5.02|4.00|2.97|8.80|2.00|15.00

>* It can be noted that after the data cleaning process, only observations of people aged between 20 and 40 years remained. It would be interesting to have more observations from people over 40, but as the amount in this database was relatively small, they were considered outliers and were removed.
>* $ 10,000 is the most obtained loan amount, but the average is $ 7,500.
>* The average annual income of the people in this database is $ 57,000 per year. The person who earns the least has an income of $ 7,200 a year against $ 140,304 for the person who earns the most.

## Some assumptions about the data
<p align="left">
	<br />
 	<img src="/1_results/5_hypotheses.jpeg" width="800" />
	<br />
	<br />
</p>

## Categorical attributes
<p align="left">
	<br />
 	<img src="/1_results/6_categorical_attributes.jpeg" />
	<br />
	<br />
</p>


Under development...
