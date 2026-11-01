---
tag: TZHD2WKNSD
kind: statement
role: theorem
name: Measurable Riemann mapping theorem
msc: [30C62]
uses: [4K6B00NYCD, A9J2KK4CEJ, TX32GDQ330]
about: [9J7GFJ1GPF, SB8KG46NHP]
sources:
  - url: https://en.wikipedia.org/wiki/Measurable_Riemann_mapping_theorem
same_as:
  wikidata: Q6804163
  wikipedia: Measurable Riemann mapping theorem
---

## Statement

Let $\mu \colon \C \to \C$ be a measurable function with $\norm{\mu}_\infty < 1$.
Then there is a unique [[quasiconformal|SB8KG46NHP]] homeomorphism $f \colon \C \to \C$ such that:

1. $f$ solves the [[Beltrami equation|9J7GFJ1GPF]] $f_{\bar z} = \mu f_z$ almost everywhere on $\C$.
2. $f(0) = 0$ and $f(1) = 1$.

## Remarks

When $\mu$ has compact support, one looks for $f$ of the form $f(z) = z + \frac{1}{\pi}\int_\C \frac{h(w)}{z - w}\, dA(w)$, where $h = f_{\bar z}$.
The Beltrami equation then becomes $h = \mu + \mu S h$, where $S$ is the [[Beurling–Ahlfors transform|TX32GDQ330]].
The operator $S$ is an isometry of $L^2$, and its norm on $L^p$ is close to $1$ for $p$ close to $2$.
So the equation has a solution given by a Neumann series in $L^p$ for some $p > 2$.
The general case follows by composing solutions.
Uniqueness holds because two normalized solutions differ by a $1$-quasiconformal, hence conformal, self-map of $\C$ fixing $0$ and $1$, which is the identity.
The theorem also gives analytic dependence of $f$ on $\mu$, a fact that is central in Teichmüller theory and holomorphic dynamics.
The condition $\norm{\mu}_\infty < 1$ cannot be weakened to $\abs{\mu} < 1$ almost everywhere: for some such $\mu$ no homeomorphic solution exists.

## Explanations

### L1 human

Imagine that at each point of the plane someone draws a tiny ellipse, with the only rule that the ellipses are never thinner than a fixed ratio.
The theorem says that there is a way to deform the plane so that all these ellipses become circles.
The deformation is unique once two points are pinned down.
So any such field of ellipses is just the round structure of the plane seen through a distorted map.

### L2 human

The theorem is the main existence result for [[quasiconformal mappings|SB8KG46NHP]].
It turns questions about conformal structures into questions about bounded measurable functions, which can be changed freely.
In complex dynamics it is used in quasiconformal surgery: one builds an invariant ellipse field and then straightens it to get a new holomorphic map.
In Teichmüller theory it shows that Beltrami coefficients parametrize deformations of Riemann surfaces, and the holomorphic dependence on $\mu$ gives the complex structure of [[Teichmüller space|ZZGC6BZNJ5]].
For $\mu = 0$ the solution is the identity, so the statement extends the uniqueness of conformal automorphisms of $\C$ fixing two points.
