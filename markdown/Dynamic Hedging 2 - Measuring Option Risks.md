<ndtag category = "Derivatives" editdate="2024-09-11" createdate="2022-12-13" tag="Hedging"></ndtag>

<!-- 
   1 done
   2 done
   3 done
   4 done
   5 
   6 
   7 done
   8 done
   9 done
   10 doing
   11 done
   12 done
   13 done
   14 done
   15 done
   16 done
   17 done
   18 done
   19 done
   20 done
   21 done
   22 doing
-->

Real world and Black-Scholes-Mertion assumptions

### <!-- C7 p128 --> Adaping BSM: The Delta
Risk management rule: continuous time models should be used for pricing and getting a benchmark fair value, not to hedge.
#### The Continuous Time Delta is Not Always A Hedge Ratio
(Continuous time) delta is sometimes nothing meaningful, e.g., for barrier option, the real time delta might explode but the whole risk (maximum loss) is totally reasonable.
Some trader trick the delta of a barrier by changing the expiration date.
Modified delta $Delta=\frac{1}{2}(\frac{\Delta c}{\Delta S^-}+\frac{\Delta c}{\Delta S^+})$

#### Delta as a Measure for Risk
Not complete to show the whole view of risk. (long call and short put have the same delta)

#### Confusion: Delta by the Cash or by the Forward
Forward delta: option's sensitivity to the PV of a foward contract
Cash delta: option's sensitivity to the underlying spot price.
When dealing with options on futures (where we also have the spot underlying to trade), we need discount it with cash-future growth rate.



#### Delta for Linear Instruments
##### Delta For A Forward
Forward price: $F=e^{(r-r_f)t}S$
price of a long forward contract with price $K$: $f=(F-K)e^{-rt}$
delta of a forward contract should be $e^{-r_ft}$
delta of a futures contract should be $e^{(r-r_f)t}$ because it settles daily and does not need discounting
For linear derivative, delta is stable
? delta for foreign currency forwards

#### Delta and the Barrier Options
Do not use real time delta, but discrete delta.

#### Delta and the Bucketing
A bucket is the bundling of the exposures by groups of neighboring maturities to show basis risk.

##### Delta in the Value at Risk
Equivalent position = face value\*delta\*expected move + 0.5\*gamma\*(expected move)^2
This calculation ignores higher greeks, the best method to view the risk is through repricing at different movements.

#### Delta, Volatility, and Extreme Volatility
With $d\ln S=\sigma dB_t$, it must have a $-\frac{1}{2}\sigma^2$ drift to make $S_t$ remain martingale.
A call on a bond can also be viewed as a put on yield. Yet both yields and prices cannot be lognormal and have a fat right tail at times of high volatility. 
Traders often mix bond futures (priced on a lognormal price) and bonds priced on a lognormal yield. This can carry serious consequences for a large book at high volatility.
The probability of being ITM using on part of a pair as a numeraire is delta for the counterparty.


### <!-- C8 p145 --> Gamma and Shadow Gamma
#### Simple Gamma
A range needs to be associated with every gamma measurement because gamma changed sharply across underly price and time.
#### Gamma Imperfections for a Book
A practically sound way is to calculate discrete gamma for up and down respectively.
Risk reversal: up-gamma and down-gamma have different sign for some increments
#### Correction for the Gamma of the Back Month
For options on futures, if the underlyings have the different maturities, there should be two adjustment:

1. with contango or backwardation, one unit contract will have different size of delta cash.
2. gamma should be adjusted considering relative volatility. If the back month had 12% more volatility than front (move by 1.12 points against move by 1 point), the backmonth gamma should be adjusted by 1.12.

? what is the difference of between the adjustment above and mark different iv for different maturity? 

#### Shadow Gamma
Given the volatility predicted (i.e. deterministic) under different underlying moves, calculate delta and gamma.

#### Shadow Gamma and the Skew
skew gamma is also called asymmetrical shadow gamma.

#### GARCH Gamma
use GARCH to predict volatility and calculate shadow gamma then.

