<ndtag category="CFA II" createdate="2025-07-20" editdate="2025-08-03" tag="Time-Series"></ndtag>


##### Simple Linear Regression
t-statistic (for simple linear regression): $t=\frac{\widehat{b}_1}{s_{\widehat{b}_1}}$, where $\text{df} = n-k-1$ and $s_{\widehat{b_1}}=\frac{s_e}{\sqrt{\sum(x_i-\overline{x})^2}}$

### <!-- C1 p13 --> Basics of Multiple Regression and Underlying Assumptions
Assumptions:  (1) linearity, (2) homoskedasticity, (3) independence of errors, (4) normality, and (5) independence of independent variables
#### Hypothesis Testing for Independent Variables
Hypothesis:
* $H_0$: $b_j=b_{jH}$; $H_a$: $b_j\neq b_{jH}$
* $H_0$: $b_j\geq b_{jH}$; $H_a$: $b_j< b_{jH}$
* $H_0$: $b_j\leq b_{jH}$; $H_a$: $b_j> b_{jH}$

t-statistic: $t=\frac{\widehat{b}_j-b_{jH}}{s_{\widehat{b}_j}}$, where $\text{df} = n-k-1$  and $s_{\widehat{b}_j}=s_e[(X^TX)^{-1}]_{jj}$
confidence interval: $\widehat{b}_j\pm t_cs_{\widehat{b}_j}$

###  <!-- C2 p35 --> Evaluating Regression Model Fit and Interpreting Model Results 
#### Anova Analysis
||df|SS|MS|
|:-:|:-:|:-:|:-:|
|Regression|k|SSR|MSR=SSR/k|
|Error|n-k-1|SSE|MSE=SSE/(n-k-1)|
|Total|n-1|SST|-|

$\text{SST}=\text{SSR}+\text{SSE}$
$\text{SST}=\sum(Y_i-\overline{Y})^2$
$\text{SSE}=\sum(Y_i-\widehat{Y}_i)^2$
$\text{SSR}=\sum(\widehat{Y}_i-\overline{Y})^2$
standard error of esitmates ($s_e$): $\text{SEE}=\sqrt{\frac{\text{SSE}}{n-k-1}}=\sqrt{\text{MSE}}$

F-statistic: $F=\frac{\text{MSR}}{\text{MSE}}=\frac{\text{SSR}/k}{\text{SSE}/(n-k-1)}$, reject $H_0$ if $F>F_c$, always a one tailed test
#### Goodness of Fit
coefficient of determination: $R^2=\frac{\text{SSR}}{\text{SST}}$, where $R^2=r^2$ for simple linear regression
adjusted $R^2$: $\overline{R}^2=1-\frac{\text{SSE}/(n-k-1)}{\text{SST}/(n-1)}=1-\frac{n-1}{n-k-1}(1-R^2)$
Akaike’s information criterion(AIC): $\text{AIC}=n\ln\frac{\text{SSE}}{n}+2(k+1)$
* measure of model parsimony

Schwarz’s Bayesian information criterion (BIC or SBC): $\text{BIC}=n\ln\frac{\text{SSE}}{n}+(k+1)\ln n$
* AIC is preferred for prediction while BIC is more likely to be used for seeking best fitness

#### Testing Joint Hypotheses for Coefficients
Unrestricted model: $Y_i=b_0+b_1X_1i+\dots b_kX_ki+\epsilon_i$
Restricted model: $Y_i=b_0+b_1X_1i+\dots b_{k-q}X_{(k-q)i}+\epsilon_i$
$H_0$: $b_1=\dots =b_q=0$
$H_1$: at least one $b_j\neq 0$
F-statistic: $F=\frac{(SSE_R-SSE_U)/q}{SSE_U/(n-k-1)}$

### <!-- C3 p59 --> Model Misspecification
#### Misspecified Functional Form
* important variabels omitted
* variables need to be transformed
* inappropriate scaling of variables
* pools data incorrectly

might lead to heteroskedasticity, serial correlation or multicollinearity

#### Violations of Regression Assumptions: Heteroskedasticity
unconditional heteroskedasticity: error variance not correlated with independent variables, no major problems
conditional heteroskedasticity: error variance correlated with independent variables, creating significant problems for statistical inference

##### Consequences
* $\widehat{b}_j$ not affected
* $s_{\widehat{b}_j}$ are most likely underestimated, t-statistics will be inflated
* F-test also unreliable

##### Testing for Conditional Heteroskedasticity
Breusch-Pagen $\chi^2$ test, $H_0$: no heteroskedasticity
Residual regression: $\varepsilon_i=a_0+\dots+a_kX_k+\epsilon_k$
BP statistic: $\chi^2=nR^2_{\text{resid}}$ with df=k, one tailed test

