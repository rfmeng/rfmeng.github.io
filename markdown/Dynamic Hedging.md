<ndtag category = "Derivatives" editdate="2024-09-13" createdate="2022-12-13" tag="Hedging"></ndtag>

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

### <!-- C1 p23 --> Introduction to the Instruments
#### Derivatives
A derivative is a security whose price ultimately depends on that of another asset.
A nonlinear derivative is that it presents a nonzero second order derivative with repect to some parameter.
(? to be prove) Non linear derivatives has gamma and gamma needs to be accompanied by time decay.

   * (-) an informal proof comes from contamination principle, the profit of the derivative is simlilar to the notion of heat transfer. 

General assets include:

* (Mostly) linear synthetic securities
  * Baskets: weighted average of securiteis
  * Spreads: difference between securities
* Time dependent noncontingent derivatives
  * Linear or Quasi-linear: swaps, currency, fowards, FRA, eurodollars 
  * Nonlinear: squared or cubed forward payoffs
* Nonlinear contingent claims
  * Options categories
#### Synthetic Securities
A synthetic security is a linear combination of primary instruments in the markets.
But there are geometric average index (e.g. U.S. dollar index) and they present convexity.
#### Time Dependent Linear Derivatives
(? foward foward) floating rate agreements and Eurodollars could be forward-forwards
#### Noncontingent Time-Dependent Nonlinear Derivatives
LIBOR-square (payoff will be $(S-K)^2$ for one party and the negative for the other) or LIBOR-cube
#### Options and Other Contingent Claims
##### Simple Options
A put on Mark/Dollar (the right to sell Marks and buy dollars) is a call on Dollar/Mark.
A put on yields is a call on bonds.
(?) A call on SP500 is put on cash indexed fund managers, because their PnL is computed in SP500 units.
Intrinsic value of European option should be difference between strike and corresponding foward. Because the option is not exercised before expiration, the only price that matters is the term market price of the asset (for delivery on the expiration of the option).

###### ND Note
Risk management companies which are subsidiary corportion of futures company (RMSC) trade forwards on futures and options on futures. 
Because of margin system, the interest rate should be close to 0.
To make it 0 drift under risk neutral measure, yield should be the same to interest rate.
A reasonable interest rate which is more practical for futures might be funding cost times the maintainance margin rate. This fully presents the funding cost of futures.
Yet the difference will be small. 
The price of European call $(S,K,T,\sigma,r,q)=(100,100,1/12,0.3,0.03,0.03)$ is 3.445 and of $(S,K,T,\sigma,r,q)=(100,100,1/12,0.3,0.01,0.01)=3.451$.
$Europeancall(100,100,1,0.3,0.03,0.03)=11.571$ and $Europeancall(100,100,1,0.3,0.01,0.01)=11.805$.

#### Hard and Soft Optionality
hard: an explicit strike price
soft: built-in convexity but no real strike price
(? expample) Soft optionality presents generally milder gamma and other Greeks but will present some stable features across time.
#### Basic Rules of Options Equivalence
(? described in C13) "Pin Risks" cause put-call parity not to hold for listed options.
Traders should use forward delta, but most risk management systems disclose cash delta as does the Black-Scholes-Merton formula.
Put call parity $p+Se^{-qt}=c+Ke^{-rt}$. In cash delta sense, put + $e^{-qt}$ = call. In forward delta sense, put + 1 = call. Because the price of a existent forward contract is $e^{-rt}(Se^{(r-q)t}-K) = Se^{-qt}-Ke^{-rt}$.
A forward delta for a European option is the equivalent cash position with the same delivery date as the underlying asset.

