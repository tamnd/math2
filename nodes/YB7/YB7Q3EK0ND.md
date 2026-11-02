---
tag: YB7Q3EK0ND
kind: statement
role: theorem
name: Sz.-Nagy's dilation theorem
msc: [47A20, 47A45]
uses: [HM2HHE3J51, MM0EJ2GDE4, 0B8KZRT28M]
about: [MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/Sz.-Nagy%27s_dilation_theorem
same_as:
  wikidata: Q7664013
  wikipedia: Sz.-Nagy's dilation theorem
---

## Statement

Let $H$ be a [[Hilbert space|HM2HHE3J51]] and let $T \colon H \to H$ be a contraction, that is, a bounded linear operator with $\norm{T} \le 1$.
Then there is a Hilbert space $K$ that contains $H$ as a closed subspace.
There is also a [[unitary operator|MM0EJ2GDE4]] $U \colon K \to K$ such that
$$T^n = P_H U^n|_H \quad \text{for all integers } n \ge 0,$$
where $P_H$ is the [[orthogonal projection|0B8KZRT28M]] of $K$ onto $H$.
Moreover, $K$ can be chosen as the closed span of $\bigcup_{n \in \Z} U^n H$.
With this choice, the pair $(K, U)$ is unique up to a unitary isomorphism that fixes $H$.

## Remarks

Proof idea: the defect operator $D = (I - T^*T)^{1/2}$ satisfies $\norm{Tx}^2 + \norm{Dx}^2 = \norm{x}^2$.
On $\bigoplus_{n \ge 0} H$, the operator $(x_0, x_1, \ldots) \mapsto (T x_0, D x_0, x_1, x_2, \ldots)$ is an isometry, and it compresses to the powers of $T$ on the first copy of $H$.
Every isometry extends to a unitary operator on a larger space, which gives $U$.

Example: the unilateral shift on $\ell^2(\N)$ is a contraction, and the bilateral shift on $\ell^2(\Z)$ is a unitary dilation of it.

The compression property holds only for powers $n \ge 0$; for negative $n$ one has $T^{*\abs{n}} = P_H U^n|_H$ instead.

## Explanations

### L1 human

A contraction is an operator that never increases lengths.
The theorem says that every contraction is the shadow of a unitary operator, which preserves lengths, acting on a bigger space.
To see $T^n x$, apply $U$ to $x$ $n$ times in the big space and then project back onto $H$.

### L2 human

The dilation turns questions about a contraction into questions about a unitary operator, where the spectral theorem is available.
An immediate consequence is [[von Neumann's inequality|7KS1W5K54S]].
The minimal unitary dilation is the starting point of the Sz.-Nagy–Foias model theory of contractions and of the [[commutant lifting theorem|3TVXB7X266]].
