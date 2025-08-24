<ndtag category="CFA II" tag="Derivatvies" createdate="2025-08-24" editdate="2025-08-24"></ndtag>


### <!-- C1 p15 --> Pricing and Valuation of Forward Commitments
#### Forwards Contracts
##### General Formula
* Pricing: $F_0(T)=S_0(1+r_f)^T$
* Valuation: for long party, value: $(F_t(T)-F_0(T))/(1+r_f)^{T-t}$
* Benefits and Costs of Carrying Assets: $F_0(T)=(S_0-PVB+PVC)(1+r_f)^T$
  * PVB: present value of holding benefits
  * PVC: present value of holding cost

##### Fixed-Income Forwards and Equity Forwards

##### Forward Rate Agreement
a×b FRA, FRA rates are simple interest rates and quoted on 30/360 basis
* a: number of months until contract expires
* b: number of months until underlying loan is settled
* payment exchanges at time b

$1+\frac{30b}{360}S_b=(1+\frac{30a}{360}S_a)(1+\frac{30(b-a)}{360}FR)$

#### Fixed Income Futures
bonds' transaction settled at full price but the quotation price is flat
* the clean price of a bond with coupon 4% and interest rate 4% will be flat but the full price will be zigzag

a basket of deliverable bonds: 100,000 par value T-bonds with any coupon but with a maturity of at least 15 years
* A price quote of 95-18 is equal to 95.5625% (18/32)
* the underlying asset is a hypothetical 30 year treasury bond with 6% coupon

cheapest to deliver: avoid short squeeze (逼空)
Conversion Factor (CF): principal invoice amount = Quoted futures price × CF
total invoice amount = principal invoice amount + accrued interest
* the futures contract seller will receive

example:
* underlying of Euro-bond futures quoted at 108 and has accured interset of 0.083
* Euro-bond futures matures in one month
* at expiration the underlying bond will have accrued interest of 0.25 and no coupon payments due until the futures contract expires
* conversion factor of the underlying bond is 0.729535 and risk free rate is 0.1%
* futures price:
  * (108 + 0.083 - PVC) × 1.001^(1/12) = p × 0.729535 + 0.25
  * PVC is present value of coupon received, in this example, 0
  * the two accrued interest refers to two coupon payments

#### Swap Contracts
##### Interest Rate Swaps
floating rate payments are typically made in arrears: the interest rate is determined at the beginning of the period but the payment is made at the end of the same period
on each coupon-reset day, the floating-rate bond has a value equal to its par value

###### Pricing 
$1=F\sum D_n+D_n$
* F: fixed swap rate
* D: discount factor
* all simple interest rate, should adjusted by time


###### Valuation
example1:
* quarterly pay will swap last for 1 year
* at T=0, LIBOR are 90-day 2.5%, 180-day 3%, 270-day 3.5%, 360-day 4%
* 30 days later, LIBOR are 60-day 3%, 150-day 3.5%, 240-day 4%, 330-day 4.5%
* at T=0:
  * D1 = 1 / (1 + 2.5% × 90 / 360) = 0.9938, D2 = 0.9852, D3 = 0.9744, D4 = 0.9615
  * F = (1 - D4) / (D1 + D2 + D3 + D4) = 0.98%, swap rate = 0.98% × 4 = 3.92%
* at T=1:
  * D1 = 1 / (1 + 3% × 60 / 360) = 0.9950, D2 = 0.9856, D3 = 0.9740, D4 = 0.9604
  * fixed coupon bond: 0.98% × (D1 + D2 + D3 + D4) + D4 = 0.998767
  * floating coupon bond: (1 + 2.5% / 4) × D1 = 1.001219

example2:
* two years ago, we entered a annual-reset 7-year IRS with fixed swap rate of 2%
* discount factor is 0.990, 0.978, 0.965, 0.952, 0.938 for the next 5 years
* valuation of IRS:
  * Ft = (1 - D5) / (D1 + D2 + D3 + D4 + D5) = 1.29%
  * Vt = (F0 - Ft) × (D1 + D2 + D3 + D4 + D5) = 0.03425

##### Currency Swaps
Cross Currency Swap (CCS): 
* principal amount of currency swap is exchanged at the beginning and returned at termination
* on settlement dates, interest payments are not netted
* China receives dollar principal and pays the dollar interest

###### Pricing
###### Valuation
the CCS is nominated in 7 CNY and 1 USD at the beginning, when the exchange rate is 6 CNY/USD, the 1 CNY value should be adjusted to 7 CNY and then divided by 6.


##### Equity Swaps
notional amount is not exchanged and payments are netted
total return swap: dividend is also paid



### <!-- C2 p93 --> Valuation of Contingent Claims
#### Binomial Option Valuation Model
##### Binomial Model
$\pi_u=\frac{(1+r_f)^T-d}{u-d}$


##### Interest Rate Option
$u=d=1/2$, because interest rate should be an martingale
call payoff = max(0, uderlying rate - exercise rate) × notional principal


#### Black-Sholes-Merton Model
##### Initial Model
##### Black Model
###### Option on Futures
$c=e^{-rT}F(T)N(d_1)+Ke^{-rT}N(d_2)$

###### Interest Rate Option
for a m×n structure, $c=Ne^{-r_f^cn\frac{30}{360}}[F_{m\times n}N(d_1)-KN(d_2)]\frac{n-m}{12}$

###### Swaption
swaption: option on swap
payer swaption: option on a swap to pay fixed, received floating.
payer swaption is equivalent to call on floating rate
V(payer) = NP × accrual period × PVA × [FN(d1) - KN(d2)]
* PVA: sum of discount factor


##### Option Greeks
