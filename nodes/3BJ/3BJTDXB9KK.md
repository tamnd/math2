---
tag: 3BJTDXB9KK
kind: definition
name: Orthogonal polynomials on the unit circle
msc: [42C05, 33C47]
defines: 3F9G3DRQ62
uses: [0VGMEBVW1M, FQTXV6BQZG, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials_on_the_unit_circle
---

## Definition

Let $\partial\mathbb{D} = \set{z \in \C : \abs{z} = 1}$ and let $\mu$ be a Borel [[probability measure|0VGMEBVW1M]] on $\partial\mathbb{D}$ whose [[support|FQTXV6BQZG]] is an infinite set.
Give the polynomials the inner product $\ip{p}{q} = \int_{\partial\mathbb{D}} p(z) \overline{q(z)} \, d\mu(z)$ of the [[Lebesgue space|SASP14MA1Z]] $L^2(\partial\mathbb{D}, \mu)$.
For $n \ge 0$, the *monic orthogonal polynomial* $\Phi_n$ of degree $n$ is the unique polynomial of the form $\Phi_n(z) = z^n + \text{(terms of lower degree)}$ such that
$$\ip{\Phi_n}{z^k} = 0 \quad \text{for } k = 0, 1, \dots, n - 1.$$
The *orthonormal polynomials* are $\varphi_n = \Phi_n / \norm{\Phi_n}$.

## Remarks

The condition on the support makes $\ip{p}{p} > 0$ for every nonzero polynomial $p$, since a nonzero polynomial has finitely many zeros.
Then $\Phi_n$ is $z^n$ minus its orthogonal projection onto the span of $1, z, \dots, z^{n-1}$, which shows existence and uniqueness.
Such measures are called *nontrivial*.

Example: let $\mu$ be the normalized arc length $d\theta / 2\pi$, with $z = e^{i\theta}$.
Then $\ip{z^n}{z^k} = \frac{1}{2\pi} \int_0^{2\pi} e^{i(n - k)\theta} \, d\theta = 0$ for $k \ne n$, so $\Phi_n(z) = z^n$ and $\norm{\Phi_n} = 1$.

Non-example: let $\mu = \delta_1$, the point mass at $1$.
Its support is finite, and the polynomial $z - 1$ has norm $0$.
The orthogonality conditions for $n = 1$ give $\ip{z + c}{1} = 1 + c = 0$, so $\Phi_1 = z - 1$, which is zero in $L^2(\mu)$; the construction breaks down and does not give an orthonormal sequence.