#### American Options, Early Exercise and Other Headaches
See <a href="https://quant.stackexchange.com/questions/33121/soft-american-options">Soft American Options </a>.
If one has American option (in the money) and does not exercise, he would have $\max(S_T-K,0)$ at expiration. Or he can exercise, borrowing $K$ at $r$, long the underly and long a put (whose price should be close to 0). Then he will have $\max(K-S_T,0)-Ke^{rt}+e^{qt}S_T$ at maturity. The payoff at the second case is $\max(S_T-K,0)+(e^{qt}-1)S_T-(e^{rt}-1)K$. We just need to find whether the extra part $(e^{qt}-1)S_T-(e^{rt}-1)K\approx qtS_T-rtK=rt(S_T-K)+(q-r)tS_T$ is positive.
##### Soft Rule
Under soft cases, $q\approx r$. The second part would be close to 0. We just need to find whether time value of option is greater or time value of money between time of consideration and expiration.
$Europeancall(100,80,3/12,0.157,0.06,0.06)=19.707$
$Europeancall(100,80,3/12,0.157,0.06,0)=21.193$
$Europeanput(100,80,3/12,0.157,0.06,0.06)=0.005$
$Europeanput(100,80,3/12,0.157,0.06,0)=0.002$
The funding cost of time value would be $20*0.06*3/12=0.3$, when $q=0.06$, the option should be exercised. Even if $q=0$, the option should still be exercised or selled to market.
What we do test here is whether the time value is negative.
This kind of American option is called pseudo-European option.
###### ND Note
RMSC trades pseudo-European options.
##### Hard Rule
Or difficult rule. Under this case we should compare two rates.
When the underlying is currency with 20% interest. Early exercise would have additional benefits because we gain funding cost of the intrinsic value $rt(S_T-K)$ and interest from underly $(q-r)tS_T$ at the same time. 
The payoff for put considering early exercise would be $\max(S_T-K,0)-e^{qt}S_T+e^{rt}K$, the second part is equivalent to $rt(K-S_T)-(q-r)tS_T$. It will never be early exercised then.
$Europeancall(100,120,3/12,0.157,0.06,0.20)=0.007$
$Europeanput(100,120,3/12,0.157,0.06,0.20)=23.098$


###### ND note
The market always tends to flow to simplicity.
##### A Brief Warning About Early Exercise Tests
An additional refinement should be the use of a volatility term structure by retesting with the highest possible volatility between time 0 and maturity. (It might be the case that exercise in the future will be optimal decision.)
When dealing with large-size position, dealers upon exercise become short OTM options, better to test liquidity for such strike before.
##### Consequence: Smile-Calendars
Put-call parity might not hold for American options, because of expected life. The exercisable one would be priced with short period volatility. 
(?) When 3-month options trade at 15.7%, an exercisable 80 call would be priced at 1-day volatility (say 13%) while 80 put would trade at 20% (skewness).

   * (-) It might be that American option's price is at least intrinsic value, and compared to exercise "truly", traders will sell it and gain more profit, driving down the price.
  
Hard American options are more valuable than European options, because they harbor a compound option on interest rates or volatility. The difference increases with higher volatility of volatility or volatility of interest rates.
##### American Options Nobody Ever Exercises 
Options on futures where there is a marks-to-market daily. (Also like RMSC.)

#### Forwards, Futures and Forward-Forwards
To hedge one unit of forward, use $h=e^{-rt}$ units of futures. The price of a future contract with strike $K$ is $Se^{(r-q)t}-K$, compared to $Se^{-qt}-Ke^{-rt}$ for forward.
##### Credit
Each party's credit line will reduce in a swap trade loop in OTC markets, which will not happen on a standardized exchange.
##### Marks-to-Market Differences
Forwards' curve has fewer points than futures'.
An arbitrageur might never reflect the accurate liquidating value of his position from resultant PnL because of different settlement time point.
##### Correlation between the Future and the Financing
When there is positive correlation between financing rate $r$ and future contract $F$, the future will be convex and trade above the forward.
##### Forward-Forward
Exchange an asset at one period against the reverse trade at a later period.
$FF(t_1,t_2)=F(t_2)/F(t_1)$
It is a form of forward rate agreement. Party A lend money to party B on one future date and the reverse happend on a longer future date.
#### Core Risk Management: Distinction between Primary and Secondary Risks
* For an equity derivative portfolio, interest risk is secondary risk through possible effect on time structure.
* For a fixed income derivative book, the whole interest rate curve is primary risk.
* For a currency book, both interest rates are part of primary risk if volatility of interest rate is high.
#### Applying the Framework to Swaps
(? why swap) Swap is multiasset insturment composed of correlated segments. Framework on multiasset options and correlation matrices would work.
For index-amortizing swaps, use of American digital options would perform.


### <!-- C2 p52 --> The Generalized Option
For risk management purposes, 6 dimensions of analysis are crucial.
#### Homogeneity of the Structure
A time-homogeneous structure refers to a payoff structure does not contractually change through time.
Defered strike option: strike is not determined until strike setting time, it will appear no delta and no gamma (but shadow gamma) but will have some vega.
Nonhomogeneous structure includes window option, a barrier option whose barriers are lifted after a certain period.

