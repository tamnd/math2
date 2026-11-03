---
tag: RMQ4JB26AT
kind: problem
name: Newsvendor model
msc: [90B05, 90C15]
uses: [0H8H7ZTHW2, 0X60VE98HN, 0WQNRCNY3M]
about: [NQH9JRA8EX]
sources:
  - url: https://en.wikipedia.org/wiki/Newsvendor_model
same_as:
  wikidata: Q3130009
  wikipedia: Newsvendor model
history:
  posed_by: "Francis Ysidro Edgeworth"
  first_stated: "1888"
  notes: "Edgeworth used the model for the cash reserves of a bank; the name refers to a seller of newspapers who must decide how many copies to buy for one day."
---

## Problem

A seller buys $q \ge 0$ units of a perishable good at unit cost $c > 0$ before the demand $D$ is known.
The seller sells them at unit price $p > c$.
The demand $D$ is a nonnegative random variable with [[cumulative distribution function|0H8H7ZTHW2]] $F$ and finite mean, and unsold units are worth nothing.
The profit is $\Pi(q) = p \min(q, D) - c q$.
The problem asks for an order quantity $q$ that maximizes the expected profit $\mathbb{E}[\Pi(q)]$.

## Remarks

The problem is solved.
An order quantity $q^*$ is optimal exactly when $F(q^{*-}) \le (p - c)/p \le F(q^*)$, where $F(q^{*-})$ is the left limit of $F$ at $q^*$; in particular one may take the [[quantile|0X60VE98HN]]
$$q^* = F^{-1}\Big(\frac{p - c}{p}\Big) = \inf\Big\{q : F(q) \ge \frac{p - c}{p}\Big\}.$$
The number $(p - c)/p$ is called the critical fractile.
The reason is marginal: one more unit earns $p - c$ if it sells, which happens with probability $P(D > q)$, and loses $c$ otherwise.
So raising $q$ pays as long as $(p - c) P(D > q) > c P(D \le q)$, that is, $F(q) < (p - c)/p$.
Example: with $D$ uniform on $\set{1, \dots, 10}$, $p = 4$ and $c = 1$, the critical fractile is $3/4$, and $q^* = 8$.
With a salvage value $v < c$ for unsold units and a penalty $s$ for unmet demand, the critical fractile becomes $(p - c + s)/(p - v + s)$.

## Explanations

### L1 human

A newspaper seller must decide each morning how many papers to buy, without knowing how many will sell.
Too few papers lose sales; too many papers are thrown away.
The answer is to buy enough to cover demand with a certain probability, set by how much a sale earns compared with how much a wasted paper costs.
