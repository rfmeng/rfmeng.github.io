<ndtag category = "FRM II" editdate="2024-11-10" createdate="2024-09-11" tag="Portfolio-Management"></ndtag>

## A. Factor Investing
### <!-- C1 p13 --> Factor Theory
#### The 2008-2009 Financial Crisis
Many asset classes crash all at once (fixed income, equity, hedge fund, commodity).
The concept of diversification seems dead.

#### Factor Theory
Factors are to assets what nutrients are to food.
1. Factors matter, not assets
2. Different investors need different risk factors.
3. Assets are bundles of factors

#### CAPM
Utility is $U=E(R)-\frac{1}{2}\gamma\sigma^2$, we can get $E(R_M)-r_f=\bar{\gamma}\sigma_M^2$, where $\bar{\gamma}$ is the risk aversion of the average investor.
As the market becomes more volatile, the expected return of the market increases and equity prices contemporaneously fall. This happens in 2008 crisis and the realized return is indeed high.

? Higher beta means low diversification benefits.
If the payoff of an asset tends to be high in bad times, this is a valuable asset to hold and its risk premium is low.


#### Multifactor Models
? arbitrage pricing theory
? pricing kernel

#### Failures of the CAPM
Mean-variance utility: asymmetric treatment of risk
single period investment
homogeneous expectations
inidividual investors are price takers
information is costless and available to all investors


#### The Fall of Efficient Market Theory
Weak form, semi-strong form and strong form

The explanations of deviations from efficiency have two froms:
1. Rational explanation: we have not found all factors
2. Behavioral explanation: people underreact or overreact to events; there are structural barriers

### <!-- C2 p26 --> Factors
#### Value Investing
* Macro, fundamental-based facotrs
* Investment factors
  * static factors
  * dynamic factors (hedge fund)

#### Macro Factors
Macro factors affect all investors and the prices of assets.
A shock to a factor matters more than the level of a factor.
##### Economic Growth
Volatility tends to be high during bad times.
##### Inflation
High inflation tends to be bad for both stocks and bonds.
##### Volatility
Volatility and stock returns have negative relations (leverage effect).
Bonds offer some respite during high volatility.
Manage Volatility: long put, volatility swap
##### Other Macro Factors
productivity, demographic, political (less need to pay attention to because it changes at longer time window, like decades)

#### Dynamic Factors
style factor, smart beta: Fama-French value factor and size factor and momentum factor
Since the mid-1980s there has not been any significant size effect, because rational investors bid up the price.
#### Value Factor
Value investing: long value stocks (high book-to-market ratio) and short growth stocks.
book-to-market ratio: net asset / market value
Rational theory: value firms are riskier because that cannot shift their frim activities to more profitable activities in bad times.
Behavioral theory: investors tend to overextrapolate past growth rates in to the future.


##### Momentum Factor
Four-factor model.
WML or UMD, winner minus losser
Behavioral theory: delayed overration and underreaction

### <!-- C3 p41 --> Alpha (and the Low-Risk Anomaly)

#### Active Management
##### Definition of Alpha 
Alpha is average return in excess of a benchmark.
Tracking error is the standard deviation of alpha.
Information ratio: $IR=\frac{\text{active return}}{\text{tracking error}}=\frac{\alpha}{\bar{\sigma}}$. IR is sharpe Ratio when the benchmark is risk-free rate.

##### Creating Alpha
###### Grinold's fundamental law
$IR\approx IC\times \sqrt{BR}$, where $IC$ is correlation of the manager's forecast with the actual returns and $BR$ is how many bets are taken.
Limitations: 
* IC are assumed to be constant across BR, actually it drops with scaling
* Difficult to have truly independent forecasts in BR, long 10 value stocks and short 10 growth stocks does not mean making 20 bets.

#### Factor Benchmarks
Ideal benchmark:
* well defined
* tradable
* replicable
* adjusted for risk
##### Factor Regressions
(? why include rf) Risk adjusted regression $r_t-r_{ft}=\alpha+\beta(R_t-r_{ft})+\varepsilon_t$
t-test statistic for two sided test is 1.96 for 95% and 2.58 for 99%.
##### Time-Varying Factor Exposures
Style analysis seeks to rectify two potential shortcomings of factor regression:
* Fama-French portfolios are not tradable
* factor loadings may vary over time

Regression based on a shorter but rolling time window with index fund, and get a seires of beta.
##### Non-Linear Payoffs
buying and selling options changes the distribution of returns and spell masquerade alpha.

