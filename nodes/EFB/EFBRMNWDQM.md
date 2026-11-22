---
tag: EFBRMNWDQM
kind: statement
role: proposition
name: Alternating sum of dimensions in an exact sequence
msc: ["15A03", "18G35"]
topics: [QHKTJ89V6S]
audience: grad
about: [946YAZNYKX]
uses: [CBDM280TDF, 05G2G0P224, 018W3V3TCT]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Euler_characteristic
    locator: Homological algebra
---

## Statement

Along an exact sequence that starts and ends with $0$, the dimensions cancel when you add them with alternating signs.
Let $F$ be a field, and let
$$0 \to V_0 \xrightarrow{f_0} V_1 \xrightarrow{f_1} \cdots \xrightarrow{f_{n-1}} V_n \to 0$$
be an [[exact sequence|CBDM280TDF]] of [[finite-dimensional|018W3V3TCT]] vector spaces over $F$.
Then
$$\sum_{i=0}^{n} (-1)^i \dim V_i = 0,$$
where $\dim$ is the [[dimension|05G2G0P224]].

## Remarks

### Why each hypothesis is needed

Exactness is needed at every place.
The sequence $0 \to \R \to 0$ is not exact at $\R$, since the image of the incoming map is $0$ and the kernel of the outgoing map is $\R$, and its alternating sum is $1$.

The two outer zeros are part of the hypothesis.
The single map $\R \to \R^2$, $t \mapsto (t, 0)$, is a sequence with no inner place, so it is exact with nothing to check, yet $1 - 2 = -1$.
With the zeros added, $0 \to \R \to \R^2 \to 0$ is not exact, because the map is not onto.

Finite dimension is needed for the sum to be a number.
For infinite-dimensional spaces the formula has no meaning, since $\infty - \infty$ is not defined.

### What it gives you

For $n = 2$ the statement is about a short exact sequence $0 \to U \to V \to W \to 0$, and it says $\dim V = \dim U + \dim W$.

For a linear map $T \colon V \to W$ between finite-dimensional spaces, apply it to the exact sequence $0 \to \ker T \to V \xrightarrow{T} W \to \operatorname{coker} T \to 0$, where $\operatorname{coker} T = W / \operatorname{im} T$:
$$\dim \ker T - \dim V + \dim W - \dim \operatorname{coker} T = 0.$$
Since $\dim \operatorname{coker} T = \dim W - \operatorname{rank} T$, this is the [[rank-nullity theorem|0W4FSW1TVB]] $\dim V = \dim \ker T + \operatorname{rank} T$.
The same equation says that the index $\dim \ker T - \dim \operatorname{coker} T$ equals $\dim V - \dim W$, so it does not depend on $T$.
For example, every linear map $\R^5 \to \R^3$ has a kernel of dimension at least $2$, since the index is $2$ and $\dim \operatorname{coker} T \ge 0$.

### The converse

The converse is false.
The sequence $0 \to \R \xrightarrow{0} \R \to 0$ has alternating sum $1 - 1 = 0$, but it is not exact, because the zero map is neither injective nor onto.
Dimensions alone cannot see whether the maps fit together.

## History

The alternating sum of dimensions is a linear version of the Euler characteristic.
Its oldest instance is Euler's formula $V - E + F = 2$ for convex polyhedra, and Poincaré generalized it to alternating sums of Betti numbers in his work on analysis situs in the 1890s.

## Explanations

### L1 human

In an exact sequence, each space is split into two parts: the part that comes in from the left and the part that goes out to the right.
Each part is counted once with a plus sign and once with a minus sign.
So everything cancels.
In $0 \to \R \to \R^3 \to \R^2 \to 0$, the count is $1 - 3 + 2 = 0$.

### L2 human

Let $T \colon \R^3 \to \R^3$ be the projection $T(x, y, z) = (x, y, 0)$ onto the $xy$-plane, and use the four-term sequence of $T$.

1. The kernel of $T$ is the $z$-axis, of dimension $1$.
2. The image of $T$ is the $xy$-plane, so $\operatorname{coker} T = \R^3 / \operatorname{im} T$ has dimension $3 - 2 = 1$.
3. The exact sequence $0 \to \ker T \to \R^3 \xrightarrow{T} \R^3 \to \operatorname{coker} T \to 0$ gives
$$1 - 3 + 3 - 1 = 0.$$

The typical use is to find one unknown dimension from the others in a long exact sequence.
Watch out: the signs must alternate along the whole sequence, and forgetting a term at either end, such as the cokernel, breaks the count.

### L3 human

The statement says that the Euler characteristic of an exact complex is $0$.
For any bounded complex of finite-dimensional spaces, the alternating sum of the dimensions equals the alternating sum of the dimensions of the homology spaces, which is the invariance of the [[Euler characteristic|RNDDWDAFJ5]].
An exact complex has zero homology, so the statement is the special case.
The [[proof|AQA03KNXD6]] is a telescoping sum built on the [[first isomorphism theorem|0MTBGVZ4XJ]], and it works for any quantity that adds up along short exact sequences, such as the length of a module of finite length.
