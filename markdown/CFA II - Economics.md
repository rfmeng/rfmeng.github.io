<ndtag category="CFA II" tag="Economics" createdate="2025-08-03" editdate="2025-08-09"></ndtag>

### <!-- C1 p389 --> Currency Exchange Rates: Understanding Equilibrium Value
#### Exchange Rate Calculation
Price currency/Base currency: 7 CNY/USD
bid-ask spread: often stated as pips, except for yen (0.01)
* USD/EUR could be quoted as \$1.4124~\$1.4128, the spread is \$0.0004 (4 pips)

interbank spread depends on
* currency pair involved
* time of day (trading time of New York and London)
* market volatility

##### Basic Concepts of FX Market
##### Cross Rate Calculation
$(\frac{A}{B})_{\text{bid}}=(\frac{A}{C})_{\text{bid}}(\frac{C}{B})_{\text{bid}}$
$(\frac{A}{B})_{\text{bid}}=1/(\frac{B}{A})_{\text{bid}}$
A dealer is quoting the AUD/GBP spot rate as 1.5060-67, which means bid 1.5060 and ask 1.5067.

##### Triangular Arbitrage
Compare the dealer quote and the interbank cross rate quote.

##### Forward Exchange Rate
If forward quote is higher than spot price, we say
* base currency is trading at a forward premium
* price currency is trading at a forward discount


|Maturity|Rates|
|:-:|:-:|
|Spot|1.0511/1.0519|
|30 days|+3.9/+4.1|

This means forward bid/ask is 1.0511+3.9/10000 and 1.0519+4.1/10000. The base currency is trading at forward premium

###### Mark-to-Market Value
A existing forward contract's net present value.

#### International Parity Condition
##### Interest Rate Parity
###### Covered Interest Rate Parity
$F_{f/d}(1+i_d)=S_{f/d}(1+i_f)$
$\frac{F_{f/d}-S_{f/d}}{S_{f/d}}=\frac{i_f-i_d}{1+i_d}\approx i_f-i_d$
The domestic currency will trade at a forward premium if the foreign risk-free interest rate is higher.

###### Uncovered Interest Rate Parity
无抛补利率平价
$S_{f/d}^e(1+i_d)=S_{f/d}(1+i_f)$
Interest rate parity when investors do not use forward contract to arbitrage.
The change in spot rate over the investment horizon should, on average (expectation), equal the differential in interest rates between two countries.
The parity is of long term equilibrium sense. The idea that higher interest rate will result in appreciation of currency is short term behavior.

Assumptions:
* investors risk-neutral
* expected appreciation/depreciation of the exchange rate offsets the yield difference

In domestic currency terms, the investment return on an uncovered foreign-currency-denominated investment is equal to $(1+i_f)(1-\%\Delta S_{f/d}^e)$


###### FX Carry Trade
When UIRP does not hold, investor invests in a higher yielding currency using funds borrowed in a lower yielding currency (funding currency), during periods of low volatility (high volatility will spell huge cash risk).
* Example: exchange rate for USD/GBP is 1.50 today and 1.49 one year later. Interest rate is 3% for U.K. and 1% for U.S. The profit to borrow in the U.S. and invest in the U.K. is:
  * Gross return = $(1+i_f)(1-\%\Delta S_{f/d}^e)=(1+3\%)(1-0.67\%)-1=2.31\%$
  * Net return = 2.31% - 1% = 1.31%

###### Forward Rate Parity
If both covered interest rate parity and uncovered interest rate parity hold, we have $F_{f/d}=S_{f/d}^e$, which means the forward exchange rate will be an unbiased predictor of the future spot exchange rate.
CIRP must hold because of lack of arbitrage. The question of whether FRP holds is dependent upon whether UIRP holds.

##### Purchasing Power Parity
Absolute PPP: $S_{f/d}=\frac{P_f}{P_d}$
Relative PPP: $\%\Delta S_{f/d}\approx\pi_f-\pi_d$
Ex-ante PPP: $\%\Delta S_{f/d}^e\approx\pi_f^e-\pi_d^e$
high inflation will cause currency depreciate

##### International Fisher Effect
Fisher effect: $i=r+\pi^e$, where $i$ is nominal interest rate and $\pi^e$ is expected inflation rate.
If UIRP and Ex-ante PPP hold, we have $r_f=r_d$ (Real Interest Rate Parity).
International Fisher effect: If RIRP holds, $i_f-i_d\approx\pi_f^e-\pi_d^e$.

