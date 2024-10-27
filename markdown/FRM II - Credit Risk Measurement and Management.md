<ndtag category = "FRM II" editdate="2024-10-21" createdate="2024-10-21" tag="Risk-Management"></ndtag>


### <!-- 1. C1 p15 --> Fundamentals of Credit Risk
#### What is Credit Risk
Insolvency: asset less than liability

#### Transactions and Entities
loaned money, lease obligation, receivables, prepayment for goods or services.
deposits, claim or contingent claim, derivative

##### Entities Exposed to Credit Risk
###### Financial Institutions
Banks: extend credit
Asset managers: debt credit risk
Hedge Funds: funds view the probability of an entity defaulting as an opportunity to deploy capital.
Insurance Companies: underwriting activities (for loans), investment portfolio and reinsurance recoverables
Pension funds: credit risky assets

###### Corporates
account receivables
derivative trading activities
supply chain

###### Individuals
deposit, investment activity

### <!-- 2. C2 p25 --> Governance
#### The Three Lines of Defense
1. business owners: primarily own and manage risk
2. risk management, compliance and legal: monitors and oversees risk 
3. internal audit, external auditors and special audit committees: independent assurance of the risk management

#### Guidelines
also called credit policies or risk management standards
CRO
breach of guidelines: immediate termination of employment


#### Skill
##### Delegation of Authority
Credit committees: highest level approval
###### Risk Parameters
exposure, credit quality and tenor

#### Limit
the maximum loss to withstand

#### Oversight
compensation should never be based on profitability of the business
CRO reports directly to CEO and has pribileged access to risk committee
near business operation departments

### <!-- 3. C5 p57 --> Introduction to Credit Risk Modeling and Assessment
#### Development
regulatory: capital adequacy ratio
analytical: CAMEL (capital adequacy, asset quality, management, earnings and liquidity)

##### Regulatory Framework
Basel I: simplistic guidelines for credit risk
Basel II: credit risk, operational and market risk
Basel III: more strict capital requirement and liquidity

##### Analytical Methods
CAMELS (sensitivity): 1-5 points, and 1 is best

#### Credit Risk Assessment Approaches
##### Quantitative Measurement
expected loss (EL): $EL=PD\times EAD\times LGD$
* probability of default：  usually set to be one year
* Exposure at default:
* Loss given default: recovery rate = 1 - LGD

##### Types
###### Judgmental Approaches
also called expert systems or qualitative approaches
5C Analysis: character (personality), capacity (ability to repay the loan), capital, collateral, conditions (business environment)
###### Data-Driven Empirical Models
to find relationship between default and input varaibles
###### Financial Models
structural model: default is endogenous process 
reduced form models: default is exogenous random variable

### <!-- 4. C6 p71, C9 p119 --> Credit Rating
#### External Ratings
##### Credit Scoring System to Credit Rating System
data-driven method
Credit Scoring: automated analytical numerical score
Credit rating: combination of analytical and judgemental assessments

###### External Models
rating agencies such as Moody's, S&P and Fitch

###### Through the Cycle vs. Point in Time
* Through the Cycle: long-term orientation covering at least one business cycle
  less frequency, most agencies use
* Point in Time: timely update for new information

##### Development Process
data → model fitting → validation → definition and validation of ratings → implementation, monitoring and review

##### Credit Rating Agencies
See <a href="https://rfmeng.github.io/pages/CFA%20I/CFA%20I%20-%20Fixed%20Income%20(2).html#nav2.3">here</a>, mostly for long-term credit ratings. 
D is for already defaulted.

###### Criticism
1. lack of transparency and accountability, conflict of interest
2. promoting debt explosion
3. poor predictive ability
4. pro-cyclicality

#### Internal Ratings
##### Altman Z-Score Model
linear discriminant analysis
$Z=1.21x_1+1.4x_2+3.30x_3+0.6x_4+0.999x_5$
* $x_1$: working capital / total assets
* $x_2$: retained earnings / total assets
* $x_3$: EBIT / total assets
* $x_4$: market value of equity / book value of liability
* $x_5$: sales / total assets

