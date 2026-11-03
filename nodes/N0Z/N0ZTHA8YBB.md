---
tag: N0ZTHA8YBB
kind: conjecture
name: Gersten conjecture
msc: ["19E08", "19D45", "13D15"]
uses: [W4BRV4PT2F, 63XXTF6B5M, 5GVFZWMWC8]
about: [W4BRV4PT2F, 5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch%27s_formula
history:
  posed_by: S. M. Gersten
  first_stated: "1973"
---

## Statement

Let $R$ be a [[regular local ring|63XXTF6B5M]] with field of fractions $F$, and let $n \ge 0$.
For a prime ideal $\mathfrak{p}$ of $R$ let $k(\mathfrak{p})$ be its residue field, and let $K_m$ denote Quillen's [[algebraic K-groups|5GVFZWMWC8]], with $K_m = 0$ for $m < 0$.
Then the [[Gersten complex|W4BRV4PT2F]]
$$0 \to K_n(R) \to K_n(F) \to \bigoplus_{\operatorname{ht} \mathfrak{p} = 1} K_{n-1}(k(\mathfrak{p})) \to \bigoplus_{\operatorname{ht} \mathfrak{p} = 2} K_{n-2}(k(\mathfrak{p})) \to \cdots$$
is exact.

## Remarks

In particular the conjecture says that $K_n(R) \to K_n(F)$ is injective.
Quillen proved the conjecture when $R$ is a local ring of a smooth variety over a field, or more generally essentially smooth over a field.
Panin extended it to all regular local rings that contain a field.
For regular local rings of mixed characteristic it is open in general.

For $n = 1$ the conjecture says that a unit of $F$ with valuation $0$ at every height one prime lies in $R^\times$.
This holds because a regular local ring is a unique factorization domain.

## Explanations

### L1 human

A regular local ring is the algebra of functions near a smooth point.
The conjecture says that the K-theory of such a ring is built in a clean way.
The pieces are the K-theory of its fraction field and of the residue fields of its prime ideals.
When true, it makes K-theory behave like a cohomology theory with good local properties, and it gives Bloch's formula relating K-theory to algebraic cycles.
