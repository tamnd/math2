---
tag: 4JAEKN22Y5
kind: statement
role: theorem
name: Kahan summation algorithm
msc: [65G50, 65B10]
uses: [RTKRSC3KPH, JA3QXVF2B8, CPN6SD3BTV, CMXHRNWY35]
about: [CPN6SD3BTV]
sources:
  - url: https://en.wikipedia.org/wiki/Kahan_summation_algorithm
same_as:
  wikidata: Q2982293
  wikipedia: Kahan summation algorithm
---

## Statement

Let $x_1, \ldots, x_n$ be numbers in a binary [[floating-point|RTKRSC3KPH]] system with rounding to nearest and unit roundoff $u$ (see [[machine epsilon|JA3QXVF2B8]]).
Assume that no overflow or underflow occurs.
The *Kahan summation algorithm* computes $\hat s$ as follows, in floating-point operations:
start with $s = 0$ and $c = 0$; for $i = 1, \ldots, n$ set $y = x_i - c$, $t = s + y$, $c = (t - s) - y$, $s = t$; finally $\hat s = s$.
Then
$$\hat s = \sum_{i=1}^{n} (1 + \mu_i) x_i \quad\text{with}\quad \abs{\mu_i} \le 2u + O(n u^2),$$
and hence
$$\Bigl| \hat s - \sum_{i=1}^{n} x_i \Bigr| \le \bigl( 2u + O(n u^2) \bigr) \sum_{i=1}^{n} \abs{x_i}.$$

## Remarks

The variable $c$ holds the low-order part lost when $y$ is added to the large running sum $s$.
The difference $t - s$ recovers what was actually added, and subtracting $y$ gives minus the [[round-off error|CPN6SD3BTV]] of the addition.
This correction is fed back into the next term.
The proof tracks the rounding errors of the four operations through the loop; the key point is that, in binary arithmetic, $c$ captures the rounding error of $s + y$ almost exactly.
For comparison, plain recursive summation only gives the bound $\frac{(n-1)u}{1 - (n-1)u} \sum \abs{x_i}$, which grows linearly in $n$.
The result is a [[backward error|CMXHRNWY35]] bound: $\hat s$ is the exact sum of the slightly perturbed terms $(1 + \mu_i) x_i$.
The relative error $\abs{\hat s - s}/\abs{s}$ can still be large when $\sum \abs{x_i} \gg \abs{\sum x_i}$, that is, when the sum is ill-conditioned.
Optimizing compilers that treat floating-point addition as associative can simplify $c$ to $0$ and destroy the method.

## Explanations

### L1 human

Adding many numbers on a computer loses a little accuracy at each addition, and these losses can add up.
Kahan's trick keeps a second variable that remembers the small part lost at each step and adds it back in the next step.
With this, the error no longer grows with the number of terms: it stays about twice the error of a single rounding, as long as $n u$ is small.

### L2 human

The bound should be compared with the bound $\gamma_{n-1} \sum \abs{x_i}$, $\gamma_k = ku/(1 - ku)$, for recursive summation and $\gamma_{\lceil \log_2 n \rceil} \sum \abs{x_i}$ for [[pairwise summation|SVSVMWA9NQ]].
Compensated summation costs four floating-point operations per term instead of one, but removes the dependence on $n$ from the leading term.
It is the simplest example of an error-free transformation: the pair $(t, -c)$ represents $s + y$ exactly or nearly exactly.
The same idea underlies compensated algorithms for dot products and polynomial evaluation.
