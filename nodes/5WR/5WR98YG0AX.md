---
tag: 5WR98YG0AX
kind: definition
name: Virtual fundamental class
msc: [53D45, 14N35, 57R95]
defines: 5VXYQ4BXRB
uses: [F45VQ47GPV, P4DZM975BV, WWX7H5W1RP, 913WEQERBE, A2PDZ8GA9C, ZEA0PEM3B2, M0Q5CFJ7ZH, BJX6QS0ANT]
sources:
  - url: https://en.wikipedia.org/wiki/Virtual_fundamental_class
---

## Definition

Let $V$ be an [[oriented|913WEQERBE]] [[smooth manifold|F45VQ47GPV]] of dimension $n$, and let $E \to V$ be an oriented real [[vector bundle|P4DZM975BV]] of rank $r$.
Let $s$ be a smooth [[section|WWX7H5W1RP]] of $E$ whose zero set $X = s^{-1}(0)$ is compact.
Let $U$ be an open neighbourhood of $X$ with compact closure in $V$.
Choose a smooth section $s'$ of $E$ with these properties:

1. $s'$ agrees with $s$ outside a compact subset of $U$.
2. $s'$ is [[transverse|A2PDZ8GA9C]] to the zero section.
3. No section $(1 - t) s + t s'$ with $t \in [0, 1]$ has a zero on $\overline{U} \setminus U$.

Then $Z = s'^{-1}(0) \cap U$ is a compact oriented submanifold of dimension $d = n - r$.
The *virtual fundamental class* of $X$ in $U$ is the image of the [[fundamental class|ZEA0PEM3B2]] of $Z$ in [[singular homology|M0Q5CFJ7ZH]]:
$$[X]^{\mathrm{vir}} = [Z] \in H_d(U; \Q).$$
The number $d$ is the *virtual dimension*.

## Remarks

The class does not depend on the choice of $s'$.
Two choices are joined by a generic homotopy whose zero set is an oriented cobordism between the two zero sets inside $U$.
The classes for smaller neighbourhoods map to the classes for larger ones.
If $s$ itself is transverse to the zero section, then $X$ is a compact oriented manifold of dimension $d$ and $[X]^{\mathrm{vir}}$ is its fundamental class.
For a general Kuranishi structure the same construction is done chart by chart with multivalued perturbations, which is why rational coefficients are used.

Example: let $V = S^2$, $E = T S^2$ and $s = 0$, so $X = S^2$ and $d = 0$.
A generic vector field on $S^2$ has isolated zeros whose signed count is $2$, the value of the [[Euler class|BJX6QS0ANT]] of $T S^2$ on the fundamental class of $S^2$.
So $[X]^{\mathrm{vir}} = 2 \, [\mathrm{pt}] \in H_0(S^2; \Q)$, although $X$ has dimension $2$.


Non-example: for $V = \R$, $E = \R \times \R$ and $s = 0$, the zero set $X = \R$ is not compact.
The perturbations $s' = \varepsilon$ and $s' = \varepsilon x$ have $0$ and $1$ zeros, so no well-defined class arises; this is why compactness is required.
