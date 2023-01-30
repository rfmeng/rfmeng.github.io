<ndtag category = "Derivatives" editdate="2022-12-13" createdate="2022-12-13" tag="OFD Notes"></ndtag>

### <!-- C1 --> Introduction
### <!-- C2 --> Mechanics of Futures Markets
### <!-- C3 --> Hedging Strategies Using Futures
### <!-- C4 --> Interest Rates
#### Forward Rate Agreements
Two parties agreed on $T_0$ that on $T_2$, a floating interest on $T_1$ LIBOR and a fixed interest $R_K$ are exchanged, where $R_K=R_F$ to make the agreement value 0. On $T_2$, the party pays $LR_K(T_2-T_1)$ receives $LR_M(T_2-T_1)$.
The reason when $R_K=R_F$, FRA has value 0 is that all cash flow could be replicated as follows.
|activity|$T_0$|$T_1$|$T_2$|
|-|-|-|-|
|borrow $Le^{-R_1T_1}$ at $T_0$|$-Le^{-R_1T_1}$|$L$||
|invest $L$ at $R_M$ until $T_2$||$-L$|$L+LR_M(T_2-T_1)$|
|borrow some money until $T_2$|$L[1+R_F(T_2-T_1)]e^{-R_2T_2}$||$-L-LR_F(T_2-T_1)$|
Note that $e^{R_1T_1}[1+R_F(T_2-T_1)]=e^{R_2T_2}$, the three activities have 0 value in total and 0 cashflow at $T_0$ and $T_1$, only one cashflow $L(R_M-R_F)(T_2-T_1)$ at $T_2$. Thus the FRA should be value 0.

### <!-- C5 --> Determination of Forward and Futures prices

### <!-- C6 --> Interest Rate Futures
Interest rate futures prices increase when bond prices increase
#### Day Count and Quotation Conventions
actual/actual, 30/360 and actual/360
US treasury bill quoted with discount rate: $P=\frac{360}{n}(100-Y)$, where $P$ is quoted price and $Y$ is cash price
clean price and dirty price 
#### Treasury Bond Futures
any government bond that has between 15 and 25 years maturity can be deliverd
conversion factor for a bond: quoted price per dollar of principal under 6% with semiannual compounding 
delivery price:
$\text{most recent settlement price}\times\text{conversion factor}-\text{accrued interest}$
theoretical future price is difficult to determine because of cheapest-to-deliver choice
#### Eurodollar Futures
futures on the interest that will be paid on $\$$1 million for a future 3-month period
Eurodollar interest rate is essentially the same as LIBOR
maturity ranges from 3 months to 10 years
The contract is designed so that a one-basis-point move in quote corresponds to  $\$$25 gain or loss per contract, because 1 bp change in the future corresponds to change in the underlying (3-month LIBOR):$$1000000\times0.0001\times0.0025=25$$
final settlement price is $100-R$, where $R$ is 3-month LIBOR
contract price is then $10000[100-0.25(100-Q)]$, where $Q$ is the quote (settlement price)
Eurodollar futures higher than FRA forward rate because of daily settlement and different payment date, both making forward rate lower
one convexity adjustment is $\text{forward rate}=\text{futures rate}-\frac{1}{2}\sigma^2T_1T_2$
where $\sigma$ is standard deviation of 1-year interest rate, all in continuous compounding
with Eurodollar forward rate, we could extend LIBOR spot rate into longer terms
#### Duration-Based Hedging Strategies Using Futures
hedge ratio calculated by the duration at the maturity
#### Hedging Portfolios of Assets and Liabilities
hedge duration


### <!-- C7 --> Swaps
#### Mechanics of Interest Rate Swaps
for interest rate swap, on each payment date, LIBOR at the begining of that payment period is used instead of spot rate on that date
"Plain vanilla" LIBOR-for-fixed swaps on
US interest rates are usually structured so that the financial institution earns about 3 or 4 basis points (0.03% or 0.04%) on a pair of offsetting transactions (which is bid-ask spread for market maker)
swap rate: midpoint of bid-ask spread
"assume" a swap where fixed rate equals to current swap rate has 0 value
#### Confirmation
legal agreement underlying a swap, draft facilitated by International Swaps and Derivatives Association (ISDA)
#### Comparative-Advantage Argument
##### Criticism
floating rate is 6-month based and leaves an opportunity to change the spread every 6 months, there is a term mismatch, namely, rollover risk
the spreads between rates offered to different parties are a reflection of default probability
#### Nature of Swap Rates
LIBOR is the rate of interest at which AA-rated banks borrow for periods up to 12 months from other banks
a 5-year swap rate is equivalent to continuously lend money to AA borrower, therefore less than 5-year AA borrowing rate (AA rating might not maintain throughout the whole 5 years)
LIBOR is only for maturities out to 12 months, use Eurodollar futures? to produce LIBOR out to 2 years, use swap rate to generate LIBOR/swap zero curve further
#### Valuation of Interest Rate Swaps
use LIBOR/swap rates to discount
value as $V_{swap}=B_{fl}-B_{fix}$ or value as a series of FRAs
#### Term Structure Effects
a swap is value 0 at inception, the value of each individual might not
#### Fixed-for-Fixed Currency Swaps
exchange principal and interest payments at two fixed rate in two currencies, the principal exchange happens at the beginning and at the end of the life of the swap
a practical fixed-for-fixed currency swap should not leave foreign currency risk for particpants
value as two bonds or value as a series of forward contracts
#### Other Currency Swaps
fixed-for-floating currency swap: fixed-for-fixed currency swap + interest rate swap
foating-for-floating currency swap: fixed-for-fixed currency swap + 2 interest rate swap
#### Credit Risk
swap has RELU-like exposure for financial institutes
CCP needs intial margin and variation margin
credit default swap is to pay the CDS spread to protect principal of bond of reference entity
#### Other Types of Swaps
Variations on the Standard Interest Rate Swap: commercial paper rate is used instead of LIBOR
Equity Swaps: total return on index and interest 
options: embedded option or option on swap (swaption)
Commodity Swaps, Volatility Swaps, and Other Exotic Instruments

