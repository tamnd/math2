---
tag: V192HFRX5A
kind: definition
name: Box–Jenkins method
msc: [62M10, 62M20]
defines: JX775JPB0N
uses: [KTDVZP4DF2, B1HNX0YT0Z, YCZHYY8VE5, 11YRFWD951, 0FREPFKNS7, 0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins_method
---

## Definition

Let $x_1, \dots, x_n$ be an observed time series.
The *Box–Jenkins method* fits an [[ARIMA($p$, $d$, $q$) model|KTDVZP4DF2]] to the series and then uses it to forecast.
It repeats the following three stages until the checks of stage 3 are passed:

1. Identification: choose $d$ so that the differenced series $\nabla^d x_t$ looks stationary. Then choose tentative orders $p$ and $q$ from the sample [[autocorrelation function|YCZHYY8VE5]] and [[partial autocorrelation function|11YRFWD951]] of $\nabla^d x_t$.
2. Estimation: estimate the parameters of the [[ARMA($p$, $q$) model|B1HNX0YT0Z]] for the differenced series by [[maximum likelihood|0FREPFKNS7]] or by nonlinear [[least squares|0BYTQ4X1HC]].
3. Diagnostic checking: test whether the residuals of the fitted model behave like white noise, for instance with a portmanteau test. If they do not, return to stage 1 with a modified model.

## Remarks

The identification stage uses typical patterns.
For an AR($p$) model the partial autocorrelation vanishes beyond lag $p$ while the autocorrelation decays gradually.
For an MA($q$) model the autocorrelation vanishes beyond lag $q$ while the partial autocorrelation decays gradually.

Example: suppose the sample autocorrelation of a series decays very slowly.
Suppose that of its first differences has a single significant value, at lag $1$.
Then stage 1 suggests $d = 1$, $p = 0$ and $q = 1$, that is ARIMA($0$, $1$, $1$).

Non-example: fitting one fixed AR($1$) model by least squares without examining the residuals is not the Box–Jenkins method, because stage 3 and the loop back to stage 1 are missing.

The method prefers parsimonious models, with as few parameters as give an adequate fit.
Seasonal ARIMA models are handled in the same way, with seasonal differences and seasonal orders.