#### Advanced Shadow Gamma
For options on futures or forwards, consider both expected volatility and interest (or carry) rate moves.
A currency dropdown might company with higher interest rate, driving foward price lower.

### <!-- C9 p160 --> Vega and the Volatility Surface
#### Vega and Modified Vega
Most vegas decrease with time, except lookback and reverse kkock-out.
Vega of ATM options stays the same when volatility rises but the vega of the options away from the money rises. Because $\mathcal{V} \approx 0$ when $d_1=0$, this is close for ATM options.

##### Vega and the Gamma
Vega profit should be integral of the gamma profits.

##### The Modified Vega
Vega of different maturities should not be compared, net or added. It is assumed that one Brownian motion affects the volatility for one maturity and that the rest of them follow in some known proportion.
Modified vega = $\sum w_iV_i$, with $V_i$ the vega for different maturities and $F_i$ the volatility weight.
The convention is to use a volatility factor pillared around the 3-month. All options would be compared with that maturity in their sensitivity.

##### How to Compute the Simple Weigtings
###### "Theoretical" Weighting
? use $\frac{1}{\sqrt{t}}$ as the weight compared to 3-month.

###### Empirical Weighting
ratio should be $\frac{\text{sum of absolute changes in one period}}{\text{sum of absolute changes in the other period}}$.

#### Forward Implied Volatilities
Forward implied volatility is imperative for path-dependent or defered-start options.
? Eurodollar options are not fungible assets, vega analysis could distort the risk.

##### Bucket Vega
(? to be proved) Vanilla options present a linear sensitivity in time buckets, but path-dependent options are not. Barrier knock out options could long vega in one bucket and short vega in the adjacent one. 
(-? not formal) Gamma has distribution, the odds of being at the stongest point are slim. Gamma is more even at the begining. Expectation of gamma profit does not vary with the period.

   * (-) An proof might be like this:
   Suppose over maturity $T$, the volatility maintains level $\sigma$, among which there is period $t$, whose forward volatility changes to $\sigma +\Delta \sigma$.
   The total variance is then $\sigma^2T+\Delta \sigma ^2t+2\sigma\Delta \sigma t$, this is roughly equivalent to long term valtility $\sigma$ changes to $\sigma+\frac{t}{T}\Delta\sigma$, corresponding to total variance $\sigma^2T+\Delta\sigma ^2\frac{t^2}{T}+2\sigma\Delta \sigma t$, if considering $\Delta\sigma ^2\frac{t^2}{T}\ll2\sigma\Delta \sigma t$ ($\frac{t}{T}<1$ and $\Delta\sigma<\sigma$).
   Then price change of the option $\mathcal{V}\frac{t}{T}\Delta\sigma = \frac{t}{T}\mathcal{V}\Delta\sigma$, where we just divide vega in proportion of time.

##### Multifactor Vega
It does not apply for value-at-risk system, because it is for short-term hedging rather than worst-case scenario. This could be considered a second-degree value-at-risk method since, the principal instrument is the expectation of the second moment.
Calculate correlation matrix
? pnl calculation


##### Volatility Surface
Calendar spread is called horizontal and strike spread is called vertical, and the mixture is called diagonal.
Dupire's local volatility is the volatility between two points $(S,t)$ and $(S+dS, t+dt)$, it is forward instantaneous volatility.
(? p164) The American feature is weak.
It gives an example of fitting the surface volatility on $(\sqrt{x},\frac{1}{\sqrt{x}},y,y^2,y^3,y^4,y^5)$.
The pitfall of building the volatility surface as a function of (delta, maturity) is having to determine the delta as delta is a function of volatility.

#### The Method of Squares for Risk Management
Cutting the position into squares of strike and maturity and then apply multifactor vega analysis.
This is required in skewed market.

### <!-- C10 p180 --> Theta and Minor Greeks
Expected price tomorrow of a call value is the same as today's.
#### Theta and the Modified Theta
##### Modifying the Theta
Modified theta: price difference of option under different volatilities.