#### Type of Payoff: Continuous and Discontinuous
Digital (discontinous) and ramp (continuous)

#### Barriers
#### Dimension of the Structure and the Number of the Assets
1 + the number of variables affecting its value (one is for time)
American currency option is sensitive on interest rates and the curve, it is of higher dimension.
Multiasset structure by construction: such as using USD-DEM and AUD-USD to hedge DEM-AUD cross option.

#### Order of the Options
Higher order options: option on option
Higher order greeks are unstable

#### Path Dependence
soft-path-dependent: lookback option, barrier option
hard-path-dependent: Asian option

### <!-- C3 p62 --> C3. Market Making and Market Using
* local: floor market maker
* paper: end customers
* arbs: arbitrageurs
#### Booker Runners versus Price Takers
book runner also called market maker

#### Commoditized and Nonstandard Products
##### Trading Risk in Commoditized Products
Cash products: almost not liquidity risk

#### Proprietary Departments
Banks saw the success of their hedge fund customers, had an overspill of back-office capability and start proprietary departments
But because of different utility function (risk apetite), their performance did not match expectations: under the need of diversification, PnL from traders offest each other, drawing the value of the bonus option down.
#### Tacit Rules in Market Making
For the more established and liquid markets, traders have the (implicit) obligation to quote big order to other dealer. They face the same big order problem.
Very liquid products have highly developed rulse, dow to how long a person can wait before the quote becomes invalidated. It is not acceptable to come back to the same dealer after "passing", to quote too much without trading, or to pass on a "choice" market, when the bid and the offer are the same.

#### Market Making and the Price for Immediacy

#### Market Making and Autocorrelation of Price Changes
Most studies report an autocorrelation for frequent price changes, but 4-minute price change is the minimum time lag to show autocorrelation.
4-minute volatility is lower than bid-ask spread, so only market maker can capture the advantage.
(?) Only market maker could benefit from a submartingale and in a limited way.

#### Market Making and the Illusion of Profitability
Traders find a fair value and mark the derivative up, then recognize most of the difference as a profit, neglecting the subsequent hedging cost (which is significant especially when the liquidity is poor).


#### Adverse Selection, Signaling, and the Risk Management
Counterparty might have extrainformation
market maker lose money chronically during shock but produce profit in normal conditions, like shorting volatility.

#### Value Trading versus the Greater Fool Theory
like 左侧交易 vs 右侧交易

#### Monkeys on a Typewritter
##### The Statistical value of Track Records
the "winning probability" is counterintuitively high, increase the number of trades and make the bets smaller to see the true result

##### More Modern Methods of Monitoring Traders
It is based on trading frequency and trend. Traders who frequently rebalances his book would capture the true distribution.

##### The ArcSine Law of the PnL
A stop-loss will not change the expectation of a trader. It will present frequent small losses and infrequent large gains.
##### Risk Management Rules
1. When judging a nonmarket-marking trader, a large share of his profitability is attributable to luck.
2. The ratio of luck to skills decreases with the transaction frequency.
3. In general, traders become extremely arrogant and difficult to manage when they are very profitable. A trading manager must be able to face wrongly profitable traders without being influenced by their PnL.


### <!-- C4 p82 --> C4. Liquidity and Liquidity Holes
#### Liquidity
Slippage is variation between average execution price and initial middle point of bid and ask. This should be practitioner's measurement for liquidity.

#### Liquidity Hole
Temporary event where lower prices bring accelerated supply and higher prices accelerated demand.

#### Liquidity and Risk Management


#### Stop Orders and the Path of Illiquidity
Large sell might not be able to find the counterparty because of their suspicion of information they do not have.
There exists liquidity vacuum to trigger stop order.

#### Barrier Options and the Liquidity Vacuum
The holder of short postion of a knock-out call has the incentive to unwind the delta to trigger the knockout event.

#### One-Way Liquidity Traps
Easy in, hard out.

#### Holes, Black-Scholes, and the Ills of Memory
price's memorylessness is not true because of the stop-loss order or barrier option, which results in predictable market movement
even the most liquid markets display acute weakness at the most liquid of times

#### Limits and Market Failures
Circuit breakers in the SP500 stop the market for five minutes if it opens within a certain range. It appears to be a successful experiment, providing a psychological buffer for traders.

