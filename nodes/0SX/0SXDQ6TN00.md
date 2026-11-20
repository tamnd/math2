---
tag: 0SXDQ6TN00
kind: statement
role: theorem
name: Dimension of a quotient space
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0BR3FY5Q8M]
uses: [0SVR29SV1V, 05G2G0P224, 018W3V3TCT]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.finrank_quotient_add_finrank
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

Let $F$ be a field, let $V$ be a [[finite-dimensional|018W3V3TCT]] vector space over $F$, and let $W$ be a subspace of $V$.
Then the [[quotient space|0SVR29SV1V]] $V / W$ is finite-dimensional, and
$$\dim(V / W) + \dim W = \dim V,$$
where $\dim$ is the [[dimension|05G2G0P224]].
Equivalently, $\dim(V / W) = \dim V - \dim W$.

## Remarks

### Why each hypothesis is needed

- $V$ must be finite-dimensional for the form $\dim V - \dim W$. For $V = \R[x]$, the subspaces $x^2 \R[x]$ and $V$ itself both have countably infinite dimension, but the quotients have dimensions $2$ and $0$, see [[polynomials modulo x²|~86678d6f]]. So $\dim V$ and $\dim W$ do not determine $\dim(V / W)$.
- $W$ must be a subspace, since otherwise $V / W$ is not defined, as for [[a line that misses the origin|~6118285a]].
- With dimensions as cardinal numbers, the sum form $\dim(V / W) + \dim W = \dim V$ still holds in infinite dimension, since $V \cong W \oplus V / W$.

### Consequences

- The number $\dim(V / W)$ is the [[codimension|~ccb24df5]] of $W$ in $V$. In finite dimension it equals $\dim V - \dim W$.
- Every complement of $W$ has dimension $\dim V - \dim W$, since it is [[isomorphic to the quotient|~7fe638c8]].
- With the [[first isomorphism theorem|0MTBGVZ4XJ]], the formula gives the rank–nullity theorem: $\dim V - \dim \ker f = \dim(V / \ker f) = \dim \operatorname{im} f$.
- With the [[second isomorphism theorem|0APN65D6Y6]], it gives the [[Grassmann formula|06HTJNCMPA]] for $\dim(U + W)$.
- $W = V$ if and only if $\dim W = \dim V$, since $V / W = 0$ exactly when $W = V$.

### Converse

If $W$ is a subspace of $V$ with $\dim W$ and $\dim(V / W)$ finite, then $V$ is finite-dimensional.
A basis of $W$ together with lifts of a basis of $V / W$ is a basis of $V$.

## History

The formula appears in the early abstract treatments of quotient spaces, for example in van der Waerden's *Moderne Algebra* and in Halmos's *Finite-Dimensional Vector Spaces* of 1942.
Its proof by extending a basis follows the method of Steinitz's exchange lemma.

## Explanations

### L1 human

Dividing by a subspace removes its dimensions.
What remains has the dimension of the space minus the dimension of the subspace.
Ordinary space divided by a plane leaves one dimension.

### L2 human

Let $V = \R^4$ and $W$ the span of $(1, 0, 1, 0)$ and $(0, 1, 0, 1)$.

1. The two vectors are independent, so $\dim W = 2$.
2. The theorem gives $\dim(\R^4 / W) = 4 - 2 = 2$.
3. The [[proof|6JGF4G3QRC]] finds a basis: extend the basis of $W$ by $e_1$ and $e_2$, and take $e_1 + W$, $e_2 + W$.
4. The worked computation is in [[a quotient of R⁴|~737e4bcc]].

The trap is to use the formula in infinite dimension, where $\infty - \infty$ has no meaning.

### L3 human

The formula says that dimension is additive on short exact sequences $0 \to W \to V \to V / W \to 0$.
This makes the dimension an Euler characteristic on finite-dimensional spaces, and the [[alternating sum formula|~78f0e572]] for exact sequences follows.
For modules over a ring, the length of a module of finite length is additive in the same way.
