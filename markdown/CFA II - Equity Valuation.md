<ndtag category="CFA II" tag="Equity" createdate="2025-08-17" editdate="2025-08-28"></ndtag>


### <!-- C1 p237 --> Equity Valuation: Applications and Processes
#### Value and Price
##### Intrinsic Value
##### Sources of Perceived Mispricing
$\mathbb{E}(IV)-P=(IV-P)+[\mathbb {E}(IV)-IV]$
* perceived mispricing = true mispricing + estimation error
* alpha (abnormal return): IV - P

##### Going-Concern Value and Liquidation Value
going-concern value > liquidation value
* Going-Concern value: going-concern assumption
* liquidation value: value of company if liquidation
  * orderly liquidation value: adequate time to realize liquidation value

#### Selecting the Appropriate Valuation Model
* Absolute valuation models: intrinsic value compared to market price
  * discounted cashflow model (DCF) or present value model
    * Dividend discount model (DDM)
    * Free cashflow model (FCF)
    * Risidual income model (RI)
  * asset-based model
    * natural resources
* Relative valuation models: relative comparison to similar assets
  * typically using price multiples

Common Adjustments for Valuation:
* investor has controlling position: control premium
* price could be realized for block of shares: blockage factor


Sum-of-the-Parts Value (breakup value, private market value):
* company with segments having different valuation characteristics
 
Conglomerate Discount: discount to the company operating in multiple unrelated business compared to company with narrower focuses
* inefficiency of internal capital marktes
* endogenous factors: poorly performing companies tend to expand in unrelated business

#### Process of Valuation
Porter's five forces:
* intra-industry rivalry
* threat oif new entrants
* threat of substitutes
* bargaining power of suppliers
* bargaining power of buyers

Porter's 3 competitive strategies:
* cost leadership
* differentiation
* focus

### <!-- C2 p283 --> Discounted Dividend Valuation
#### Framework of Model
##### DCF Model
intrinsic value $V_0=\sum\frac{CF_i}{(1+r)^i}$
cashflow could be:
* dividends
* free cash flow
  * Free Cash Flow to Equity (FCFE)
    * use $r_e$
  * Free Cash Flow to the Firm (FCFF): 实体现金流
    * use WACC
* residual income: earnings in excess of the investors' required return


##### Basic Concepts of DDM
DDM is from the perspective of non-controlling interest investors
suitable for using DDM:
* mature firms, profitable but not fast growth

##### Estimation of Infinite Stream
1. $V_0 = \sum\frac{D_t}{(1+r_e)^t}+\frac{P_t}{(1+r_e)^t}$
2. future dividends have stylized growth patterns
3. a finite number of dividends and a terminal value

example: company have $D_0=1$, payout ratio is 40%, $g_s=9%$ for the first four years, $r_e=10%$, trailing P/E for t = 4 is 15
* EPS for year 4 is $E_4=1.09^4/40\%=3.52$
* terminal value in year 4 is 15*3.52 = 52.93
(?) dynamic P/E ratio

#### Gordon Growth Model
##### Basic Concepts
$V_0=\frac{D_1}{r_e-g}$, $V_0=\sum\frac{D_1(1+g)^{t-1}}{(1+r_e)^t}$
* $g$ is growth rate for dividend
* $r_e\leq \text{ROE}$

GGM should consider GDP growth, industry life cycle stages and Porter's five force model
GGM can accurately value companies repurchasing shares after adjusting dividend growth rate

sustainable growth rate is for earnings and dividends if we assume
* growth from internally generated sources (no new equity issued)
* some key financial ratios remain unchanged
* $g=\text{ROE}\times b$, where $b$ is rentention rate
* $g=\frac{\Delta \text{RE}}{\text{Equity}}=\frac{b\times \text{NI}}{\text{Equity}}$

$\text{ROE} =\frac{\text{Net Income}}{\text{Sales Revenue}}\times\frac{\text{Sales Revenue}}{\text{Asset}}\times\frac{\text{Asset}}{\text{Equity}}$
* ROE = Net Profit Margin × Asset Turnover × Financial Leverage
* equity at the beginning of the period should be used

##### Applications
###### Valuation of Preferred Stock
$V_0=\frac{D}{r}$
* $r$: discount rate or capitalization rate, higher than junior ranking debt yield

