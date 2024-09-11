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











