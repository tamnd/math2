---
tag: MRKVM2VVNN
kind: example
name: Gauss map
msc: [11K50, 37A44, "37E05"]
instance_of: [556WBDAHNP, AZRPHS478B]
uses: [04VA28F3HB, 2Z2QVWZ262, CNZV00JQRC]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Kuzmin%E2%80%93Wirsing_operator
---

## Example

The *Gauss map* is
$$G \colon [0, 1) \to [0, 1), \qquad G(x) = \frac{1}{x} - \floor{\frac{1}{x}} \text{ for } x \ne 0, \qquad G(0) = 0.$$
If $x = [0; a_1, a_2, a_3, \dots]$ is the [[continued fraction expansion|04VA28F3HB]] of an irrational $x \in (0, 1)$, then $a_1 = \floor{1/x}$ and $G(x) = [0; a_2, a_3, \dots]$.
So $G$ shifts the continued fraction digits, as the doubling map shifts binary digits.

The *Gauss measure* is the probability measure
$$\mu(A) = \frac{1}{\log 2} \int_A \frac{dx}{1 + x}.$$
It is $G$-invariant; check on $A = [0, t)$ with $0 < t \le 1$.
The preimage $G^{-1}[0, t)$ is, up to the point $0$, the disjoint union over $n \ge 1$ of the intervals $\big(\frac{1}{n + t}, \frac{1}{n}\big]$.
The measure of the $n$-th interval is $\frac{1}{\log 2}\big(\log\frac{n+1}{n} - \log\frac{n+t+1}{n+t}\big)$.
The partial sum up to $N$ telescopes to $\frac{1}{\log 2}\big(\log(N+1) - \log(N+1+t) + \log(1 + t)\big)$, which tends to $\frac{\log(1+t)}{\log 2} = \mu([0, t))$.

The map $G$ is [[ergodic|AZRPHS478B]] for $\mu$, and $\mu$ is equivalent to [[Lebesgue measure|2Z2QVWZ262]].
Hence for Lebesgue almost every $x$, the digit $k$ appears among the $a_n$ with frequency $\frac{1}{\log 2}\log\frac{(k+1)^2}{k(k+2)}$, the Gauss–Kuzmin distribution.
The [[transfer operator|CNZV00JQRC]] of $G$ for Lebesgue measure is the Gauss–Kuzmin–Wirsing operator, $(\mathcal{L}\varphi)(x) = \sum_{n \ge 1} \frac{1}{(x+n)^2} \varphi\big(\frac{1}{x+n}\big)$, and the density $\frac{1}{(1+x)\log 2}$ is its fixed point.

## Explanations

### L1 human

The Gauss map takes a number between $0$ and $1$, flips it to $1/x$, and keeps only the fractional part.
Doing this again and again reads off the digits of the continued fraction of the number, one at a time.
Gauss found the measure that this map preserves, a density that is a bit larger near $0$ than near $1$.
Ergodic theory then tells how often each digit appears in the continued fraction of a typical number: the digit $1$ appears about $41.5\%$ of the time.
