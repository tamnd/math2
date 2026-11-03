---
tag: TQSRSNWX51
kind: concept
name: Merton model of credit risk
msc: [91G40, 91G20]
sources:
  - url: https://en.wikipedia.org/wiki/Merton_model
same_as:
  wikidata: Q85784999
  wikipedia: Merton model
---

## Summary

The Merton model of credit risk treats the equity of a firm as a call option on the value of its assets.
The strike of this option is the face value of the debt.
It was proposed by Robert Merton in 1974.
The firm defaults when its asset value at the debt maturity is below the face value of the debt.
It is the first structural model of credit risk: default is explained by the dynamics of the firm's balance sheet.

## Explanations

### L1 human

A firm owns assets and owes a fixed amount of debt, due on one date.
On that date, if the assets are worth more than the debt, the owners pay the debt and keep the rest.
If not, the owners walk away and the lenders take the assets.
So the owners hold a call option on the firm's assets, and the lenders hold a safe bond minus a put option.
For example, with assets worth $120$ and debt of $100$, the owners keep $20$; with assets worth $80$, they get nothing and the lenders lose $20$.
