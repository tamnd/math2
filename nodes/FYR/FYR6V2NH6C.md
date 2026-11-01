---
tag: FYR6V2NH6C
kind: statement
role: theorem
name: Phragmén–Lindelöf principle
msc: [30C80, 30D20]
uses: [0DG0Z72CQD, 048F2P90WR]
about: [0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Phragm%C3%A9n%E2%80%93Lindel%C3%B6f_principle
same_as:
  wikidata: Q4378868
  wikipedia: Phragmén–Lindelöf principle
---

## Statement

Let $\alpha > \frac{1}{2}$ and let $S = \set{z \in \C \setminus \set{0} : \abs{\arg z} < \frac{\pi}{2\alpha}}$ be the open sector of opening $\pi / \alpha$.
Let $f$ be continuous on the closure $\bar S$ and [[holomorphic|0DG0Z72CQD]] on $S$.
Assume that $\abs{f(z)} \le M$ for each $z$ on the boundary of $S$.
Assume also that there are constants $C > 0$ and $\beta < \alpha$ with $\abs{f(z)} \le C \exp(\abs{z}^{\beta})$ for all $z \in S$.
Then $\abs{f(z)} \le M$ for all $z \in S$.

## Remarks

Proof idea: pick $\gamma$ with $\beta < \gamma < \alpha$ and put $g_\varepsilon(z) = f(z) \exp(-\varepsilon z^{\gamma})$ for $\varepsilon > 0$.
On $\bar S$ one has $\operatorname{Re} z^{\gamma} \ge \cos\left(\frac{\gamma \pi}{2\alpha}\right) \abs{z}^{\gamma}$ with a positive cosine, so $g_\varepsilon \to 0$ at infinity.
The [[maximum modulus principle|048F2P90WR]] on bounded pieces of $S$ gives $\abs{g_\varepsilon} \le M$, and $\varepsilon \to 0$ gives the claim.
The growth condition cannot be relaxed to $\beta = \alpha$.
The function $\exp(z^{\alpha})$ has modulus $\exp(r^{\alpha} \cos(\alpha \theta))$ at $z = r e^{i\theta}$, which is $1$ on the boundary rays and unbounded on the positive axis.
There are similar statements for strips, half-planes and other unbounded domains; the [[Hadamard three-lines theorem|WHS58R43N0]] is one of them.

## Explanations

### L1 human

On a bounded region, the maximum principle says that a holomorphic function is bounded inside by its bound on the boundary.
On an unbounded region such as a sector, this can fail, because the function can grow fast toward infinity.
The Phragmén–Lindelöf principle says that the maximum principle still holds if the function does not grow too fast.
The allowed speed depends on the opening of the sector: the narrower the sector, the faster the allowed growth.

### L2 human

The principle is used throughout the theory of entire functions and in analytic number theory.
It gives convexity bounds for $L$-functions in vertical strips, and it underlies results such as [[Lindelöf's theorem|XBM7J5R1VQ]] and Carlson's theorem.
