<ndtag category = "Derivatives" editdate="2024-09-11" createdate="2022-12-13" tag="Hedging"></ndtag>

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










