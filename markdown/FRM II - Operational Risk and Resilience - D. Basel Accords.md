<ndtag category = "FRM II" editdate="2024-11-04" createdate="2024-10-31" tag="Risk-Management"></ndtag>

## D. Basel Accords
Basel tower, more details
|I|II|II.5|FRTB|III|
|:-:|:-:|:-:|:-:|:-:|
|1988|1999|2009|2012|2014|

## <!-- C21 p339 --> Capital Regulation Before the Global Financial Crisis
Basel I, Basel I Amendment, Basel II
### Basel I
#### Motivations
G10's common interest that banks have enough equity to absorb large losses.
A global minimum standard to "level to playing field".

#### Content
it includes credit risk and capital requirements

#### Credit Risk: Standardized Approach
$\frac{\text{Tier 1 capital}}{RWA} > 4\%$ and $\frac{\text{total capital}}{RWA} > 8\%$, where total capital is regulatory capital

##### Risk-Weighted Assets (RWA):
* on-balance sheet: $\sum w_iL_i$
  higher risk, higher weight, where weight is determined by asset type and asset country
* off-balance sheet
  credit equivalent amount (CEA) is calculated by applying a conversion factor to the principal amount
* derivatives
  * current exposure method: $CEA = \max(V,0)+D$
    where $V$ is current market value, $D$ is add-on amount, determined by $a$ (add-on factor) and $L$ (principal amount)
    $D$ accounts for changes of future market value
  * original exposure method (only for interest rate and foreign exchange contracts)
    $CEA=D$, where $D$ is add-on amount

##### Capital Requirement (Ignore Finance Term)
* Tier 1 capital (core capital for solvency)
  * common equity + disclosed reserves (retained earnings) - goodwill
  * noncumulative perpetual preferred stock (not compensate past's dividend with current year's profit)
* Tier 2 capital (recapitalization of entity in resolution / reduce the impact on depositors)
  * loan loss reserves not allocated to impairment of certain assets
  * undisclosed reserves
  * hybrid instruments (convertible bond)

### Basel I Amendments
* credit risk: adjustment for derivatives
* market risk
* capital requirement
* others

#### Credit Risk: Adjustment for Derivatives
netting from ISDA, default on all transactions at the same time
Net Replacement Ratio (NRR)： $NRR=\frac{\max\{\sum V_i,0\}}{\sum\max\{V_i,0\}}$
CEA: $CEA=\max\{\sum V_i,0\}+(0.4+0.6\times NRR)\sum D_i$

#### Market Risk
market risk capital charge for trading book
|Book| Trading Book|Banking Book|
|:-:|:-:|:-:|
|Purpose|Held for trading |Held to maturity|
|Time horizon|short|long|
|Risk type|Market|Credit|
|Confidence level|99%|99.9%|
|Var time horizon|10 day|1 year|
|Examples|securities, derivatives|loan and some debt|

Market risk:
* MR (general Market Risk): systemic risk such as interest rate risk
* SR (Specific Risk): idiosyncratic (credit spread)

corporate bonds exposed to interest rate risk (MR) and credit risk (SR)

##### 1. Market Risk Capital: Standardized Approach
assigns capital separately to each item and sum ignoring correlation
* Fixed income securities and interest rate derivatives, except options
* equity securities and equity derivatives other than options
* foreign exchange
* commodities
* options

##### 2. Market Risk Capital: Internal Model Based Approach
total capital for trading assets: $0.08*12.5*(MR+SR)=MR+SR$
$MR=\max\{VaR_{t-1},m_c\times VaR_{avg}\}$
* $t-1$ is for yesterday
* $VaR_{avg}$ is for past 60 days
* $m_c$ is a multiplicative factor with minimal value 3 from backtesting

SR:
* standardized approach
* internal model:
  * 10 day 99% VaR
  * multiplier 4 and capital for specific risk could not be less than half of that from standardized approach

#### Capital Requirements
Tier 3 capital: composed of unsecured subordinated debt with original maturity of at least 2 years to meet market risk capital requirement

#### Others
backtesting 1 day, 99% VaR over the past 250 days
4 exceptions corresponds to $m_c=3$. More exceptions, higher multiplier.

### Basel II
* three pillars
* credit risk
* operation risk

#### Three Pillars
* regulatory capital
* supervisory preview process: additional capital requirements
* market discipline: disclose qualitative and quantitative information