##### Theta, Interest Carry, and Self-Financing Strategies
If interest rates are 20%, theta will be lower by 20% of the total premium (option will be cheaper and have lower theta because of the present-value-effect), but the carry costs of holding the option will offset these savings.
When calculating theta, traders should eliminate the interest cost of holding the premium.

 * (-) Suppose $r=q=0$, price of a call will be $SN(d_1)-KN(d_2)$, which has theta $\Theta$. When $r=q>0$, price will be $e^{-rt}(SN(d_1)-KN(d_2))$ and theta will consists of two parts $e^{-rt}\Theta$ and $-rU$. However, $rU$ should be added back because a long position will have to finance for the premium and a short postion will have interest income.

##### Shadow Theta
Combine theta with volatility prediction. If price stays the same for several days, it is convincible that volatility will drop.

#### Minor Greeks
##### Rho, Modified Rho
To interpolation on yield curve:

1. eliminate jaggedness (cubic spline)
2. adapt to the market

Rho assumes a parallel shift in the curve.

* rhop: risks associated with the financing of the premium of the option (risk corresponds to $e^{-rt}$ outermost in the price formula)
* rho1: $\frac{\partial U}{\partial r}$, therefore inlcuding rhop
* rho2: $\frac{\partial U}{\partial q}$

? how to calculate modified rho

##### Omega (Option Duration)
Omega is expected life of a soft path-dependent option, like first exit time for barrier option or American binary option.
The rule of premature exercise depends on volatility and carry.
We could use local volatility binomial tree to make these tests.
(?) stochastic parameter tree
Rho fudge: $\Omega=\text{Nominal duration}\times\frac{\text{rho2 of American option}}{\text{rho2 of European option}}$

  * (-) This could be partly explained by that rho2 contains $T$.

(?) The trader also can compute rho2 from the delta by assuming that the delta is a zero-coupon bond of the nominal maturity provided.

  * (-) $\text{rho2}=-Se^{-qT}N(d_1)T$, 

##### Alpha
alpha = theta/gamma, better to use shadow gamma and shadow theta
When ignoring $r$, BSM differential equation gives $\Theta+\frac{1}{2}\Gamma\sigma^2S^2=0$, therefore $\alpha = -\frac{1}{2}\sigma^2S^2$, irrelevant to maturity.
(?) Eliminating the interest carry from the equation, allows the trader to get a pure theta.
Calendar spread might have different alpha because of volatilitt's term structure.

#### Table of Greeks
gamma and theta for different volatility could be approximately calculated fractionally with a base value.

##### Stealth and Health
For barrier options, stealth is percentage difference (for large move better use $\log{K/B}$) between strike and barrier, health is percentage between spot and barrier.
Stealth could indicate how much the option resembles a vanilla.
It should be noticed when health drops below 1 standard deviation.

##### Convexity, Modified Convexity
Convexity needs to be associated with volatility of the parameter concerned.
At very high volatility, all options become concave with respect to volatility because option is capped at the price of the underlying asset.
At very high volatility, an asset becomes a call on it self because it can rise infinitely but only go down in a limited way.

##### Modified Interest Rate Convexity
(? exactly how) Convexity of a 2-year bond could hardly be compared with that of a 10-year bond since two rates exhibit different volatilities. Use modified convexity to rectify this.
##### The "Double Bubble"
Short Eurodollar provides two kinds of convexity: long zero coupon bonds and benefit from negative correlation between (Eurodollar price and interest rate).
(? mathematical way to price correlation convexity)

### <!-- C11 p204 --> The Greeks and Their Behavior
Time and volatility exerts the same effect on the option, because $\sigma$ and $t$ show at the same place in pricing formula. Time exerts its own effect through $r$ and $d$, which generally do not carry any undue significance.

#### The Bleed: Gamma and Delta Bleed (Holding Volatility Constant)
Bleed: change in delta and gamma with the passage of time.
Gamma is said to increase with time, but for OTM option being pushed further, out-of-the-moneyness would cause some gamma loss. The results are therefore mixed.
pit trader: traders in exchange
It is reasonable to explore how gamma bleed behave with repect to spot, and this is the 4th derivative.

##### Bleed with Changes in Volatility
similar to time bleed, because variance has equal effect as time to maturity.

