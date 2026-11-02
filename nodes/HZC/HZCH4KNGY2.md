---
tag: HZCH4KNGY2
kind: definition
name: Milnor number
msc: [32S05, 32S10, 32S25]
defines: 1ZE51P7GRQ
uses: [EVPZ7ZG1HB, 096Z9MP2ME, VTGYEES3VS]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_number
---

## Definition

Let $\mathcal{O}_{n+1} = \C\{z_0, \dots, z_n\}$ be the [[ring of convergent power series|EVPZ7ZG1HB]] in $n + 1$ variables.
Let $f \in \mathcal{O}_{n+1}$ with $f(0) = 0$.
The *Jacobian ideal* of $f$ is the [[ideal|096Z9MP2ME]] $J(f) = \left( \frac{\partial f}{\partial z_0}, \dots, \frac{\partial f}{\partial z_n} \right)$ of $\mathcal{O}_{n+1}$.
The *Milnor number* of $f$ at $0$ is
$$\mu(f) = \dim_\C \mathcal{O}_{n+1} / J(f),$$
a non-negative integer or $\infty$.

## Remarks

The quotient $\mathcal{O}_{n+1} / J(f)$ is called the *local algebra* or *Milnor algebra* of $f$.
The number $\mu(f)$ is finite if and only if $f$ has at most an [[isolated singularity|VTGYEES3VS]] at $0$, and $\mu(f) = 0$ exactly when $0$ is not a critical point.

Example: $f(x, y) = x^p + y^q$ with integers $p, q \ge 2$.
Then $J(f) = (x^{p-1}, y^{q-1})$, and the monomials $x^a y^b$ with $0 \le a \le p - 2$ and $0 \le b \le q - 2$ form a basis of the quotient.
So $\mu(f) = (p - 1)(q - 1)$.
For $f(z) = z_0^2 + \cdots + z_n^2$, $J(f)$ is the maximal ideal and $\mu(f) = 1$.

Non-example of a finite Milnor number: $f(x, y) = x^2 y$.
Here $J(f) = (2xy, x^2)$, and the powers $y, y^2, y^3, \dots$ are linearly independent modulo $J(f)$, so $\mu(f) = \infty$.
The singularity is not isolated: the gradient vanishes on the whole line $x = 0$.

Let $\nabla f = (\partial f / \partial z_0, \dots, \partial f / \partial z_n)$.
For an isolated singularity, $\mu(f)$ is also the topological degree of the map $z \mapsto \nabla f(z) / \norm{\nabla f(z)}$ from a small sphere about $0$ to the unit sphere.
It is also the rank of the middle homology of the Milnor fibre.