#### Reverse Slippage
(?) large order in an illiquid market cannot always win money by fooling stop loss order, they might lose as well

#### Liquidity and Triple Witching Hour
Manipulate stock close price with liquid hole to satisfy a close price order.

#### Portfolio Insurance
?

#### Liquidity and Option Pricing
adjust volatility according to transaction cost
(?) augmented volatility
When long gamma, use limit orders; when short gamma, use stop orders.
Long gamma position could earn bid ask spread by setting limit orders.
Implicit bid-offer spread is wider than the visible bid-offer spread, corresponding to the adjustment facing a large order.


### <!-- C5 p94 --> Arbitrage and the Arbitrageurs
#### A Trader's Definition
|Degree|Definition|Examples|
|:-:|:-:|:-:|
|First order|mechanical stability|currency triangular arbitrage|
|Second order|different instruments, same underlying|cash-future arbitrage|
|Second order|different underlying, same instruments|bond arbitrage|
|Third order |behavioral stablility|bond against swaps|

#### Mechanical versus Behavioral Stability
Behavioral stability exists when one has to marshal historical records to establish the a posteriori link between two instruments

#### The Deterministic Relationships
Behavioral relationships are not deterministic, but one can observe correlation:

* Hedging a bond exposure with a swap
* Using all value-at-risk numbers as exposure presents the same uncertainty


#### Passive Arbitrage
Arbitrage when operators carry one leg of the spread: investor with a security can replace it with future.

#### An Absorbing Barrier Called the "Squeeze"
A combined position of long stock and short future has potential liquidity hole when stock goes up generating paper profit and having to pay in cash for futures losses.
###### ND Note
Risk management company faces the similar situation where PnL from hedge position of futures occurs immediately while PnL from options are more paperlike.

#### Duration of the Arbitrage
Weighted average time to expiration of the absolute amounts in a book.
Predilection for the short-term profits might distort the trading decision.

#### Arbitrage and the Accounting Systems
It is often easier to arbitrage one's accounting system than the market.

* Correlation-related option will be booked different value on different shops
* Money market traders could arbitrage the credit rating of the empolyer. Namely, borrow money at low cost and lend it to low credit counterparty and book the profit.
* Traders in some houses do not pay interest on the realized losses and earn interest on the unrealized profits (profits from option will be discounted and profits from futures are not).
* Most profits on complex options show immediately on booking, which may underestimate the hedge cost.

#### Other Nonmarket Forms of Arbitrage
* credit arbitrage
* tax arbitrage: some countries impose dividend withholding tax, which could be avoided with swap
* legal arbitrage: buy option to short currency if law does not permit short selling.

#### Arbitrage and the Variance of Returns
Average arbitrageur bear higher variance of return because of carring larger amounts to realize same level profit.
"Inefficiencies in the market will last longer than traders can remain solvent"


### <!-- C6 p102 --> Volatility and Correlation
Implied correlation (calculated from option price)
why arithmetic Brownian motion works: negative prices cound not be ruled out under some situations
mixed process usually witnessed: arithmetic in short term and geometric in the long run

#### Introducing Filtering
A simplified version of the Kalman filter (or for generalized weighted sample variance):
$\bar{x}=\frac{\sum w_ix_i}{\sum w_i}$ and $s^2=\frac{\sum w_i(x_i-\bar{x})^2}{\sum w_i}$, the corresponded unbiased sample variance is $\frac{\sum w_i}{(\sum w_i)^2-\sum w_i^2}\frac{\sum w_i(x_i-\bar{x})^2}{\sum w_i}$
Kalman filter: use $\lambda^t$ as weight

###### ND Note
In practice, this volatility is very similar to Garch(1,1), where $\beta$ usually dominates to affect the volatility.

#### There Is No Such Thing as Constant Volatility and Correlation
Many count Saturday and Sundays as quarter day in the winter and less in the summer.
Some even take the effect of specific transaction time in the day into account.

#### Parkinson Number and the Variance Ratio Method
Parkinson volatility ($\sigma = \sqrt{\frac{1}{N}\sum{\frac{1}{4\ln 2}\ln\frac{S_H}{S_L}}}$):

* high and low prices are easy to be affected by manipulation
* for some illiquid market (OTC), high and low only reveal to several traders involved in the trade
* if market has discontinuities, it underestimates the real volatility