#### Balance of Payment
capital account includes financial account in CFA I
* current account: goods and service
* capital account: money

current account affects the FX rate in the long term
capital account affects FX rate in the short term:
* money inflow will cause appreciation

##### Current Account
###### 1. Flow Supply/Demand Channel
export > import → trade surplus (persistent current account surplus) → sell foreign currency → appreciation of domestic currency → affect export
amount by which exchange rates must adjust to restore current accounts to balanced positions depends on:
* reponse of import and export prices to changes in the exchange rate
* reponse of import and export demand to changes in the exchange rate

###### 2. Portfolio Balance Channel
current account imbalances shift financial wealth from deficit nations to surplus nations
trade surplus → foreign currency asset increases → reduce foreign currency holding 

###### 3. Debt Sustainability Channel
a large and persistent current account deficit will experience untenable rise in debt, will cause depreciation through investors' lack of confidence.

##### Capital Account
excessive emerging market capital inflows often plant seeds of crisis by contributing to:
* unwarranted appreciation of currency
* huge buildup in external indebtedness
* asset bubble
* consumption binge  thus current account deficit
* overinvestment in risky projects

increasing equity prices can attract foreign capital

#### Monetary and Fiscal Policy
##### 1. Mundell-Fleming Model
Consider in short term and assume inflation plays no role
high capital mobility:
* expansionary monetary policy → interest rate decrease → capital flows to high yielding countries → depreciation pressure
* expansionary fiscal policy → spending increase or tax decrease → (?) interest rate increase (- government borrows more money) → capital flows being attracted from low yielding countries → appreciation pressure

low capital mobility:
* expansionary monetary policy → boost spending and import → worsen trade balance → depreciate pressure
* expansionary fiscal policy → increase import → create trade deficit → depreciate pressure

##### 2. Monetary Approach
###### Pure Monetary Model
$MV=PY$, where $M$ is money supply, $V$ is money flow volecity, $P$ is price level and $Y$ is output
assume purchase power parity holds, money supply induces increase domestic price levels, leading to a depreciation

###### Dornbusch Overshooting Model
Assume prices have limited flexibility in the short run but flexible in the long run.
Expansionary monetary policy will lead to lower interest rate, and thus depreciation. In the short term, exchange rates overshoot (超调, higher level of depreciation) the long-run PPP implied values. The depreciation of currency is greater than depreciation implied by PPP.

##### 3. Portfolio Balance Approach
Portfolio balance approach focus on long term implications.
In the long run, expansive fiscal policy will cause central bank monetize debt and fiscal stance more restrictive, leading to currency depreciation.

#### Currency Crisis
Capital flows can be a blessing and a curse. Governments resist excessive inflow through capital control and direct intervention.
Policymaker should enable monetary authority to pursue independent monetary policies.
Definition:
* Narrow sense: fixed exchange rate to floating exchange rate
* Broad sense: volatile exchange rate

Swiss Franc crisis: central bank cannot maintain the fixed exchange rate due to appreciation pressure.

Warning signs:
* liberalized free capital markets
* large inflow of foreign capital
* banking crises
* fixed or partially fixed exchange rates are more susceptible
* ratio of exports to imports (terms of trade)
* aprreciation against historical mean
* higher inflation
* foreign exchange reserve tends to decline


### <!-- C2 p467 -->  Economic Growth
#### Importance of Economic Growth
Relationship between economic growth and equity return
E(Re):
* dividend yield + expected capital gain ($\%\Delta P$)
* ($P=\text{EPS}\frac{P}{E}$) dividend yield + expected repricing ($\%\Delta\frac{P}{E}$) + earning growth per share ($\%\Delta\text{EPS}$)
* dividend yield + expected repricing + inflation rate + real economic growth + change in shares outstanding

$E(R_e)=dy+\Delta\frac{P}{E}+i+g+\Delta S$
* $dy$: dividend yield, fairly stable
* $\Delta\frac{P}{E}$ different level over market cycles

(?) $\Delta S=\text{Net buybacks}+\text{Relative dynamism}$, where relative dynamism is number of nonlisted companies.
* More nonlisted companies, lower correlation bewteen GDP and equity return.