#### Credit Risk
##### 1. Standardized Approach
used by banks not sufficiently sophisticated
weight depend on obligor type, rating and nation.

Mitigants:
* simple approach
  exposure covered by collateral, use weight of collateral
  minimum risk weight is 20% except for sovereign debt
* comprehensive approach
  adjust the size of exposure upward and adjust the collateral downward
  new exposure = adjusted exposure - adjusted collateral

##### 2. Foundation Internal Ratings Based Approach
1 year 99.9% VaR
EL is covered by financial products pricing
$\text{capital} = UL = VaR - EL$
$\text{capital} =(WCDR-PD)\times EAD \times LGD\times MA$
* MA is maturity adjustment: $1+\frac{(M-2.5)\times b}{1-1.5\times b}$, needless to remember
* M is maturity of exposure

WCDR increases if correlation increases or PD increases.
PD has inverse relationship with correlation.
As a company becomes less creditworthy, PD increases and becomes idiosyncratic and less affected by overall market conditions.

* Foundation IRB approach: PD is given by bank, while LGD, EAD, M are supervisory values
  * netting CEA (like Basel I Amendment)
  * MA is 2.5 at most cases

##### 3. Advanced Internal Ratings Based Approach
PD, LGD, EAD, M for corporate, sovereign and bank exposures are given by bank
retail exposure use advanced IRB approach: 
* no maturity adjustment
* retail exposure have lower correlation

#### Operational Risk
##### 1. Basic Indicator Approach
$K_{BIA}=\frac{1}{n}\alpha \sum GI_i$
* $GI_i$ annual positive gross income
* number of years in which gross income is positive
* $\alpha=15\%$

##### 2. Standardized Approach
beta factors
|Business Lines| Beta Factors|
|:-:|:-:|
|Corporate Finance (Investment Bank)|18%|
|Sales and Trading (Investment Bank)|18%|
|Payment and Settlement|18%|
|Commercial Banking (Loan and deposit)|15%|
|Agency & Custody Service|15%|
|Retail Banking|12%|
|Retail Brokerage|12%|
|Asset Management|12%|

$K_{TSA}$ is positive average for beta adjusted gross income, like $K_{BIA}$.


##### 3. Advanced Measurement Approach
frequency (incidence) on loss (severity)
Loss Distribution Approach (LDA):
* parametric and Monte Carlo:
  combine incidence and severity
* scenario analysis

1 year 99.9% VaR
4 elemnts should be considered: 
* internal loss data
* external loss data
* scenario analysis (expertise)
* business environment & control

Bank must defend correlation assumptions in AMA.
Bank may offset at most 20% operational risk capital with insurance compensation or claim instead of insurance premium.

#### Solvency II
For insurance companies

Three pillars:
* quantitative requirement
* internal governance and official supervision
* disclosure and transparency

Risks:
* credit
* market
* operational
* underwriting (life, health, property & casualty insuracne)

Minimum Capital Requirement (MCR) and Solvency Capital Requirement (SCR), SCR > MCR
* below SCR: restore capital plan
  1 year 99.5% confidence
* below MCR: prevent new business and resolution, transfering its policies (insurance sold) to another company

Capital structure:
* Tier 1 capital: equity, retained earnings
* Tier 2 capital: liabilities is subordinated to policyholders
* Tier 3 capital: debt is subordinated to policyholders





## <!-- C22 353--> Solvency, Liquidity, and Other Regulation After the Global Financial Crisis
### Basel II.5
2008 crisis, BCBS recognize minimum capital for market risk is inadequate for the trading book.
Updations:
* Stressed VaR
* Incremental Risk Charge
* Comprehensive Risk Capital

#### Stressed VaR
Basel II.5 requires banks to calculate two VaRs, both are 10 days 99% VaR.
Data range:
* usual VaR: 1 to 4 years historical daily movement (and times $\sqrt{10}$)
* stressed VaR: the most stressful year (250 days) in the most recent 7 years

capital: $MR = \max\{VaR_{t-1},m_c\times VaR_{avg}\}+sMR$
$sMR=\max\{sVaR_{t-1},m_s\times sVaR_{avg}\}$
* same as Basel I Amendment

Stressed VaR is an extra pretty large amount.