With market discontinuity, use Garman-Klass volatility ($\sigma = \sqrt{\frac{1}{N}\sum{(\frac{1}{2}\ln^2 \frac{S_H}{S_L}-(2\ln 2-1)\ln^2\frac{S_t}{S_{t-1}})}}$). 
Implied volatility contains information that is not available in past prices (events). Sudden announcement of a meeting will pull up IV but freeze RV because market will be numb to any information before meeting.
Parkinson volatility gives meaningful information for:

* high and low are important for continuous barrier option
* if Parkinson volatility is higher, better adjust delta more frequently
* ? market maker edge is strongest when Parkinson volatility is higher, otherwise better to follow trend

#### Variance Ratio Method
It means variance scaled with sampling frequency. If volatility on a more frequently sampling basis is lower, there tends to be a trend; otherwise, there tends to be mean-reversion.
The instantaneous volatility (tick changes, required by BSM framework for replication of option) could be twice the daily measured one.

## <!-- Part II p122 --> Measuring option risks
#### Real world and Black-Scholes-Mertion assumptions

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


## <!-- Part III p284 --> Trading and Hedging Exotic Options
### <!-- C17 p286 --> Binary Options: European Style
#### European Binary Options
Also called digital derivatives, bet options and gap calls.
Long gamma when OTM and short gamma when ITM.
Risk reversal: vega and gamma risk flip across one point.

##### Hedging with a Vanilla
spread
##### Definition of the Bet: Forward and Spot Bets
Whether payment of preimum happens at inception or expiration.

#### Pricing with the Skew
With skew, pricing binary option with spread seams much more expensive. Does this mean market hold the expectation the probability of exercise still be the price?

##### A Formal Pricing on the Skew
The price of digital option must be determined with volatility skew shape.
$$
\text{Binary call}=\frac{\partial C(K,\sigma(K))}{\partial K}=\frac{\partial C}{\partial K}+\frac{\partial C}{\partial \sigma}\frac{\partial \sigma}{\partial K}
$$

##### The Skew Paradox
As $\sigma$ increases, the price of atm bet decreases and delta increases. The skew by increasing the potential payoff on the left integral needs to be compensated with a shift of the mean to the right to prevent short sellers get higher expected return.

##### Difference between the Binary and the Delta: The Delta Paradox Revisited
Delta will increase because of fat tail

###### Two-Currency Paradox
For currency, the price of a bet $N(d_2)$ for one party is delta $N(-d_1)$ for the opposite party.
See more in <a href="https://zhuanlan.zhihu.com/p/680794451">关于希格尔悖论的例子</a>.

##### First Hedging Consequences
The best replication for a digital is a wide risk reversal and shrink the difference between strikes as time progresses.
When the bet option is away from expiration, the real risks are the skew. When near expiration, the risks transfer to the pin.

##### The Delta is a Dirac Delta
See https://zhuanlan.zhihu.com/p/345809392.

##### Gamma for a Bet
DgammaDspot for vanilla

#### Conclusion: Statistical Trading versus Dynamic Hedging
Extremely difficult to hedge a bet with an option that has a continuous payoff.
It will be easy if overhedging delta at the barrier, at cost of worsening it away from barrier.
When dollar variance is low and there is a high number of strikes, traders could do in statistical mode and believes in law of large number by subjective valuation.
When variance is high and strikes are few, one should do replication mode with dynamic hedging by risk-neutral valuation.

#### Case Study in Binary Packages - Contingent Premium Options
Vanilla options where the option buyer pays the price only when ITM.

##### Recommend Use: Potential Devaluations
The structure works well for fat tails and authorized market barrier.

#### Case Study: The Betspreads
condor (a butterfly with 4 strikes)

##### Advanced Case Study: Multiasset Bets
Rainbow call spread


### <!-- C18 p308 --> Binary Options: American Style
#### American Single Binary Options
Howard Savery's rule of thumb is that American digital will be roughly twice the European. Because ATM American digital is worth 1 and an European is worth 0.5. This relationship will contaminate to lower prices.

##### American Binary is a Bet on Time
(? why with no drift) With no drift, the American binary remains long vega.
(?) When the delta hedge against the option incurs a negative carry (forward price is higher), the American binary longs gamma everwhere.
(?) With positive carry, American binary is like risk reversal on the same asset without drift.

##### Hedging an American Binary: Fooled by the Greeks
The gap delta caused slippage.

##### The Ravages of Time
The hedge position should be unwinded upon knockout: for longing binary call, one should buy the delta back when price goes higher than barrier.
High theta problem.

