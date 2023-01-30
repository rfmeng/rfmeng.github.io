<ndtag category = "Derivatives" editdate="2022-01-30" createdate="2022-12-13" tag="OFD Notes"></ndtag>

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













