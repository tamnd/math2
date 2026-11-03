---
tag: C75W88ZVNY
kind: statement
role: theorem
name: Helmholtz decomposition of a velocity field
msc: [76A02, 26B12, 35J05]
uses: [0299VCW1TH, 0ABK9V9Y64, 0NF6GQNXMY, 0MWV6ZTK6S, 0V33BNKZ9S, 0E0B6RA8K0, 0DEB0JMN0W, HABCJ4Y0SR, 18KXZHVF4M]
about: [0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Helmholtz_decomposition
same_as:
  wikidata: Q1153588
  wikipedia: Helmholtz decomposition
---

## Statement

Let $\mathbf{F} \colon \R^3 \to \R^3$ be a [[smooth|0V33BNKZ9S]] [[vector field|0299VCW1TH]] with compact support.
Define, for $x \in \R^3$,
$$\Phi(x) = \frac{1}{4\pi} \int_{\R^3} \frac{\nabla \cdot \mathbf{F}(y)}{\abs{x - y}} \, dy, \qquad \mathbf{A}(x) = \frac{1}{4\pi} \int_{\R^3} \frac{\nabla \times \mathbf{F}(y)}{\abs{x - y}} \, dy.$$
Then $\Phi$ and $\mathbf{A}$ are smooth and
$$\mathbf{F} = -\nabla \Phi + \nabla \times \mathbf{A}.$$
The field $-\nabla \Phi$ has zero [[curl|0NF6GQNXMY]], and the field $\nabla \times \mathbf{A}$ has zero [[divergence|0MWV6ZTK6S]].
This is the only way to write $\mathbf{F}$ as a curl-free plus a divergence-free smooth field, both tending to $0$ at infinity.

## Remarks

The proof writes $\mathbf{F} = -\Delta \mathbf{G}$ with $\mathbf{G}(x) = \frac{1}{4\pi} \int \mathbf{F}(y) / \abs{x - y} \, dy$, since $1/(4\pi \abs{x})$ is the fundamental solution of $-\Delta$.
The identity $\Delta \mathbf{G} = \nabla (\nabla \cdot \mathbf{G}) - \nabla \times (\nabla \times \mathbf{G})$ then gives the result, with $\Phi = \nabla \cdot \mathbf{G}$ and $\mathbf{A} = \nabla \times \mathbf{G}$.
For uniqueness, the difference of two decompositions is curl-free and divergence-free.
So each component is a [[harmonic function|0DEB0JMN0W]] that tends to $0$ at infinity, hence it is $0$ by Liouville's theorem.
Without a decay condition uniqueness fails: the constant field $(1, 0, 0)$ is both the gradient of $x_1$ and the curl of $(0, 0, x_2)$.
The theorem extends to fields that decay fast enough at infinity and, with boundary conditions, to bounded domains; the [[Hodge decomposition|HABCJ4Y0SR]] is the version for differential forms on manifolds.

## Explanations

### L1 human

Every reasonable flow of a fluid is the sum of two simpler flows.
One flows out of sources and into sinks without any swirling.
The other swirls around without any sources or sinks.
The theorem says how to find the two pieces from the sources and the swirls of the original flow.

### L2 human

In fluid mechanics, the decomposition writes a velocity field as $\mathbf{u} = \nabla \phi + \nabla \times \boldsymbol{\psi}$, a potential part plus a solenoidal part.
The divergence of $\mathbf{u}$ only affects the potential part, and the vorticity only affects the solenoidal part.
This explains why vorticity alone determines an incompressible flow that decays at infinity (the Biot–Savart law).
The projection onto divergence-free fields, often called the Leray projection, is used to remove the pressure from the incompressible [[Navier–Stokes equations|18KXZHVF4M]].
The formulas for $\Phi$ and $\mathbf{A}$ are Newtonian potentials, that is, solutions of Poisson's equation for the [[Laplacian|0E0B6RA8K0]].