##### Understanding the Vega Convexity
Vega of American binary is concave. Hedge vega with vanilla will cause short position of fourth moment.
(?) From a trader's experience, the worst moment to be short is fourth because of lack of compensation.

  * (-) No potential profit but only potential loss.

Risks include:

* Duration risk
* Gap risk: unwind slippage of hedge position
* Vega risk: after knock out
* Vega concavity: better hedge with positive fourth moment

##### Trading Methods
(?) American binary options are truly options on time rather than options on the asset.
They can only be hedgable with instruments that are similarly options on time.
It is best to divorce a barrier book from a vanilla position.

##### Case Study: At-Settlement American Binary Options
More difficult to trade, creating a short gamma area around the barrier.

##### Other Greeks
Less significant.

#### American Double Binary Options
Ameircan double bet is bet with a lower strike and a higher strike.
American double bets trade at a very narrow discount of the bet value.
A double bet trading at 80% of face value implies, (no drift and no interest rates), that it has about 20% of the nominal time to live.

##### Vega of the Double Binary
Even much more concavity than the single barrier.
Above an iv 20% (3 month) the bet reaches a price close to 100%.

##### Other Applications of American Barriers
###### Amortizing Interest Rate Securities
Maturity, coupon or principal could vary according to whether predefined rate was reached in the market.

###### Credit Risk
Regard government note as a bet on not default, the price of the bet is total paper minus some recovery value. 

### <!-- C19 p325 --> Barrier Options (I)
#### Barrier Options (Regular)
Reguar barrier options are defined as trigger happened only when OTM.
##### Knock-Out Options
Sometimes size of hedge position large enough to impact the market could create profit.

###### Customer Demand for Knock-Out Options
* Fund managers hold a large stock exposure, who would sell it themselves at the barrier level and seek protection for sell-off.
* Chartists that believe a trend with a stop-loss point.

###### Discontinuity at the Barrier
Delta of barrier option OTM is higher to compensate the same ITM payoff with cheaper price.
The unwinding slippage cost should be considered (as American bet).

##### Knock-In Options
###### Customer Demand for Knock-In Options
Mean-reversion market opinions.
Long the barrier means the operator would benefit from the hitting of the triger. (short knock-out or long knock-in)

##### Effects of Volatility
Knock-in has convex vega while knock-out has concave vega, because volatility brings the barrier closer in a nonlinear way.

##### Adding the Drift: Complexity of the Forward Line
(?) A regular knock-out will never have a delta higher than one if the forward line is flat. In an upward sloping forward curve, the delta of the calls can be higher than one.
Delta higher than one will lead to negative gamma somewhere.

  * (-) The higher than one delta might come from the fact that spot goes higher, forward price goes more higher, which drive the probability of knock-out down near the barrier. Away from the barrier, this effect will fade.
  When price is 1 unit higher, the payoff at expiration of vanilla are 1 higher in the ITM zone. By contamination principle, the price should be higher, but the increase less than 1.

(?) When maturity is long relative to distance between strike and barrier, the price of knock-out is like the payoff of European one on expiration. 

  * (-) Not like, the payoff might have a difference. Only the shape is similar.

##### Risk Reversals
(?) Vega could be hedged with risk reversals (to eliminate volga): vega increases in one direction and fades in the other.

  * (-) For risk reversals with strikes not symmetric, the more ATM leg will have more constant vega, and the more OTM leg will have a more convex vega (with regard to volatility). And more close leg will dominate to maintain a slightly positive vega. This makes the whole profile similar to vega of barrier options.

##### Put/Call Symmetry and the Hedging of Barrier Options
###### Option Symmetry
A call with strike $K_1$ and a put with strike $K_2$ under same volatility, if $K_1K_2=F^2$, $\sqrt{K_1}$ units of put and $\sqrt{K_2}$ units of call will have exact vega and gamma.

A knock-out call could be replicated as that long OTM call and short OTM put whose strike is symmetrical to call at the barrier. Then when the underly reaches barrier, the combination should be worth 0, under the assmption of no skew.
The risk reversal is nothing but some form of risk reversal. 
The barrier call should be cheaper when there is a downside skew.
A knock-in call could be replicated as long put, and at barrier execute the price 0 risk reversal to switch to a call.
###### Benefits of the Method
1. Pricing the skew
2. Pricing the volatility curve
   It means taking term structure (volatility ladder) into account, because two legs react to different periods.
