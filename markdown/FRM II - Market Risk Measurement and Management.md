<ndtag category = "FRM II" editdate="2024-10-10" createdate="2024-10-10" tag="Risk-Management"></ndtag>




### <!-- C1 p13 --> Estimating Market Risk Measures
#### Data
Geometric return data: $R_t=\ln \frac{P_t+D_t}{P_{t-1}}=\ln(1+r_t)$

#### Estimating Historical Simulation VaR

#### Estimating Parametric VaR
1. Normal VaR
   PnL or arithmetic return is normal.
   $VaR = |\mu-z_\alpha\sigma|$, where inside the absolute value sign it is usually a negative number
2. $P_t=e^{R_t}P_{t-1}$ where $R_t$, called geometric return, follows normal. This implies $P_t$ and VaR follow lognormal. 
   $VaR(\alpha)=(1-e^{\mu_R-z_\alpha\sigma_R})P_{t-1}$

#### Estimating Coherent Risk Measures
Expected shortfall (ES) is a coherent measure and is subadditive.
Calculation: average of tail VaR of different percentile.
#### Estimating the Standard Errors of Risk Measure Estimators
confidence interval

### <!-- C2 p29 --> Non-Parametric Approaches
#### Estimation of Historical Simulation VaR and ES
##### Basic Historical Simulation
equal weight

##### Bootstrap Historical Simulation
resample with replacement, get multiple samples, calculate multiple VaR and take average

##### Non-parametric Density Estimation
Basic historical simulation only estimates discrete VaR value, 95.1% VaR is not available with 100 PnL observations.
Draw lines through mid-points on the edges of the bars of histogram to gain empirical pdf.
#### Weighted Historical Simulation
##### Shortfall of Traditional Simulation
equal-weight structure makes risk estimates unresponsive to major events: rare large loss in the tail could not be reflected into VaR.
ghost effects: a VaR that unduely highly because of small cluster of high loss observations and the measured VaR will continue to be high until n days.

##### Age-Weighted
exponential weighted
it gives us the option of letting our sample size grow over time.

##### Volatility-Weighted
$r_{t,i}^*=\frac{\sigma_{T,i}}{\sigma_{t,i}}r_{t,i}$, where $r_{t,i}$ is actual return for asset $i$ on day $t$, $\sigma_{t,i}$ is volatility forecast on day $t$, $\sigma_{T,i}$ is current forecast of volatility.

##### Correlation-Weighted
historic returns multiplied by revised correlation matrix (equivalently variance-covariance matrix)
(variance-covariance matrix $\Sigma=A^TA$, $R^*=A_TA_t^{-1}R$)

##### Filtered Historical Simulation
using GARCH to adjust return and then bootstrap


### <!-- C3 p50 --> Parametric Approaches: Extreme Value
#### Generalized Extreme Value Theory
Generalized extreme-value (GEV) distribution
If tail shape $\xi>0$, GEV becomes the Frechet distribution, tail is heavy, similar with Levy, t and Pareto distribution.
If tail shape $\xi=0$, GEV becomes the Gumbel distribution, tail is light, similar with normal and lognormal.
If tail shape $\xi<0$, GEV becomes the Weibull distribution, lighter tail.
###### Which One to Choose
Choose Gumbel if tail index is insignificant and Frechet otherwise.
A safer option is always to choose the Frechet.


#### Peaks-Over-Threshold (POT)
Deals with the application of EVT to the distribution of excess losses over a high threshold.
$F_u(x)=P\{X\leq X+u|X>u\}=\frac{F(x+u)-F(u)}{1-F(u)}$

##### Generalized Pareto Distribution
two parameters: a positive scale parameter $\beta$ and a tail index parameter $\xi$.

##### Estimation
VaR and ES:
* $u$ threshold in percentage term
* $N_u$ is the number of observations exceeding threshold
* $n$ is the total observations

#### Multivariate EVT
curse of dimensionality: as the dimensionality rises, Multivariate EV events rapidly become much rarer.


### <!-- C4 p61 --> Backtesting VaR
(? whether to remember statistic critical value)
#### Setup for Backtesting
#### Model Backtesting with Exceptions
##### Model Verification Based on Failure Rates
A test can be applied verify the model when $T$ is large
$H_0$: the model is correctly calibrated.
Test statistic $z=\frac{x-pT}{\sqrt{p(1-p)T}}$ which follows standard normal, where $x$ is the number of exceptions.
The test should two-sided because $x$ could be too small and too large.

##### Unconditional Coverage Model 
The exceptions should be evenly spread over time, the model ignores conditioning.
(ignore formula) log-likelihood ratio, $LR_{uc}=-2\ln(1-p)^{T-N}p^N+2\ln(1-\frac{N}{T})^{T-N}(\frac{N}{T})^N$, which follows Chi-square with one degree of freedom.
1. nonrejection region $\frac{N}{T}$ should shirnk with more data obtained
2. for small value of $p$, it becomes increasing difficult to confirm deviations, resulting in systematically overestimates risk. 

