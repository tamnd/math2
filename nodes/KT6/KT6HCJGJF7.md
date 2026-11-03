---
tag: KT6HCJGJF7
kind: example
name: Rule 110
msc: [68Q80, 37B15]
instance_of: [5QXNC6NTVN]
uses: [2CM2MC5HQ6, JE3PC89MVM]
sources:
  - url: https://en.wikipedia.org/wiki/Rule_110
same_as:
  wikidata: Q1876486
  wikipedia: Rule 110
---

## Example

*Rule 110* is the one-dimensional [[cellular automaton|2CM2MC5HQ6]] with states $\set{0, 1}$, neighbourhood $\set{-1, 0, 1}$ and the following local rule $f$.

| $x_{i-1} x_i x_{i+1}$ | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
|---|---|---|---|---|---|---|---|---|
| new $x_i$ | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 |

The bottom row, read as a binary numeral, is $01101110_2 = 64 + 32 + 8 + 4 + 2 = 110$, which gives the name under Wolfram's numbering.
The global map is $F(x)_i = f(x_{i-1}, x_i, x_{i+1})$ for all $i \in \Z$.
It is a cellular automaton because the new value at each site depends only on the sites at offsets $-1, 0, 1$.
The same rule $f$ is used at every site.

Check on a small configuration: let $x$ have a single $1$ at site $0$ and $0$ elsewhere.
At site $-1$ the neighbourhood is $001$, so the new value is $1$.
At site $0$ it is $010$, so the new value is $1$.
At site $1$ it is $100$, so the new value is $0$.
All other sites see $000$ and stay $0$.
So $F(x)$ has $1$ at sites $-1$ and $0$, and the pattern grows to the left.

## Remarks

Rule 110 is [[Turing complete|JE3PC89MVM]]: suitable initial configurations make it simulate any Turing machine.
Matthew Cook proved this by showing that it simulates cyclic tag systems, which are themselves universal.
The simulation needs an infinite background pattern that repeats periodically, so it does not start from a configuration with finitely many $1$s.
It is among the simplest known systems that are Turing complete.

## Explanations

### L1 human

Imagine an infinite row of lamps, each on or off.
At each tick every lamp looks at itself and its two neighbours and switches by a fixed table of eight cases.
For Rule 110 the table is simple, yet the patterns that appear are rich: small structures move through a regular background and collide.
With careful starting patterns these collisions can carry out any computation a computer can do.