###### Justified P/E Ratio
Justified Leading P/E (动态市盈率): $\frac{V_0}{E_1}=\frac{D_1}{E_1 (r-g)}=\frac{1-b}{r-g}$
Justified Trailing P/E (静态市盈率): $\frac{V_0}{E_0}=\frac{D_1}{E_0 (r-g)}=\frac{(1-b)(1+g)}{r-g}$

###### Implied Rate of Return and Growth Rate
$r=\frac{D_1}{P_0}+g$
* if implied growth rate is higher than sustainable growth rate, the stock is overvalued

###### Present Value of Growth Opportunities
(?) ROE > r or ROIC > WACC
Companies without positive NPV projects should distribute all earnings in dividends.
$V_0=\frac{E_1}{r}+\text{PVGO}$, where $E_1$ is dividend of no growth.


#### Multi-Stage DDM
##### Two-Stage Model: Distinct Phases
growth cann fall into three stages:
1. high growth phase
   * rapid EPS growth, negative FCF
   * ROE>r, low dividend payout
2. transition phase
   * sales and EPS growth slow, postive FCF
   * ROE approaches r, dividend increases
3. mature and sustainable growth phase
   * growth at economy-wide rate
   * ROE = r, high competition

$V_0=\sum_{t=1}^n\frac{D_0(1+g_S)^t}{(1+r)^t}+\frac{D_0(1+g_S)^n(1+g_L)}{(1+r)^n(r-g_L)}$
* $g_S$ is for short term and $g_L$ is for long term 

##### Two-Stage Model: H-Model
Growth rate declines linearly from an abnormal high rate to the mature growth rate during stage 1.
$V_0=\frac{D_0(1+g_L)}{r-g_L}+\frac{D_0H(g_S-g_L)}{r-g_L}$
* $g_S$: high growth rate at the beginning of stage 1
* $H$: half life in years of the stage 1

##### Three-Stage Model
Combination of H-model and two stage model

### <!-- C3 p13 --> Free Cash Flow Valuation
#### Basic Concepts of FCFs
Free cash flows are the cashflow after:
* fulfilling all obligations (expenses and taxes)
* without impacting on the future growth growth of the company
* FCFF: available to the company's suppliers of capital
  * if FCFE negative
  * if capital structure is changing
* FCFE: available to the common equity
  * if the company's capital structure is stable

FCFE could be greater or less than dividends
FCFE model takes a control perspective

#### Calculation of FCFs
##### Basic Formula

$\text{FCFF}=\text{EBIT}\times(1-t)+\text{NCC}-\text{WCInv}-\text{FCInv}$
* NCC: Non-Cash Charges, depreciation or amortization
* WCInv: working capital investment excluding cash and short-term debt (notes payable and current portion of long-term debt)
  * working capital = current asset - current liability
  * excluding cash and short-term debt: this portion of cash is for financing activity, not for operating activity 
* FCInv: net fixed capital investment

Other formula: 
* $\text{FCFF}=\text{NI}+\text{NCC}+\text{Int}\times(1-t)-\text{WCInv}-\text{FCInv}$
  * EBIT - Interest - Tax = Net income
* $\text{FCFF}=\text{EBIT}\times(1-t)+\text{NCC}-\text{WCInv}-\text{FCInv}$
  EBIT = EBITDA - NCC
* $\text{FCFF}=\text{EBITDA}\times(1-t)+\text{NCC}\times t-\text{WCInv}-\text{FCInv}$
* $\text{FCFF}=\text{CFO}+\text{Int}\times (1-t)-\text{FCInv}$
  * NI - (CFI and CFF) + NCC - WCInv = CFO
  * assume CFI and CFF have little effect

FCFE: 
* $\text{FCFE}=\text{FCFF}-\text{Int}\times(1-t)+\text{NB}$
  * NB: net borrowings
    * increase in notes payable/current portion of long-term debt/long-term debt

##### More Details about the Parameters
FCInv (fixed capital investment):
* use gross value not book value, because depreciation is considered in NCC

If the company has preferred stock, $NI_\text{total}=NI_\text{common}+D_\text{preferred}$.

#### Usages of FCFs
the company paying dividend does not change FCFF/FCFE, because dividend/repurchase is attribution of free cashflow.
|Statement of Cashflows| Free Cashflows|
|:-:|:-:|
|Net income|Net income|
|+ NCC|+ NCC|
|- WCInv|- WCInv|
|= CFO|= CFO|
||+ Int × (1-t)|
|- FCInv|- FCInv|
||= FCFF|
|+ Net borrowing|+ Net borrowing|
||- Int × (1-t)|
||= FCFE|
|- Dividend|- Dividend|
|+- stock issues or repurchases|+- stock issues or repurchases|
|= Net change in cash|= Net change in cash|

