<h1>Fixed Income (2)</h1>
<h3>Understanding Fixed-Income Risk and Return</h3>
<h4>INTRODUCTION AND OVERVIEW OF A FIXED-INCOME SECURITY</h4>
<!--  -->
horizon yield: the annualized holding-period
rate of return, calculated use the realized reinvestment future value and the current price
capital gain or loss: the bond’s carrying value and selling price
interest risk consists of coupon reinvestment risk and market price risk (selling price)

<h4>MACAULAY AND MODIFIED DURATION</h4>
<!--  -->
Macaulay duration is weighted average of time to receive payments, where weight are the shares of the full price:
<img src="images/CFA-fixed income-income risk-macaulay duration.png" width="100%"/>

30/360 convention: $DayCountFactor=\frac{360(Y_2-Y_1)+30(M_2-M_1)+(D_2-D_1)}{360}$
$MacDur=\frac{1+r}{r}-\frac{1+r+N(c-r)}{c[(1+r)^N-1]+r}-\frac{t}{T}$, this is duartion in terms of periods, to be anuallized
Modified duration: $ModDur=\frac{MacDur}{1+r}$, where $r$ is the yield-to-maturity per period
$\%\Delta PV^{Full}\approx-AnnModDur\times\Delta AnnYield$

<h4>APPROXIMATE MODIFIED AND MACAULAY DURATION</h4>
<!--  -->
$ApproxModDur=-\frac{PV_+-PV_-}{2PV_0\Delta Yield }$, where  price when the yield-to-maturity is reduced is denoted $PV_-$
$ApproxMacDur=(1+r)ApproxModDur$, where $r$ is the yield per period.

<h4>EFFECTIVE AND KEY RATE DURATION</h4>
<!--  -->
effective duration: $EffDur=-\frac{PV_+-PV_-}{2PV_0\Delta Curve }$, where $\Delta Curve$ denotes a parallel shift in the benchmark yield curve
effective duration is useful for bond that contains an embedded call option, because callable bond does not have a well-defined internal rate of interest
key rate duration (partial duration): $KeyRateDur^k=-\frac{\Delta PV}{PV\Delta r^k}$, where $r^k$ stands for the $k$th key rate
$\sum KeyRateDur=EffDur$ (understand this like partial derivative)

<h4>PROPERTIES OF BOND DURATION</h4>
<!--  -->
duration change with time (t):
<img src="images/CFA-fixed income-income risk-duraiton change from time.png" width="100%"/>

duration change with time to maturity (T):
<img src="images/CFA-fixed income-income risk-duraiton change from time to maturity.png" width="100%"/>

callable bond:
<img src="images/CFA-fixed income-income risk-callable price.png" width="100%"/>

putable bond:
<img src="images/CFA-fixed income-income risk-putable price.png" width="100%"/>

<h4>DURATION OF A BOND PORTFOLIO</h4>
<!--  -->
two way to calculate duration of bond portfolio:
* definition method, see the portfolio as a single bond
* weighted average of the individual bond durationsthat comprise the portfolio

<h4>MONEY DURATION AND THE PRICE VALUE OF A BASIS POINT</h4>
<!--  -->
money duration (dollar duration): $MoneyDur = AnnModDur × PV^{Full}$
$\Delta PVFull \approx –MoneyDur × \Delta Yield$
price value of a basis point (or PVBP, PV01, DV01): $PVBP=-\frac{PV_{+1bp}-PV_{-1bp}}{2}$

<h4>BOND CONVEXITY</h4>
<!--  -->
$\%\Delta PV^{Full}\approx-AnnModDur\Delta Yield+\frac{1}{2}AnnCon(\Delta Yield)^2$
$ApprxCon=\frac{PV_++PV_--2PV_0}{PV_0(\Delta Yield)^2}$
to annualize convexity, it should be divided by the periodicity squared
$\Delta PV^{Full}\approx-MoneyDur\Delta Yield+\frac{1}{2}MoneyCon(\Delta Yield)^2$
$MoneyCon=AnnCon\times MarketValue$
longer time-to-maturity, a lower coupon rate, and a lower yield-to-maturity lead to greater convexity
effective convexity: $EffCon=\frac{PV_++PV_--2PV_0}{PV_0(\Delta Curve)^2}$

<h4>INVESTMENT HORIZON, MACAULAY DURATION AND INTEREST RATE RISK</h4>
<!--  -->
term structure of yield volatility: the volatility of bond yields-to-maturity and times-to-maturity
*Macaulay duration indicates the investment horizon for which coupon reinvestment risk and market price risk offset each other*
duration gap: difference between the Macaulay duration of a bond and the investment horizon
<img src="images/CFA-fixed income-investment horizon.png" width="100%"/>
When the investment horizon is greater than the Macaulay duration, the risk is to lower interst rate

<h4>CREDIT AND LIQUIDITY RISK</h4>
<!--  -->
benchmark yield change: inflation and real rate
spread change: credit and liquidity (selling and buying of the bond)

<h4>EMPIRICAL DURATION</h4>
<!--  -->
empirical duration: statistical model


<h3>Fundamentals of Credit Analysis</h3>
<h4>CREDIT RISK</h4>
<!--  -->
credit risk: default risk and loss severity
In general, the less debt an issuer has outstanding, the less frequently its debt trades.

<h4>CAPITAL STRUCTURE, SENIORITY RANKING, AND RECOVERY RATES</h4>
<!--  -->
priority of claims: first lien loan, second lien loan, senior unsecured, senior subordinated and then junior subordinated
Priority of claims: Not always absolute, because of the negotiation between creditors

<h4>RATING AGENCIES, CREDIT RATINGS, AND THEIR ROLE IN THE DEBT MARKETS</h4>
<!-- 78 -->
notching: the higher the senior unsecured rating, the smaller the notching adjustment (for recovery rate)

<img src="images/CFA-fixed income-bond rating.png" size="100%"/>

<h4>TRADITIONAL CREDIT ANALYSIS: CORPORATE DEBT SECURITIES</h4>
<!--  -->
equity analysts focus more on income and cash flow statements; whereas credit analysts focus more on the balance sheet and cash flow statements

<h5>The Four Cs of Credit Analysis: A Useful Framework</h5>
<h6>Capacity</h6>
<!--  -->
capacity refers to he ability of the borrower to make its debt payments on time
capacity includes industry analysis and company analysis
* Porter's five force model
* Industry fundamentals
* Company fundamentals
* ratios analysis
<h6>Colleteral</h6>
<h6>Covenant</h6>
<h6>Character</h6>
Character refers to the quality of managemen

<h4>CREDIT RISK VS. RETURN: YIELDS AND SPREADS</h4>
<h5>Spread</h5>
<!--  -->
Credit cycle: As the credit cycle improves, credit spreads will narrow

<h4>HIGH-YIELD, SOVEREIGN, AND NON-SOVEREIGN CREDIT ANALYSIS</h4>
<h5>HIGH-YIELD DEBT</h5>
<!--  -->
sources of liquidity:
1. Cash on the balance sheet
2. Working capital
3. Operating cash flow
4. Bank credit facilities
5. Equity issuance
6. Asset sales

The parent’s reliance on cash flow from its subsidiaries implies a lower recovery rating in default
covenant:
* change of control put: in the event of an acquisition, bondholders have the right to require the issuer to buy back their debt

<h5>SOVEREIGN DEBT</h5>
<!--  -->
two key issues: ability to pay and willingness to pay
<h5>Non-Sovereign Government Debt</h5>
<!--  -->
General obligation (GO) bonds: unsecured bond, supported by the taxing authority
revenue bonds: related to a specific project