##### Going into the Expiration of a Vanilla Option
On expiration, it does not mean that delta should be adjusted in a binary form. Smoothing is the golden rule.

###### Why Hedge Fully at Strike Does Not Work?
1. It is hard to hedging the entire face value at one tick.
2. The costs of replicating an option by hedging the entire face value at the strike or by continuously rebalancing the delta are expected to be the same. The option price can also be derived through strike hedging strategy.
3. The frequency of rebalancing does not affect the fair value of the option.

#### DdeltaDvol (Stability Ratio)
$\text{DdeltaDvol}=\frac{\partial \Delta}{\partial \sigma}=\frac{\partial \mathcal{V}}{\partial S}$
(? path-dependent portfolio testing) 
(-) When portfolio contain calendar spreads, volatility change will not have the same margin effect as time elapse.

##### Test 1 of Stability
Positive DdeltaDvol: delta increases with volatility increase, which means the book is net short options below the money and net long above the money.

##### Test 2 of Stability: The Asymptotic Vega Test
Test 1 under higher volatility, this is for stress testing as it gives way OTM options undue importance.

#### Moments of an Option Position
* Third moment: delta of gamma, called skew.
* Fourth moment: gamma of gamma, called tail.

Odd moments are indicators of symmetry while even moments are indicators of convexity.
Higher order moments are for compound options. An installment option (a fifth-order compound option) requires at least analysis for 9 moments for hedging stability.
Positions neutral in lower moments might have increasing exposure in higher moments, which is difficult to trade.

#### Ignoring Higher Greeks: The Lock Delta
Delta (upside asymptotic and downside asymptotic) when $S=0$ and $S=\infty$, this is important because at these boundaries, options behave like linear assets and sensitivity to volatility will be nil.
OTC dealers use regular parametric scenario analysis for their portfolio, therefore do not have watchdog protection from nonstatistical risks (large range move).

###### ND Note
LME and CME contracts have daily price limits.

### <!-- C12 p221 --> Fungibility, Convergence, and Stacking
#### Fungibility
Fungibility refers to the degree of specificity required for the satisfaction of the deliverability obiligation.
Fungibility reflects the feasibility of risk-neutral replication of a derivative security.
The market for the more fungible one will be larger and more liquid.
The opening interest should not exceed the deliverable commodities, otherwise the long party has the incentive to force the delivery.
##### Ranking of Fungibility
An extremely fungible commodity is a currency that a bank can create electronically and wire anywhere in the world.
The other extreme is a physical commodity that needs to be delivered at one specific location.
The commodity can escape all rules when it comes to a perishable or live animal, because it is hard to extend its life.

##### Fungibility and the Term Structure of Prices: The Cash-and-Carry Line
One can always buy the asset and bear carrying cost (financial and physical storage) if the asset does not go through deterioration and sell it in the future. Therefore, there exists an upper boundary in forward curve called maximum contango.
(?) Eurodollar is not fungible because the contracts do not overlap.

##### Fungibility and Option Arbitrage
When asset is of low fungibility, components of calendar should be treated separately, because it does not have a perfectly arbitrageable forward curve. 
(?) The stability of second derivatives will be higher than first ones. If the deltas of the 9-month does not properly hedge that of the 3-month, the gamma hedges will be more stable.

##### Changes in the Rules of the Game
Sometimes the central banks create a wedge between the domestic and offshore markests (change the rules) for currency.

#### Convergence
* First-order convergence: short a future contract
* Second-order convergence: spread
* Butterfly convergence: future contract butterfly

##### Mapping Convergence
###### Fixed-Income Instrument
Dollar convergence is equivalent to carry plus drop on the curve in basis points.
The drop on the curve should be computed by repricing the bond on the zero-curve with one day shorter to go.
###### Eurodollar Future
Interpolating between contracts and repricing in a similar way.

##### Convergence and Convexity
Theta due to convexity should be excluded: securities of the Government National Mortgage Association (GNMAs) need to be priced on a an option-adjusted basis.

##### Volatility and Convergence
The carry is often compensation for the holding risks.

##### Convergence and Biased Assets

