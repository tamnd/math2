---
tag: XKGEV5RP3T
kind: definition
name: Coefficient of determination
msc: [62J05]
defines: B45RMKMVZ5
uses: [YM708KHV2W, 03Y6AQ2S0J]
sources:
  - url: https://en.wikipedia.org/wiki/Coefficient_of_determination
---

## Definition

Let $y_1, \dots, y_n$ be observed values of a response, not all equal, and let $\hat y_1, \dots, \hat y_n$ be the fitted values of a regression model.
Let $\bar y = \frac{1}{n} \sum_{i=1}^n y_i$ be the [[sample mean|03Y6AQ2S0J]].
The *total sum of squares* is $SS_{\mathrm{tot}} = \sum_{i=1}^n (y_i - \bar y)^2$.
The *residual sum of squares* is $SS_{\mathrm{res}} = \sum_{i=1}^n (y_i - \hat y_i)^2$.
The *coefficient of determination* is
$$R^2 = 1 - \frac{SS_{\mathrm{res}}}{SS_{\mathrm{tot}}}.$$

## Remarks

Example: take the points $(x_i, y_i) = (0,0), (1,1), (2,3)$ and fit $y = a + bx$ by [[ordinary least squares|YM708KHV2W]].
The fit is $b = 3/2$, $a = -1/6$, with fitted values $-1/6$, $4/3$, $17/6$.
Then $SS_{\mathrm{res}} = 1/36 + 4/36 + 1/36 = 1/6$ and $SS_{\mathrm{tot}} = 16/9 + 1/9 + 25/9 = 14/3$, so $R^2 = 1 - 1/28 = 27/28$.

When the fit is by ordinary least squares with an intercept, $SS_{\mathrm{tot}} = SS_{\mathrm{reg}} + SS_{\mathrm{res}}$ with $SS_{\mathrm{reg}} = \sum_i (\hat y_i - \bar y)^2$.
So $R^2 = SS_{\mathrm{reg}} / SS_{\mathrm{tot}}$ lies in $[0, 1]$.
In that case $R^2$ is the square of the sample correlation between $y$ and $\hat y$.
For a straight line fit it is the square of the sample correlation between $x$ and $y$.

Non-example: if the fitted values do not come from least squares with an intercept, the formula can give a negative number.
With the same data and the constant prediction $\hat y_i = 3$, one gets $SS_{\mathrm{res}} = 13 > SS_{\mathrm{tot}}$, so $R^2 < 0$.

The *adjusted* $R^2$ for a model with $p$ coefficients, including the intercept, is $1 - (1 - R^2)(n - 1)/(n - p)$.
It penalises extra regressors.
