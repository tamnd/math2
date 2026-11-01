---
tag: AVD8S4NW3B
kind: definition
name: Probabilistic method
msc: [05D40, 60C05]
defines: 3B55HNS754
uses: [0NFPJVJJHX, 031TPJVS74, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Probabilistic_method
---

## Definition

Let $\Omega$ be a nonempty finite set of objects and let $P$ be a property that objects in $\Omega$ may have.
A proof by the *probabilistic method* that some element of $\Omega$ has $P$ does the following:

1. It puts a probability measure $\Pr$ on $\Omega$, making it a [[probability space|0NFPJVJJHX]].
2. It shows that the [[event|031TPJVS74]] $\set{\omega \in \Omega : \omega \text{ has } P}$ has positive probability.
3. It concludes that this event is nonempty, so some element of $\Omega$ has $P$.

A common form of step 2 uses a random variable $X$ on $\Omega$: if the [[expected value|0WQNRCNY3M]] satisfies $\mathbb{E}[X] \ge t$, then $X(\omega) \ge t$ for some $\omega$.

## Remarks

Erdős' bound for diagonal Ramsey numbers is an example.
Let $k \ge 3$ and $n = \floor{2^{k/2}}$, and colour each edge of the complete graph $K_n$ red or blue independently with probability $1/2$.
The expected number of monochromatic copies of $K_k$ is $\binom{n}{k} 2^{1 - \binom{k}{2}}$, and this is less than $1$.
So some colouring has no monochromatic $K_k$, and the [[Ramsey number|0K9QVPJYJF]] satisfies $R(k, k) > \floor{2^{k/2}}$.
An argument that only shows that the event has probability at least $0$ is not a proof by this method.
Step 2 fails there, and an event of probability $0$ may be empty.
The method also applies to infinite probability spaces, with the same conclusion that an event of positive probability is nonempty.