##### Correcting for Heteroskedasticity
* (?) robust standard errors: White-corrected standard errors
* (?) generalized least squares model

#### Violations of Regression Assumptions: Serial Correlation
error terms are correlated with one another

##### Consequences
coefficient estimates not affected
if one independent variable is lag of denpendent variable, the cofficient estimates will be affected
positive serial correlation: underestimate standard errors 
negative serial correlation: overestimate standard erros

##### Testing for Serial Correlation
Durbin-Watson (DW) test limited for detecting first-order serial correlation
Breusch-Godfrey (BG) test: 
* $\widehat{\varepsilon}_t=a_0+\dots+a_kX_{tk}+p_1\widehat{\varepsilon}_{t-1}+e_t$
* $H_0$: $p_1=0$
* F-distributed with $n-p-k-1$ and $p$ degrees of freedom, where $p$ is number of lags


##### Correcting for Serial Correlation
* serial correlation consistent standard error (also called robust standard error)
* modify the regression

#### Violations of Regression Assumptions: Multicollinearity
##### Consequences
estimates of regression coefficients extremely imprecise and unreliable
standard errors of coefficient inflated

##### Testing for Multicollinearity
classic method: t-tests indicate no significance while $R^2$ is high and F-test indicates overall significance
Variance inflation factor (VIF):
* $\text{VIF}_j=\frac{1}{1-R_j^2}$, where $R_j^2$ is $R^2$ of regression $X_j$ on other $X_i$
* $\text{VIF}_j>10$, multicollinearity

##### Correcting for Multicollinearity
* excluding independent variables
* using a different proxy 
* increasing the sample size


### <!-- C4 p85 --> Extensions of Multiple Regression
#### Influence Analysis
regression results can be biased by a small number of observations
influential observation: whose inclusion may significantly alter regression results
high-leverage poiont: extrem value of independent variable
* (? calculation) leverage ($h_{ii}=x_i^T(X^TX)^{-1}x_i$) measures distance between the value of $i$ observation and mean of all obervations
* $0\leq h_{ii}\leq 1$, higher value, more influence
* rule of thumb: $3\frac{k+1}{n}$

outlier: extreme value of dependent variables
* studentized residual ($t_{i*}=\frac{e_i^*}{s_{e^*}}$, where $e_i^*=Y_i-\widehat{Y}_{i*}$)

Cook's Distance (Cook's D): $D_i=\frac{e_i^2}{(k+1)MSE}\frac{h_{ii}}{(1-h_{ii})^2}$
* $2\sqrt{\frac{k}{n}}$ is critical value
* decides whether an observation is influential


#### Dummy Variables 
qualitative variables: nominal type and ordinal type
intercept ($b_0$): average value of dependent variable for the omitted category
intercept dummy: $Y=b_0+d_0D+b_1X+\varepsilon$
slope dummy: $Y=b_0+d_1DX+b_1X+\varepsilon$
#### Multiple Linear Regression with Qualitative Dependent Variables
logistic model: $\ln\frac{p}{1-p}=b_0+bX+\varepsilon$, where $\frac{p}{1-p}$ is odds


### <!-- C5 p121 --> Time Series Analysis
#### Linear Trend Models
$Y_t=b_0+b_1t+\varepsilon_t$, constant change amount with time

#### Log-Linear Trend Models
$\ln Y_t=b_0+b_1t+\varepsilon_t$, constant growth rate with time (exponential growth)

#### Trend Models and Testing for Correlated Errors
trend model not apprropriate with serial correlation

#### AR Time-Series Models and Covariance-Stationary Series
AR(p), p-order autoregressive model: $y_t=b_0+b_1y_{t-1}+\dots+b_py_{t-p}+\varepsilon_t$ 
Covariance stationary, a key assumption for AR model variables to be valid:
* $E(X_t)=\mu$
* $Var(X_t)=\sigma^2$
* constant and finite covariance with itself for a fixed number of periods in the past or future in all periods $Cov(y_t,y_{t-s})=\lambda_s$

#### Comparing Forecasting Model Performance
* In-sample forecasts errors
* out-of-sample forecasts errors
* Root mean squared error criterion: smallest RMSE for the out-of-sample data is best

#### Instability of Regression Coefficients
models estimated with shorter time series are usually more stable (financial relationships are inherently dynamic) but less reliable