#### Low Risk Anomaly
Stocks with low betas and low volatilites have high returns.
Minimum variance portfolios do better than the market portfolio.
Explanation:
* Leverage constraints: investors are unabe to take on more leverage
* Agency problems: fund managers long stocks only and thus cannot short negative alpha stocks.
* Investors prefer high-volatility stocks and bid up stocks.


## B. Portfolio Risk Management
### <!-- C4 p65 --> Portfolio Construction
* This chapter proceeds as GD video, not as textbook.
#### Inputs for Portfolio Construction
##### 5 Inputs
1. current portfolio
2. alpha
3. covariances
4. active risk aversion
5. transactions costs
##### Refining Alphas
From naive forecast to raw forecast, and finally refining alpha. Naive forecast refers to naive factor regression, and raw forecast refers to some investment view.
Refining alphas are adjusted so that they are in line with investor's desires for risk contral and various constraints.
###### Scale the Alphas
(?) $\alpha = \sigma\times IC\times \text{score}$, where score follows $\mathcal{N}(0,1)$.
* (-) This should be interpreted as we get a score $\frac{\alpha}{\sigma\times IC}$ which follows normal.
###### Trim Alpha Outliers
remove 3 std outliers.
###### Neutralization
Benchmark might have alpha itself, which should be removed. 
Benchmark-neutral and cash-neutral alphas:
* if benchmark has alpha $\Delta\alpha$
* stock's alpha should be adjusted with $\beta\times \Delta\alpha$


##### Active Risk Aversion
Utility of alpha is of form $\alpha_p-\lambda_A\sigma_\alpha^2$, with fixed IR, we have optimal point $\lambda_A=\frac{IR}{2\sigma_\alpha}$.
##### Transaction Costs
Transaction costs should be amortized over the investment horizon.
If the manager is not sure of his alpha, less revision may be a safeguard.
Rebalancing for very short horizons would involve frequent reactions to noise not signal.

$MCVA_n=\alpha_n-2\lambda_A\sigma_\alpha MCAR_n$
* marginal contribution to value added
* marginal contribution to active risk: change of $\sigma_\alpha$ as more of stock $n$ added.


#### Portfolio Construction Techniques
##### Screen
Rank assets by alpha, select top to buy and bottom to sell
Screen is robust, it depends only on ranking.
##### Stratificaion
split assets into mutually exclusive categories and do screen for each category
##### Linear Programming
objective of linear programming: maximize the portfolio's alpha less traction costs while remaining in the risk control dimensions.
##### Quadratic Programming
More inputs mean more noise.

#### Dispersion
Difference between maximum return and minimum return among all the separate account portfolios.


### <!-- C5 p81 --> Portfolio Risk: Analyticla Methods
Two assumptions:
1. delta-normal model: normally distributed
2. traditional portfolio analysis: convariance matrix

(95% z score: 1.645, 99% z score: 2.326)

#### Portfolio VaR
##### Diversified VaR
$\sigma_p = \sqrt{w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2 \rho \sigma_1\sigma_2}$
$VaR_p=z_\alpha\sigma_p V_p=\sqrt{VaR_1^2+VaR_2^2+2VaR_1VaR_2\rho}$

##### Undiversified VaR
sum of individual VaRs
diversification benefit: difference between diversifed VaR and undiversified VaR

##### Correlation
Under assumtption of same $\rho$ and $\sigma$ and $w$ across the portfolio, we can get $\sigma_p = \sigma_i\sqrt{\rho}$

#### VaR Tools
##### Marginal VaR
$MVaR_i=\frac{\partial VaR}{\partial \text{investment}}=\frac{\partial zV_p\sigma_p}{\partial V_pw_i}=z\frac{\partial \sigma_p}{\partial w_i}=z\frac{Cov(R_i,R_p)}{\sigma_p}=\frac{VaR_p\beta_i}{V_p}$

##### Incremental VaR
the change in VaR owing to a new position
$\text{Full Incremental VaR}=VaR_{p+a}-VaR_p$
$\text{Incremental VaR}\approx MVaR_iV_i$

##### Component VaR
$CVaR_i=MVaR_iV_i$
Percentage contibution to VaR of component: $\frac{CVaR_i}{VaR_p}=w_i\beta_i$

#### Using VaR for Risk Management
1. Global minimum VaR
Lowering position with the highest MVaR and adding position with the lowest MVaR.
When reaching global minium VaR, all MVaR and beta must be equal.
2. Taking return and risk into consideration
maximize Sharpe ratio $\frac{R_p-R_f}{VaR_p}$, so add allocation to the postion with the highest excess expected return to marginal VaR


