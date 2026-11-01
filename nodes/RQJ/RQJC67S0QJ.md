---
tag: RQJC67S0QJ
kind: statement
role: theorem
name: Law of the iterated logarithm
msc: [60F15]
uses: [00MRN0FARV, 0T3RZQXDYD, 0ST21PGDAP, 04DXAFN2ES, 0477R9PYAE, 04VZE3FZXF]
about: [04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_the_iterated_logarithm
same_as:
  wikidata: Q198740
  wikipedia: Law of the iterated logarithm
---

## Statement

Let $X_1, X_2, \dots$ be [[i.i.d.|00MRN0FARV]] real random variables with $E[X_1] = 0$ and $E[X_1^2] = 1$.
Let $S_n = X_1 + \cdots + X_n$.
Then, [[almost surely|0ST21PGDAP]],
$$\limsup_{n \to \infty} \frac{S_n}{\sqrt{2 n \log \log n}} = 1 \quad \text{and} \quad \liminf_{n \to \infty} \frac{S_n}{\sqrt{2 n \log \log n}} = -1,$$
where $\log$ is the [[natural logarithm|04DXAFN2ES]] and $\limsup$ is the [[limit superior|0T3RZQXDYD]].

## Remarks

This version under a finite second moment is the Hartman–Wintner theorem; Khinchin proved the first case, for coin tossing.
One proof first treats the [[Wiener process|22735FGJV6]] $W$, for which $\limsup_{t \to \infty} W_t / \sqrt{2 t \log \log t} = 1$ almost surely.
The upper bound uses the Gaussian tail and the [[Borel–Cantelli lemma|0T6WS7TT77]] along a geometric sequence of times $t_k = q^k$.
The lower bound uses the [[second Borel–Cantelli lemma|0NWXRAMEE7]] for the independent increments between these times.
The case of general $X_k$ then follows by a strong approximation of the walk by Brownian motion, such as [[Skorokhod's embedding theorem|XHTYZ7ER4Z]].

Example: take a simple symmetric [[random walk|04VZE3FZXF]], with steps $\pm 1$, and fix $\varepsilon > 0$.
Almost surely, the walk exceeds $(1 - \varepsilon)\sqrt{2 n \log \log n}$ for infinitely many $n$.
Almost surely, it exceeds $(1 + \varepsilon)\sqrt{2 n \log \log n}$ for only finitely many $n$.

The theorem sits between two other limit theorems.
The [[strong law of large numbers|0DFWHQ839T]] gives $S_n / n \to 0$ almost surely.
The [[central limit theorem|0EPZC4Z1FC]] gives that $S_n / \sqrt{n}$ converges in distribution, and it implies that $\limsup_n S_n / \sqrt{n} = \infty$ almost surely.

## Explanations

### L1 human

A random walk with fair steps of size about $1$ drifts away from $0$ by about $\sqrt{n}$ after $n$ steps.
Over an infinite time, it reaches slightly further now and then.
The law of the iterated logarithm gives the exact size of its record excursions: $\sqrt{2 n \log \log n}$.

### L2 human

The result describes the almost sure size of the fluctuations of sums, which neither the strong law nor the central limit theorem determines.
The normalisation $\sqrt{2 n \log \log n}$ is the boundary between the scale $\sqrt{n}$ of the central limit theorem and larger scales that the walk exceeds only finitely often.
Strassen's functional form describes the whole set of limit points of the rescaled path.
