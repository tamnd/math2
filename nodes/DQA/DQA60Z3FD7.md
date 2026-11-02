---
tag: DQA60Z3FD7
kind: example
name: Veronese embedding
msc: [14N05, "14E25"]
instance_of: [CDS1VWB7A3]
uses: [ZT9A6JK8QF, A4H4CZ2V35, CDS1VWB7A3, 2C3PAQ7H50]
sources:
  - url: https://en.wikipedia.org/wiki/Veronese_surface
---

## Example

Let $k$ be an algebraically closed field, and let $n \ge 1$ and $d \ge 1$ be integers.
There are $\binom{n + d}{d}$ monomials of degree $d$ in $x_0, \dots, x_n$; let $N = \binom{n + d}{d} - 1$.
The *Veronese embedding* of degree $d$ is the map of [[projective spaces|ZT9A6JK8QF]]
$$\nu_d \colon \mathbb{P}^n \to \mathbb{P}^N, \qquad [x_0 : \dots : x_n] \mapsto [x^{\alpha}]_{\abs{\alpha} = d},$$
which lists all monomials $x^\alpha = x_0^{\alpha_0} \cdots x_n^{\alpha_n}$ with $\alpha_0 + \dots + \alpha_n = d$.

Check that it is a [[morphism|CDS1VWB7A3]]: the monomials are [[homogeneous polynomials|2C3PAQ7H50]] of the same degree $d$.
So scaling $x$ by $\lambda$ scales all of them by $\lambda^d$.
They never vanish together, since $x_i^d$ is among them and some $x_i \ne 0$.

Check that it is injective: if $x_i \ne 0$, then the monomials $x_i^{d-1} x_j$ for $j = 0, \dots, n$ are the coordinates of $x_i^{d-1} \cdot (x_0, \dots, x_n)$, which recover $[x]$.
In fact $\nu_d$ is an isomorphism onto its image, which is a [[projective variety|A4H4CZ2V35]] of dimension $n$.

For $n = 1$ and $d = 2$, $\nu_2([s : t]) = [s^2 : st : t^2]$, and the image is the conic $z_0 z_2 = z_1^2$ in $\mathbb{P}^2$.
For $n = 1$ and $d = 3$, the image of $[s : t] \mapsto [s^3 : s^2 t : s t^2 : t^3]$ is the twisted cubic curve in $\mathbb{P}^3$.
For $n = 2$ and $d = 2$, the image is the Veronese surface in $\mathbb{P}^5$.

Under $\nu_d$, a hypersurface of degree $d$ in $\mathbb{P}^n$ becomes the intersection of the image with a hyperplane of $\mathbb{P}^N$.

## Explanations

### L1 human

The Veronese map replaces a point by the list of all products of its coordinates of a fixed degree.
For the projective line and degree two, the point $[s : t]$ goes to $[s^2 : st : t^2]$, and the image is a conic.
The trick turns curved equations of degree $d$ into linear equations in the new coordinates.
This lets one study hypersurfaces of degree $d$ with the tools of linear algebra on a bigger space.