higher than 3 is impossible to default, lower than 1.8 very possible.

#### Probability of Default
##### Definitions Related to Probability of Default
Cumulative default probability: P(issuer default in three years)
Marginal default probability (unconditional/joint): P(issuer default in third year)
Conditional PD: P(default in third year | survive in the second year)
$(1-\bar{d})^3=(1-d_1)(1-d_2)(1-d_3)$, where $d$ is conditional PD

###### Survival Effect and Mean-Reversion Effect
For investment-grade bonds, the marginal probability increases with time while speculative-grade bonds' decreases with time.

##### Migration Matrix
NR is for not rated.

##### Recovery Rate and Default Rate
LGD = 1 - RR (Recovery rate)
recovery rate is negatively related to PD


### <!-- 5. C9 p119, C12 p157 --> Estimating Default Probabilities from Credit Spreads
#### Using Hazard Rate to Estimate Default Probabilities
##### Default Intensity Model
under exponential distribution, no default within $t$ is $P(X=0)=e^{-\bar{\lambda}t}$.
$\lambda$ is conditional default probability at $dt$ and $\bar{\lambda}$ is 

#### Spread and Hazard Rate
##### Using Spread to Estimate Hazard Rate
$\bar{\lambda}(T)(1-RR)=s(T)$, expected loss = extra profit
* $\bar{\lambda}(T)$: hazard rate in $T$
* $RR$: recovery rate
* $s(T)$: credit spread in $T$

##### Credit Spreads
###### CDS Spread
pay CDS spread and receive principal insurance

###### Bond Yield Spread
bond yield spread = YTM - risk free rate
Bond's liquity is not as good as CDS
risky bond + CDS = risk-free bond
* CDS-bond basis: CDS spread - bond yield spread
  CDS-bond basis is positive during crisis
  if the bond is cheaper than par, the basis tend to be positive (bond is sold and  CDS s bought)

###### Asset Swap Spread
pays coupon on the bond, receives floating reference rate plus asset swap spread.
(?) coupon payer of the swap should pay the opponent the discounted price part: if bond price is 95 for 100 par value, 5 should be payed.

##### Matching Bond Prices
match expected loss at different time point, recovery part does not need to be discounted at default.

#### Comparison of Default Probability Estimates
##### PD from Historical Data vs. from Credit Spread
the PD from credit spread is higher, the difference between the two hazard rates tend to grow as credit quality declines
The nonsystematic risk of bond is difficult to diversify, the bond return is limited upside.

##### Real-World and Risk-Neutral Default Probabilities



### <!-- 6. C5 p57, C9 p119 --> Estimating Default Probabilities from Equity Prices
#### Merton Model
##### Assumption
assume firm with simple debt structure, consisting of a zero-coupon bond matured at T.
##### Credit Risk as Option 
payoff of equity value is $\max\{E_T-F,0\}$, where $F$ is repayment required on debt.
For equity price, $E_0=V_0N(d_1)-Fe^{-rT}N(d_2)$, $PD=1-N(d_2)$.

##### Distance to Default
$d_2$ is called DtD or DD
asset = equity + debt
to solve unobserved $V_0$ and $\sigma_V$, we could solve BSM and $N(d_1)V_0\sigma_V=E_0\sigma_E$

##### Limitations of Merton Model
applicable only to liquid, publicly traded company
rely on static and simple capital structure

#### KMV Model
Real-world PD: $d_2=\frac{\ln V_0-\ln F+(\mu-\frac{1}{2}\sigma_V^2)T}{\sigma_V\sqrt{T}}$
Risk-neutral PD is higher than real-world PD

##### Extension of Merton Model
Moody's KMV Expected Default Frequency (EDF) model and Kamakura: transform risk-neutral PD to real-world PD, find the map between DtD and real-world PD.
The default threshold: function of short-term debt and long-term debt.

