---
tag: 5DHPVQ9B4X
kind: definition
name: Strongly measurable function
msc: [28B05, 46G10, 28A20]
defines: JDM2M1FRY6
uses: [N4KDT83V3S, 7WMBX7M4P6, 0BDTTM24DP, 056FSKG32J]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner_measurable_function
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]] and let $E$ be a [[Banach space|0BDTTM24DP]] over $\R$ or $\C$.
A function $s \colon X \to E$ is a *simple measurable function* if it takes finitely many values and $s^{-1}(\set{e}) \in \Sigma$ for each $e \in E$.
This extends the notion of a [[simple function|7WMBX7M4P6]] to values in $E$.
A function $f \colon X \to E$ is *strongly measurable* if there is a sequence $(s_n)$ of simple measurable functions $s_n \colon X \to E$ with
$$\lim_{n \to \infty} \norm{s_n(x) - f(x)} = 0 \quad \text{for every } x \in X,$$
that is, $s_n \to f$ [[pointwise|056FSKG32J]] on $X$.

## Remarks

Example: let $X = [0, 1]$ with the Borel σ-algebra and let $f \colon X \to E$ be continuous.
The function $s_n$ that equals $f(k/n)$ on $[k/n, (k+1)/n)$ for $0 \le k < n$ and $f(1)$ at $1$ is simple and measurable, and $s_n(x) \to f(x)$ by continuity, so $f$ is strongly measurable.

Non-example: let $X = [0, 1]$ with the σ-algebra $\set{\varnothing, X}$ and $f(x) = x$ with values in $E = \R$.
A simple measurable function is then constant, so a pointwise limit of such functions is constant, and $f$ is not strongly measurable.

When $E = \R$ or $E = \C$, a function is strongly measurable if and only if it is measurable.
For a measure $\mu$ on $(X, \Sigma)$, a function is called *strongly $\mu$-measurable* or *Bochner measurable* when it agrees $\mu$-almost everywhere with a strongly measurable function.
The image of a strongly measurable function is a separable subset of $E$, because it lies in the closure of the countable set of values of the $s_n$.