##### Conditional Coverage Model 
observed exceptions could cluster or bunch.
$LR_{cc}=LR_{uc}+LR_{ind}$
If $LR_{ind}$ exceeds critical value, independence assumption should be adjected and conditional model should be used.

##### Type I and Type II Error
Type I error: correct model is rejected
Type II error: incorrect model is not rejected
$P(\text{Type I error})=\alpha$, power of test: $1 - P(\text{Type II error})$

#### Basel Rules
Backtesting is necessary to allow internal VaR(99%) models for capital management.
up to 4 exceptions are acceptable (current version is 99% VaR for 250 trading days, 2.5 theoretically), there is progressively increasing multiplicative factor. ($k$ is for capital requirement)
##### When to apply penalty
1. Basic integrity of the model: the penalty should apply.
2. Model accuracy could be improved: the penalty should apply.
3. intraday trading: the penalty should be considered.
4. bad luck: no guidance, except it is expected to occur at least sometime.

### <!-- C5 p71 --> VaR Mapping
#### Basis of VaR Mapping
the current values of the portfolio positions are replaced by exposures on the risk factors.
Two kinds of mapping:
* exact allocation: like derivatives
* estimation: a stock is replaced by stock index by regression

#### Methods of VaR Mapping
##### Fixed Income portfolio
factor: zero-coupon bonds
par value bond: intial price equal to par value
###### Principal Mapping
one risk factor is chosen that corresponds to the average portfolio maturity.
overstates the true risk, because it ignores intervening coupon payments (shorter maturity, smaller VaR ratio)
###### Duration Mapping
one risk factor is chosen that corresponds to the average portfolio duration.

###### Cash-Flow Mapping
Undiversified VaR: sum of VaR of PV of all cash flows, assuming perfect correlation
Diversified VaR: (if $\mu=0$) $VaR_p=\sqrt{VaR_1^2+VaR_2^2+2\rho VaR_1VaR_2}$
 
###### Benchmarking
duration mapping
tracking error VaR: VaR of the deviation between portfolio and benchmark


##### Linear Derivative
###### Forward
long foreign currency forward = long foreign currency spot + long foreign bill + short U.S. bill
when calculating dollar PV, use spot exchange rate
###### FRA


###### Interest-Rate Swap
floating and fixed rate swap
##### Nonlinear Derivative
call = long asset - short bill (from BS formula)



### <!-- C7 p117 --> Correlation Basics: Definitions, Applications and Terminology
#### Financial Correlation Risk
CDS: pay fixed CDS spread and obtain principal in case of default
correlation risk occurs when long Spain bond and buy CDS from another bank, the worst case is they both default.

#### Correlation in Trading
1. value of multi-asset option is very sensitive to correlation
2. quanto option: options that allow domestic investor to exchange his option payoff in a foreign currency back into home currency at a fixed exchange rate.
   the more positive the correlation, the lower the price for the quanto option call
3. correlation swap
4. another way of buying correlation is buy call on index and sell call on individual stocks


#### Correlation in Risk Management
1. Market Risk
2. Credit Risk: default correlation within sectors higher than between sectors
   Investment grade bond default probability increases with maturity, bond in distress shows the opposite. If the company survives the problematic period, default rate will decrease.
3. Systemic risk: systemic risk and correlation risk are highly correlated.
4. Concentration risk

#### Correlation in the Financial Crisis
CDO: collateralized debt obligations
equity tranches value increases as correlation increases, but default probability increases and finally decreases in value.
correlations between the tranches increased.





### <!-- C8 p137 --> Empirical Properties of Correlation
#### Correlation and Correlation Volatility
correlation among stocks is highest during recession.
correlation volatility is highest in normal economic states
positive relationship between correlation level and correlation volatility

#### Mean Reversion
mean reversion is presented if there is negative relationship between $S_t-S_{t-1}$ and $S_{t-1}$
$S_t-S_{t-1}=a(\mu_S-S_{t-1})\Delta t+\sigma_S\varepsilon\sqrt{\Delta t}$, where $0\leq a\leq 1$ is mean reversion rate.
get $a$ through regression $S_t-S_{t-1}$ on $S_{t-1}$

#### Autocorrelation
$AC(\rho_t,\rho_{t-1})=\frac{Cov(\rho_t,\rho_{t-1})}{\sigma_t,\sigma_{t-1}}$
AR(1) model: $S_t=a\mu_S+(1-a)S_{t-1}$, therefore $1-a = AC$ because of correlation is stationary

autocorrelation is highest under 2-day lag

