---
tag: JX775JPB0N
kind: concept
name: Box–Jenkins method
msc: [62M10, 62M20]
sources:
  - url: https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins_method
same_as:
  wikidata: Q895497
  wikipedia: Box–Jenkins method
---

## Summary

The Box–Jenkins method is an iterative procedure for building an [[ARIMA model|KTDVZP4DF2]] of a time series and using it to forecast.
It cycles through model identification, parameter estimation and diagnostic checking until the fitted model describes the data adequately.
George Box and Gwilym Jenkins set it out in their 1970 book *Time Series Analysis: Forecasting and Control*.

## Explanations

### L1 human

The method is a recipe a forecaster follows step by step.
First, look at plots of the data and of its autocorrelations to guess a simple model.
Second, fit that model to the data.
Third, check whether what the model leaves unexplained looks like pure noise; if not, go back and try another model.
For example, a sample partial autocorrelation that cuts off after lag $2$ suggests trying an AR($2$) model.