#### Incremental Risk Charge (IRC)
The specific risk charge is to capture default, a reaction to regulatory arbitrage, which is named Incremental Default Risk Charge (IDRC).
Besides default risk, credit risk also includes credit spread and credit rating change. As a result, IDRC is widened to IRC.

#### Comprehensive Risk Capital (CRC)
Basel II assumes constant correlation.
For correlation book (securitizations/re-securitizations/relating derivatives), it is nonsystemic risk.
Replace other indicators with CRC for the correlation book.

##### 1. Standardized Approach
capital ratio is determined by instrument type and credit ranking

##### 2. Internal Model Approach
routinely rigorous stress tests


### Basel III
* Capital Requirements
* Liquidity Risk
* Counterparty Credit Risk

#### Capital Requirements
##### Capital Structure
Tier 1 capital (going-concern capital):
* Tier 1 equity capital
  common equity / retained earnings / a limited amount of minority interest / unrealized gains and losses
* additional tier 1 capital
  non-cumulative perpetual perfered equity (subordinated to depositors) / subordinated debt (callable after 5 years) / convertible debt / minority interest not in core tier 1 

Tier 1 capital excludes, goodwill, intangibles, deferred tax assets, shortfall of reserves related to IRB EL. (no need to remember)

Tier 2 capital (gone concern capital) protects depositors and creditors after failure:
* unsecured, unguaranteed debt / instruments subordinated to depositor and subordinated debt (with 5 years maturity and callable after 5 years)

(?) total capital includes general loan loss reserves (for UL), at most 1.25% standardized approach RWA or 0.6% of IRB RWA could be included in capital.

##### Capital Ratio
Minimum capital requirement (at all times):
* Tier 1 equity capital must be at least 4.5% of RWA
* Total Tier 1 capital must be at least 6% of RWA
* Total capital (total Tier 1 + tier 2) must be at least 8% of RWA

Capital Conservation Buffer (CCB):
in normal times (against stressed time) core Tier 1 equity capital equal 20 2.5% of RWA
(?) core Tier 1 equity capital
  * (-) temporarily understood as tier 1 equity capital

Countercyclical Capital Buffer (CCB):
vary at the discretion of national supervisors and between 0 and 2.5% of RWA, must be met with core Tier 1 equity capital
* to prevent the incentive of decreasing loan during recession (less loan, lower RWA)
* to provide for macroprudential restraint of overheating

G-SIBs Buffer: higher loss absorption requirment
extra equity equal 1%, 1.5%, 2%, 2.5%, 3.5% of RWA
Living wills: when distressed, how to recapitalize and operate as a going concern
(G-SII for insure, D-SIB for domestic banks)

Leverage ratio: Tier 1 capital to leverage exposure (LE)
* minimum leverage ratio of 3%
* leverage exposure includes on-balance-sheet assets and fractions of off-balance-sheet assets
* LE does not set risk adjusted weight for on-balance-sheet asset, compared to RWA

Contingent Convertible Bonds (CoCos): 
increase equity automatically when distress occurs
common trigger is ratio of core tier 1 capital to RWA falls below a threshold
CoCos may (in some countries) be included in Additional Tier 1 or Tier 2
* as bond, it cost less than equity
* higher ROE in normal time

#### Liquidity Risk
banks need to survive liquidity pressures
liquidity ratio higher than 100%

##### 1. Liquidity Coverage Ratio (LCR)
$LCR = \frac{\text{high quality liquid assets}}{\text{net cash outflow in 30 days period}}$
acute stress examples: 
* downgrade of bank's debt by 3 notchs
* partial loss of deposit
* increased haircut on secured funding

##### 2. Net Stable Funding Ratio (NSFR)
$NSFR=\frac{\text{available amount of stable funding}}{\text{required amount of stable funding}}$
* numerator: each category of funding (liability and equity) multiplied by ASF factor
* denominator: each category of funding (asset) multiplied by RSF factor
  RSF factor reflect the permanence of the funding required
  lower liquidity, higher RSF


#### Counterparty Credit Risk
CVA risk: standardized approach and basic approach

#### Legislation and Regulations after Crisis
macroprudential
compensation for staff should be dependent on risk
derivatives trade must be through CCP
Office of Credit Rating
risk committee
issuers of securitizations required to retain at least 5% of each tranche



