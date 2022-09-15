<h1>Quantitative Methods</h1>
<h3>Time value of money</h3>
interest rate can be thought of as rate of return, discount rate and opportunity cost
<br>r = Real risk-free interest rate + Inflation premium + Default risk premium + Liquidity premium + Maturity premium
<br>nominal risk-free interest rate = Real risk-free interest rate + Inflation premium (90 day US Treasure Bill)
<br>stated annual interest rate and quoted interest rate, like "a particular CD pays 8 percent compounded monthly"
<br> effective annual rate
<ul><li>annuity: finite set of level cash flows<ul><li>ordinary annuity: first cash flow occurs at t=1</li><li>annuity due: first cash flow occurs at t=0</li></ul></li><li>perpetuity</li></ul>
<h3>Organizing, Visualizing, and Describing Data</h3>
numerical versus categorical data
<br>cross-sectional vs. time-series vs. panel data; 
<br> structured(financial statement, ) vs. unstructured data.

| numerical |categorical |
|  ----  | ----  |
| <ul><li>continuous</li><li>discrete</li></ul>  |<ul><li>nominal<br>(number cannot rank)</li><li>ordinal<br>number cannot be arithmetically operated</li></ul> |
variable, also called field, attribute or feature
contingency table -> confusion matrix
chi-square test of independence
<h4>DATA VISUALIZATION</h4>
frequency polygon (plt.plot)
<br>bar chart for category data while histogram for numerical data
<br>bar chart are ordered by frequency in descending order and the chart includes a line displaying cumulative relative frequency, then it is called a Pareto Chart
<br>group bar chart (or clustered bar chart), stacked bar chart
<br>tree map
<br>word cloud(or tag cloud)
<br>line chart for normal data while, frequency polygon for frequency
<br>bubble line chart
<br>scatter plot matrix
<br>heat map ("colored contigency table")
<h4>MEASURES OF CENTRAL TENDENCY</h4>
<!--  -->
a 5% **trimmed mean** discards the lowest 2.5% and the highest 2.5% of values
95% **winsorized mean** sets the bottom 2.5% of values equal to the value at or below which 2.5% of all the values lie (as will be seen shortly, this is called the “2.5th percentile” value)
unimodal, bimodal and trimodal. When all the values in a dataset are different, the distribution has no mode because no value occurs more frequently than any other value.
modal interval: bin with the highest frequency
harmonic mean is average price under periodic investment of a fixed amount of money, this is called cost averaging
<h4>QUANTILES (or FRACTILES)</h4>
<!--  -->
Given a set of observations, the yth percentile is the value at or below which y% of observations lie.
**quartile, quintile, decile, percentile**
**interquartile range** (IQR) = Q3-Q1
percentile $L_y=(n+1)\frac{y}{100}$, then use linear interpolation to determine $P_y$
Box and whisker plot
<h4>MEASURES OF DISPERSION</h4>
<!---->
range: maximum - minimum
mean absolute deviation
sample variance
$X_G\approx \overline{X}-\frac{s^2}{2}$, where $X_G$ is geometric mean and $s$ is standard deviation
<h4>DOWNSIDE DEVIATION AND COEFFICIENT OF VARIATION</h4>
target semideviation (or target downside deviation)
$s_{Target}=\sqrt{\sum_{X_i\leq B}^n\frac{(X_i-B)^2}{n-1}}$
CV, coefficient variation, $CV=\frac{s}{\overline{X}}$
<h4>THE SHAPE OF THE DISTRIBUTIONS</h4>
<!-- -->
A distribution that is not symmetrical is skewed.A return distribution with positive skew has frequent small losses and a few extreme gains. A return distribution with negative skew has frequent small gains and a few extreme losses.
sample skewness: $Skewness\approx\frac{1}{n}\frac{\sum(X_i-\overline{X})^3}{s^3}$
positively(right) skewed: mean>median, longer right tail
Kurtosis
<ul><li>leptokurtic (or fat-tailed)</li>
<li>platykurtic (or thin-tailed)</li>
<li>mesokurtic </li></ul>
A normal distribution has kurtosis
of 3
sample excelss kurtosis: $K_E\approx\frac{1}{n}\frac{\sum(X_i-\overline{X})^4}{s^4}-3$
<h4>CORRELATION BETWEEN TWO VARIABLES</h4>
<!--  -->
sample correlation: $s_{XY}=\frac{\sum{(X_i-\overline{X})(Y_i-\overline{Y})}}{n-1}$
spurious correlation: chance relationships, mixed with two variable with a third variable, two variables relating to a third variable
<h3>Probabiltiy Concepts</h3>
<!--  -->
odds: $p/(1-p)$
*conditional variance: $Var(X|Y)=E(X^2|Y)-E(X|Y)^2$
<!--  -->
<h3>Common Probability Distributions</h3>
<!--  -->
Central limit theorem
Modern portofolio theory
<h4>safety-first rules</h4>
<!-- 267 -->
To avoid shortfall risk (minimize $P(R_P< R_L)$), is to max safety-first ratio $SFRatio=\frac{E(R_P)-R_L}{\sigma_P}$. So the highest Sharpe ratio is the portfolio with the lowest probabiltiy to lose to risk free rate.
<h4>lognormal</h4>
<!-- by 274 -->
$ln(S_T/S_0)=\sum{ln(S_i+1)/ln(S_i)}$, approximately normal by central limit theorem
<h4>STUDENT’S T-, CHI-SQUARE, AND F-DISTRIBUTIONS</h4>
<!--  -->
$s^2=\frac{\sum{(X_i-\overline{X})^2}}{n-1}$, $t=\frac{\overline{X}-\mu}{s/\sqrt{n}}$ follows t-distribution with mean 0 and degree of freedom $n-1$
<h4>MONTE CARLO SIMULATION</h4>
<!--  -->
<h4>Sampling and Estimation</h4>
<!-- 306~360 -->
<h3>Hypothesis Testing</h3>
<!-- -->
In hypothesis testing, we test to see whether a sample statistic is likely to come from a population with the hypothesized value of the population parameter.
statistical inference: estimation and hypothesis testing
Null hypothesis $H_0$ and alternative hypothesis $H_a$, the null hypothesis is what we want to reject in favor of the alternative hypothesis
<b>test statistics and their distributions(p364)</b>
|Decision| $H_0$ true |$H_0$ false |
|---|  ----  | ----  |
|fail to reject|correct<br> True negative| Type II error<br>False negative |
|reject| Type I error<br> False positive| correct<br>True positive|
level of significance (probability of type I error) $\alpha$ and confidence level $1-\alpha$; power of the test $1-\beta$ and probability of type II error $\beta$
$p$-value is the smallest level of significance at which the null hypothesis can be rejected.
The $p$-value for the true null hypothesis are generally uniformly distributed between 0% and 100%
<h4>MULTIPLE TESTS AND INTERPRETING SIGNIFICANCE</h4>
<!--371-->
False discovery rate(FDR)=$\frac{FP}{TP+FP}$
mulitple testing problem: run a test many times, there tend to be rejecting results
False discovery approach: find the highest $k$ such that $p(k)\leq \alpha\frac{\text{rank of i}}{\text{Number of tests}}$
if the power of the test is low or the sample size is small, we should becautious because there is a good chance of a false positive.
<h4>ND MATTERS</h4>
<!--  -->
t distribution has fatter tails, as $n\rightarrow\infty$, t distribution approaches the standard normal distribution
Test of the mean of the differences (paired comparisons test), (two population are dependent)
In contrast to t-test, chi-square test and F-test is sensitive to violations of its assumptions. If the sample is not random or if it does not come from a normally distributed population, inferences based on a chi-square test are likely to be faulty.
<h4>PARAMETRIC VS. NONPARAMETRIC TESTS</h4>
<!--  -->
Parametric (concerned with parameter and a definite set of assumptions)
nonparametric procedures in four situations:
* when the data we use do not meet distributional assumptions
* when there are outliers
* when the data are given in ranks or use an ordinal scale
* when the hypotheses we are addressing do not concern a parameter (a sample is random or not, a sample comes from a distribution or not)
<h4>TESTS CONCERNING CORRELATION</h4>
<!--  -->
Pearson correlation (bivariate correlation) 
As the sample sizes increase as ever-larger datasets are examined, the null hypothesis is almost always rejected and other tools of data analysis must be applied
Spearman rank correlation coefficient(Spearman's rho Lecture 15): $r_s=1-\frac{6\sum d_i^2}{n(n^2-1)}$
frequency table, contigency table or two-way table
<h3>Introduction to Linear Regression</h3>
<!-- 431 -->
sum of squares total (SST,variation of $Y$): $\sum(Y_i-\overline{Y})^2$
$Y_i=X_ib+\varepsilon_i$, error $\varepsilon$ represents the difference between the observed $Y$ and the expected value
residual $e_i=Y_i-\widehat{Y}_i$
minimize sum of squares error (SSE)
For simple linear regression (SLR, one independent variable), $\widehat{b}_1=\frac{Cov(X,Y)}{Var(X)}$, $\widehat{b}_0=\overline{Y}-\widehat{b}_1\overline{X}$
cross-sectional and time-series regression
SST=SSR+SSE
coefficient of determination: $R^2=\frac{SSR}{SST}=\frac{\sum(\widehat{Y}_i-\overline{Y})^2}{\sum(Y_i-\overline{Y})^2}=r^2$
<!-- 455 -->
