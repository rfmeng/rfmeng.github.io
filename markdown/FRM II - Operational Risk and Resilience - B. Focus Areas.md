<ndtag category = "FRM II" editdate="2024-11-04" createdate="2024-10-31" tag="Risk-Management"></ndtag>

## B.a. Cyber Threats and Information Security Risks

### <!-- C8 p149 --> Cyber-Resilience: Range of Practices
#### Cyber Resilience Standards and Guidelines
through IT and operational risk standards
business continuity planning and outsourcing have relevance to cyber risk
no international standard

#### Cyber Governance
1. Cyber-Security Strategy
  expected but not required
  sector-specific or across multiple industires
2. Management Roles and Responsibilities
3. Cyber risk awareness culture
4. architecture and standard
5. cyber security workforce

#### Approaches on Cyber-Risk Management
supervision of cyber-resilience
information security controls
incident response and recovery
cybersecurity and resilience metrics

#### Communication and Sharing of Information (***)
* sharing among banks:
  no common standard
  regulators not involved
  financial industry's culture
* sharing from banks to regulators
  mandatory
  informal flowback
* sharing among regulators
  least frequent
  mandatory or voluntory
* sharing from regulators to banks
  publicly available
* sharing with security agencies
  mandatory or voluntory

#### Interconnections with Thrid Parties
difficult gaining assurance of cyber-resilience
Third parties is in a broad sense:
* outsourcing
* service and product not considered outsourcing (power, telecommunication)
* interconnected counterparties such as Financial Market Infrastructure (FMI)

##### Analysis Areas
* governance of third-party interconnections
  contractual framework
* business continuity and availability
  backup provider
* information confidentiality and integrity
* specific practices regarding visibility of third party interconnections
  regulators informed about the material outsourcing agreements
* audit and testing
  guarantee "rights to inspect and audit" providers
  compliance testing: red teaming exercises
* resources and skills

intrusive on-site inspections and off-site supervison are widespread
  
### <!-- C9 p171 --> Case Study: Cyberthreats and Information Security Risks
#### Information Security Risks (ISR)
taxonomy of IRS:
* internal causes versus external causes
* data theft versus data loss

|Data Incidents|Theft or corruption|Loss or unvoluntary|
|:-:|:-:|:-:|
|External or third parties|digital: hacking, virus infection, phishing <br> physical: theft, social engineering| disaster, system disruption, third party failure|
|Internal| theft<br>departing employees take proprietary information|digital: database loss, backup loss, device loss, error when sending documents <br> physical: loss of documents, loss of archives, accidental mentions of confidential information when communicating|

#### Cyber Risk Management: Frameworks
ISO standards do not provide implementable guidance, but act as evaluation grids for those who want to achieve certification

#### Essential of Cybersecurity Protection and Monitoring
Information security protection: confidentiality, integrity, availability (CIA)
information control: 
* behavioral
  training, awareness, rules of conduct, password, supervision, sanctions
* technical
  preventative, detective

#### Equifax Case Study
hackers access databases and extract consumers' personal information through dipute portal

##### Lessons
* lack of comprehensive inventory of IT assets
* failure of risk management policy enforement and enfore the patch management policy
* inconsistent communication among employees on remediation
* expired SSL certificate
* poor external communication during crisis (after 6 months)

## B.b. Financial Crime and Fraud

### <!-- C10 p179 --> Sound Management of Risks Related to Money Laundering and Financing of Terrorism 
#### Best Practices (***)
Banks should not establish a threshold transaction value and reveiw all transactions above the threshold.
Terrorist screening is not risk-sensitive and should be carried out irrespective of the risk profile.
Bank should freeze fund without delay and without prior notice.

Three defense lines, second line is s chief AML/CFT officer who should have direct reporting to board.

Enhanced due diligence:
* annoymous account with large balance
* large size of cross-border transaction account
* foreign politically exposed person

Bank should not open an anonymity account, while confidential numbered accounts are not annoymous.
Even if a customer has opened a bank account at a reputable bank, he cannot be categorized as low risk.
A bank should conduct its own due diligence even if the customer's name in anther bank is subject to the same CDD standard.
An applicant refused by another bank should be considered higher-risk and apply enhanced due diligence.

##### Technology
automated processes should be employed
regulators encourage advanced analytics like machine learning
The bank providing correspondent banking services tends to increase its ML/FT risk.

##### Abroad Business
appoint a chief AML/CFT officer for the whole group
apply stricter standard of the home and host countries
integrate information lf customer and his beneficial owner



### <!-- C11 p193 --> Case Study: Financial Crime and Fraud
#### Financial Fraud Risk Management
##### Internal Fraud
* selection: about recuitment
* prevention: seggregation of duties, authorizations
* detection: reconciliations, whistleblowing
* deterrents: forensic analysis