3. Hedging: hedge gamma

###### Pitfalls of the Method
1. It needs stable skew
2. It needs a flat and constant forward curve. (Symmetrical strike responds to it.)

(?) There might not be a real duration susceptible of hedging the skew owing to the instability of the stopping time.

  * (-) It refers to two different duration legs.

The forward curve needs to be flat, otherwise it might not hedge exactly. (Because of $(\frac{B}{S})^{2\lambda}$ in barrier option price.)

###### Gammas of Structures Compared with That of the Risk Reversal
Under high interest rate, the barrier option presents negative gamma above barrier.

###### Skew Implies Instability
(? iv to deduce underly distribution, what is third moment, third to what?) The existence of a skew is accompanied by a noticeable shifting of the third moment and a strong fifth moment.

##### Barrier Decomposition under Skew Environments
Long skew means having the vega increase in the rally, benefiting from a positive third moment. 
(?) Positive skew means put has higher iv.
To price barrier options under skew (to use which vol), use risk reversal decomposition.
Under skew, risk reversal replication only works for today, because the combination has nonzero theta.
(?) The T decomposition formula is: Barrier with skew = Barrier without skew + EV the residual of the replicating portfolio/conditional on hitting time

##### The Reflection Principle
Under this perspective, the barrier symmetry comes from path reflection.
|Price|Intrinsic|Path1|Path2|Net|
|:-:|-:|-:|-:|-:|
|102.97|2.97|1||1|
|101.98|1.98||||
|100.99|0.99|3|1|2|
|100.00|0.00||||
|99.01|0.00|3|3|0|
|98.02|0.00||||
|97.03|0.00|1|3||
|96.04|0.00||||
|95.05|0.00||1||

With binomial tree, knock-out option could be priced with the original path deducted by the common path. (By relection principle, the paths that overlapped by two initial price are the path that touched the barrier.)
Without skew and drift, a regular knock-out option is equal to vanilla minus the same vanilla priced at $\frac{B^2}{S}$ adjusted by $\frac{S}{B}$. 
Call with strike priced with a 96.04 spot will be equal in price to the 96.04 put priced with 100 spot.

##### Girsanov
(?) how to adjust binary tree to relect distribution

##### Effect of Time on Knock-Out Options
Regular ATM knock-out has similar theta to ATM vanilla, while knock-in has a relatively linear theta.

##### First Exit Time and Its Risk-Neutral Expectation
(?) The barrier option should be priced with the volatility corresponding to the expected first exit time.

  * (-) It is not like vanilla, from which the volatility surface is generated. Therefore, it is reasonble to interpolating on the spot iv surface for vanilla. However, under framework of local vol, only few paths of underlying involved use of forward volatility near the expiration, more weight should be put on volatility of shorter term.

(?) It is recommended to hedge at a shorter maturity than the nominal one.

  * (-) See single volatility fudge.

##### Issues in Pricing Barrier Options
###### The Single Volatility Fudge
(?) For a regular knock-out call, the major leg (call) needs to be priced with the nominal maturity, while the second leg (put) needs to be priced with the first exit time.

  * (-) Better to match vega. Vega is highest at strike, a vanilla interpolated at shorter term could replicate the barrier component best.

The hedges in forward assets that correspond to an option position need to be scattered to match the distribution of first exit time.

###### A More Accurated Method: The Dupire-Derman-Kani Technique
It is computer intensive.
(? what is exact implementation in the paper p358)

##### Additional Pricing Complexity: The Variance Ratios
(? why) In a mean-reverting market, the barrier component of a barrier option is overpriced. Because it is more likely to be knocked out when there is high level of intraday negative auto-correlation.

  * (-) Intuitively, a rally will provide 50% probability to not to knock out under trend, but not in the mean-reverting market.

(? to be verfied in China futures market) From author's experience, every market exhibits mean reversion within a one-day framework.
(? seems to be typo) If close-to-close volatility is lower than the Parkinson number, the barrier component is underpriced by the regular method. 


### <!-- C20 p360 --> Barrier Options (II)
#### Reverse Barrier Options
##### Reverse Knock-Out Options
Reverse knockouts generally have negative gamma.
Reverse barrier options have high intrinsic value and little time value, they are more like a bet when close to barrier.

##### Case Study: The Knock-Out Box
It is cheap, but lack enough profit zone.

