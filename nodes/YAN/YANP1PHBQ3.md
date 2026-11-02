---
tag: YANP1PHBQ3
kind: statement
role: theorem
name: Minkowski–Hlawka theorem
msc: [11H31, 11H06, 52C17]
uses: [WN9V7WSJKF, 4P5PSWADJD, HF32CBN5MA, 1XWBY4N0VT]
about: [4P5PSWADJD]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski%E2%80%93Hlawka_theorem
same_as:
  wikidata: Q6867867
  wikipedia: Minkowski–Hlawka theorem
---

## Statement

Let $n \ge 2$ and let $\zeta$ be the [[Riemann zeta function|1XWBY4N0VT]].
Then there is a [[lattice|WN9V7WSJKF]] [[sphere packing|HF32CBN5MA]] of equal balls in $\R^n$ whose [[density|4P5PSWADJD]] is at least
$$\frac{\zeta(n)}{2^{n-1}}.$$

## Remarks

Minkowski stated the result, and Edmund Hlawka gave the first proof in 1943.
A standard proof averages over lattices.
Siegel's mean value theorem says that for a random lattice $\Lambda$ of covolume $1$ and an integrable $f$, the mean of $\sum_{v \in \Lambda \setminus \set{0}} f(v)$ is $\int_{\R^n} f$.
Applied to the indicator of a ball of volume $V < 1$, this gives a lattice of covolume $1$ with no nonzero point in the ball.
Balls of half the radius centred at its points then form a packing of density $V/2^n$.
Counting only primitive vectors and using the symmetry $v \mapsto -v$ improves the condition to $V < 2\zeta(n)$, which gives the bound $\zeta(n)/2^{n-1}$.
For $n = 2$ the bound is $\zeta(2)/2 = \pi^2/12 \approx 0.82$, below the true optimum $\pi/\sqrt{12} \approx 0.91$.
The argument is not constructive: it shows that good lattices exist without exhibiting one.

## Explanations

### L1 human

In high dimensions it is hard to pack balls well, and good explicit packings are rare.
The theorem guarantees that some lattice arrangement fills at least about $2^{-n+1}$ of space.
It does so by showing that a randomly chosen lattice does this well on average, so a good one must exist.

### L2 human

The lower bound $\zeta(n) 2^{1-n}$ is roughly $2^{-n}$, and upper bounds such as [[Rogers' bound|QHPXB39SN7]] and the Kabatiansky–Levenshtein bound are also exponentially small, but with a different exponent.
Closing this exponential gap is a central open problem.
Later work improved the lower bound by factors linear in $n$, for example Ball's bound $2(n - 1) \zeta(n) 2^{-n}$, and Venkatesh obtained a further $\log \log n$ factor in infinitely many dimensions.
The same averaging idea underlies existence proofs for good error-correcting codes.
