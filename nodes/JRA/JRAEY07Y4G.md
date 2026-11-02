---
tag: JRAEY07Y4G
kind: statement
role: theorem
name: Lê–Ramanujam theorem
msc: [32S15, 32S05, 32S50]
uses: [VTGYEES3VS, 1ZE51P7GRQ, 0QT00PB5G2]
about: [1ZE51P7GRQ, VTGYEES3VS]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_number
---

## Statement

Let $n \ne 2$ be a non-negative integer.
Let $F(z, t)$ be a holomorphic function on a neighbourhood of $(0, 0)$ in $\C^{n+1} \times \C$, and write $f_t(z) = F(z, t)$.
Assume that, for all $t$ in a neighbourhood of $0$, $f_t(0) = 0$ and $f_t$ has an [[isolated singularity|VTGYEES3VS]] at $0$.
Assume also that the [[Milnor number|1ZE51P7GRQ]] $\mu(f_t)$ does not depend on $t$.
Then, for all $t$ small enough, there is a [[homeomorphism|0QT00PB5G2]] $\phi$ between neighbourhoods of $0$ in $\C^{n+1}$ with $\phi(0) = 0$ and $\phi(f_0^{-1}(0)) = f_t^{-1}(0)$.
In words, a $\mu$-constant family of isolated hypersurface singularities has constant topological type.

## Remarks

Lê Dũng Tráng and C. P. Ramanujam proved the theorem in 1976.
The proof shows that the Milnor fibrations of $f_0$ and $f_t$ are related by an h-cobordism, and then applies the h-cobordism theorem of Smale.
That theorem needs the cobordism to have dimension at least $6$, which is why the case $n = 2$, surfaces in $\C^3$, is excluded; this case is still open.
The converse holds: the Milnor number is a topological invariant of the hypersurface germ, so a family of constant topological type has constant $\mu$.

Example: $f_t(x, y) = x^4 + y^4 + t x^2 y^2$ for $t$ near $0$.
For $t \ne \pm 2$ the quartic form $f_t$ is a product of four distinct linear factors, so $f_t$ has an isolated singularity with $\mu(f_t) = 9$.
The theorem says that all these germs are topologically the same as $x^4 + y^4$, four lines through the origin.

## Explanations

### L1 human

Deform a singular hypersurface by changing a parameter, and keep track of the Milnor number, which is an integer computed by algebra.
If this number never jumps, the theorem says that the shape of the singularity, as seen by topology, does not change at all.
So a single integer controls the topology in families, except for surfaces in $\C^3$, where the method breaks down and the question is still open.

### L2 human

The theorem is a central result of equisingularity theory, which asks when a family of singularities should count as having the same singularity.
For plane curves, $n = 1$, constant $\mu$ is equivalent to constant topological type, and to constant Puiseux characteristics.
Later work showed that a $\mu$-constant family is in fact topologically trivial as a family when $n \ne 2$.
The Milnor number is upper semicontinuous in families, so it can only jump up at special parameter values.