If $\mu$ is given, use $\mu$.

### <!-- 7. C7 83 --> Credit Scoring and Retail Credit Risk Management
#### Retail Credit Risk
##### Basel's Definition of Retail Exposures
home mortgages: loan to value ratio
home equity loan (home equity line of credit, HELOC): hybrid between a consumer loan and a mortgage loan, secured by residential properties
installment loan: revolving loan, such as credit card
small business line
##### Retail Credit Risk vs. Corporate Credit Risk
* retail credit risk: default by a single consumer is not expensive, expected loss could be built into price
* Corporate credit risk: concentrations of exposures

##### Dark Side of Retail Credit Risk
1. not all innovative retail credit products have enough historical data
2. the security will change under different economic environment
3. the tendency to default is complex product of social and legal system
4. operational issue affects the credit assessment

##### From Default Risk to Customer value
risk based pricing

#### Credit Scoring
##### Types of Credit Score Model
* Credit Bureau Scores: known as FICO scores, developed by Fair Isaac Corporation
* Pooled models: similar strategy for customers with similar credit portfolio, tailored to industry
* Custom models:

##### Key Variables in Mortgage Credit Assessment
debt-to-income ratio, FICO, loan-to-value ratio

#### From Cutoff Scores to Default Rates and Loss Rates

##### Measuring the Performance of Scorecard
cumulative accuracy profile (CAP), consider fraction of default found and ranked scores, $\text{accuracy ratio} = \frac{\text{area under perfect actual model }}{\text{area under perfect Models}}$

diagonal line corresponds to a random model


### <!-- 8. C8 97 --> Country Risk
#### Source of Country Risk
##### Life Cycle
developing country more risk, mature markets have more stable GDP growth.

##### Economic Structure
dependency on specific area of economics will cause the economy more unstable

##### Political Risk
authoritarian governments create discontinuous risk, democratic governments create continuous risk
corruption
physical violence
nationalization or expropriation risk

##### Legal Risk

##### Composite Risk Measure

#### Sovereign Country Risk
##### Sovereign Debt
###### Foreign Currency Defaults
it is more likely to default on bank debt than official debt
Latin American accounts for a large part for soverign default
local currency defaults: the speedier restructure than break the international law
tradeoff between inflation and default
###### Consequence of Sovereign Default Risk
reputation, capital market, real output, political instability, trade retaliation

###### Factors Determining Sovereign Default Risk
* debt to GDP
* pensions/social service commitment
* revenue (tax)
* political risk
* implicit guarantees: help from rich member countries

##### Sovereign Credit Rating
the ratings are sticky
to private creditors and not to official creditors
the difference between foreign and local soverign rating results from the independence of monetary policy

##### Soverign Default Spread
there has to be a default free security in the currency
little evidence that CDS spread is superior to market spread



### <!-- 9. C4 47 --> Credit Loss Distribution
$\text{Credit VaR}=WCL-EL$, where WCL is worst case loss at the given confidence level and EL is expected loss

#### Expected Loss and Unexpected Loss
$EL=PD\times EAD \times LGD$, where LGD is also called loss rate (LR).

##### Unexpected Loss
! Unexpected is standard deviation of credit loss
$UL_i=EAD_i\times\sqrt{PD_i\times\sigma_{i,LGD}^2+LGD_i^2\times\sigma_{i,PD}^2}$
$\sigma_{PD}^2=PD\times(1-PD)$

##### Portfolio EL and UL
$EL_p=\sum EL_i=\sum EAD_i\times PD_i\times LGD_i$
$UL_p\leq \sum UL_i$

###### Unexpected Loss Contribution
$ULC_i=\frac{UL_i\sum_j UL_j\rho_{ij}}{UL_p}$

For large $n$, $ULC_i= UL_i\sqrt{\rho}$

