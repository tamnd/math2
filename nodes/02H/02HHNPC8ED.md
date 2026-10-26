---
tag: 02HHNPC8ED
kind: statement
role: theorem
name: Casorati–Weierstrass theorem
aliases: [sokhotski-theorem, casorati-weierstrass-sokhotski-theorem]
msc: [30D30]
uses: [0YKDJBV26S, 0BSQDZWF34]
sources:
  - url: https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem
    locator: Formal statement of the theorem
  - url: https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem
    locator: Proof of the theorem
same_as:
  wikidata: Q2226962
  wikipedia: Casorati–Weierstrass theorem
---

## Statement

Let $c \in \mathbb{C}$, let $r > 0$, and let $f$ be [[holomorphic|0DG0Z72CQD]] on the punctured disc $0 < |z - c| < r$.
Assume that $c$ is an [[essential singularity|0YKDJBV26S]] of $f$.
Then for each $\delta$ with $0 < \delta < r$, the image $f(\{z : 0 < |z - c| < \delta\})$ is dense in $\mathbb{C}$.
Thus for each $w \in \mathbb{C}$ there is a sequence $z_n \to c$ with $z_n \neq c$ and $f(z_n) \to w$.

## Remarks

Proof idea: if the image of a punctured disc misses a disc $|w - w_0| < \varepsilon$, then $g(z) = 1/(f(z) - w_0)$ is bounded near $c$. By [[Riemann's theorem|0BSQDZWF34]], $g$ is holomorphic at $c$, and then $c$ is removable or a pole of $f$.
[[Picard's great theorem|08QA8QTM71]] is a much stronger statement.
In the Russian literature, the theorem has the name of Sokhotski.

## Explanations

### L1 human

Near an essential singularity, the function comes as close as you like to each complex number.
For example, $e^{1/z}$ comes close to $5$, to $-i$ and to $0$ on each small disc around $0$.
