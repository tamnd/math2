---
tag: KXC9KHWVGE
kind: definition
name: Convolution
msc: ["43A15", "22D15", "44A35"]
defines: 2Z29JN3VES
uses: [AHV05ZBCYW, VY0HXD3GC4, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]] $\mu$.
Let $f, h \colon G \to \C$ be functions in [[$L^1(G)$|SASP14MA1Z]], the space of $\mu$-integrable functions.
The *convolution* of $f$ and $h$ is the function $f * h$ on $G$ given by
$$(f * h)(x) = \int_G f(y) \, h(y^{-1} x) \, d\mu(y)$$
for every $x \in G$ at which the integral converges absolutely.

## Remarks

The integral converges absolutely for almost every $x$, and $f * h$ lies in $L^1(G)$ with $\norm{f * h}_1 \le \norm{f}_1 \norm{h}_1$.
Convolution is associative, and it is commutative when $G$ is abelian.

Example: $G = (\R, +)$ with Lebesgue measure, $f = h = \mathbf{1}_{[0, 1]}$.
Then $(f * h)(x) = \int_\R \mathbf{1}_{[0,1]}(y) \mathbf{1}_{[0,1]}(x - y) \, dy$ is the length of $[0, 1] \cap [x - 1, x]$.
This equals $x$ for $0 \le x \le 1$, $2 - x$ for $1 \le x \le 2$, and $0$ otherwise: a triangle function.

Non-example: for $f = h = 1$ on $\R$, the defining integral $\int_\R 1 \, dy$ diverges at every $x$, so the convolution is not defined; the hypothesis $f, h \in L^1$ fails.

On $(\Z, +)$ with counting measure, $(f * h)(n) = \sum_{m \in \Z} f(m) h(n - m)$, the Cauchy product of coefficient sequences.
The convolution of probability distributions is the special case of measures, which describes sums of independent random variables.
