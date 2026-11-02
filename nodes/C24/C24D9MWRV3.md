---
tag: C24D9MWRV3
kind: definition
name: Parametrix
msc: [58J40, 35S05, 35A08]
defines: Z97HVFD6JE
uses: [CGBX1N9V8H, P4DZM975BV, F45VQ47GPV, K2NK9A8M5F, FF27N0BWTP]
sources:
  - url: https://en.wikipedia.org/wiki/Parametrix
---

## Definition

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] without boundary with a smooth positive density $\mu$.
Let $E$ and $F$ be smooth [[vector bundles|P4DZM975BV]] over $M$.
For a smooth vector bundle $V$ over $M$, let $\Hom(V, V)$ also denote the bundle over $M \times M$ with fibre $\Hom(V_y, V_x)$ at $(x, y)$.
A linear operator $R \colon \Gamma(V) \to \Gamma(V)$ is *smoothing* if there is a smooth section $K$ of this bundle such that
$$(R u)(x) = \int_M K(x, y) \, u(y) \, d\mu(y) \quad \text{for all } u \in \Gamma(V).$$
Let $P \colon \Gamma(E) \to \Gamma(F)$ be a [[differential operator|CGBX1N9V8H]].
A *parametrix* for $P$ is a continuous linear operator $Q \colon \Gamma(F) \to \Gamma(E)$ such that $QP - \id$ and $PQ - \id$ are smoothing.

## Remarks

An operator $Q$ with only $QP - \id$ smoothing is a left parametrix, and one with only $PQ - \id$ smoothing is a right parametrix.
Two parametrices of the same operator differ by a smoothing operator.
For constant-coefficient operators on $\R^n$, a parametrix corresponds to a distribution $e$ with $P e = \delta + \omega$ for a smooth function $\omega$, an approximate [[fundamental solution|K2NK9A8M5F]].
An elliptic operator of order $m$ has a parametrix that is a [[pseudo-differential operator|FF27N0BWTP]] of order $-m$.

Example: on the circle $S^1 = \R / 2\pi\Z$ with $d\mu = dx$, let $P = -d^2/dx^2$ on functions, and define
$$Q\Bigl(\sum_{n \in \Z} c_n e^{inx}\Bigr) = \sum_{n \ne 0} \frac{c_n}{n^2} \, e^{inx}.$$
Then $PQu = QPu = u - c_0$, where $c_0 = \frac{1}{2\pi} \int_0^{2\pi} u(y) \, dy$.
So $QP - \id$ and $PQ - \id$ are both the operator with the constant smooth kernel $K(x, y) = -\frac{1}{2\pi}$, and $Q$ is a parametrix.

Non-example: the zero operator is not a parametrix for $P = -d^2/dx^2$.
Here $PQ - \id = -\id$, and the identity is not smoothing.
An operator with a continuous kernel extends to a compact operator on $L^2(S^1)$, while the identity of an infinite-dimensional Hilbert space is not compact.

## Explanations

### L1 human

A parametrix inverts an operator up to an error that has a smooth kernel, an error that makes every input smooth.
