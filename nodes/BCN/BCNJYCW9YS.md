---
tag: BCNJYCW9YS
kind: definition
name: Additive character
msc: [11T24, 43A40]
defines: 2WMYTJD33F
uses: [0B1261B5ED, 082GHNPJ53, 0JYTG5K9Y4, H1WNVN5V7F, 0ZXZ82FTX2, WPE5Z53QYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Character_(mathematics)
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]], and let $(R, +)$ be its additive [[abelian group|082GHNPJ53]].
An *additive character* of $R$ is a [[group homomorphism|0JYTG5K9Y4]] $\psi \colon (R, +) \to \C^\times$, that is, a map with
$$\psi(x + y) = \psi(x)\, \psi(y) \quad \text{for all } x, y \in R.$$
The additive character $x \mapsto 1$ is the *trivial* additive character.

## Remarks

Then $\psi(0) = 1$ and $\psi(-x) = \psi(x)^{-1}$.
If $R$ is finite, every value $\psi(x)$ is a root of unity, so $\psi$ is a [[character|H1WNVN5V7F]] of the abelian group $(R, +)$ with values in the unit circle.
For topological rings, such as $\R$ or the $p$-adic numbers, one asks $\psi$ to be continuous with values in the unit circle.

Example: for a prime $p$, the map $\psi(x) = e^{2\pi i x / p}$ on $\Z/p\Z$ is well defined, since changing $x$ by a multiple of $p$ does not change the value.
It is an additive character, because $e^{2\pi i (x + y)/p} = e^{2\pi i x/p} e^{2\pi i y/p}$.

Example: for the [[finite field|0ZXZ82FTX2]] $\F_q$ with $q = p^m$, the map $\psi(x) = e^{2\pi i \operatorname{Tr}(x) / p}$, where $\operatorname{Tr} \colon \F_q \to \F_p$ is the [[field trace|WPE5Z53QYJ]], is a nontrivial additive character, the canonical one.
Every additive character of $\F_q$ is $x \mapsto \psi(ax)$ for exactly one $a \in \F_q$.

Non-example: for an odd prime $p$, the map $x \mapsto e^{2\pi i x^2/p}$ on $\Z/p\Z$ is not an additive character.
At $x = y = 1$ it gives $e^{8\pi i/p}$ for $x + y$, but $e^{2\pi i/p} \cdot e^{2\pi i/p} = e^{4\pi i/p}$, and these differ because $2/p$ is not an integer.
