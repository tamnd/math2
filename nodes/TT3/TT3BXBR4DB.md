---
tag: TT3BXBR4DB
kind: concept
name: Partial correlation
msc: [62H20]
specializes: [0DNN9B6Q2F]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_correlation
same_as:
  wikidata: Q2998010
  wikipedia: Partial correlation
---

## Summary

The partial correlation of two random variables given some control variables is a [[correlation|0DNN9B6Q2F]].
It is the correlation that remains after the linear effect of the controls is removed from both variables.
It separates a direct linear association from one that only passes through the controls.
For jointly normal variables it is zero exactly when the two variables are [[conditionally independent|0THJ7416DX]] given the controls.
This makes it the basic tool of Gaussian [[graphical models|Q3FQAD1BXG]].

## Explanations

### L1 human

Ice cream sales and sunburn cases rise and fall together, but both follow the temperature.
To see whether they are linked beyond the temperature, predict each one from the temperature by a straight line and keep only the leftover parts.
The partial correlation is the correlation of these two leftovers.
If $X = Z + U$ and $Y = Z + V$ with $Z, U, V$ uncorrelated, then $X$ and $Y$ are correlated, but their partial correlation given $Z$ is $0$.
