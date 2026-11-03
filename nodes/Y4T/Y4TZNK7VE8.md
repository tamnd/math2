---
tag: Y4TZNK7VE8
kind: definition
name: Thomason–Trobaugh K-theory of schemes
msc: ["19E08", 18F25]
defines: ECFW7KP0SX
uses: [5A35TYZD02, WQ82C0M3QB, C9JEC2WQKV, P4DZM975BV, X7JG1QEB9Q, 2C1M0NWPB0, Y2467453Q5, RRK8P6TXG2]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Definition

Let $X$ be a quasi-compact and quasi-separated [[scheme|5A35TYZD02]].
A [[chain complex|WQ82C0M3QB]] $E$ of $\mathcal{O}_X$-modules is *perfect* if every point of $X$ has an open neighbourhood $U$ with the following property.
The restriction $E|_U$ is [[quasi-isomorphic|C9JEC2WQKV]] to a bounded complex of [[vector bundles|P4DZM975BV]] on $U$.
Let $\operatorname{Perf}(X)$ be the category of perfect complexes on $X$, made small by the usual bound on cardinality.
Make it a [[Waldhausen category|X7JG1QEB9Q]] with:

1. cofibrations the maps that are degreewise split monomorphisms of $\mathcal{O}_X$-modules;
2. weak equivalences the quasi-isomorphisms.

The *Thomason–Trobaugh K-theory* of $X$ is the [[K-theory spectrum|2C1M0NWPB0]] $K(X) = K(\operatorname{Perf}(X))$, and $K_n(X) = \pi_n K(X)$ for $n \ge 0$.

## Remarks

Assume that $X$ has an ample family of line bundles, for example that $X$ is quasi-projective over a commutative Noetherian ring.
Then $K(X)$ is equivalent to Quillen's [[K-theory of vector bundles|Y2467453Q5]] on $X$.
Thomason and Trobaugh also defined a nonconnective version $K^B(X)$, whose negative homotopy groups extend Bass's negative K-groups to schemes.

Example: for $X = \operatorname{Spec} A$ with $A$ a commutative ring, a complex of $A$-modules is perfect exactly when it is quasi-isomorphic to a bounded complex of finitely generated projective $A$-modules.

Non-example: let $A = k[x]/(x^2)$ for a field $k$, and let $M = A/(x) = k$, viewed as a complex in degree $0$.
Its minimal free resolution $\cdots \to A \xrightarrow{x} A \xrightarrow{x} A \to k \to 0$ never stops, so $M$ is not quasi-isomorphic to a bounded complex of finitely generated projective modules, and $M$ is not perfect.