#### Credit Loss Distribution and Capital
##### Derive Economic Capital for Credit Risk
confidence level corresponds to bank's target credit rating
$EC_p=UL_p\times CM$, where EC is economic capital, CM is capital multiplier

##### Credit Loss Distribution
highly skewed, upward limited
beta distribution is recommended

##### Problems with the Quantification of Credit Risk
the credits are illiquid assets
ignoring multi-period nature of credits

### <!-- 10. C10 135, C11 145, C12 157 --> Default Correlation and Credit VaR
#### Default Correlation
joint probability that both firms will default is $\pi_{12}$
$\rho=\frac{\pi_{12}-\pi_1\pi_2}{\sqrt{\pi_1(1-\pi_1)}\sqrt{\pi_2(1-\pi_2)}}$

##### Drawbacks of Default Correlation
joint default is relatively rare event
small correlations have large impact
computationally intensive

#### Credit VaR
some consider only losses from defaults, others also consider downgrade or credit spread changes

##### Credit VaR vs. Market VaR
horizon for credit VaR is 1 year, and for market VaR 1 day

##### Default Correlation and Credit VaR

##### The Effect of Granularity on Credit VaR
Granular: cotains more independent credits, each of which is a smaller fraction of the portfolio
For a given default probability, credit VaR decreases as the credit portfilio becomes more granular. (?) The convergence is more drastic with a high default probability. 
* (-) Higher PD, higher EL, higher VaR.
If portfolio contains a very large number of independent small positions, the credit VaR tends to be 0.

### <!-- 11. C10 135, C11 145, C12 157 --> Regulatory Capital
#### Single Factor Model
##### Gaussian Copula Model for Time to Default
define $t_1$ as the time to default of company 1.
$a_1=N^{-1}(Q_1(t_1))$, where $Q_1$ is cdf of $t_1$.

##### Model Description
$a_i=\beta_i m +\sqrt{1-\beta_i^2}\varepsilon_i$, where $m$ and $\varepsilon_i$ are independent standard normal.
The default behavior $X_i=a_i$ is divided into two parts, $\beta_i\in [-1,1]$ with market and the residual idiosyncratic risk.
$\rho_{i,j}=\beta_i\beta_j$, which reduce the number of pairwise correlation from $C_n^2$ to $n$.

##### Unconditional Default Distribution
Assume $\beta_i=\beta$ for all $i$, which implies PD is same for all companies.

##### Conditional Default Distribution
conditional on market situation $\bar{m}$, default happens if $a_i$ lower than some threshold $K$.
$a_i$ fllows $N(\beta\bar{m},1-\beta^2)$

#### Vasicek Model
Basel II internal-ratings-based's (IRB) target: find a conditional PD on the 99.9% worst case market senerio.

##### Worst Case Default Rate
$a_i=\sqrt{\rho} \bar{m} +\sqrt{1-\rho}\varepsilon_i$
default rate conditional on $\bar{m}$: $N(\frac{N^{-1}(PD)-\sqrt{\rho}\bar{m}}{\sqrt{1-\rho}})$
99.9% percentile worst case PD $WCDR = N(\frac{N^{-1}(PD)-\sqrt{\rho}N^{-1}(0.001)}{\sqrt{1-\rho}})$
capital requriement/credit VaR: $(WCDR-PD)\times EAD \times LGD$
only one 99.9% confidence level participates in the standard, just for market factor $m$
$\rho$ is called correlation parameter.

##### Regulatory Capital
if maturity is longer than 1 year, credit quality decrease but not default might happen, this shoudld be multiplied by a maturity adjustment factor (MA).

###### Basel II
$\rho$ is given

### <!-- 12. C4 47, C5 57, C10 135, C12 157 --> Economic Capital
#### Creditmetrics
##### Rating Transition Matrices
based on historical data
ratings momentum: a company downgraded recently is more likely to be downgraded again.
0.5 year transition matrices is square root


##### Credit VaR
###### Sampling and Correlation Model
use correlation of equity return as correlation of transition probability.

