---
tag: 8XTJWCEZ60
kind: definition
name: Rajchman measure
msc: ["43A46", "42A63", "43A25"]
defines: NAG5J826M5
uses: [AHV05ZBCYW, NY6TYHRGMS, 5X8PK7H6W3, FMW57WNPDB]
sources:
  - url: https://en.wikipedia.org/wiki/Rajchman_measure
---

## Definition

Let $G$ be a locally compact abelian group, and let $\widehat{G}$ be its [[Pontryagin dual|FMW57WNPDB]].
Let $\mu$ be a finite regular [[complex measure|NY6TYHRGMS]] on the Borel sets of $G$.
Its [[Fourier–Stieltjes transform|5X8PK7H6W3]] is the function $\hat\mu(\gamma) = \int_G \overline{\gamma(x)} \, d\mu(x)$ for $\gamma \in \widehat{G}$.
The measure $\mu$ is a *Rajchman measure* if $\hat\mu$ vanishes at infinity on $\widehat{G}$.
This means that for every $\varepsilon > 0$ there is a compact set $K \subseteq \widehat{G}$ with $\abs{\hat\mu(\gamma)} < \varepsilon$ for all $\gamma \notin K$.

## Remarks

On the circle $\mathbb{T} = \R / 2\pi\Z$, the dual is $\Z$, and the condition reads $\hat\mu(n) = \int e^{-int} \, d\mu(t) \to 0$ as $\abs{n} \to \infty$.

Example: let $d\mu = f \, dt$ with $f \in L^1(\mathbb{T})$.
Then $\hat\mu(n)$ is the $n$-th Fourier coefficient of $f$ up to a constant factor, and it tends to $0$ by the [[Riemann–Lebesgue lemma|WVKDC011KP]].
So every [[absolutely continuous|P0P21KDV6E]] measure is Rajchman.

Non-example: the point mass $\delta_0$ has $\hat\delta_0(n) = 1$ for every $n$, so it is not Rajchman.
The Cantor measure on the middle-thirds Cantor set, viewed on $\R/\Z$, is not Rajchman either.
It is invariant under $x \mapsto 3x \bmod 1$, so its coefficients at $n = 3^k$ all equal its coefficient at $n = 1$, which is not $0$.

The Rajchman measures form a closed ideal of the measure algebra $M(G)$ that contains $L^1(G)$.
Menshov showed that there are singular measures on the circle that are Rajchman.