### <!-- C6 p95 --> VaR and Risk Budgeting in Investment Management
#### Specific Risks in Investment Management
##### Types of Risks
1. abolute risk is about dollar loss 
   relative risk is about loss relative to its benchmark
2. policy-mix risk is about passive strategy (risk of tracking error when benchmark is mix of index)
   active-management risk is the opposite

##### Funding Risk 
funding risk: asset less than liability
It is for defined benefits plan: employer takes responsibility of investment; as opposed to defined contribution plan, employee takes responsibility
Funding risk: the assets will not be sufficient to cover the liabilities of the fund.

###### Surplus
$\text{Surplus} = \text{Assets} - \text{Liabilities}$
$R_\text{surplus}=\frac{\Delta \text{Surplus}}{\text{Asset}}=R_\text{asset}-\frac{L}{A}R_\text{liability}$
$SaR=|E(\Delta surplus)-zc\sigma_{surplus}|$
confidence interval

###### Sponsor Risk
cash-flow risk: fluctuation in contributions
Economic risk: violation in business
* if the firm enjoys greater profit, surplus risk may be less of a concern

#### Risk Budgeting
|Characteristic|Sell Side|Buy Side|
|:-:|:-:|:-:|
|Horizon|short (1 day)|long|
|Turnover|rapid|slow|
|Leverage|high|low|
|Risk Measures|VaR|tracking error|
|Risk contemporaneously|position limits|diversification|

investment process of large investors: 
* strategic, long term asset allocation study
* delegate fund managers


##### VaR Applications to Investment Management
instituions exposed to diversity of risk
using VaR to monitor and control risk:
* check complicance: unauthorized investment
* monitor risk: reverse engineered to understand where risk comes from

##### Risk Budgeting
decomposing the aggregate risk of a portfolio into its constituents
risk budget for specific asset class and active manager

* across asset classes: confirm portfolio VaR does not exceed limit
* across active managers:
  (?) weight of portfolio managed by manager: $w_i=\frac{\frac{IR_i}{TE_i}}{\frac{IR_p}{TE_p}}$
  residual weight is allocated to index
  relative risk budget: tracking error VaR
  * (-) maximize portfolio IR

### <!-- C7 p107 --> Risk Monitoring and Performance Measurement
VaR vs. Tracking error
#### Three-Legged Risk Management Stool
* risk plan
* risk budget
* risk monitoring

#### RMU & Performance Measurement
##### Risk Management Unit (RMU)
measure risk but not manage risk

##### Liquidity Consideration
liquidity duration: $LD_i=\frac{Q_i}{0.15\times V_i}$
* $Q_i$: number of shares held in security
* $V_i$: daily volume of security
* 15%: do not exceed 15% if daily volume

##### Performance Measurement
risk adjusted performance 
green zone: actual outcomes compared to target, green / yellow / red zone



### <!-- C8 p129 --> Portfolio Performance Evaluation

#### Conventional Theory

##### Return Calculation
* time weighted return: geometric average
  ability to select investment underly, suited for mutual fund manager
* dollar weighted return: IRR
  investment time choosing
  suited for hedge fund manager
calculator

##### Risk Adjusted Performance Measures
Sharpe ratio: $\frac{R_p-R_f}{\sigma_p}$
Treynor ratio: $\frac{R_p-R_f}{\beta_p}$
* well-diversifed portfolio: Sharpe ratio and Treynor ratio give the same ranking
* not well-diversifed portfolio: Treynor ratio may be ranked higher

Jensen's alpha: $R_p-[R_f+\beta_p(R_M-R_f)]$
information ratio: $\frac{\alpha_p}{\sigma (\alpha_p)}$
Modigliani-squared Measure ($M^2$): $M^2=\frac{\sigma_M}{\sigma_p}(R_p-R_f)-(R_M-R_f)$, same ranking as Sharpe ratio


#### Market Timing
shifting fund between market index and safe asset

##### Regression
* no market timing ($b$ is constant): $R_p-R_f=a+b(R_M-R_f)+e_p$
* Treynor and Mazuy: $R_p-R_f=a+b(R_M-R_f)+c(R_M-R_f)^2+e_p$
  $c>0$ means there exists market timing
* Henriksson and Merton: $R_p-R_f=a+b(R_M-R_f)+c(R_M-R_f)D+e_p$
  $D$ is a dummy variable with 1 for $R_M>R_f$
  $c>0$ means there exists market timing