#### Best-fit Distributions for Correlations
Equity: Jonhnson special bounded distribution
Bond: GEV and then normal
default probability: Jonhnson special bounded distribution


### <!-- C9 p145 --> Financial Correlation Modeling 
#### Copula functions
A copula is a distribution function with standard uniform marginal distributions.
Sklar theorem: given marginal distribution $F$ and $G$, joint distribution $H$ and copula $C$ are one-to-one, $C(u,v)=H(F^{-1}(u),G^{-1}(v))$.

##### Gaussian Copula
$C_G(u_1,u_2)=M(F_1^{-1}(u_1),F_2^{-1}(u_2);\rho)$, where $M$ is CDF of standard normal.

###### CDO Valuation
cumulative default probabilities $Q$ for entity $i$ at a fixed time $t$.
The Gaussian default time copula $C_{GD}=M(N^{-1}(Q_1(t)),N^{-1}(Q_2(t));\rho)$

### <!-- C11 p167 --> The Science of Term Structure Models
#### Binomial Interest Rate Tree
adjust up probability and down probability such that the current value match the market price.
##### Arbitrage-Free Valuation of Derivatives
The law of one price: same good same price

##### Risk-Neutral Pricing
the difference between true probability and risk neutral probability is described in terms of drift in interest rates

#### Issues with Interest Rate Tree Model
##### Recombineing Tree vs. Non-Recombining Tree
Non-recombining tree has 4 nodes at state 2, which supports state-dependent volatility.

##### Option-Adjusted Spread
the spread such that the market price of a security equals its model price when discounted values are computed at risk-neutral rates plus that spread.
adding 10 basis points to the discount rates (between every state)

##### Appropriateness of BSM Model
BSM does not apply to bond options
1. bond price is not random, it must converge to its face value at maturity, so does volatility.
2. BSM assumes interest rate is constant


### <!-- C12 p179 --> The Evolution of Short Rates and the Shape of the Term Structure
#### Expectations
determines level of interest rate

#### Volatility
determines downward-sloping shape of interest rate curve, resulting from the effect of convexity on the spot rate.
$E[\frac{1}{1+r}]>\frac{1}{E[1+r]}$, yield is reduced by convexity.

#### Risk Premium
determines upward-sloping shape of interest rate curve.
In short term, the risk premium effect dominates and the term structure is mildly upward-sloping.



### <!-- C13 p187 --> The Art of Term Structure Models: Drift
#### No Drift
$dr=\sigma dw=\sigma \varepsilon \sqrt{dt}$
Interest Rate Tree: $u=r+\sigma\sqrt{dt}$, $d=r-\sigma\sqrt{dt}$
Limitations: flat interest rate term strucutre and flat volatility term structure 

#### Constant Drift
risk neutral drift is combination of expectation and risk premium
$dr=\lambda dt + \sigma dw=\lambda dt + \sigma \varepsilon \sqrt{dt}$
assumes parallel shift of term structure curve if interest rate changes

#### Ho-Lee Model: Time-Dependent Drift
$dr=\lambda_t dt + \sigma dw=\lambda_t dt + \sigma \varepsilon \sqrt{dt}$
Ho-Lee model is arbitrage-free model, the $\lambda_t$ is used to match the market prices.
Quote the prices of securities that are not actively traded based on the prices of more liquid securities.

##### Issues
It assumes market prices are fair, but security prices may be distorted due to non interest rate factors.
For the purpose of value securities relative to one another, equilibrium models should be used.

#### Vasicek Model: Mean-Reverting Drift
$dr=k(\theta-r)dt+\sigma dw$
##### Interest Rate Tree
The tree does not recombine. To recombine it, take average of the two nodes and adjust the related risk neutral probability and interest rate with two equations (mean and std).

##### Half Time
Expectation of the rate after $T$ years: $r_0e^{-kT}+\theta(1-e^{-kT})$
The time it takes the factor to progress half the distance toward its goal: $\tau=\frac{\ln 2}{k}$

##### Effectiveness 
The standard deviation increases with horizon more slowly. The total variance will increase, but the annualized volatility will decrease.
It supports nonparallel shift.



### <!-- C14 p199 --> The Art of Term Structure Models: Volatility and Distribution
#### Time-Dependent Volatility
$dr=\lambda(t)dt+\sigma(t)e^{-at}dw$, where $a$ is decay rate.

##### Compared to Vasicek Model
total variance resembles the impact of mean reversion.
It is parallel shift model while Vasicek implies nonparallel shift.
To quote fixed income option prices (that are not easily observable), use time-dependent volatility model; to value and hedge fixed income securities, use Vasicek.

#### Cox-Ingersoll-Ross Model
$dr=k(\theta-r)dt+\sigma\sqrt{r}dw$, where $\sigma$ is yield volatility and $\sigma\sqrt{r}$ is annualized basis-point volatility.
Interest rates are bounded by 0.