Difference of equity return bewteen China and U.S. can be explained by $\Delta S$, China has lower net buybacks and higher relative dynamism. 

#### Production Function
##### Formula Introduction
$Y=Af(K,L)=AK^\alpha L^{1-\alpha}$
$y=\frac{Y}{L}=Ak^\alpha$
$\frac{\Delta Y}{Y}=\frac{\Delta y}{y}+\frac{\Delta L}{L}$
$\frac{\Delta Y}{Y}=\frac{\Delta A}{A}+\alpha\frac{\Delta K}{K}+(1-\alpha)\frac{\Delta L}{L}$

##### Cobb-Douglas Production Function
$Y=Af(K,L)=AK^\alpha L^{1-\alpha}$
* $A$: total factor productivity (technology)
* $\alpha$: share of GDP paid out to the suppliers of capital

To compute $\alpha$, let marginal product of capital equat to rental price of capital $r$, $MPK=\frac{\Delta Y}{\Delta K}=r$, we have $\alpha=r\frac{K}{Y}$.

Properties:
* constant return to scale $f(tK,tL)=tf(K,L)$: increasing all inputs by a fixed percentage leads to the same percentage increase in output
* diminishing marginal productivity (keeping the other input unchanged)

Consider $y=\frac{Y}{L}=Ak^\alpha$, lower $\alpha$, diminishing marginal productivity more significant

###### Capital Deepening vs. Technological Progress
When economy reaches steady state, where the marginal product of capitals equals its marginal cost, capital deepening is useless.

##### Solow's Growth Accounting Equation
$\frac{\Delta Y}{Y}=\frac{\Delta A}{A}+\alpha\frac{\Delta K}{K}+(1-\alpha)\frac{\Delta L}{L}$
* growth rate in potential GDP = long term growth rate of technology + $\alpha$ long term growth rate of capital + $(1-\alpha)$ long term growth rate of labor 
* $\alpha$: elasticity of output with respect to capital ($\frac{\partial \frac{\Delta Y}{Y}}{\partial \frac{\Delta K}{K}}$)
* rate of technological change is not directly measured and must be estimated

$Y=yL$, $\frac{\Delta Y}{Y}=\frac{\Delta y}{y}+\frac{\Delta L}{L}$

##### Extending the Production Function
Including more input into production function:
* natural resources
  * Dutch disease: currency appreciation driven by strong export demand for resources makes other segements of economy less uncompetitive globally.
* labor supply
  * population growth, labor force participation, net immigration and average hours worked
* human capital: knowledge and skills workers acquire
* ICT (Information, Computer and Technology) and Non-ICT capital
* technology
* public infrastructure


#### Theories of Growth
##### Classical Growth Theory
by Thomas Malthus, also known as 马尔萨斯人口论
population growth accelerates when level of per capita income rises above the subsistence income (minimum income needed to maintain life)
technology advances → $Y$ ↑ →  higher population growth ↑ → diminishing marginal return of labor → lower per capita income
The classical model predicts that in the long run, the adoption of new technology results in a larger but not richer population. There is no economic growth.
This is doubted because when GDP is high, birth rate will decrease.

##### Neoclassical Grwoth Theory
by Robert Solow
(?) steady-state rate of growth when output to capital ratio $\frac{Y}{K}$ is constant, so we have $\frac{\Delta y}{y}=\frac{\Delta k}{k}$.
* (-) Here we start from result to gain a proper form of per "effective" capita production/capital $y$ and $k$.
  * Divide both sides of production function $A^tL$, we gain $\frac{Y}{A^tL}=(\frac{K}{A^{\frac{t-1}{\alpha}}L})^\alpha$. The objective is to eliminate existence of $A$ in the per "effective" capita production function $y=f(k)$. Let $t=\frac{t-1}{\alpha}$, we have $t=\frac{1}{1-\alpha}$.
  * So the per "effective" capita production/capital is $y=\frac{Y}{A^{\frac{1}{1-\alpha}}L}$ and $k=\frac{K}{A^{\frac{1}{1-\alpha}}L}$ and we have $y=k^\alpha$.
  * $d\ln k=d\ln K-\frac{1}{1-\alpha}d\ln A-d\ln L=\frac{dK}{K}-\frac{1}{1-\alpha}\theta-n$, $\frac{dk}{k}=\frac{sY}{K}-\delta-\frac{1}{1-\alpha}\theta-n=\frac{sy}{k}-\delta-\frac{1}{1-\alpha}\theta-n$
  * $dk=sy-(\delta+\frac{1}{1-\alpha}\theta+n)k$
  * $dk=0$ in steady state → $\frac{Y}{K}=\frac{y}{k}=\psi$