### <!-- C23 363 --> High-Level Summary of Basel III Reforms
Motivations: lessons from crisis
##### Motivations for Revising the Basel III Framework
###### Initial Phase
* tier 1 equity capital: a greater focus on going-concern loss-absorbing capacity
* higher capital level for stressed time
* RWA acutely miscalibrated (credit rating in standardized approach)
* macroprudential elements (G-SIB)

###### Revise in 2017
restore credibility of RWA and improve the comparability of banks' capital ratio (encourage standardized approach)
* enhancing robustness and risk sensitivity of standardized approach for credit risk, CVA risk and operational risk
* constraining use of internal model approaches by limits on inputs, remove internal model for CVA and operational risk
* leverage ratio buffer for G-SIB
* replace Basel II output floor 

#### Standardized Approach to Credit Risk
* improving granularity and risk sensitivity
* reducing reliance on credit rating
* output floor and enchance comparability

##### Not to Remember
* for residential real estate exposure, risk weights vary by LTV instead of single weight
* a standalone treatment for covered bond is introduced
* a standalone treatment for project finance, object finance (large asset), commodities finance

#### Internal Ratings-Based Approaches for Credit Risk
Basel II IRB approach 3 shortcomings:
* excessive complexity
* lack of comparability
* lack of robustness for certain asset classes (equity)

3 revisions:
* removing the option for advanced IRB approach for exposure to large and mid-sized corporates, exposures to banks and other financial institutions (***)
  no IRB for equity asset
* input floor for conservativism
* providing greater specification of parameter estimation to reduce RWA variability

#### CVA Risk Framework
revise CVA framework:
* risk sensitivity
* robustness
* consistency

#### Operational Risk Framework
Standardized Measurement Approach (SMA) replace the approaches before


#### Leverage Ratio Framework
additional 50% of G-SIB's risk weighted higher-loss absorbency requirment
leverage ratio G-SIB buffer: additional tier 1 capital
capital conservation ratio is constrained by tier 1 capital ratio and tier 1 leverage ratio

#### Output Floor (整体底线)
RWA must be calculated as the higher of:
* total RWA using any approach combination
* 72.5% of RWA using only standardized approach


### <!-- C24 373 --> Basel III: Finalizing Post-Crisis Reforms
#### Standardized Measurement Approach: Operation Risk Capital Charge
* business indicator
* business indicator component
* internal loss multiplier

minimal operational risk capital: $ORC=BIC\times ILM$
for banks in bucket 1 (BI less than 1 billion Euros), $ILM=1$
national supervisors may set $ILM=1$
banks which do not meet loss data standards should be set $ILM\geq 1$

* SMA is a single, non-model-based method
* AMA is able to use a range of alternative models

##### Business Indicator (BI)
derived from average data from 3 years.
$BI=ILDC_{avg}+SC_{avg}+FC_{avg}$
* ILDC: interest, lease, dividend component
* SC: service component
* FC: financial component

##### Business Indicator Component (BIC)
$BIC = BI\times \text{marginal BI coefficients}$
calculation is like individual income tax

##### Internal Loss Multiplier (ILM)
$ILM=f(LC,BIC)$
* $LC$: 15 times average annual operational risk losses incurred over previous 10 years
  5 years is OK
  if age less than 5 years, set $ILM=1$
* when $LC=BIC$, $ILM=1$


#### Loss Data Identification, Collection and Treatment
##### General Criteria
* internal loss data must be based on 10 years period
* map loss into 7 categories
* operational loss events related to credit risk that are accounted for in credit RWA should not be included in the loss data set
  like loan fraud (external fraud)
* operational loss related to market risk are treated as operational risk
  fat finger

##### Specific Criteria
loss data set
gross loss, net loss and recovery definitions:
* direct charges
  settlement to P&L account, write-downs, impairment
* external expenses direct link to operational risk event and cost of repair to restore
  legal cost
* provisions or reserves accounted for in P&L against potential operational loss impact
* definitive material financial impact temporarily booked in transitory and not reflected in P&L
* timing loss should be amortized

gross loss, net loss and recovery excludes:
* cost of general maintenance contracts on PP&E (property plant and equipment)
* upgrade or improvement expenditures
* insurance premium

### FRTB
issued 2012. Final version is Minimum Capital Requirement for Market Risk in 2016.
* liquidity horizon
* market risk capital charge

See <a href="https://rfmeng.github.io/pages/CFA%20I/CFA%20I%20-%20Fixed%20Income%20(2).html#nav2.3" target="_blank">FRTB in Market Risk</a>.