### <!-- C8 --> Securitization and the Credit Crisis of 2007

### <!-- C9 --> OIS Discounting, Credit Issues, and Funding Costs 
before credit crisis of 2007, LIBOR/swap rates are proxies for risk-free rate
#### The Risk-Free Rate
derivatives market does not use treasury rates as risk-Free rates, because they are artificially low
after credit crisis, banks use OIS rate for collateralized transactions and LIBOR or other higher rate for non-collateralized transactions
#### OIS Rate
overnight index swap
fed funds rate: overnight unsecured borrowing rate of interest between financial institutions, supervised by the central bank
effective federal funds rate: weighted average of the rates in brokered transactions (with weights proportional to transaction size)
OIS: a swap where a fixed rate for a period (e.g., 1 month or 3 months) is exchanged for the geometric average of the overnight rates during the period
3-month LIBOR-OIS spread: generate because of default risk during the 3 months
any hint of an imminent credit problem is likely to lead to a financial institution being excluded from the overnight market
construct OIS zero curve when OIS rates are used for discounting
OIS usually shorter than 5 years, regard LIBOR-OIS spread as stable for longer term
#### Valuing Swaps and FRAS with OIS Discounting
value FRA assuming that forward rate is realized, discounting by OIS rate
#### OIS vs. LIBOR: Which Is Correct
use LIBOR for uncollaterized transaction because of funding cost
use OIC for uncollaterized transaction because when risk-free portfolio is set up we should use risk-free rate
#### Credit Risk: CVA and DVA
discount rate is not used as a way of allowing for credit risk when a derivative is valued
CVA (credit value adjustment): expected loss from counterparty's default
DVA (debit value adjustment): expected gain from its own default
CRA (collateral rate adjustment): interest paid on colleteral
true value is $f_{nd}-CVA+DVA-CRA$
####  Funding Costs
if a company uses its average funding cost (e.g. 7%) as a hurdle rate for all projects, low-risk project (e.g. 6% with risk-free rate 5%) will tend to seem unattractive and high-risk projects will tend to seem attractive
controversial FVA (funding value adjustment): adjustment if bank's average funding cost were used as "risk-free" discount rate
(ND: should use marginal funding cost rather than average funding cost)

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

### <!-- C19 -->  The Greek Letters
#### Delta Hedging
the cumulative cost of dynamic hedging should be close to BSM price, the cost comes from buy-high and sell-low
more options in a portfolio, more feasible to hedge
#### Theta
time passage is of certainty, therefore no need to hedge.
#### Gamma
Short-life at-the-money options have very high gammas
#### Vega
two options needed to make a portfolio Gamma neutral and Vega neutral
#### Extension of Formulas
delta of futures contract is $e^{(r-q)t}$

### <!-- C20 -->  Volatility Smiles
#### Volatility Smile is the Same for Calls and Puts
#### Foreign Currency Options
from implied volatility, we could gain implied distribution, it is fat-tail.
if everyone else believes lognormal distribution, we could buy deep OTM option to make money.
the volatility smile becomes less pronounced as option maturity increases:
* percentage impact of nonconstant volatility on implied volatility usually becomes less pronounced
* percentage impact of jumps on both prices and implied volatility becomes less pronounced
#### Equity Options
volatility skew for equities: strike price increases, IV increases
implied distribution: under same mean and standard deviation, the implied has heavier left tail and less heavy right tail
Explanation:
* financial leverage and market value 
* "crashophobia"
#### Alternative Ways of Characterizing the Volatility Smile
* calculate implied volatility with $K/S_0$ or $K/F_0$
* calculate IV on delta, where ATM option is option with delta 0.5
#### Term Structure and Volatility Surfaces
volatility is self-returning 
to price new option, use interpolation to obtain new implied volatility
when defining volatility smile on $\frac{1}{\sqrt{T}}{\ln (\frac{K}{F_0})}$
#### Greek Letters
delta changes, because $\frac{\partial \sigma_{imp}}{\partial S}$ is no longer 0
#### Role of the Model
if changing to another model, the pricing of many nonstandard exotic derivatives might be affected
#### When a Single Large Jump is Anticipated
if a large jump(no clear direction is to happen), volatility smile bows up

### <!-- C21 --> Basic Numerical Procedures





















