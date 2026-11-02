---
tag: DC4JPVPXEJ
kind: definition
name: Obstruction theory
msc: [55S35, 55S36]
defines: ZZWHGGFB4P
uses: [D0DAFG8QK6, 5W95QFHXPR, P976WYEFMB, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Obstruction_theory
---

## Definition

Obstruction theory is built on the obstruction cocycle, defined as follows.
Let $(X, A)$ be a [[relative CW complex|D0DAFG8QK6]], and let $X_k$ be the union of $A$ with the cells of $X$ of dimension at most $k$.
Let $n \ge 1$ and let $Y$ be a path-connected space whose fundamental group acts as the identity on the [[homotopy group|P976WYEFMB]] $\pi_n(Y)$.
Then free homotopy classes of maps $S^n \to Y$ correspond to elements of $\pi_n(Y)$.
Let $g \colon X_n \to Y$ be a map.
Fix an orientation of each $(n+1)$-cell $e$ of $X \setminus A$, with attaching map $\varphi_e \colon S^n \to X_n$.
The *obstruction cocycle* of $g$ is the cellular cochain
$$c(g) \in C^{n+1}(X, A; \pi_n(Y)), \qquad c(g)(e) = [g \circ \varphi_e].$$
Its class $[c(g)]$ lies in $H^{n+1}(X, A; \pi_n(Y))$, which is isomorphic to the cellular cohomology and to [[singular cohomology|6N7BC70CX0]] of the pair.

## Remarks

The basic facts of obstruction theory are these.

1. The cochain $c(g)$ is a cocycle.
2. The map $g$ extends to $X_{n+1}$ if and only if $c(g) = 0$.
3. The class $[c(g)]$ is zero if and only if the restriction of $g$ to $X_{n-1}$ extends to a map $X_{n+1} \to Y$.

Fact 2 holds because a map $S^n \to Y$ extends over $D^{n+1}$ exactly when it is null-homotopic.
Fact 3 is proved with the difference cochain of two maps that agree on $X_{n-1}$.

Example: let $(X, A) = (D^{n+1}, S^n)$, where $X \setminus A$ is a single $(n+1)$-cell, so $X_n = S^n$.
Let $n \ge 1$, $Y = S^n$, and let $g$ be the identity of $S^n$.
Then $c(g)$ sends the top cell to the generator of $\pi_n(S^n) \cong \Z$, so $g$ does not extend; this is the no-retraction theorem.

Non-example: if $\pi_1(Y)$ acts nontrivially on $\pi_n(Y)$, the value $[g \circ \varphi_e]$ is only defined up to this action, so $c(g)$ is not defined with constant coefficients; one then uses local coefficients.
