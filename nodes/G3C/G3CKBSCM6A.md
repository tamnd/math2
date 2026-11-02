---
tag: G3CKBSCM6A
kind: definition
name: Polynomially convex set
msc: ["32E20"]
defines: AD3474PVHR
uses: [0R6EWFKRCF, 07GNX8GCYP]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

Let $K \subseteq \C^n$ be a [[compact set|0R6EWFKRCF]].
Its *polynomially convex hull* is
$$\hat K = \set{z \in \C^n : \abs{p(z)} \le \max_{w \in K} \abs{p(w)} \text{ for every polynomial } p \in \C[z_1, \dots, z_n]},$$
where the polynomials are the [[polynomials in several variables|07GNX8GCYP]] with complex coefficients.
The set $K$ is *polynomially convex* if $\hat K = K$.

## Remarks

Always $K \subseteq \hat K$, and $\hat K$ is compact.
It coincides with the [[holomorphically convex hull|CD6SMMZSW8]] of $K$ in $D = \C^n$, because entire functions are uniform limits of their Taylor polynomials on compact sets.

Example: a compact convex set $K$ is polynomially convex.
If $z \notin K$, there is a complex linear function $\ell$ with $\operatorname{Re} \ell(z) > \max_K \operatorname{Re} \ell$.
Then $f = e^{\ell}$ satisfies $\abs{f(z)} > \max_K \abs{f}$, and the Taylor polynomials of $f$ converge to $f$ uniformly on $K \cup \set{z}$, so some polynomial $p$ has $\abs{p(z)} > \max_K \abs{p}$.

Non-example: the unit circle $K = \set{\abs{z} = 1}$ in $\C$.
By the maximum principle, $\abs{p(0)} \le \max_K \abs{p}$ for every polynomial $p$, so $0 \in \hat K$ but $0 \notin K$.

For $n = 1$, a compact set $K \subseteq \C$ is polynomially convex exactly when $\C \setminus K$ is connected.