#### Estimation of FCFs
* forecast overall growth rate of FCFs, usually $g_\text{FCFF}\neq g_\text{FCFE}$
* forecast components of FCFs
* sales-based forecasting method
  * assume $\frac{\text{FCInv}-\text{Dep}}{\Delta \text{Sales}}$ and $\frac{\text{WCInv}}{\Delta \text{Sales}}$ will keep constant
  * debt ratio (DR) $\frac{D}{D+E}$ will keep constant
  * $\text{NB}=\text{DR}\times(\text{FCInv}-\text{Dep}+\text{WCInv})$
  * $\text{FCFE}=\text{NI}-(1-\text{DR})\times(\text{FCInv}-\text{Dep}+\text{WCInv})$

#### Applications of FCFs in Valuation Models
* Firm value: FCFFs discounted at WACC
* Equity value: FCFEs discounted at return on equity
* Equity value: firm value - market value of debt

choice of FCFF or FCFE:
* FCFE: stable capital structure
* FCFF: varying capital structure, negative FCFE

If company has significant non-operating assets, such as excess cash/securities/land held for investment, value of the firm should conclude the non-operating assets part.

### <!-- C4 p109 --> Market-Based Valuation: Price and Enterprise Value Multiples
#### Basic Concepts of Multiples
justifed/warranted/intrinsic price multiples: fair value multiples

#### Price Multiples
##### P/E Ratio
rationale: earnings power is a chief driver of investment value
problems related to trailing EPS:
* underlying/persistent/continuing/core earnings: earnings remove gain or loss on asset/loss provisions/accounting estimates change
* Molodovsky Effect: buy if high P/E ratio
  * company in cyclical industry will have low earnings during recessions
  * normalized EPS: remove cyclical component
    1. average EPS
    2. average ROE × Book Value Per Share (BVPS)
    average considers size effect

P/E-to-Growth (PEG): P/E divided by expected growth rate of earnings
* in default, use forward P/E
* assumes linear relationship between P/E and growth rate

##### Earnings Yield and Dividend Yield
P/E ratio could be negatvie and could not be used to rank
earnings yield: $\frac{E_1}{P_0}$ (leading)
high D/P strategy: value investing strategy
* justified leading dividend yield: r-g 
* value investing is against growth investing

##### P/B Ratio
Book Value per Share (BVPS): investment for common shareholders
appropriate for valuing companies with liquid assets
misleading if significant difference in asset size
justified P/B ratio: $\frac{ROE-g}{r-g}$ (ROE = NI / BVPS)

##### P/S Ratio
P/S Ratio: price / sales
* suitable for distressed firms
* sales more stable and robust than EPS

##### P/CF Ratio
difficult to manipulate
operating cashflows under IFRS and GAAP may not be comparable

#### Enterprise Value Multiples
EV/EBITDA 
EV = MV of common stock + MV of preferred stock + MV of debt - cash - short-term investments
* EV is to measure the net price an acquirer would pay

other multiples:
* EV/FCFF
* EV/EBITDAR: rent expense, for airline industry
* EV/S: P/S does not consider sales revenue to pay debt

#### Momentum Valuation Indicators
momentum investment vs. contrary investment (buy loser sell winner)
unexpected earnings: reported EPS - expected EPS
standardized unexptected earnings: (reported EPS - expected EPS) / std of difference
relative strength indicator: stock return / index return

#### Central Tendency
weighted harmonic mean

### <!-- C5 p225 --> Residual Income Valuation
#### ! Concepts of Residual Income
##### Basic Concepts
Residual Income (RI): net income - cost of equity
* also called economic profit
* cost of equity is marginal cost of equity (additional cost equity)
* also refered as abnormal earnings

in the long term, companies earn equal to the cost of capital should sell at book value

##### Calculations of Residual Income
$RI_t = NI_t-BV(E_{t-1})\times r_e$
$RI_t = BV(E_{t-1})\times (ROE-r_e)$
$RI_t = NOPAT_t - \text{total capital charge}$
* Net Operating Profit After Tax (NOPAT): $EBIT_t\times (1-t)$
* $RI_t = EBIT_t\times (1-t)-\text{cost of debt} - \text{cost of equity}$
* $RI_t = EBIT_t\times (1-t)-WACC\times\text{total capital}$
  * weights should use book value

