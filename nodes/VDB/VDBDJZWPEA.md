---
tag: VDBDJZWPEA
kind: concept
name: Order polynomial
msc: [06A07, 05A15]
sources:
  - url: https://en.wikipedia.org/wiki/Order_polynomial
same_as:
  wikidata: Q55627850
  wikipedia: Order polynomial
---

## Summary

The order polynomial of a finite poset $P$ counts the [[order-preserving maps|0A7KV2WB7A]] from $P$ to a chain with $m$ elements, as a function of $m$.
This count is a polynomial in $m$ of degree $\abs{P}$, and its leading coefficient is the number of [[linear extensions|W8DZ5KGGHN]] of $P$ divided by $\abs{P}!$.
It was introduced by Richard Stanley, who proved a reciprocity theorem linking it to the count of strictly order-preserving maps.

## Explanations

### L1 human

Label the elements of a poset with numbers from $1$ to $m$ so that larger elements never get smaller labels.
The number of ways to do this depends on $m$, and it is always given by a polynomial in $m$.
For a set of $p$ elements with no relations, every labelling is allowed, so the count is $m^p$.
For a chain of $2$ elements, a labelling is a pair $a \le b$, and there are $m(m+1)/2$ of them.