##### Credit Spread Risk
Historical simulation presents survivor bias: if company is alive today, it did not default in the past and no default in future.

###### Constant Level of Risk Assumptions
reblance: sell the rating changed bond and buy a new BBB bond every month.

#### Credit Risk Plus
$n$ loans and $m$ will default, the defaults are independent to each other.
If $q$ is small and $n$ is large, the distribution converges to Poisson.
The convergence exists even if the PD are different, an average is converged.
Assume default number follows Gamma, the default number follows negative binomial.
If default number has 0 std, there is no default correlation.
As $\sigma$ increases, the probability $q_n$ has higher volatility, large number and small number of defaults are more likely to happen, thus higher correlation.



### <!-- 13. C12 157, C14 183 --> Derivatives
#### Derivatives Market
small number of large counterparties

##### Counterparty Credit Risk
##### Clearing
otc derivatives could be centrally cleared

##### Market Participants
* large player: large global banks, called dealer.
  need to be a member to participate in CCP clearing
* End user: corporate, sovereign, financial institutions
  directional position and unwilling to commit to margining or posting collateral

##### Collateralization
most products are OTC traded.

* centrally cleared: daily collateralization in cash
* collateralized: bilateral derivatives
* uncollateralized: one of the parties is end user

###### Banks and End Users
end user hedge on a one-for-one (order) basis rather than macro basis.

##### ISDA 
The International Swaps and Derivatives Association

###### ISDA Master Agreement
market standard, to remove legal uncertainties
all transactions referenced are combined into a single net obligation.
default events:
* credit support default
* misrepresentation
* bankruptcy
* merger without assumption (new party merge one party and does not follow obligation)

loss for the party should be net value of derivative and collateral


#### CCP and Modeling Derivatives Risk
##### Historical Ways
* SPV (special purpose vehicle/entity, or SPE)
* derivatives product companies: generally AAA rated
  DPC's fate interacts with parent company
* monolines and CDPCs: extension of DPC, mostly for credit derivative

##### Central Clearing of OTC Derivatives
initial margin is above the variation margin
default fund: from CCP's member to avoid systemic risk
CCP absorbs the domino effect (as a buffer for systemic risk)

##### Derivatives Risk Modelling
VaR, ES

### <!-- 14. C15 207 --> Counterparty Risk
only one party takes lending risk while counterparty risk is typically bilateral

#### Settlement, Pre-Settlement and Margin Period of Risk
settlement risk: due to timing difference
margin period of risk: blank time window between margin call and margin received, there is not enough margin
pre-settlement risk: so called counterparty risk

#### Mitigations of Counterparty Risk
netting
collateral
hedging: CDS
other contractual clauses

### <!-- 15. C16 221, C17 239 --> Netting Close-out and Related Aspects
#### Cashflow Netting
payment netting: reduce time and cost associated with making payment
reduce operational risk, counterparty risk and liquidity risk

##### Currency Netting and CLS
Non-deliverable forward (NDF) transaction: currency is cash-settled based on the NDF rate and the prevailing FX rate.

###### Continuous Linked Settlement (CLS)
payent versus payment: only after both currencies have arrived does CLS Bank make the outgoing payment to both parties.

##### Multilater Netting
###### Clearing Rings
multilateral netting before the development of central clearing
Portfolio Compression: minimize gross notional of positions in the market

###### Compression Algorithm
participants can specify constraints 
total notional could be choosed as minimized target, alternative choices could be squared notinal or total number of positions

#### Value Netting
##### Close-out Netting
when a party defaults, close-out netting aims at a timely termination and settlement of the net value of all transactions
* close-out: the right to terminate transactions and cease any contractual payment
* netting: the right to offset value across transactions

if the survivor party is owed money, it could initiate a bankruptcy claim, jumping to bankruptcy queue for net value

###### Close-out Netting and ISDA
close-out netting reduces counterparty risk (pre-settlement risk)
to determine a close-out amount, use value or data offered by third party