#### Violations of Assumption
##### Autoregressive Heteroskedasticity (ARCH)
error variance is correlated with independent variables
$\widehat{\varepsilon}_t^2=a_0+a_1\widehat{\varepsilon}_{t-1}^2+u_t$
if $a_1$ is statistically significant, generalized least squares must be used
ARCH model can predict the variance of the residuals

##### Serial Correlation 
autocorrelation: $\rho(\varepsilon_t,\varepsilon_{t-k})$
usually because of seasonality
correcting of seasonality: include a seasonal lag in AR model $y_t=b_0+b_1y_{t-1}+b_2y_{t-4}+\varepsilon_t$ for quarterly data and $b_2y_{t-12}$ for monthly data

##### Mean Reversion 
mean-reverting level for AR(1): $x=\frac{b_0}{1-b_1}$
covariance stationary → finite mean-reverting model
$|b_1|<1$ in AR(1) model → finite mean-reverting model

###### Random Walk
$x_t=x_{t-1}+\epsilon_t$, best predictor is $x_{t-1}$
random walk with a drift $x_t=b_0+x_{t-1}+\varepsilon_t$
random walk will not exhibit covariance stationary (variance grows with $t$)\
a time series must have a finite mean reverting level to be convariance stationary
least squares regression method does not work for AR(1) model on random walk

###### Unit Root
unit root: $b_1=1$
t-test for $b_1=1$ in AR model is invalid to test unit root
Dickey-Fuller test $x_t-x_{t-1}=b_0+g_1x_{t-1}+\varepsilon_t$
* $H_0$: $g_1=0$; $H_1$: $g_1<0$
* t-statistic and use revised critical values

correcting: first differencing $y_t=x_t-x_{t-1}$

#### Regressions with Multiple Time Series
DF test should be used to detect unit root
if both timeseries have a unit root, but they have cointegration, linear regression can be used.
cointegration: linear combination of them is stationary


### <!-- C6 p209 --> Machine Learning
#### Definition
Supervised learning:
* regression problems
* classification problems

Unsupervised learning:
* dimension reduction
* clustering

artificial intelligence (AI)
deep learning and reinforcement learning

#### Evaluating ML Algorithm Performance
Division of Dataset:
* training set
* validation set
* test set (out-of-sample)

total out-of-sample errors based on trading set $S$:$$\mathbb{E}_{S,y}(y-\hat{f}_S(x))^2=(\bar{f}(x)-\mathbb{E}(y|x))^2+\mathbb{E}_S(\bar{f}_S(x)-\bar{f}(x))^2+Var(y|x)$$
* $(\bar{f}(x)-\mathbb{E}(y|x))^2$: bias error (high bias implies underfitting)
* $\mathbb{E}_S(\bar{f}_S(x)-\bar{f}(x))^2$: variance error
* Var(y|x): base error, due to randomness in the data

##### Prevent Overfitting
complexity reduction and cross-validation (k-fold)

#### Supervised Machine Learning Algorithms
##### Penalized Regression
LASSO (Least Absolute Shrinkage and Selection Operator), $\text{penalty}=\lambda\sum |b_k|$
* data should be standardized so the features have 0 mean and 1 variance

##### Support Vector Machine
##### K-Nearest Neighbor
##### Classification and Regression Tree
##### Ensemble Learning
bootstrap aggregating (or bagging): $n$ new training datasets from random sampling with replacement
random forest: CART via bagging method

#### Unsupervised Machine Learning Algorithms
##### Dimension Reduction
Principal component analysis
##### Clustering
K-means clustering
hierarchical clustering (agglomerative and divisive)
* dendrogram: hierachical tree

### <!-- C7 p287 --> Big Data Projects
structured data and unstructured data (text, image, audio)

#### Characteristics
volume, variety and velocity
fourth V: veracity (credibility and reliability of data sources)

#### Data Preparation and Wrangling
data preparation: cleansing
* incompleteness
* invalidity error
* inaccuracy error
* inconsistent
* duplicate

data wrangling: preprocessing
* transformation: extraction, aggregation (multiple variables into one), filtration, selection and conversion
* scaling

text preparation:
* remove html tags
* remove punctuations
* remove numbers
* remove white spaces

text wrangling
* text normalization (lowercasing, stop words, stemming and lemmatization)
* bag of words
* document term matrix

#### Data Exploration
exploratory data analysis (EDA): heat maps and word clouds
feature selection
feature engineering: creating new features

EDA on text:
* text classification
* topic modeling
* sentiment analysis

feature selection on text: selecting a subset of terms or tokens

feature engineering on text:
* numbers coverted into a token
* N-grams
* name entity recognition
* part of speech: tag every token in text with a corresponding part of speech (verb, nounce)