##### Hedging Reverse Knock-Outs: A Graphical Case Study
The trader sells \$100 million of one-year 5.60 dollar-put FRF call for \$800k, with a KO feature at 4.85, where implied vol is 0.104, with $r=0.07$ and $ q=0.06$.
When option has one day left, the delta could be 20 around the barrier.
Vega and gamma are difficult to hedge because the direction of these two greeks change with time and underly price.
As a trader the author prefers a dangerous trade left roughly unhedged than accurately mishedged.

#### Double Barrier Options
The first exit time is so short, and the way to study them is to examine American double bets.

##### Alternative Barrier Options
A SCUD (second currency underlying) is an option on one asset in one currency with barrier struck on the exchange rate.
A dollar-based fund is long Japanese stocks would like to buy stock put which terminates if the currency appreciates. When the option is terminated, it could make profit.
The correlation between assets makes the alter native barrier resemble a regular one. Independence makes the barrier become a bet on the other option.

##### The Exploding Option
Reverse knock-out with a rebate equal to the exploding payoff.

##### Capped Indexed Option
Reverse knock-out with a rebate equal to the difference between strike and outstrike, and it terminates at the close price rather than terminates anytime like exploding options.

###### The Legality of the Triggering
For underlying asset traded OTC, it could be difficult to confirm the real time price. The best solution (suggested by the author) is to turn to a third party  setting order to see if completed.

###### Barriers and Price Manipulation
In illiquid market, the party longing the barrier could try to hit the barrier with small size transaction to gain profit. (like the case for a cash-settled options)

#### Reading a Risk Management Report
(? two country paradox) The currency in which the P/L is computed should be in the numeraier currency and delta should be expressed in countercurrency.

  * (-) compute pnl cash and raw delta (not delta cash)

##### Gap Risk
The report should show senerio where barrier is touched and the stop-loss is executed.
The gap risk (gap between barrier and the executed price of stop-loss order) should be considered.
The stop-loss order should not be set before the barrier, which will create short gamma position.

##### Gaps and Gap Reports
A mined market is one that has many gapdelta orders and will therefore experience a high level "whipping" and mean reverting volatility around these prices. The opposite is called a cleared market.

### <!-- C21 p389 --> Compound, Choosers, and Higher Order Options
Compound options are extremely sensitive to higher derivatives with respect to spot, particularly vvol. This makes a constant volatility type model dangerous to use.
No known formula to price compound options using stochastic volatility.
Second-order option $(\Phi_1,K_1,\Phi_2,K_2,t_1,t_2)$ is an option with the right to buy a European option for a predetermined price, where $\Phi$ denotes the call/put type.

#### Vega Convexity: the Costs of Dynamic Hedging
Second-order option has convex vega (with respect to volatility).
##### Uses of Compound Options: Hedging Barrier Vega
barrier options present extreme vega concavity as a package.

#### Chooser Options
Options that could turn into either a put or a call at some predetermined time.
The simple chooser has one strike, the "gutspin" chooser allows choice for two strikes.
The price is between maximum of call and put, and straddle.
Chooser resembles a rainbow option because trader has to pick one of two assets. A put and a call are two negatively correlated assets.
A chooser show more convex vega than vanilla.

#### A Few Application of the Higher Order Options
Caption, floortions: options on caps and floors

### <!-- C22 p396 --> Multiasset Options
Multiasset structures include:

* Choice: options involving a choice between instruments: best of, worst of, rainbow options.
* Linear combinations: underly is baskets or spreads
* Product or quotients: underly is product between two instruments, the underly is still lognormal. Easy to price, hard to hedge.

#### Choice Between Assets: Rainbow Options
$\text{Rainbow}(\Phi_1,K_1,...,\Phi_n,K_n,t)$, provides maximum of payoff among different options.
##### Correlation Vega
A matrix corresponds to change in price which results from a change in correlation.
The method could be pushed further for covariance.

##### Correlated and Uncorrelated Greeks
(? why B moves accordingly) Partial delta: sensitivity of the structure to changes in the price of asset A assuming B moves according to its correlation to A.
(?) Outperformance Option: payoff of the form minimum or maximum among assets

#### Linear Combinations
An option on a linear combination of assets. Asian options can be included in it.

##### Basket Options
Options on a weighted sum of two or more assets.

##### Lognormality


### <!-- C23 p416 --> Minor Exotics: Lookback and Asian Options










