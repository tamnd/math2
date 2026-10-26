---
tag: ~ae22ad2b
kind: statement
role: theorem
name: Homotopy invariance of line integrals of closed forms
aliases: [helmholtz-theorem-for-lamellar-fields]
msc: [26B20]
uses: [~979a322d, ~e6672d67, ~b28f28ba, ~b33b5f45, ~d05c0400, ~94fe5da2]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes%27_theorem
    locator: Helmholtz's theorem
  - url: https://en.wikipedia.org/wiki/Stokes%27_theorem
    locator: Conservative forces
  - url: https://en.wikipedia.org/wiki/Closed_and_exact_differential_forms
    locator: Vector field analogies
---

## Statement

Let $U \subseteq \mathbb{R}^3$ be open, and let $F \colon U \to \mathbb{R}^3$ be a vector field of class $C^1$ with $\nabla \times F = 0$ on $U$.
Let $c_0, c_1 \colon [0, 1] \to U$ be piecewise smooth [[closed curves|~b28f28ba]].
Suppose that there is a piecewise smooth map $H \colon [0, 1] \times [0, 1] \to U$ with $H(t, 0) = c_0(t)$, $H(t, 1) = c_1(t)$ and $H(0, s) = H(1, s)$ for all $s, t \in [0, 1]$.
Then
$$\oint_{c_0} F \cdot d\mathbf{r} = \oint_{c_1} F \cdot d\mathbf{r}.$$

## Remarks

Proof: apply [[Stokes' theorem|~b33b5f45]] to the surface $H([0, 1]^2)$. The curl term is zero, and the integrals along the curves $s \mapsto H(0, s)$ and $s \mapsto H(1, s)$ cancel.
If $c_1$ is a constant loop, then $\oint_{c_0} F \cdot d\mathbf{r} = 0$.
On a [[simply connected|~d05c0400]] domain, each loop deforms to a point, and a smoothing argument gives a piecewise smooth $H$. So curl-free $C^1$ fields on such domains are [[conservative|~94fe5da2]].
The condition $\nabla \times F = 0$ means that the 1-form $F_1 \, dx + F_2 \, dy + F_3 \, dz$ is closed. This explains the name of the theorem.

## Explanations

### L1 human

For a field with no swirl, the work around a loop does not change when you slide and bend the loop continuously inside the domain.
A loop that can shrink to a point therefore has zero work.