#### Stacking Techniques
Stacking is a short-term hedging technique minimizing execution of a multiple leg hedge by concentrating on a few liquid instruments.
One can do correlation matrix analysis minimizing total variance for a multiple contracts position.

### <!-- C13 p235 --> Some Wrinkles of Option Markets
#### Expiration Pin Risks
Expiration variance for options position.
It exists because there are usually lags between the close of an option market and the decision on whether assign, which kind of prolongs the life of option.
If news is in favor of a direction, the holding party might exercise an OTM option.
Quarterly option on future: same expiration corresponds to future; the other is called serial option on future.

#### Sticky Strikes
The option long position holder's hedge will cause the strike an absorbing state for the underly, until some fresh power pushes it away.

#### Market Barriers
Market barrier: 

* currency band where central banks limit the market from trading through some level
* a floor price of an agricultural commodity
* market limits (when reached cause the exchange to shut) is a weaker form of market barrier

Fair game (martingale) need volatility decreases when it is near the barrier.
The market barrier for currency spot will not limit the price of forward, which means the interest rate will change at the mean time. (interest rate volatility rise)

#### What Flat Means
A flat position is a position that does not present any market risk.

### <!-- C14 p242 --> Bucketing and Topography
#### Static Straight Bucketing
Divide exposure into its nominal expiration.
Some knock in options and defered strike options' exposure start at a future point, and some barrier are calendar spread. The straight bucketing can be misleading.

##### The Forward or "Forward-Forward" Bucket
Move the concerned parameter in a cell to leave the others constant to calculate exposure.
(? gamma) For European option, each bucket should share the equal portion of gamma and vega.

#### Topography
##### Strike Topography (or Static Topography)
Divide net positions into time-strike two-dimensional space.
(? how is this related to delta space) Scale the strike as volatility, the 101 with 1 day maturity and 115.7 with 1 year maturity should be put in the same column.

##### Dynamic Topography (Local Volatility Exposure)
Senerio analysis, greeks at different levels for different time passed.
This analysis could not show the effect of barrier option, because it is path-dependent and could knock out.
##### Barrier Payoff Topography
worst case senerio loss
(?) payoff topograhpy


### <!-- C15 p251 --> Beware the Distribution
#### The Tails
Adverse select forms the volatility smile.
##### Random Volatility
In the old days, traders attribute the inflated prices to the lottery effect, which means investors were ready to buy lottery ignoring of real value.
The prime reason for higher price of OTM options is vvol.
The reason that random volatility results in fat tails is that conditional on price get OTM strike, it is more probable that volatility is higher.
It is difficult to establish a dependence between asset price and volatility:

1. Return and volatility might be nonlinearly correlated. SP500 futures' volatility drop after a small rally but increases after a larger one.
2. Volatility correlates to the range of underlying prices.

Hybrid lognormal brings extra kurtosis (from mgf).

##### Histograms from the Markets
Traders betting against the fat tails typically make bets against the peak, tring to make profits when nothing happens rather than during extreme moves.
Pareto-Levy distribution
#### The Skew and Biased Assets
The density skew cannot reflect correlation between price and volatility.
(? this effect might be already relfected in price) The author is extremely suspicious of differentiating price with respect to strike to get the distribution, because it ignores the path dependency that arises from changes in volatility.
The value of the skew for a dynamic hedger resides more in the behavior of implied volatility along the path leading to a terminal value than in the probability of the asset ending up on such terminal value.

##### Biased Assets
Assets that volatility increases in sell-off.
Two poles of extreme regime for biased assets:

* Notice the skew dynamics

| Characteristic | Type 1 Regime | Type 2 Regime |
| :---: | :---: | :---: |
| Market condition | A severe break in a  market following a  protracted rally (or a  quiet period) | A normal condition  where the market offers  high returns through  high "carry" or positive  "trend" |
| Historical volatility | Increases | Generally low |
| Implied volatility | Increases markedly, often overshoots historical | Low, generally close to  historical. Out-of-the-money calls trade  usually lower than  recent historical |
| Skew | Flatter skew but higher  volatility | High skew at lower  volatility generally from  call selling. The lower  the volatility, the higher  the skew. |
| Serial correlation | Often negative  autocorrelation,  "whipping" markets | Positive autocorrelation,  a slow, "quiet trend" |
| Correlation with other  assets | Total breakdown of  correlations. Low  correlations increase. High correlations  decrease | Medium, stable correlation with similar  assets |

