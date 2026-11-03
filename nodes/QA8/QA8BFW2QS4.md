---
tag: QA8BFW2QS4
kind: statement
role: theorem
name: Paley–Wiener theorem for symmetric spaces
msc: ["43A85", "43A90", "22E30"]
uses: [XJS07AJ50Y, T2EB8R9HEV, A5JB9JQKR0, 0V33BNKZ9S, 0G4F0XB9X2, JGCQX7ESVE, A6MQCW28KZ]
about: [E06PG40SVD]
sources:
  - url: https://en.wikipedia.org/wiki/Paley%E2%80%93Wiener_theorem
---

## Statement

Let $G$ be a connected noncompact [[semisimple Lie group|XJS07AJ50Y]] with finite centre and $K$ a [[maximal compact subgroup|T2EB8R9HEV]].
Let $\mathfrak g = \mathfrak k \oplus \mathfrak p$ be the Cartan decomposition, $\mathfrak a \subseteq \mathfrak p$ a maximal abelian subspace, and $W$ the Weyl group of the restricted roots.
Give $\mathfrak p$ and $\mathfrak a^*$ the norms $\abs{\cdot}$ induced by the Killing form, and for $\lambda \in \mathfrak a^*_\C$ let $\abs{\operatorname{Im} \lambda}$ be the norm of its imaginary part.
By the [[Cartan decomposition|A5JB9JQKR0]] each $g \in G$ is $g = k \exp X$ with $k \in K$ and $X \in \mathfrak p$ unique; put $\sigma(g) = \abs{X}$.
Let $\hat f(\lambda) = \int_G f(g) \varphi_{-\lambda}(g) \, dg$ be the [[spherical transform|JGCQX7ESVE]], with $\varphi_\lambda$ given by [[Harish-Chandra's formula|A6MQCW28KZ]].
Fix $R > 0$.
Let $\mathcal{D}_R$ be the space of [[smooth|0V33BNKZ9S]] bi-$K$-invariant functions $f$ on $G$ with support in $\set{g : \sigma(g) \le R}$.
Let $\mathcal{E}_R$ be the space of $W$-invariant [[entire functions|0G4F0XB9X2]] $F$ on $\mathfrak a^*_\C$ such that, for every integer $N \ge 0$,
$$\sup_{\lambda \in \mathfrak a^*_\C} \, (1 + \abs{\lambda})^N \, e^{-R \abs{\operatorname{Im} \lambda}} \, \abs{F(\lambda)} < \infty.$$
Then $f \mapsto \hat f$ is a bijection from $\mathcal{D}_R$ onto $\mathcal{E}_R$.

## Remarks

The function $\sigma(g)$ is the Riemannian distance from the origin $K$ to $g K$ in $X = G / K$, for the metric given by the Killing form.
So the support condition says that $f$ lives on the closed ball of radius $R$.
That $\hat f$ has this growth follows from Harish-Chandra's formula and integration by parts with the Laplacian.
The converse uses the inversion formula of the [[Plancherel theorem for spherical functions|PHYHP9TW29]] and a contour shift, where the explicit form of the [[c-function|4X2N0BN3M0]] controls the poles of $\abs{c(\lambda)}^{-2} = (c(\lambda) c(-\lambda))^{-1}$.
The theorem is due to Helgason and Gangolli; Helgason later proved a version for the [[Helgason Fourier transform|K533EAPKKY]] of functions that are not radial.

Example: for $G = \R^n \rtimes \mathrm{SO}(n)$ and $K = \mathrm{SO}(n)$, which is not semisimple but has the same structure, the analogous statement is the classical [[Paley–Wiener theorem|THY12GPZ8C]] for radial functions on $\R^n$.

## Explanations

### L1 human

A function with compact support has a Fourier transform that extends to an entire function of controlled exponential growth, and the classical Paley–Wiener theorem says this describes the transforms exactly.
The same is true for radial functions on a symmetric space such as the hyperbolic plane, with the spherical transform in place of the Fourier transform.
The radius of the support is read off from the exponential growth rate in the imaginary directions.

### L2 human

The theorem identifies the image of $C_c^\infty(K \backslash G / K)$ under the spherical transform, and with it the convolution algebra of compactly supported radial functions as an algebra of entire functions.
Helgason used it to prove that invariant differential operators on $X$ are surjective on smooth functions.
In rank one the Weyl group is $\set{\pm 1}$, and $W$-invariance is the evenness familiar from the radial Fourier transform on $\R$.