#### AML Risk Management
* selection: know your client (KYC)
* prevention: 
* detection: 
* deterrents: escalation to financial intelligence unit (FIU), closure of accounts

##### Money Laundering 
* placement: money enters bank
* layering
* intergation or extraction

#### Case Study: USAA
AML mangement failure: deliberately late submit of suspicious activity report
AML remediation (lookback)
COVID-19 makes it more difficult to identify anomalies

## B.c. Third-Party Risk Management 
### <!-- C12 p201 --> Guidance on Managing Outsourcing Risk
vendor/contractor

#### Risks from the Use of Service Providers
* compliance: service provider violates regulations
* concentration: limited service providers
* reputational
* country: foreign service provider
* operational:
* legal

####  Service Provider Risk Management Programs
##### Due Diligence 
prior to engaging the vendor
business background, financial performance, operations and internal control

##### Contract Provision (**)
* scope: rights and responsibilities
* cost and compensation
* right to audit: optionally included
* performance standards
* information confidentiality and security
* ownership and license
* indemnification: claim from the service provider's negligence
* default and termination
* dispute resolution
* limits on liability: for service providers
* insurance: service provider buy insurance
* customer complaint: specify responsibility of both parties
* business resumption and contingency plan of the service provider: developed by the service provider
* foreign-based service providers: different standards for local and foreign vendor
* subcontracting: same contractual provisions should apply to subcontractor
  service providers have overall accountability for all services
   
### <!-- C13 p209 --> Case Study: Third-Party Risk Management 
#### Third-Party Risk
cost-saving, competitive advantage

##### Third-Party Risk Management Framework
* business model decision
* evaluation, risk rating
* requests for proposal (RFP) and contracts
* monitoring
* remediation or termination

#### Case Study: Capital One Data Breach
AWS's employee steal SSN and bank account numbers
Lessons: security hygiene

#### Case Study: OCC Fines Morgan Stanley
MS decommission 2 wealth management business data servers. MS did not exercise due diligence.

## B.d. Investor Protection and Compliance Risks in Investment Activities 
### <!-- C14 p215 --> Case Study: Investor Protection and Compliance Risks in Investment Activities
#### Markets in Financial Instruments Directive (MIFID)
MIFID: trade transparency obligation to prevent market abuse
MIFID II: data on trading activity

#### Dodd-Frank
* whistleblowers are granted protections
* CCP
* financial stability
* Volcker Rule: prevent commercial banks from engaging in speculative and proprietary trading

#### Fine Cases
UBS misrepresneted auction rate securites to investors as safe, cash equivalent products, which is liquidity risk. Refine 10 billion.
JP Morgan spoofing in precious metals
Deutsche bank routing customer order through smart order router, which creates delays of execution and causes lower fill rate.

##### Lessons
fines should be more than benefits accumulated

## B.e. Model Risk and Model Validation 

### <!-- C15 p219 --> Supervisory Guidance on Model Risk Management 
#### Model
#### Model Risk
* incorrect model
* misused

#### Model Risk Management
##### 1. Development, Implementation
documentation, testing
##### 2. Validation
* evaluation
  sensitivity analysis and scenario analysis
* ongoing monitoring
  * process verification: data and procedure
  * benchmarking
##### 3. Outcome Analysis (Backtesting)
parallel outcomes analysis: dynamically revised

#### Challenges to Effective Validation Process
system integration: data from different sources
widespread use of vendor products: modeling expertise is external


### <!-- C16 p233 --> Case Study: Model Risk and Model Validation 
#### Model Risk Management Function
MRM function sits in second line and independent of model development
Tradeoff between cost of validation and model risk:
* highest-tier: reviewed in detail
* high-tier: validated every 2 to 3 years
* lowe-tier: tailored validation

All models undergo annual review of environment.

#### Case Study: Gaussian Copula and CDO Pricing
constant correlation assumption

#### Case Study: Barclays' Acquisition of Lehman Brothers and the Excel Spreadsheet Error 
trading contracts were hidden Barclay did not want to buy
seemingly simplistic tools or models need the right review

#### Case Study: NASA Mars Orbiter
Lockheed Martin engineering team used English units of measurement (imperial)


## C. Capital Planning
### <!-- C18 p255 --> Risk Capital Attribution and Risk-Adjusted Performance Measurement
Risk capital (economic capital): cushion that provides protection against unexpeted loss
Regulatory capital: protect interests of investors

traditional use of economic capital
* funding and absorb risk
* target solvency
* highly opaque, high risk

new use of economic capital:
* performance measurement and incentive compensation
* active portflio management
* pricing transactions

#### Risk-Adjusted Return on Capital (RAROC) (***)
$RAROC=\frac{\text{after-tax expected risk-adjusted net income}}{\text{economic capital}}$
after-tax expected risk-adjusted net income = expected revenue - costs - expected loss - taxes + return on risk capital +- transfers
* expecte loss (PD amount)
* return on risk capital: risk free securities
* transfers: correspond to transfer pricing mechanisms, it happens for a bank department
* tax: apply for all income and loss

