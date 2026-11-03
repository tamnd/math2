---
tag: A5QK739JWQ
kind: concept
name: Monte Carlo methods in finance
msc: [91G60, 65C05]
specializes: [HWP11G3HTN]
sources:
  - url: https://en.wikipedia.org/wiki/Monte_Carlo_methods_in_finance
same_as:
  wikidata: Q6904707
  wikipedia: Monte Carlo methods in finance
---

## Summary

Monte Carlo methods in finance compute prices and risk figures by simulating many random scenarios and averaging the results.
The price of a derivative is a discounted expected payoff under a [[risk-neutral measure|858BHBY2BD]].
The [[Monte Carlo method|HWP11G3HTN]] estimates this expectation by a sample mean.
The error shrinks like $1/\sqrt{N}$ for $N$ scenarios, whatever the number of risk factors.
This makes the method the tool of choice for path-dependent options and for models with many sources of risk.

## Explanations

### L1 human

To price an option by Monte Carlo, imagine the future many times over.
In each imagined future, simulate the path of the stock price and compute what the option pays.
Average these payoffs and discount the average back to today.
For example, simulating $10\,000$ futures of a stock and averaging $\max(S_T - K, 0)$ gives an estimate of a call price.
Quadrupling the number of simulations halves the typical error.