With $\frac{\Delta y}{y}=\frac{\Delta A}{A}+\alpha\frac{\Delta k}{k}$, we have $g^*=\frac{\Delta y}{y}=\frac{1}{1-\alpha}\frac{\Delta A}{A}=\frac{\theta}{1-\alpha}$ and $G^*=\frac{\Delta Y}{Y}=\frac{\theta}{1-\alpha}+\frac{\Delta L}{L}=\frac{\theta}{1-\alpha}+n$.

In closed economy, investment must be funded by domestic saving $I=sY$.
* $s$ is saving faction of income
* physical capital depreciates at a constant rate $\delta$.
* $\Delta K=sY-\delta K$

steady-state rate of growth when output to capital ratio $\frac{Y}{K}$ is constant: $\frac{\theta}{1-\alpha}=s\frac{Y}{K}-\delta-n$ and $\frac{Y}{K}=\frac{1}{s}(\frac{\theta}{1-\alpha}+\delta+n)\equiv\psi$.
MPK (marginal product of capital) $\alpha\frac{Y}{K}$ is also constant.

Steady state equilibtrium $sy=(\frac{\theta}{1-\alpha}+\delta+n)k$ occurs at the point where savings and actual gross investment per worker are suffiicient to:
* provide capital for new workers entering the workforce at rate $n$
* replace plant and equipment wearing out at rate $\sigma$
* deepen the physical capital stock at rate $\frac{\theta}{1-\alpha}$

##### Endogenous Grwoth Theory
It is regarded Endogenous because technology growth in Solow model in exogenous. Modificaition conclude:
* $Y=AfK^\alpha(EL)^{1-\alpha}$, where $E$ implies labor gain experience in production process.

No diminishing marginal returns to capital.
capital accumulation is main factor accouting in the long run.
R&D expenditures have large postivie externalities.
In the endogenous growth model, the economy does not reach a steady growth rate.
Saving and investment can generate self-sustaining growth at a permanently higher rate.
Higher saving rates implies a permanently higher growth rate.

##### Convergence Debate
* Absolute convergence
  * developing countries will eventually catch up with developed countries in per capita output.
  * The neoclassical model does not imply absolute convergence.
* Conditional convergence
  * conditional on same $s$, $n$ and $f(K,L)$
  * same level or per capita output and steady state growth rate.
* Club convergence
  * Rich and middle income countries that are members of the club are converging to the income level.
  * Poor countries can join the club with appropriate institutional changes.

Endogenous growth model makes no prediction that convergence should occur.

##### Growth in an Open Economy
Opening up the economy can affect growth rate:
* countries can shift resources into industries where they have comparative advantage
* fund from global markets
* technology from global markets
* increases competition in demestic market

For neoclassical model, convergence should occur more quickly.
For endogenous model, a more open trade policy will permanently raise the rate of economic growth.

### <!-- C3 p553 --> Economics of Regulation 
#### Economic Rationale for Regulation
Regulation for economy
* informational frictions
* externalities
* weak competition (monopoly or oligopoly)
* social objectives

Regulation for financial markets:
* protect investors
* integrity of markets
* disclosure
* mitigate agency problems
* prudential supervision of financial institutions

Antitrust regulation

#### Regulators and Regulatory ToolS
Legislative body, court and regulatory body.
Industry self-regulatory bodies.
Regulatory interdpendencies:
* regulatory capture theory (规制俘虏): regulatory body will be influnced or controlled by the industry
* regulatory competition: regulators compete with each other
* regulatroy arbitrage: business shop for the most suitable regulation

Regulatory tools:
* price mechanisms
* restrict/mandate some activities
* provide public goods
* finance private projects

#### Analysis of Regulation
Cost-benefit analysis:
* regulatory burden: cost of regulation
* net regulatory burden: cost less benefits
* approach: natural experiments and trial, regulatory sandboxes (经济特区)

Analysts need to understand how regulation affects companies and industries:
* likelihood of regulatory change
* impact of regulatory change




