---
tag: HFEA4FKGW1
kind: statement
role: theorem
name: Poincaré–Birkhoff–Witt theorem
msc: [17B35, 16S30]
uses: [SCZ8PRVY00, 04C5ZBG1WT, 0KCQ9Y3QKA, PBGF9TXMB7, 8HFAEGFQT1, R1PTHQACWM]
about: [SCZ8PRVY00]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Birkhoff%E2%80%93Witt_theorem
same_as:
  wikidata: Q2270905
  wikipedia: Poincaré–Birkhoff–Witt theorem
---

## Statement

Let $k$ be a [[field|04C5ZBG1WT]] and let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over $k$.
Let $(x_i)_{i \in I}$ be a [[basis|0KCQ9Y3QKA]] of $\mathfrak g$ indexed by a totally ordered set $I$.
Let $U(\mathfrak g)$ be the [[universal enveloping algebra|SCZ8PRVY00]] of $\mathfrak g$ with its canonical map $\iota \colon \mathfrak g \to U(\mathfrak g)$.
Then the ordered monomials
$$\iota(x_{i_1}) \iota(x_{i_2}) \cdots \iota(x_{i_m}), \qquad m \ge 0, \quad i_1 \le i_2 \le \cdots \le i_m,$$
form a basis of $U(\mathfrak g)$ over $k$, where the monomial with $m = 0$ is $1$.

## Remarks

That the ordered monomials span is easy: any product of the $\iota(x_i)$ can be reordered.
Each swap of neighbours changes it by a product of lower length, by the relation $xy - yx = [x, y]$.
Linear independence is the hard part.
A standard proof builds an action of $\mathfrak g$ on the polynomial ring $S(\mathfrak g)$ that sends each ordered monomial applied to $1$ to the matching polynomial monomial.
The Jacobi identity is used to check that this is an action.
In particular $\iota$ is injective, so every Lie algebra over a field is a Lie subalgebra of an associative algebra with the commutator bracket.
Equivalently, the [[associated graded algebra|8HFAEGFQT1]] of $U(\mathfrak g)$ for its [[filtration|R1PTHQACWM]] by length of products is isomorphic to the [[symmetric algebra|PBGF9TXMB7]] $S(\mathfrak g)$.
Example: for $\mathfrak{sl}_2$ with basis $f < h < e$, the elements $f^a h^b e^c$ with $a, b, c \ge 0$ form a basis of $U(\mathfrak{sl}_2)$.
Over a commutative ring instead of a field, the theorem holds when $\mathfrak g$ is free as a module, but it can fail in general.

## Explanations

### L1 human

The enveloping algebra is defined by generators and relations, and such definitions can collapse.
The theorem says that nothing collapses here: the enveloping algebra is exactly as large as a polynomial ring in a basis of the Lie algebra.
You may write every element as a combination of monomials with the basis elements in a fixed order, and this way of writing it is unique.

### L2 human

The theorem is the basic structural fact about $U(\mathfrak g)$.
It shows that $\mathfrak g$ embeds in $U(\mathfrak g)$, that $U(\mathfrak g)$ has no zero divisors, and that $U(\mathfrak g)$ is Noetherian when $\mathfrak g$ is finite-dimensional, by passing to the polynomial ring $S(\mathfrak g)$.
For a subalgebra $\mathfrak h \subseteq \mathfrak g$, it shows that $U(\mathfrak g)$ is a free $U(\mathfrak h)$-module, which is the key input for Verma modules and induced representations.
It also gives the vector space isomorphism $S(\mathfrak g) \to U(\mathfrak g)$ by symmetrisation in characteristic $0$.
