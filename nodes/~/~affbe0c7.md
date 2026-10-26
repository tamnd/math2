---
tag: ~affbe0c7
kind: statement
role: theorem
name: Recurrence for derangements
msc: [05A05]
uses: [~7cf8240d, ~08b1956d]
sources:
  - url: https://en.wikipedia.org/wiki/Derangement
    locator: Counting derangements
---

## Statement

Let $n$ be a natural number, and let $D_m$ be the number of [[derangements|~7cf8240d]] of an $m$-element set.
Then
$$D_{n+2} = (n + 1)\,(D_{n+1} + D_n).$$

## Remarks

Together with $D_0 = 1$ and $D_1 = 0$, the recurrence gives all values: $1, 0, 1, 2, 9, 44, 265, \dots$
A proof looks at a derangement $\sigma$ of $\{1, \dots, n + 2\}$ and the value $i = \sigma(n+2)$. There are $n + 1$ choices of $i$. The case $\sigma(i) = n + 2$ gives $D_n$ derangements, and the other case gives $D_{n+1}$.
Another recurrence is $D_{n+1} = (n + 1) D_n + (-1)^{n+1}$.

## Explanations

### L1 human

Look at where the last element goes, say to position $i$.
Either $i$ goes back to the last position, and the other $n$ elements form a derangement. Or it does not, and this acts like a derangement of $n + 1$ elements.
