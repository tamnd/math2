---
tag: B45RMKMVZ5
kind: concept
name: Coefficient of determination
msc: [62J05]
sources:
  - url: https://en.wikipedia.org/wiki/Coefficient_of_determination
same_as:
  wikidata: Q192830
  wikipedia: Coefficient of determination
---

## Summary

The coefficient of determination, written $R^2$, measures how much of the variation of a response is explained by a fitted regression model.
It compares the residual sum of squares with the total sum of squares around the mean.
For [[ordinary least squares|YM708KHV2W]] with an intercept, it lies between $0$ and $1$ and equals the squared correlation between the observed and the fitted values.
It is the most common summary of goodness of fit in [[linear regression|41FVC4P5JB]].

## Explanations

### L1 human

Imagine predicting each data point by the overall average; the squared errors add up to the total variation.
A regression line usually does better, and $R^2$ is the share of that total variation that the line removes.
An $R^2$ of $0.9$ means the fitted model leaves only a tenth of the original variation unexplained.
For the points $(0,0)$, $(1,1)$, $(2,3)$, the least squares line gives $R^2 = 27/28$.
A high $R^2$ does not prove that the model is correct or that one variable causes the other.