##### Residual Income Forecasts
clean surplus relationship: book value of equity ending = book value of equity beginning + net income - dividend
* satisfied if only RE change affect book value of equity

accounting issues:
* clean surplus relationship: violated if items bypass the income statement and direct adjustments to equity are made
  * unrealized value of some financial instruments (FVOCI)
  * foreign currency translation
  * certain pension adjustments
* balance sheet adjustment
  * significant off-balance-sheet items
  * significant difference between BV and MV
* intangible items:
  * goodwill considered acquisition
  * R&D
* nonrecurring items
* cookie jar reserves (excess loss or expenses)


##### Commercial Implementations
economic value added (EVA): NOPAT - WACC × total capital
* NOPAT and TC are adjusted

market value added (MVA): market value of company - book value of total capital
EVA and MVA are measuring internal corporate performance and determining executive compensation

Tobin's q = market value of debt and equity / replacement cost of total assets


#### ! Valuation Models
##### Single Stage Model
$V_0=B_0+\sum\frac{RI_t}{(1+r_e)^t}$
assume constant growth rate for residual income: $V_0=B_0+\frac{RI_1}{r_e-g}=B_0\frac{ROE-g}{r_e-g}$

##### Multi-Stage Model
V0= B0 + PV (interim high-growth RI) + PV (continuing RI)
* using P/B ratio: $V_0=B_0+\sum_{t=1}^T\frac{NI_t-rB_{t-1}}{(1+r)^t}+\frac{P_T^*-P_T}{(1+r)^T}$
* using persistence factor: RI will decline to 0 over time after year T
  * $PV_{T}(\text{continuing RI})=\frac{RI_{T+1}}{1+r_e-w}$
  * $w$: persistence factor, between 0 and 1
  * $PV_{0}(\text{continuing RI})=\frac{PV_T}{(1+r_e)^T}$
#### Model Comparisons

### <!-- C6 p293 --> Private Company Valuation
#### Public vs. Private Company Valuation
#### Private Company Valuation Uses and Areas of Focus
* transaction related valuations
* compliance related valuations
  * finance reporting
  * tax reporting
* litigation related
  *  shareholder disputes

#### Earnings Normalization and Cash Flow Estimation
##### ! Earnings Normalization
* public companies
  * audited financial statements
* private
  * reviewed (审阅): opinion letter, limited assurance
  * compiled (汇编): no opinion letter

related party transaction:
* arm's length transaction: normal transaction

##### Cashflow Estimation

#### Private Company Discount Rates and Required Rate of Return
##### Factors Affecting Private Company Discount Rates
* size premiums
* less debt availability, relying more on equity and higher WACC
* in an acquisition context, use target company's discount rate, not the acquirer's (otherwise premium)
* projection risk: specific adjustment

##### Required Rate of Return Models
* CAPM
* expanded CAPM: small-cap premium + company specific stock premium
* build-up approach: rf + equity risk + small-cap + industry risk + company-specific

#### Valuation Discounts and Premiums
##### Strategic Buyer/Financial Buyer
* strategic buyer: buy the company and realize a strategy
* financial buyer: unwill to take advantage of strategic operation

##### Discount for Lack of Control
DLOC = 1 - 1 / (1 + control premium)

##### Discount for Lack of Marketability
total discount = 1 - (1 - DLOC) × (1 - DLOM)
estimates:
* common stock price - restricted stock price
* price differences before and after IPO
* at the money put option premium


#### ! Private Company Valuation Approaches
##### Income Approach
* Free cashflow: 
* capitalized cashflow: $\frac{FCFF_t}{WACC-g}$
  * Reinvestment Rate (RIR): $\frac{g}{WACC}$
  * $FCFF_{t+1}=EBIT_{t+1}(1-t)(1-RIR)$
  * $IV=\frac{FCFF_{t+1}}{r_e-g}$ excluding payments to debtholders
* excess earnings: 
  * RI = normalized income - working capital × return on wc - fixed assets × return on fa

##### Market Based Approach
* Guideline Public Company Method (GPCM)
  * ? $\beta_\text{unlevered}=\frac{\beta_\text{levered}}{1+(1-t)\frac{D}{E}}$
  * find unlevered beta of comparable listed companies
  * calculate levered beta use private company's capital structure
  * price volatility is magnified because of debt (lever)
* Guideline Transactions Method (GTM)
* Prior Transaction Method (PTM)

##### Asset Based Approach
not used for going concerns
usually the lowest valuation