##### Nonparallel Accounting
Stocks and government bonds have no consciously short party, because price going up does not draw unhappiness to the majority.

##### Value Linked to Price
For company and government, higher stock/asset price lowers volatility, making it less risky.

##### Reverse Assets
Gold, and to a lesser extent the Swiss franc, the German mark, and the yen, often behave exactly as the opposite of a regular asset as capital flights.

##### Volatility Regimes
The high volatility for a short time followed by a low volatility for a long period shows a fat tail.
It is likely that after first move down in regime Type 1, slow rally and fast sell-off are more probable to happen.

##### Correlation between Interest Rates and Carry
Usually strong for biased assets.

#### More Advanced Put-Call Parity Rules
* Barrier products: knock-out + knock-in = vanilla
* American binary options: knock-out rebate
* Rainbow options (multi assets): no put-call parity
* Compound options: put-call parity holds on higher order

### <!-- C16 p269 --> Options Trading Concepts
Static replication includeds, semiexact option equivalence, like inexact barrier hedge
For static hedge, one could construct a binomial tree and optimize for some objection function like weighted quadratic difference of payoff and greeks one each node.
Greeks to match on every state:

* delta
* modified gamma
* modified vega
* theta
* modified rho
* bleed
* correlation delta (if any)

The need of dynamic hedging is from the exact match greeks are expensive.
spreading: buying options and selling different options at the same time

#### Initiation to Volatility Trading: Vega versus Gamma
Calendar spread
##### (?) Basic Forms of Option Strategies
Simple trades with simple products:

* Straddles, strangles, butterflies, volatility bets.


Complex trades with simple products:

* Long leptokurtosis (fourth moment bet).
* Playing the volatility term structure.
* Calendar/diagonal spreading.
* Long vega convexity.
* Long the Eurodollar "dampening" effect.
* Distribulional arbitrage: skew trading.


Simple trades with complex products:

* Playing the variance ratio with barrier options.
* Bets and the reflecting barriers.

Complex trades with complex products:

* Distributional arbitrage through contingent premium options.
* Playing the second order convergence with barriers: arbitraging the slope of the curve
* Playing the reverse knock-out convexity against ramp options.
* Arbitraging higher moments of the distribution with a combination ofbet and compound options.

#### Soft versus Hard Deltas
Soft delta: hedge with option, with delta asymptotically vanished.
Hard delta: hedge with underly

###### ND Note
For example, currenty price is 100. We long at 100 and short at 112. Gamma is square at 106. 
| Asset | 100 | 102 | 104 | 106 | 108 | 110 | 112 | 114 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Delta | 0 | 10 | 15 | 17 | 15 | 12 | -10 | -50 |
| Gamma | long | long | long | square | short | short | very short | very short |

When it comes to 16, we have long delta. 

* Selling underly will make it worse at 114 with more negative delta. 
* Doing nothing ignures gamma profit.
* If sell put at 100 and buy put at 106, this will mildly rebalance gamma and lock the gamma profit at the same time.

#### Volatility Betting
##### First-Order
Long option everywhere and dynamicly neutralize delta

##### (?) Second-Order
Options with different strikes and maturities.

##### Third-Order
Correlation between volatility and asset price (bet vanna).

##### Fourth-Order
vvol, through buying otm options or calendars and short atm, benefiting from fat tails.

#### Case Study: Path Dependence of a Regular Option
Path dependence has large effect on total PnL.
This effect could be reduced by higher hedge frequency, which yields higher cost.
Also, the life of a trader is too short for adequate time diversification.
Traders have some form of absorbing barrier in their PnL, like maximum loss, which will spell more negative runs.

#### Simple Case Study: The "Worst Case" Scenario
Dynamic hedger will lose more than option premium with delta hedging. Like hold an OTM call and sell futures but price never reaches strike.

