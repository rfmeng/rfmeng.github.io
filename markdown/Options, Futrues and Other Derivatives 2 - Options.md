<ndtag category = "Derivatives" editdate="2022-01-30" createdate="2022-12-13" tag="OFD Notes"></ndtag>

### <!-- C10 --> Mechanics of Option Markets
#### Terminology
total value = intrinsic value + time value
open interest: total long (or short) order over the market
#### Commissions
commissions of the underlying might lead to a preference of selling the option rather than exercise them
### <!-- C11 --> Properties of Stock Options
#### Bounds
$c\leq S_0$ and $C\leq S_0$, because a call provides a right to buy a stock
similarly, $P\leq K$ and $p\leq Ke^{-rT}$
$c\geq \max(S_0-Ke^{-rT},0)$ and $p\geq \max(Ke^{-rT}-S_0,0)$ for non-dividend-paying stock
$C=c$
#### Put-Call Parity
$S_0-K\leq C-P\leq S_0-Ke^{-rT}$
$P\geq K-S_0$, by "Americanness"
#### Put-Call Parity and Capital Sturcture
a company fund by equity and debt, suppose at $T$, a principal $K$ should be paid to debtholder, then the payoff at $T$ should be $\max(A_T-K,0)$ for shareholder. Value for equity is then $c$, value for debtholder is then $Ke^{-rT}-p$, this should sum to the total asset. Thus we have $A_0 = c+Ke^{-rT}-p$

### <!-- C12 --> Trading Strategies Involving Options
#### Principal-Protected Notes
an option and a zero-coupon bond
#### Option and Underlying
covered call and protective put
#### Spreads
Multiple Options of Same Type
bull/bear spread: buy one and sell one
box spread: bull call spread and bear put spread, fixed payoff $K_2-K_1$
butterfly spread
calendar spread: two options with different maturities
#### Combinations
combination of options of different types
straddle
strip: one call and two puts, same strike
strap: two calls and one put, same strike
strangle: like straddle

### <!-- C13 --> Binomial Trees
risk neutral probability: $p=\frac{e^{r\Delta t}-d}{u-d}$
to match volatility: $p(u-1)^2+(1-p)(d-1)^2-[p(u-1)+(1-p)(d-1)]^2=\sigma^2\Delta t$
then a solution is $u=e^{r\Delta t}$ and $d=e^{-r\Delta t}$


### <!-- C14 --> Wiener Process and Ito Lemma
### <!-- C15 --> Black-Scholes-Merton Model
### <!-- C16 --> Employee Stock Option
#### Accounting Issues
Accounting standards have now changed to require the expensing of all stock-based compensation at its fair value on the income statement
could use varable strike price, such as change with S&P 500
#### Valuation
"Quick and Dirty": estimate expected life and use BSM
Binomial Tree Approach: estimate leaving rate and probability of exercise
Exercise Multiple Approach
market-based approach: auction or so
#### <!-- actually C15 --> Dilution 
annoucement of grant of employee option will lead to stock price's decrease
stock price after decrease is used in the valuation of the option
the payoff to an option holder if the option is exercised is $\frac{NS_T+MK}{N+M}-K$
#### Backdating Scandals
make the grant date of employee option earlier for lower strike price

### <!-- C17 --> Options on Stock Indices and Currencies
call options on high-interest currencies and put options on low-interest currencies are the most likely to be exercised prior to maturity
#### Currency Options
range forward: long postion of a $K_2$ call and short postion of a $K_1$ put where $K_2>K_1$

### <!-- C18 --> Futures Options
#### Nature of Futures Options
If a call futures option is exercised, the holder acquires a long position in the underlying futures contract plus a cash amount equal to the most recent settlement futures price minus the strike price. The long position could be closed immediately, this is effective to $\max(F-K,0)$.
#### Reasons for the Popularity
* futures market is more liquid (commodity or treasury bond), the price could be know immediately
* lower transaction cost
* exercise is settled in cash, no requirement of capital
* traded side by side, more efficient

#### Put-Call Parity
$c+Ke^{-rT}=p+F_0e^{-rT}$
a European put and cash of $F_0e^{-rT}$ and long position in futures
#### Valuation Using Binomial Trees
risk neutral probability $p=\frac{1-d}{u-d}$, resulting from the fact that futures' daily settlement
#### Drift of a Futures Price when Risk-Neutral
because the price to enter a futures contract is 0, the expected payoff must also be 0
the assumption in stochastic way is $dF=\sigma Fd\tilde{B_t}$
#### Black's Model for Valuing Futures Options
Consider an asset $Y_t=F_te^{-r(T-t)}$, $dY=rYdt+\sigma Yd\tilde{B_t}$, futures option and option with $Y$ being underlying are equivalent then we can just price the latter
#### American Options
relationship between values of American futures options and American spot options are to be determined, depending on contango or backwardation
#### Futures-Style Options
futures contracts on the payoff from an option
it is never optimal to exercise an American futures-style options on a futures contract early