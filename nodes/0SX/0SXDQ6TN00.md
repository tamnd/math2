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

Dividing a finite-dimensional space by a subspace removes exactly the dimensions of the subspace.
Let $F$ be a field, let $V$ be a [[finite-dimensional|018W3V3TCT]] vector space over $F$, and let $W$ be a subspace of $V$.
Then the [[quotient space|0SVR29SV1V]] $V / W$ is finite-dimensional, and
$$\dim(V / W) + \dim W = \dim V,$$
where $\dim$ is the [[dimension|05G2G0P224]].
Equivalently, $\dim(V / W) = \dim V - \dim W$.
More precisely, if $w_1, \dots, w_m, v_{m+1}, \dots, v_n$ is a basis of $V$ that starts with a basis of $W$, then $v_{m+1} + W, \dots, v_n + W$ is a basis of $V / W$.

## Remarks

### Why each hypothesis is needed

The hypothesis that $V$ is finite-dimensional is needed for the difference form.
In $V = \R[x]$, the subspace $x^2 \R[x]$ and the subspace $V$ itself both have countably infinite dimension, but the quotients have dimensions $2$ and $0$, as [[polynomials modulo $x^2$|PHA4SATHWE]] shows.
So $\dim V$ and $\dim W$ alone do not determine $\dim(V / W)$, and "$\infty - \infty$" has no value.
The sum form survives in infinite dimension if we read dimensions as cardinal numbers.
The reason is that $W$ has a complement, and every complement is isomorphic to $V / W$, so $V \cong W \oplus V / W$.

The hypothesis that $W$ is a subspace is needed for $V / W$ to exist at all.
For [[a line that misses the origin|E3MQ50YQNR]] there is no quotient.

### Bases of the quotient from a complement

The basis in the statement has a second description.
The vectors $v_{m+1}, \dots, v_n$ span a [[complement|0M83V17KHX]] $C$ of $W$, that is, $V = W \oplus C$.
For any complement $C$ and any basis $c_1, \dots, c_k$ of $C$, the cosets $c_1 + W, \dots, c_k + W$ form a basis of $V / W$, because the map $C \to V / W$, $c \mapsto c + W$, is an isomorphism by the theorem that [[every complement is isomorphic to the quotient|244KTXDJHW]].
For example, in $\R^3$ with $W$ the $xy$-plane, the $z$-axis is a complement, and $(0, 0, 1) + W$ is a basis of $\R^3 / W$, which has dimension $3 - 2 = 1$.

### What it gives you

The number $\dim(V / W)$ is the [[codimension|JJCGJ1EGCQ]] of $W$ in $V$, and in finite dimension it equals $\dim V - \dim W$.
All complements of $W$ have this same dimension.
A subspace $W$ equals $V$ if and only if $\dim W = \dim V$, since $V / W = 0$ exactly when $W = V$.

With the [[first isomorphism theorem|0MTBGVZ4XJ]], the formula gives the [[rank-nullity theorem|0W4FSW1TVB]]:
$$\dim V - \dim \ker f = \dim(V / \ker f) = \dim \operatorname{im} f.$$
With the [[second isomorphism theorem|0APN65D6Y6]], it gives the [[dimension formula for sums of subspaces|06HTJNCMPA]]:
$$\dim(U + W) - \dim W = \dim U - \dim(U \cap W).$$

### The converse

If $W$ is a subspace of $V$ such that $W$ and $V / W$ are both finite-dimensional, then $V$ is finite-dimensional.
Take a basis of $W$ and one representative of each vector of a basis of $V / W$.
Together these vectors form a basis of $V$, so $\dim V = \dim W + \dim(V / W)$ in this case too.

## History

The formula is the quotient form of the rank-nullity theorem, and textbooks prove it either directly by extending a basis or as a consequence of rank-nullity.
Axler's *Linear Algebra Done Right* proves it in its section on quotient spaces.

## Explanations

### L1 human

Dividing by a subspace flattens all of its directions to nothing.
What remains has the dimension of the whole space minus the dimension of the subspace.
For example, ordinary three-dimensional space divided by a plane through the origin leaves one dimension, a line of parallel planes.

### L2 human

Let $V = \R^4$ and let $W$ be the span of $(1, 0, 1, 0)$ and $(0, 1, 0, 1)$.
The two vectors are independent, since neither is a multiple of the other, so $\dim W = 2$.
The theorem gives
$$\dim(\R^4 / W) = 4 - 2 = 2.$$
The [[proof|6JGF4G3QRC]] also gives a basis: extend the basis of $W$ by $e_1$ and $e_2$, and take $e_1 + W$ and $e_2 + W$.
The computation is carried out in [[a two-dimensional quotient of $\R^4$|CX9P5CZF5N]].
The typical use is to find the dimension of a quotient without describing it, and then to compare it with a space you know.
Watch out: the formula is about $V / W$ and not about a set difference; $\R^4 \setminus W$ is not a subspace at all.

### L3 human

The formula says that dimension is additive on short [[exact sequences|946YAZNYKX]] $0 \to W \to V \to V / W \to 0$.
From this one gets the [[alternating sum formula|EFBRMNWDQM]] for longer exact sequences, so dimension behaves like an Euler characteristic.
For modules over a ring, the length of a module of finite length is additive on short exact sequences in the same way.
In infinite dimension the useful invariant is the codimension $\dim(V / W)$ itself, which can be finite even when $\dim W$ is infinite.
