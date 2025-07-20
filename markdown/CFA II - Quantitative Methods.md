<ndtag category="CFA II" createdate="2025-07-20" editdate="2025-07-20" tag="Regression"></ndtag>

### <!-- C1 p13 --> Introduction to the Instruments
##### Simple Linear Regression

t-statistic (for simple linear regression): $t=\frac{\widehat{b}_1}{s_{\widehat{b}_1}}$, where $\text{df} = n-k-1$ and $s_{\widehat{b_1}}=\frac{s_e}{\sqrt{\sum(x_i-\overline{x})^2}}$


#### Basics of Multiple Regression and Underlying Assumptions
Assumptions:  (1) linearity, (2) homoskedasticity, (3) independence of errors, (4) normality, and (5) independence of independent variables
##### Hypothesis Testing for Independent Variables
Hypothesis:
* $H_0$: $b_j=b_{jH}$; $H_a$: $b_j\neq b_{jH}$
* $H_0$: $b_j\geq b_{jH}$; $H_a$: $b_j< b_{jH}$
* $H_0$: $b_j\leq b_{jH}$; $H_a$: $b_j> b_{jH}$

t-statistic: $t=\frac{\widehat{b}_j-b_{jH}}{s_{\widehat{b}_j}}$, where $\text{df} = n-k-1$  and $s_{\widehat{b}_j}=s_e[(X^TX)^{-1}]_{jj}$
confidence interval: $\widehat{b}_j\pm t_cs_{\widehat{b}_j}$

#### Evaluating Regression Model Fit and Interpreting Model Results 
##### Anova Analysis
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
##### Goodness of Fit
coefficient of determination: $R^2=\frac{\text{SSR}}{\text{SST}}$, where $R^2=r^2$ for simple linear regression
adjusted $R^2$: $\overline{R}^2=1-\frac{\text{SSE}/(n-k-1)}{\text{SST}/(n-1)}=1-\frac{n-1}{n-k-1}(1-R^2)$
Akaike’s information criterion(AIC): $\text{AIC}=n\ln\frac{\text{SSE}}{n}+2(k+1)$
* measure of model parsimony

Schwarz’s Bayesian information criterion (BIC or SBC): $\text{BIC}=n\ln\frac{\text{SSE}}{n}+(k+1)\ln n$
* AIC is preferred for prediction while BIC is more likely to be used for seeking best fitness

##### Testing Joint Hypotheses for Coefficients
Unrestricted model: $Y_i=b_0+b_1X_1i+\dots b_kX_ki+\epsilon_i$
Restricted model: $Y_i=b_0+b_1X_1i+\dots b_{k-q}X_{(k-q)i}+\epsilon_i$
$H_0$: $b_1=\dots =b_q=0$
$H_1$: at least one $b_j\neq 0$
F-statistic: $F=\frac{(SSE_R-SSE_U)/q}{SSE_U/(n-k-1)}$

#### Model Misspecification
##### Misspecified Functional Form
* important variabels omitted
* variables need to be transformed
* inappropriate scaling of variables
* pools data incorrectly

might lead to heteroskedasticity, serial correlation or multicollinearity: 

##### Violations of Regression Assumptions: Heteroskedasticity
unconditional heteroskedasticity: error variance not correlated with independent variables, no major problems
conditional heteroskedasticity: error variance correlated with independent variables, creating significant problems for statistical inference

###### Effects
* $\widehat{b}_j$ not affected
* $s_{\widehat{b}_j}$ are most likely underestimated, t-statistics will be inflated
* F-test also unreliable

###### Testing for Conditional Heteroskedasticity
Breusch-Pagen $\chi^2$ test, $H_0$: no heteroskedasticity
Residual regression: $\varepsilon_i=a_0+\dots+a_kX_k+\epsilon_k$
BP statistic: $\chi^2=nR^2_{\text{resid}}$ with df=k, one tailed test

###### Correcting for Heteroskedasticity
* robust standard errors: White-corrected standard errors
* generalized least squares model

































