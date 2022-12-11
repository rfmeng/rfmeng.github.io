<ndtag category="CFA I" tag="Derivatives" createdate="2022-12-11" editdate="2022-12-11"></ndtag>
<h3>Derivative markets and instruments</h3>
<h4>Derivatives: introduction, definitions, and uses</h4>
<!-- -->

DEFINITION: A derivative is a financial instrument that derives its performance from the performance of an underlying asset.
two classes:
* forward commitments: forward contracts, futures contracts, and swaps
* contingent claims

<h4>The structure of derivative markets</h4>
<!--  -->
Exchange-Traded Derivatives Markets: clearing (verify execution of transaction) and settlement
Over-the-Counter Derivatives Markets
OTC market is less liquid

<h4>Types of derivatives: introduction, forward contracts</h4>
<h4>Types of derivatives: futures</h4>
<!--  -->
mark to market (or daily settlement)
intial margin
margin call if the margin account lower than maintainance margin
some future contracts contain price limits
delivery: use last day's settlement price as delivery price, but the longer should settle the gain or loss in his margin account first

<h4>Types of derivatives: swaps</h4>
<!--  -->
<h4>Contingent claims: options</h4>
<!--  -->
option premium: price of option
for call option, it is called in the money is $S_t>K$

<h4>Contingent claims: credit derivatives</h4>
<!--  -->
total return swap: swap between total return of a bond/loan and fixed/floating interest
credit spread option: a call option in which the underlying is the credit spread
credit-linked note (CLN): the buyer of the credit-linked receives less principal if default happens, the protection buyer issues CLN
credit default swap (CDS): CDS buyer pays a series of payment and receives compensation for credit losses

<h4>Types of derivatives: asset-backed securities and hybrids</h4>
convertible bond, callable bond etc.

<h4>Derivatives underlyings</h4>
other: weather, electricity and disaster

<h4>The purposes and benefits of derivatives</h4>
<!--  -->
Risk Allocation, Transfer, and Management
Information Discovery, such as future price and implied volatility
Operational Advantages: lower transaction cost than underlying, greater liquidity than underlying; and short selling is easy
Market Efficiency

<h4>Criticisms and misuses of derivatives</h4>
<!--  -->
Speculation and Gambling
Destabilization and Systemic Risk

<h4>Elementary principles of derivative pricing</h4>
<!--  -->
storage and arbitrage
arbitrage opportunity exists if relative price changes:
<p class="wrapper" style="text-align:center;">
<img src="images/CFA I/CFA I-derivative-arbitrage opportunity.png" width="450px" max-width="100%" align="center"></p>


<h3>Basics of derivative pricing and valuation</h3>
<h4>Basic derivative concepts, pricing the underlying</h4>
<!--  -->
convenience yield (include dividend) net of storage cost 
cost reduce the current price and the convenience yield increase the current price
cost of carry: cost - benefit
$S_0=\frac{ES_T}{(1+r+\lambda)^T}-\theta+\gamma$, where $\theta$ is cost and $\gamma$ is benefit

<h4>The principle of arbitrage</h4>
<h4>Pricing and valuation of forward contracts: pricing vs. valuation; expiration; initiation</h4>
<!--  -->
$F_0(T)=(S_0-\gamma+\theta)(1+r)^T$

<h4>Pricing and valuation of forward contracts: between initiation and expiration; forward rate agreements</h4>
<!--  -->
$V_t(T)=S_t-(\gamma-\theta)(1+r)^T-F_0(T)(1+r)^{-(T-t)}$

<h5>Forward rate agreements</h5>
FRA: fixed rate for floating rate, one time
<p class="wrapper" style="text-align:center;">
<img src="images/CFA I/CFA I-derivative-FRA.png" width="450px" max-width="100%" align="center"></p>

<h4>Pricing and valuation of futures contracts</h4>
<!--  -->
if futures prices and interest rates are uncorrelated, forwards and futures prices will be the same

<h4>Pricing and valuation of swap contracts</h4>
a series of forward contract priced at swap price

<h4>Pricing and valuation of options</h4>
<!--  -->
time value: the difference between the market price of the option and its intrinsic value
time value decay: price converges to intrinsic value

<h4>Lower limits for prices of european options</h4>
<!--  -->
minimum value of option:
* $c_0\geq max(0,S_0-X/(1+r)^T)$
* $p_0\geq max(0,X/(1+r)^T-S_0)$

<h4>Put-call parity, put-call-forward parity</h4>
<!--  -->
put call parity: $S_0+p_0$ = $c_0+X/(1+r)^T$, which corresponds to protective put and ficuciary call
put-call-forward parity: $F_0/(1+r)^T+p_0$ = $c_0+X/(1+r)^T$

<h4>Binomial valuation of options</h4>
<h4>American option pricing</h4>
<!--  -->
minimum value of option:
* $C_0\geq max(0,S_0-X/(1+r)^T)$
* $P_0\geq max(0,X-S_0)$

American call early exercise: right before ex-dividend drop





