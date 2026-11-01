---
tag: GCQ23XT6VD
kind: statement
role: theorem
name: Ostrowski's theorem
msc: [12J10, 11R04]
uses: [BT5V3TSNY6, WGN82TCEF2, 01826KMG2H, 0FFXKTKKQC, 03HDF50VN4, BT6T702C28]
about: [BT5V3TSNY6]
sources:
  - url: https://en.wikipedia.org/wiki/Ostrowski%27s_theorem
same_as:
  wikidata: Q2919401
  wikipedia: Ostrowski's theorem
---

## Statement

Let $\abs{\cdot}_*$ be a nontrivial absolute value on the field $\Q$ of rational numbers.
Then $\abs{\cdot}_*$ is equivalent either to the usual [[absolute value|0FFXKTKKQC]] $\abs{\cdot}_\infty$ or to the [[p-adic absolute value|WGN82TCEF2]] $\abs{\cdot}_p$ for exactly one [[prime number|01826KMG2H]] $p$.
Here two absolute values are equivalent when one is a positive real power of the other.

## Remarks

Proof idea: suppose first that $\abs{n}_* > 1$ for some positive integer $n$.
Writing integers in base $b$ and letting the number of digits grow, one shows $\abs{n}_* = n^{\alpha}$ for all positive integers $n$, with a fixed $0 < \alpha \le 1$; so $\abs{\cdot}_* = \abs{\cdot}_\infty^{\alpha}$.
Otherwise $\abs{n}_* \le 1$ for all integers $n$, and the integers with $\abs{n}_* < 1$ form a nonzero prime ideal $p\Z$.
Then $\abs{x}_* = \abs{p}_*^{v_p(x)}$, where $v_p$ is the [[p-adic valuation|03HDF50VN4]], and this is a power of $\abs{x}_p$.

The absolute values $\abs{\cdot}_\infty$ and $\abs{\cdot}_p$ for different $p$ are pairwise inequivalent: for instance $\abs{p}_p < 1$ while $\abs{p}_q = 1$ for a prime $q \ne p$ and $\abs{p}_\infty > 1$.
The hypothesis of nontriviality is needed: the trivial absolute value, equal to $1$ on all $x \ne 0$, is equivalent to none of these.

## Explanations

### L1 human

There are only a few reasonable ways to measure the size of a rational number.
One is the usual size; the others are the $p$-adic sizes, one for each prime $p$, which measure divisibility by $p$.
Up to rescaling, there is nothing else.

### L2 human

The theorem explains why number theory works with the real numbers and the [[p-adic numbers|BT6T702C28]] side by side: these are the completions of $\Q$ for all its [[places|BT5V3TSNY6]].
It leads to the product formula $\abs{x}_\infty \prod_p \abs{x}_p = 1$ for $x \in \Q^\times$, and to the [[adele ring|SEH68BA1QQ]].
For a general number field, the same method shows that every place comes from a real or complex embedding or from a nonzero prime ideal.