##### Set-off
netting across product categories (loan and interest rate swap cannot set-off under default)

##### Impact of Netting
* (?) netted positions are inherently more volatile
* if credit exposures were driven by gross positions, trading with the troubled counterparty would have strong incentives to attempt to terminate
* netting redistributes value to OTC derivative creditors from other creditors

##### Multilateral Netting and Bifurcation
bifurcation: some products are clearable but others are not
partial central clearing (for only subset of trades) might not compress exposure as CCP

##### Additional Termination Event
credit quality deteriorating
tricker: rating downgrade, low market capitalization, low net value
clause: provide a replacement counterparty, provide more margin, offer third-party guarantee
potential danger:
* cliff-edge effect: single notch rating downgrade might cause a dramatic consequence



### <!-- 16. C17 239 --> Margin
#### Margin Terms
##### Rationale for Collateral
reduce counterparty risk
counterparty risk in theory can be completely neutralized under sufficient amount of margin.

##### Variation Margin
Margin period of risk (MPoR): effective delay in receiving margin

##### Initial Margin
called Independent amount in OTC market: extra margin that must be posted independently from the value of derivative
It reflects potential future exposure. (eg. 99% confidence over 10 days interval)

##### OTC Derivatives Market
For bilateral OTC derivatives, initial margin has been quite rare.
uncleared margin requirement (UMR): regulators have started to impose bilateral margin requirements, which aligning cost to CCP clearing.

##### Credit Support Annex (CSA)
* No CSA: end user
* Two-way CSA (mostly): two financial counterparties
* One-way CSA: one party receive collateral

##### Margin Terms
* Threshold
  amount below which margin is not required, leading to undercollateralization.
Threshold less than 0: post initial margin
* Minimum Transfer Amount
  smallest amount of margin that can be transfered
* Rounding
  post more and extract less
* Credit Support Amount: variation margin

##### Margin Types and Haiccuts
haircuts: discount to the value of collateral to avoid security sold at a lower price

#### Impact of Margin
##### Valuation Agent
reconsiliation the dispute

##### Impact of Margin on Exposure
margin does not reduce risk, it merely redistributes it. Other creditors will be more exposed.

##### Rehypothecation and Segregation
Rehypothecation: reuse of variation margin by the margin receiver, used as margin for another trade.This reduces the total amount of collateral in the market.
Segregation: for initial margin

##### Potential Problems of Margin
* Liquidity risk
  the non-defaulting party faces transaction costs and market volatility under default
* legal risk
  Rehypothecation and Segregation
* FX risk
* operational risk: non-standardized margin
* funding liquidity risk
  
### <!-- 17. C18 269 --> Central Clearing



### <!-- 18. C19 287 --> Future Value and Exposure
#### Metrics for Credit Exposure
##### Credit Exposure
$\text{Credit Exposure}=\max\{\text{value},0\}$
shorting options has 0 credit exposure

* Expected Future Value (EFV)
* Potential Future Exposure: equivalent measure to VaR
* Expected Positive Exposure (Expected Exposure): conditional mean on $E>0$
* Expected Negative Exposure
* Average EPE (Loan Equivalent): average EPE across all time horizons


#### Exposure Profile of Various Securities
##### Bond and Loans
exposure for loan may decline with time because of possibility of prepayment
##### Forward
square root of time
##### Interest Rate Swap
peaked shape because of payment
##### Cross-Currency Swap Exposure
combination of IRS and FX forward: fixed rate in one currency and floating rate in anther currency
The contribution of FX forward is larger

##### Swaption
forward starting swap: forward
swaption: option on whether choose to enter a swap contract with strike
after strike date, EPE for swaption is smaller than forwad starting swap because it does not exercise on some paths.

##### Credit Derivatives
CDS's PFE: has a jump due to default








#### The Impacts on Exposure




### <!-- 19. C12 157, C15 207, C20 309  --> CVA

























