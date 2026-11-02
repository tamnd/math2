---
tag: ZRHAG4NXHC
kind: statement
role: theorem
name: Bochner's theorem
msc: [43A35, 42A38, "60E10"]
uses: [ZR09S9R3AW, FMW57WNPDB, 3PRZ02APFA, HZNEQQBCW4]
about: [3PRZ02APFA]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%27s_theorem
same_as:
  wikidata: Q4936242
  wikipedia: Bochner's theorem
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] and let $\widehat{G}$ be its [[Pontryagin dual|FMW57WNPDB]].
Let $\varphi \colon G \to \C$ be a continuous function.
Call $\varphi$ [[positive-definite|3PRZ02APFA]] if $\sum_{j,k=1}^{n} c_j \overline{c_k}\, \varphi(x_j - x_k) \ge 0$ for all $n \ge 1$, $x_1, \dots, x_n \in G$ and $c_1, \dots, c_n \in \C$.
Then $\varphi$ is positive-definite if and only if there is a finite positive [[Radon measure|HZNEQQBCW4]] $\mu$ on $\widehat{G}$ with
$$\varphi(x) = \int_{\widehat{G}} \chi(x) \, d\mu(\chi) \quad \text{for all } x \in G.$$
The measure $\mu$ is then unique, and $\mu(\widehat{G}) = \varphi(0)$.

## Remarks

The easy direction: if $\varphi$ has this form, then $\sum_{j,k} c_j \overline{c_k} \varphi(x_j - x_k) = \int_{\widehat{G}} \abs{\sum_j c_j \chi(x_j)}^2 \, d\mu(\chi) \ge 0$.
For the converse, $\varphi$ defines a positive linear functional on $L^1(G)$, hence on the commutative group C*-algebra of $G$.
The spectrum of this algebra is $\widehat{G}$, and the Riesz representation theorem then gives $\mu$.
Example: for $G = \R$, the function $\varphi(x) = e^{-x^2/2}$ is positive-definite, and $\mu$ is the standard normal distribution, since $\int_\R e^{i\xi x} \frac{1}{\sqrt{2\pi}} e^{-\xi^2/2} \, d\xi = e^{-x^2/2}$.
For $G = \R$, the theorem says that the continuous positive-definite functions with $\varphi(0) = 1$ are exactly the [[characteristic functions|0V5B6D6BQH]] of probability distributions.
Continuity is needed: on $\R$ the indicator function of $\set{0}$ is positive-definite but is not the transform of any measure, since such transforms are continuous.

## Explanations

### L1 human

A positive-definite function is one that behaves like a correlation: certain sums built from it are never negative.
Bochner's theorem says that such functions are exactly the averages of waves with nonnegative weights.
In probability, it says which functions are characteristic functions of random variables.

### L2 human

The theorem is a key tool in the proof of the [[Plancherel theorem for abelian groups|V9K9TG0K3J]] and of [[Pontryagin duality|QTVC6F2P9D]].
For $G = \Z$ it is Herglotz's theorem on positive-definite sequences, with measures on the circle.
In the theory of stationary processes it gives the spectral measure of a stationary covariance function.
