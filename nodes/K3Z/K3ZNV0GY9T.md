---
tag: K3ZNV0GY9T
kind: definition
name: Berkovich space dynamics
msc: [37P50, 37P40, 14G22]
defines: 6RM4RWWSSX
uses: [1H5F1BP6XS, FKF9YGBKHF, 0XDK9CGYKJ, AYVTR2ES5B, YAH6MZVG7K]
sources:
  - url: https://en.wikipedia.org/wiki/Berkovich_space
---

## Definition

Let $K$ be an algebraically closed field that is complete for a nontrivial [[non-Archimedean absolute value|1H5F1BP6XS]] $\abs{\cdot}$, such as [[$\C_p$|FKF9YGBKHF]].
The *Berkovich affine line* $\mathbb{A}^1_{\mathrm{Berk}}$ is the set of maps $x \colon K[T] \to [0, \infty)$, written $f \mapsto [f]_x$, such that:

1. $[f g]_x = [f]_x [g]_x$ for all $f, g \in K[T]$;
2. $[f + g]_x \le \max([f]_x, [g]_x)$ for all $f, g \in K[T]$;
3. $[c]_x = \abs{c}$ for every constant $c \in K$.

It carries the weakest topology for which $x \mapsto [f]_x$ is continuous for every $f \in K[T]$.
The *Berkovich projective line* is $\mathbb{P}^1_{\mathrm{Berk}} = \mathbb{A}^1_{\mathrm{Berk}} \cup \set{\infty}$, the one-point compactification.
Each point $a \in K$ gives the point $[f]_a = \abs{f(a)}$, so $\mathbb{P}^1(K)$ is a dense subset of $\mathbb{P}^1_{\mathrm{Berk}}$.
Every [[rational map|0XDK9CGYKJ]] $\varphi \in K(z)$ of degree $d \ge 1$ extends uniquely to a continuous map $\varphi \colon \mathbb{P}^1_{\mathrm{Berk}} \to \mathbb{P}^1_{\mathrm{Berk}}$; for a polynomial $\varphi$ it is given by $[f]_{\varphi(x)} = [f \circ \varphi]_x$.
*Berkovich space dynamics* is the study of the [[iterates|AYVTR2ES5B]] $\varphi^n$ of this extended map on $\mathbb{P}^1_{\mathrm{Berk}}$, and more generally of endomorphisms of Berkovich analytic spaces.

## Remarks

Example: the *Gauss point* $\zeta$ is given by $[\sum_i c_i T^i]_\zeta = \max_i \abs{c_i}$.
It is multiplicative by Gauss's lemma, satisfies the strong triangle inequality, and restricts to $\abs{\cdot}$ on constants, so it lies in $\mathbb{A}^1_{\mathrm{Berk}}$.
It is the supremum norm on the closed unit disc, and it is not of the form $[f]_a$ for any $a \in K$.
For $\varphi(z) = z^2$, the series $f(T^2)$ has the same coefficients as $f(T)$, so $[f]_{\varphi(\zeta)} = [f]_\zeta$ and $\zeta$ is a fixed point.

Non-example: $[f] = \max(\abs{f(0)}, \abs{f(1)})$ satisfies clauses 2 and 3 but not clause 1.
Indeed $[T] = 1$ and $[T - 1] = 1$, but $[T(T - 1)] = 0$.

Berkovich showed that $\mathbb{P}^1_{\mathrm{Berk}}$ is compact, Hausdorff and path-connected.
The Berkovich line is the analytification of $\mathbb{P}^1$; a related but different notion of analytic space is the [[rigid analytic space|YAH6MZVG7K]].
