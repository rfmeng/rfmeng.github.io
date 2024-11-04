<ndtag category = "FRM II" editdate="2024-11-04" createdate="2024-10-31" tag="Risk-Management"></ndtag>

## D. Basel Accords
Basel tower, more details
|I|II|II.5|III|
|:-:|:-:|:-:|:-:|
|1988|1999|2009|2014|

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
* supervisory preview proces: additional capital requirements
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
* $\alpha=15%$

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

capital: $MR = \max\{VaR_{t-1},m_c\times VaR_{avg}\}+\max\{sVaR_{t-1},m_s\times sVaR_{avg}\}$
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
Tier 1 capital:
* Tier 1 equity capital
* additional tier 1 capital

Tier 1 capital excludes, goodwill, intangibles, deferred tax assets, shortfall of reserves related to IRB EL. (no need to remember)













