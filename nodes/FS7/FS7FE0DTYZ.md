---
tag: FS7FE0DTYZ
kind: definition
name: Primary obstruction
msc: [55S35]
defines: FCM1T5EXFV
uses: [ZZWHGGFB4P, D0DAFG8QK6, 1A943BWBQT, P976WYEFMB, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Obstruction_theory
---

## Definition

Let $(X, A)$ be a [[relative CW complex|D0DAFG8QK6]], and let $X_k$ be the union of $A$ with the cells of $X$ of dimension at most $k$.
Let $n \ge 1$ and let $Y$ be an [[$(n-1)$-connected|1A943BWBQT]] space; if $n = 1$, assume also that $\pi_1(Y)$ is abelian.
Let $f \colon A \to Y$ be a map.
Since $\pi_k(Y) = 0$ for $k < n$, the map $f$ extends to a map $g \colon X_n \to Y$.
The *primary obstruction* of $f$ is the class
$$\gamma(f) = [c(g)] \in H^{n+1}(X, A; \pi_n(Y)),$$
where $c(g)$ is the obstruction cocycle of $g$ from [[obstruction theory|ZZWHGGFB4P]].

## Remarks

The class $\gamma(f)$ does not depend on the choice of $g$.
Indeed, any two extensions of $f$ to $X_n$ are homotopic relative to $A$ on $X_{n-1}$, since $Y$ is $(n-1)$-connected.
The difference of the two extensions on the $n$-cells changes $c(g)$ by a coboundary.
The map $f$ extends to $X_{n+1}$ if and only if $\gamma(f) = 0$.
If $X \setminus A$ has no cells of dimension above $n + 1$, then $f$ extends to $X$ if and only if $\gamma(f) = 0$.

Example: let $(X, A) = (D^{n+1}, S^n)$, $Y = S^n$ with $n \ge 1$, and $f$ the identity.
Here $H^{n+1}(D^{n+1}, S^n; \pi_n(S^n)) \cong \Z$ and $\gamma(f)$ is a generator, so $f$ does not extend.

Non-example: let $Y$ be not $(n-1)$-connected, for instance $Y = S^1$ with $n = 2$.
Then $f$ need not extend over $X_2$ at all, so no class in degree $n + 1$ is defined from $f$ alone.

The same construction applies to a fibration over a CW complex with $(n-1)$-connected fibre $F$.
It gives the primary obstruction to a section, a class in $H^{n+1}$ of the base with coefficients in $\pi_n(F)$, local in general.
