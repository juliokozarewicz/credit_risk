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
	<br />
	<br />
	<img src="/1_results/0_outliers_2.jpeg">
	<br />
	<br />
 	<img src="/1_results/0_outliers.jpeg">
	<br />
	<br />
</p>

| TOTALS                     | VALUES                         
|----------------------------|--------------------------------
| Number of observations     | 28638                 
| Number of outliers         | 4888            
| Percentage of data removed | 17.07 %

>* Following the same logic performed for the missing data, the outliers will also be removed.
>* At the end of this process, the total remaining observations were 23k. This is still a good amount to generate a model.

## Table with a small sample of the data:

person_age|person_income|person_home_ownership|person_emp_length|loan_intent|loan_grade|loan_amnt|loan_int_rate|loan_status|loan_percent_income|cb_person_default_on_file|cb_person_cred_hist_length
|-|-|-|-|-|-|-|-|-|-|-|-
23|36000|RENT|0|VENTURE|C|11000|13.11|1|0.31|Y|3
28|60000|OWN|1|HOMEIMPROVEMENT|D|22000|14.09|0|0.37|Y|8
22|74000|RENT|4|VENTURE|A|5050|5.42|0|0.07|N|4
25|33000|RENT|5|MEDICAL|A|9000|7.14|0|0.27|N|2
23|56160|MORTGAGE|2|PERSONAL|B|3050|10.59|0|0.05|N|2
21|72000|MORTGAGE|5|DEBTCONSOLIDATION|A|2000|6.54|0|0.03|N|2
37|46000|MORTGAGE|9|EDUCATION|B|5000|10.75|0|0.11|N|14
23|31200|RENT|0|PERSONAL|C|3200|13.49|0|0.1|Y|2
25|98000|OWN|0|PERSONAL|A|2000|7.37|0|0.02|N|2
28|66300|MORTGAGE|11|MEDICAL|D|12000|14.11|1|0.15|N|6

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
person_age|26.39|25.00|4.21|17.71|20.00|40.00
person_income|57977.82|53597.50|26554.38|705135102.08|4080.00|140304.00
person_emp_length|4.35|4.00|3.37|11.39|0.00|14.00
loan_amnt|8485.20|7500.00|4895.01|23961130.71|500.00|23750.00
loan_int_rate|10.95|10.99|3.19|10.18|5.42|21.74
loan_status|0.21|0.00|0.40|0.16|0.00|1.00
loan_percent_income|0.16|0.14|0.09|0.01|0.01|0.44
cb_person_cred_hist_length|5.00|4.00|2.96|8.79|2.00|15.00

>* It can be noted that after the data cleaning process, only observations of people aged between 20 and 40 years remained. It would be interesting to have more observations from people over 40, but as the amount in this database was relatively small, they were considered outliers and were removed.
>* $ 10,000 is the most obtained loan amount, but the average is $ 7,500.
>* The average annual income of the people in this database is $ 57,978 per year. The person who earns the least has an income of $ 4,080 a year against $ 140,304 for the person who earns the most.

## Categorical attributes
<p align="left">
	<br />
 	<img src="/1_results/6_categorical_attributes.jpeg" />
	<br />
	<br />
</p>

>* The largest number of loans are for people who live on rent
>* The largest number of loans is related to education, followed by venture, medical, personal, debt consolidation and finally home improvement
>* The amount of defaults represents about 20.61%

## Numeric variables
<p align="left">
	<br />
 	<img src="/1_results/7_numeric_attributes.jpeg" />
	<br />
	<br />
</p>

>* People aged between 22 and 24 years account for about 37.79% of the amount of loans requested
>* People who have an annual income between 40 thousand dollars and 60 thousand dollars represent about 35.04% of the data.
>* Loan amounts that are between 4,000 and 10,000 dollars represent 55.6% of the data

## Information on the correlation between the variables
<p align="left">
	<br />
 	<img src="/1_results/8_correlation.jpeg" />
	<br />
	<br />
</p>

>* It is possible to observe that there is a considerable positive correlation between age and credit history
>* It is also possible to notice that there is a positive correlation between loan amount and the percentage of income committed to the loan

## A little more information about defaulters
For this database, it is interesting to generate some information only about the defaulters, a table will be set up where it will show notions about the average of the attributes and another table that will show the percentage of defaulters per loan grade.

loan_grade|person_income|loan_amnt|loan_int_rate|loan_status|loan_percent_income
|-|-|-|-|-|-
A|55698.0|7000.0|7.49|0.0|0.13
B|53000.0|7800.0|10.99|0.0|0.15
C|51000.0|7500.0|13.48|0.0|0.15
D|49000.0|8000.0|15.31|1.0|0.17
E|54000.0|10000.0|16.7|1.0|0.18
F|56500.0|10000.0|18.53|1.0|0.2
G|49000.0|13250.0|20.11|1.0|0.27

>* Loans become riskier for people who have a loan grade below 'D', since from then on the median indicates that the majority are in default
>* The lower the loan amount, the lower the default rate
>* The greater the commitment of income to the loan, the greater the chances of default
>* It is possible to notice the association between risk x return by noting that the higher the loan rate, the greater the loan amount and the greater the chance of default

loan_grade|not_default|default|all|percent_default
|-|-|-|-|-
A|7305|727|8032|9.05 %
B|6357|1131|7488|15.10 %
C|3909|969|4878|19.86 %
D|1024|1516|2540|59.69 %
E|229|431|660|65.30 %
F|31|93|124|75.00 %
G|1|27|28|96.43 %
All|18856|4894|23750|20.61 %

>* The default rate increases as the loan grade decreases
>* People with loan grade 'F' and 'G' have a high chance of defaulting

## Some assumptions about the data
<p align="left">
	<br />
 	<img src="/1_results/5_hypotheses.jpeg" width="700" />
	<br />
	<br />
</p>



Under development...
