<ndtag category="VIX Construction" tag="VIX" createdate="2022-12-11" editdate="2022-12-11"></ndtag>
<h3>1993-2003</h3>
Use eight options to produce the index.
Denote the strike prices below and above the current index level ($S$) as $X_l$ and $X_u$ respectively. The implied volatilities used to create the VIX index are as follows:
<p class="wrapper" style="text-align:center;">
<img src="/images/VIX Construction/options.png" width="450px" align="center"></p>

1. Average the put and call implied volatilities for each strike and maturity to reduce the number of volatilities.
$$\sigma_1^{X_l}=\left(\sigma_{c, 1}^{X_l}+\sigma_{p, 1}^{X_l}\right) / 2\\ \sigma_1^{X_u}=\left(\sigma_{c, 1}^{X_u}+\sigma_{p, 1}^{X_u}\right) / 2\\ \sigma_2^{X_l}=\left(\sigma_{c, 2}^{X_l}+\sigma_{p, 2}^{X_l}\right) / 2\\ \sigma_2^{X_u}=\left(\sigma_{c, 2}^{X_u}+\sigma_{p, 2}^{X_u}\right) / 2$$
2. Average the implied volatilities above and below the index level as follows:
$$\sigma_1=\sigma_1^{X_l}\left(\frac{X_u-S}{X_u-X_l}\right)+\sigma_1^{X_u}\left(\frac{S-X_l}{X_u-X_l}\right)\\ \sigma_2=\sigma_2^{X_l}\left(\frac{X_u-S}{X_u-X_l}\right)+\sigma_2^{X_u}\left(\frac{S-X_l}{X_u-X_l}\right)$$
3. Calculate the VIX is to interpolate between (or extrapolate from) the two maturities to create a 30 calendar day (22 trading day) implied volatility index.
$$V I X_{\text {old }}=\sigma_1\left(\frac{N_{t_2}-22}{N_{t_2}-N_{t_1}}\right)+\sigma_2\left(\frac{22-N_{t_2}}{N_{t_2}-N_{t_1}}\right)$$
where $N_{t_1}$ and $N_{t_2}$ are the number of trading days to maturity of the two contracts.
<h3>2003-2014</h3>

The generalized formula used in the VIX Index calculation is:
$$\sigma^2=\frac{2}{T} \sum_i \frac{\Delta K_i}{K_i^2} e^{R T} Q\left(K_i\right)-\frac{1}{T}\left[\frac{F}{K_0}-1\right]^2$$
where
* $VIX =100\sigma$
* $F$ is option-implied forward price (from put-call parity)
* $K_0$ is first strike equal to or otherwise immediately below the forward index level, $F$
* $K_i$ is strike price of the $i$th OTM option
* $\Delta K_i=\frac{K_{i+1}-K_{i-1}}{2}$
* $Q(K_i)$ is the midpoint of the bid-ask spread for each option with strike $K_i$
<h3>2014-now</h3>
The VIX is a 30-day expectation of volatility given by a weighted portfolio of out-of-the-money European options on the S&amp;P 500:
$$
VIX=\sqrt{\frac{2 e^{r \tau}}{\tau}\left(\int_0^F \frac{P(K)}{K^2} d K+\int_F^{\infty} \frac{C(K)}{K^2} d K\right)}
$$
where ${\tau }$ is the number of average days in a month (30 days), $r$ is the risk-free rate, $F$ is the 30-day forward price on the S&amp;P 500, and $P(K)$ and $C(K)$ are prices for puts and calls with strike $K$ and 30 days to maturity.
<h3>Reference</h3>

https://quant.stackexchange.com/questions/25157/how-was-the-old-vix-calculated
http://chesnes.com/docs/fed_docs/Hao_NewVix.pdf
https://web.archive.org/web/20091231021416/https://www.cboe.com/micro/vix/vixwhite.pdf
https://en.wikipedia.org/wiki/VIX