economical captial = risk capital + strategic captial
strategic captials = goodwill + burned-out capital
* strategic captial: investment
* burned-out capital: investment on initial stages of start up
* goodwill: amount paid above the replacement value of net asset when acquiring a firm

##### RAROC Calculation Issues
* time horizon: mostly 1 year
* PD:
  * point-in-time: individual financial instrument
  * through-the-cycle: for economic capital, current profitability and strategic decision
* confidence level:
  lower confidence level, higher RAROC, this affects the risk capital allocation
  business units tend to set lower confidence level than firmwide

##### RAROC for Capital Budgeting Decision
hurdle rate is after-tax weighted average cost of equity: $h_{AT}=\frac{CE}{CE+PE}\times R_{CE}+\frac{PE}{CE+PE}\times R_{PE}$
* CE/PE is market value of common/prefered equity

Adjusted RAROC (ARAROC): $ARAROC = RAROC-\beta_{CE}(R_M-r_f)$
accept projects if $ARAROC>r_f$

* stand-alone capital
* fully diversifed capital
* marginal capital: additional capital considering diversification


### <!-- C19 p255 --> Range of Practices and Issues in Economic Capital Frameworks 
#### Economical Capital Framework
##### Governance
senior management 
##### Risk Measure
##### Risk Aggregation (***)
less sophisticated than methodologies used in individual risk components
underestimate overall risk because individual risk components are estimated without consideration of interactions between risks (market and credit), even with "no diversification" assumptions.
5 methodologies:
* simple summation ($\rho =1 $)
* constant diversification: fixed diversification percentage
* variance-covariance matrix: not capture nonlinearities and skewness, leading to underestimate of risk
* copulas: better approximation but very difficult building a joint distribution 
* full modeling/simulation: most accurate, Monte Carlo
  simulates the impact of common risk drivers

##### Validation
preliminary stages, no uniform validation

##### Dependency Modeliing
##### Counterparty Credit Risk
unique market risk and operational risk
##### Interest Rate Risk (**)
challenges: long holding period, embedded optionality

#### Benefits and Impacts of EC (***)
EC is often parameterized as an amount of capital given a time horizon and confidence level
expected loss are accounted in the pricing of bank's product and loan loss provisioning, only unexpected losses require EC.

##### Credit Portfolio Management
measurement of level of concentration: from incremental risk contribution
##### Risk-Based Pricing
RAROC pricing
exceptions (specific customer relationship) should be monitored

##### Customer and Product Profitability Analysis
RAROC on customer level or product level

##### Management Incentives


### <!-- C20 p309 --> Capital Planning at Large Bank Holding Companies
capital adequacy process
#### Foundational Risk Management
lagging practice (bad): not account for reputational/strategic/compliance risk

#### Loss-Estimation Methodologies (***)
conservative approaches
clear narrative scenario
leading practice: estimate loss model at granular level (to trading desk level)

* lagging practice: weighted average LGD for portfolio
* leading practice: model LGD to underlying risk drivers

automation is better
Combination of roll-rate model (use past to predict future) and net charge-off model (default debt net value) is weak.

#### Resource-Estimation Methodologies 
capital resource

#### Capital Adequacy Impact assessment
risk-weight asset (RWA)
projections of size and compostion of balance sheet and RWA
use a full-revaluation approach to model bank's nonlinear postions (past 100 days, 99 days,..., to)


#### Capital Policy and Capital Planning
capital target (execution) above capital goal (finally goal)
lagging practice: triggers based on actual result or minimum regulatory capital ratio
leading practice: based on projected results

#### Internal Controls
management overlay (management attention)

#### Governance



### <!-- C17 p239 --> Stress Testing Banks
#### Historical Evolution
##### USA
supervisory capital assessment program (SCAP)
macro scenarios: GDP growth, unemployment rate, house price index
post-SCAP (**):
* from single shock to broad macro scenario
* from product or business unit level to firmwide
* from static to dynamic
* common equity threshold (capital adequacy)
* from loss to loss, revenues and costs

Comprehensive Capital Analysis and Review (CCAR)
includes banks' own stress scenarios
2011 CCAR require disclosure of macro scenario, while 2012 CCAR also require bank-level
disclosure was an important trait of SCAP, especially projected losses

##### Europe
European Banking Authority (EBA)
by asset and geography

#### Chanllenges
##### Chanllenges in Designing Scenarios
coherence (inherently multi risk factors setting)

##### Chanllenges in Modeling Losses and Revenues
from macro scenario to micro scenario, finding intermediate risk factors is important
in a stress model, use balance sheet to predict profit and loss quarterly for 2 years. The assumption is bank maintain its capital and liquidity ratios.





