#### The Courtadon Model
$dr=k(\theta-r)dt+\sigma rdw$

#### Lognormal Model
$dr=ardt+\sigma rdw$

#### Lognormal Model with Deterministic Drift
$dr=a(t)rdt+\sigma rdw$

#### Lognormal Model with Mean Reversion: Black-Karasinski Model
$dr=k(t)(\ln\widetilde{\theta}(t)-\ln r)+\sigma(t) rdw$


### <!-- C6 p85 --> Messages from the Academic Literature on Risk Management for the Trading Book
#### Lessons on VaR Implementation
##### Time Horizon
Market Risk Amendment sets horizon to be 10 days and allows to use square-root of time scaling of one-day VaR.
Appropriate time horizons should be set for different products.
Square-root will overestimate VaR if underlying exhibits GARCH(1,1) and underestimate VaR if the process has jumps.

##### Time Varying Volatility
Volatility forecastability decays quickly with time horizon, so capturing time-varying volatility may not be as important when VaR horizon is long.

##### VaR Backtesting
Actual backtesting: use historical data to estimate portfolio return, this is less informative when composition of the portfolio is changed.
Hypothetical backtesting: use historical data to estimate mean and std of component, and then estimate the portfolio distribution.
Banks backtest 1-day VaR, but 1-day VaR does not necessarily imply 10-day VaR.

##### Integrating Liquidity into VaR Models
Exogenous liquidity: the transaction cost for trades of average size
Endogenous liquidity: the volume of trade is large enough such that the bid ask spread cannot be taken as given, but is affected by the trades themselves.
only exogenous liquidity risk is integrated into VaR: $\text{cost of liquidity}=\text{position value}\times\frac{\mu+q_{99\%}\sigma}{2}$
to integrate endogenous liquidity, estimate average transaction price of optimal liquidation strategy

#### Risk Measurement for the Trading Book
coherent risk measure: subadditivity, positive homogeneity, monotonicity, transition property
backtesting ES is more complicated

##### Spectral Risk Measures
Customized average of the whole distribution.
Larger loss, larger weight.

##### Risk Aggregation
compartmentalized approach: the sum of risks measured separately (market, operations, credit), assume $\rho=1$
unified approach: $\rho<1$

Top-down approach: portfolio divided to market, credit and operational, assume $\rho=1$
bottom-up: risk factors, $\rho<1$

#### Balance Sheet Management
leverage is procyclical


### <!-- C16 p215 --> Fundamental Review of the Trading Book
FRTB: a consultative document issued by Basel Committee
#### Background
trading book: market risk capital
banking book: credit risk capital
this has in the past given rise to regulatory arbitrage.

##### Amendment
Market risk in Basel I is 10-day 99%
FRTB requires stressed 97.5% ES
For normal distributions, the two values are similar.

#### Liquidity Horizions
Basel I: 10-day
Basel II.5: 10, 20, 40, 60, 120 

#### Market Risk Capital Charge
Basel III: standardized approach and internal model approach

##### Standardized Approach
###### Risk Sensitivity Approach
1. 7 risks classes corresponding to trading desks: general interest rate, foreign exchange, commodity, equity, three categories of credit spread risk
2. Within each risk class, delta risk charge, vega risk charge and curvature risk charge are calculated.

###### Default Risk Charge
1. credit spread risk is handled using risk sensitivity approach.
2. default risk (jump-to-default) is handled by a separate default risk charge.
   exposure \* LGD \* default risk weight

###### Residual Risk Add-on
such as exotic options
calculation: notional amount \* risk weight

##### Internal Models Approach
Historical simulation approcah to estimate stressed ES with 97.5% confidence.
###### Credit Risk
1. credit spread risk: handled in a similar way to other market risk
2. jump-to-default risk: in banking book based on 1-year 99.9% VaR.

###### Backtesting
FRTB does not backtest stressed ES, it is not possible to backtest stressed measure.
1-day 12 months of data
99% and 97.5% are to be used, 12 exceptions for 99% or 30 exceptions for 97.5%.

#### Securitization
Under FRTB, the standardized approach must be used for securitizations.


### <!-- C10 p151 --> Empirical Approaches to Risk Metrics and Hedging 
#### DV01-Neutral Hedge
DV01: change of bond price in currency when its yield changes by 1 basis point.
The changes in yields among components may not be one for one.


#### Single-Variable Regression-Based Hedging
$\Delta r^{\text{portfolio}}=\alpha+\beta r^{\text{hedge instrument}}$
Hedge coefficient: $\beta$

#### Two-Variable Regression-Based Hedging


#### Level Regression vs. Change Regression


#### Principal Components Analysis

























