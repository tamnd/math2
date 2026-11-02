---
tag: QXF1VVQ5M6
kind: definition
name: Holomorphically convex hull
msc: ["32E05"]
defines: CD6SMMZSW8
uses: [507C34W0ZT, 0R6EWFKRCF, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

Let $D \subseteq \C^n$ be an [[open set|02BH3MCBQB]] and let $K \subseteq D$ be a [[compact set|0R6EWFKRCF]].
The *holomorphically convex hull* of $K$ in $D$ is
$$\hat K_D = \set{z \in D : \abs{f(z)} \le \sup_{w \in K} \abs{f(w)} \text{ for every holomorphic function } f \text{ on } D},$$
where holomorphic means [[holomorphic|507C34W0ZT]] in the sense of several variables.

## Remarks

Always $K \subseteq \hat K_D$, and $\hat K_D$ is closed in $D$.
Using $f(z) = z_j$ shows that $\hat K_D$ is bounded, and using $f = e^{\ell}$ for complex linear $\ell$, with $\abs{e^{\ell}} = e^{\operatorname{Re} \ell}$, shows that $\hat K_D$ lies in the convex hull of $K$.

Example: $D = \C$ and $K = \set{\abs{z} = 1}$.
By the maximum principle every entire $f$ satisfies $\abs{f(z)} \le \max_K \abs{f}$ for $\abs{z} \le 1$, and $f(z) = z$ excludes the points with $\abs{z} > 1$; so $\hat K_D$ is the closed unit disc.

With the same $K$ and $D = \C \setminus \set{0}$, the function $f(z) = 1/z$ is holomorphic on $D$ and has $\abs{f(z)} > 1 = \max_K \abs{f}$ for $0 < \abs{z} < 1$; so here $\hat K_D = K$.

When $D = \C^n$, the hull coincides with the polynomially convex hull, since entire functions are uniform limits of polynomials on compact sets.
