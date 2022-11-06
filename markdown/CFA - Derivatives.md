<h1>Derivatives</h1>
<h3>Derivative Markets and Instruments</h3>
<h4>DERIVATIVES: INTRODUCTION, DEFINITIONS, AND USES</h4>
<!-- -->

DEFINITION: A derivative is a financial instrument that derives its performance from the performance of an underlying asset.
two classes:
* forward commitments: forward contracts, futures contracts, and swaps
* contingent claims

<h4>THE STRUCTURE OF DERIVATIVE MARKETS</h4>
<!--  -->
Exchange-Traded Derivatives Markets: clearing (verify execution of transaction) and settlement
Over-the-Counter Derivatives Markets
OTC market is less liquid

<h4>TYPES OF DERIVATIVES: INTRODUCTION, FORWARD CONTRACTS</h4>
<h4>TYPES OF DERIVATIVES: FUTURES</h4>
<!--  -->
mark to market (or daily settlement)
intial margin
margin call if the margin account lower than maintainance margin
some future contracts contain price limits
delivery: use last day's settlement price as delivery price, but the longer should settle the gain or loss in his margin account first

<h4>TYPES OF DERIVATIVES: SWAPS</h4>
<!--  -->
<h4>CONTINGENT CLAIMS: OPTIONS</h4>
<!--  -->
option premium: price of option
for call option, it is called in the money is $S_t>K$

<h4>CONTINGENT CLAIMS: CREDIT DERIVATIVES</h4>
<!--  -->
total return swap: swap between total return of a bond/loan and fixed/floating interest
credit spread option: a call option in which the underlying is the credit spread
credit-linked note (CLN): the buyer of the credit-linked receives less principal if default happens, the protection buyer issues CLN
credit default swap (CDS): CDS buyer pays a series of payment and receives compensation for credit losses

<h4>TYPES OF DERIVATIVES: ASSET-BACKED SECURITIES AND HYBRIDS</h4>
convertible bond, callable bond etc.

<h4>DERIVATIVES UNDERLYINGS</h4>
other: weather, electricity and disaster

<h4>THE PURPOSES AND BENEFITS OF DERIVATIVES</h4>
<!--  -->
Risk Allocation, Transfer, and Management
Information Discovery, such as future price and implied volatility
Operational Advantages: lower transaction cost than underlying, greater liquidity than underlying; and short selling is easy
Market Efficiency

<h4>CRITICISMS AND MISUSES OF DERIVATIVES</h4>
<!--  -->
Speculation and Gambling
Destabilization and Systemic Risk

<h4>ELEMENTARY PRINCIPLES OF DERIVATIVE PRICING</h4>
<!--  -->
storage and arbitrage
arbitrage opportunity exists if relative price changes:
<img src="images/CFA-derivative-arbitrage opportunity.png" width="100%"/>


<h3>Basics of Derivative Pricing and Valuation</h3>
<h4>BASIC DERIVATIVE CONCEPTS, PRICING THE UNDERLYING</h4>
<!--  -->
convenience yield (include dividend) net of storage cost 
cost reduce the current price and the convenience yield increase the current price
cost of carry: cost - benefit
$S_0=\frac{ES_T}{(1+r+\lambda)^T}-\theta+\gamma$, where $\theta$ is cost and $\gamma$ is benefit

<h4>THE PRINCIPLE OF ARBITRAGE</h4>
<h4>PRICING AND VALUATION OF FORWARD CONTRACTS: PRICING VS. VALUATION; EXPIRATION; INITIATION</h4>
<!--  -->
$F_0(T)=(S_0-\gamma+\theta)(1+r)^T$

<h4>PRICING AND VALUATION OF FORWARD CONTRACTS: BETWEEN INITIATION AND EXPIRATION; FORWARD RATE AGREEMENTS</h4>
<!--  -->
$V_t(T)=S_t-(\gamma-\theta)(1+r)^T-F_0(T)(1+r)^{-(T-t)}$

<h5>forward rate agreements</h5>
FRA: fixed rate for floating rate, one time
<img src="images/CFA-derivative-FRA.png" width="100%"/>

<h4>PRICING AND VALUATION OF FUTURES CONTRACTS</h4>
<!--  -->
if futures prices and interest rates are uncorrelated, forwards and futures prices will be the same

<h4>PRICING AND VALUATION OF SWAP CONTRACTS</h4>
a series of forward contract priced at swap price

<h4>PRICING AND VALUATION OF OPTIONS</h4>
<!--  -->
time value: the difference between the market price of the option and its intrinsic value
time value decay: price converges to intrinsic value

<h4>LOWER LIMITS FOR PRICES OF EUROPEAN OPTIONS</h4>
<!--  -->
minimum value of option:
* $c_0\geq max(0,S_0-X/(1+r)^T)$
* $p_0\geq max(0,X/(1+r)^T-S_0)$

<h4>PUT-CALL PARITY, PUT-CALL-FORWARD PARITY</h4>
<!--  -->
put call parity: $S_0+p_0$ = $c_0+X/(1+r)^T$, which corresponds to protective put and ficuciary call
put-call-forward parity: $F_0/(1+r)^T+p_0$ = $c_0+X/(1+r)^T$

<h4>BINOMIAL VALUATION OF OPTIONS</h4>
<h4>AMERICAN OPTION PRICING</h4>
<!--  -->
minimum value of option:
* $C_0\geq max(0,S_0-X/(1+r)^T)$
* $P_0\geq max(0,X-S_0)$

American call early exercise: right before ex-dividend drop





