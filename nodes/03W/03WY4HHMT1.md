---
tag: 03WY4HHMT1
kind: definition
name: Number of derangements
msc: [05A05]
defines: 05WR29H2KH
sources:
  - url: https://en.wikipedia.org/wiki/Derangement
    locator: Counting derangements
---

## Definition

The derangement numbers $D_n$, for natural numbers $n$, are defined by the recursion
$$D_0 = 1, \qquad D_1 = 0, \qquad D_{n+2} = (n + 1)\,(D_n + D_{n+1}).$$

## Remarks

The first values, for $n = 0, 1, \dots, 6$, are $1, 0, 1, 2, 9, 44, 265$.
The value $D_n$ is the number of [[derangements|0TH61JR04G]] of an $n$-element set. The node [[the derangement numbers count derangements|045ENVCCZV]] states this.
Another notation is $!n$, the subfactorial of $n$.

## Explanations

### L1 human

The derangement numbers start $1, 0, 1, 2, 9, 44$.
Each new number comes from the two before it: $D_4 = 3 \cdot (D_2 + D_3) = 3 \cdot 3 = 9$.
