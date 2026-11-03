---
tag: XANFBWNFES
kind: definition
name: Beilinson regulator
msc: ["19F27", "19E15", "14C35"]
defines: SXJWFF0WAJ
uses: [5GVFZWMWC8, KQP64TH307, EXKGG9X6J0]
sources:
  - url: https://en.wikipedia.org/wiki/Beilinson_regulator
---

## Definition

Let $X$ be a [[smooth|EXKGG9X6J0]] quasi-projective variety over $\C$, let $K_n(X)$ be Quillen's [[algebraic K-group|5GVFZWMWC8]], and let $\psi^k$ be the [[Adams operations|KQP64TH307]] on $K_n(X) \otimes \Q$.
For integers $n \ge 0$ and $i$, let
$$K_n(X)^{(i)}_\Q = \{ x \in K_n(X) \otimes \Q : \psi^k(x) = k^i x \text{ for all } k \ge 1 \}$$
be the weight $i$ eigenspace.
Let $H^{j}_{\mathcal{D}}(X, \R(i))$ be the real Deligne–Beilinson cohomology of $X$, defined with differential forms of logarithmic growth along a smooth compactification.
The *Beilinson regulator* is the family of homomorphisms
$$r_{\mathcal{D}} \colon K_n(X)^{(i)}_\Q \to H^{2i-n}_{\mathcal{D}}(X, \R(i))$$
induced by Beilinson's Chern character from algebraic K-theory to Deligne–Beilinson cohomology.
For a variety over $\R$ or over $\Q$, one first passes to $\C$.
Then one takes invariants under complex conjugation, acting on both $X(\C)$ and the coefficients.

## Remarks

The groups $K_n(X)^{(i)}_\Q$ are the rational motivic cohomology groups $H^{2i-n}_{\mathcal{M}}(X, \Q(i))$, so the regulator is a map from motivic to Deligne–Beilinson cohomology.

Example: for $n = i = 1$, $K_1(X)^{(1)}_\Q = \mathcal{O}(X)^\times \otimes \Q$.
The regulator sends a unit $f$ to the class of $\log \abs{f}$ in $H^1_{\mathcal{D}}(X, \R(1))$.
For $X$ a finite set of points, this is the vector of values of $\log \abs{f}$.
For $X = \operatorname{Spec} F$ with $F$ a number field and $n = 2m - 1$, $i = m \ge 2$, Beilinson showed that the regulator agrees with the [[Borel regulator|D22EZ3CNAF]] up to a nonzero rational factor.

The weight decomposition matters: for a field $k$, the Adams operation $\psi^j$ acts on $K_1(k) = k^\times$ by $u \mapsto u^j$.
So $K_1(k) \otimes \Q$ is entirely of weight $1$, and $K_1(k)^{(i)}_\Q = 0$ for $i \ne 1$.