##### Call Option Models
$K=S_0(1+R_f)$
hold a safe security and a call option, we will get $S_0(1+R_f)$ if $S_T<K$ and $S_T$ if $S_T>K$ 
the management fee should be the value of call option (perfect timing)

#### Performance Attribution
Attribution for alpha.
bogey: benchmark

##### Attribution System
* asset allocation: broad asset market allocation choices across equity, fixed income
* selection: sector choice with in each market and security choice within each sector

Calculation:
* total contribution from asset class $i$: $w_{Pi}R_{Pi}-w_{Bi}R_{Bi}$
* contribution from asset allocation:  $(w_{Pi}-w_{Bi})R_{Bi}$
* contribution from security selection:  $(R_{Pi}-R_{Bi})w_{Pi}$ 



## C. Hedge Fund
### <!-- C9 p159 --> Hedge Funds
#### Characteristics of Hedge Funds
##### Databases of Hedge Funds
* selection bias: select better product to report
* backfill bias: when a new fund replaces a deleted fund in an index, the past performance of the new fund is inserted

Issues from Illiquid Assets: 
* lower correlation
  regression with additional lag of the market factors and sum the coefficient
* lower volatility
  taking autocorrelation into account when extrapolating to longer horizons
* higher autocorrelation

##### Evolution of Hedge Fund Industry
fall of LTCM
burst of dot-com bubble
instituion investors enter hedge fund

#### Hedge Funds Strategy
* Directional style: trending following
  * commodity trading advisors (CTA)
  * global macro: anticipate price movement, a top-down approach 
    flexible, any market with any instrument
* event-driven strategy
  extreme tails
  * merger arbitrage: capture spreads in M&A transactions after announcement
    in a fixed exchange ratio stock merger, one could long and short according to merger ratio
  * distressed securities: trade at discount
    buy and improve its operation
* relatvie value and arbitrage like strategy
  * fixed income: statistic or economic
    * swap spread trade: enter swap and repo, difference between Libor and repo
    * yield-curve spread trade: yield curve reversion
    * mortgage spread trade: prepayment rate
    * fixed income volatility trade
    * capital structure or credit arbitrage trade: misprice among equity and debt
  * convertible arbitrage: convertible bond = bond + call on stock
    misprice or vega trading
  * pair trading
* Niche strategy
  * dedicated short: net short
  * emerging market: transitional countries
  * equity market neutral: 0 beta

#### Risks in Hedge Funds
##### Hedge Fund Performance
risk profile change rapidly, hard to evaluate

##### Covergence of Risk Factors
under stress, all strategies will lose
risk cannot be mitigated by spreading to different hedge fund

##### Agency Problem
asymmetry in risk sharing between principal and agent
* high water mark: avoid incentive double counting
* lower incentive fee
* high fund closure cost
* force a fund manager invest in his fund

### <!-- C10 p199 --> Performing Due Diligence on Specific Managers and Funds
view of FoF manager
《对冲基金分析——FoF基金投资尽职调查指引》
#### Due Diligence Basics
##### Reasons for Failures
* bad investment
* fraud
* extreme event: leverage
* lack of liquidity
* poor control: insider trading

##### Due Diligence Process
due diligence questionnaire for hedge fund to complete

* Investment Management
  * Strategy
    * stop loss
  * equity ownership
  * track record reliable
  * managers
* Risk Management
  * security valuation
  * leverage and liquidity
  * consistency of fund term with the investment strategy
* operational environment
  * interncal control
  * documents and disclosure
  * service provider
* business model assessment
  * adequate cash
  * working capital come from
  * succession plan
  * break-even AUM
  * fraud risk


### <!-- C11 p213 --> Finding Bernie Madoff: Detecting Fraud by Investment Managers
a paper
#### Fraud by Investment Managers
Bernard Madoff: Ponzi scheme
mandatory disclosure

#### Information Disclosure
investment advisers: asset management or advisors
Form ADV could be used to anticipate fraud risk

#### Predicting Fraud
* disciplinary history:
  * past fraud/past affiliated fraud: no
  * past regulatory/past civil or criminal: yes
* conflicts of interest
  * referal fee: yes
  * interest in transaction (interest related): yes
  * soft dollars (other services): no
* monitoring:
  * broker in group: yes
  * Investment Company Act: yes
  * custody: no
  * dedicated CCO (chief compliance officer): no
* client type:
  * hedge fund clients: no

#### Compensated for Fraud Risk
no evidence that investors receive compensation for fraud risk

##### Barrier and Costs
lack of compensation does not mean investors are irrational because of cost of information
* barriers to access Form ADV

##### Improving Ways
allowing historical Form ADV









