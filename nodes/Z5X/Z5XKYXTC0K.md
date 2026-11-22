---
tag: Z5XKYXTC0K
kind: statement
role: proposition
name: Subspace test
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [00YC1D652K]
uses: [0EPTJA5QV4, 05EGHEQZAW]
proofs: [N8XQ4315RR]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Definition
  - book: isbn:9780134860244
    locator: Section 1.3
  - book: isbn:9780135367971
    locator: Section 2.2
---

## Statement

To show that a subset is a subspace, and hence a vector space, it is enough to check one closure condition on a nonempty set.
Let $F$ be a field, let $V$ be a [[vector space|05EGHEQZAW]] over $F$, and let $W \subseteq V$ be a subset.
Then the following three conditions are equivalent:

1. $W$ is a [[linear subspace|0EPTJA5QV4]] of $V$.
2. $W$ is nonempty, and $u + av \in W$ for all $u, v \in W$ and all $a \in F$.
3. $W$ is closed under the addition and the scalar multiplication of $V$, and $W$ with the restricted operations is a vector space over $F$.

## Remarks

### A worked use

Let $P_2(\mathbb{R})$ be the real polynomials of degree at most $2$, and let $W = \{p \in P_2(\mathbb{R}) : p(1) = 0\}$.
The zero polynomial has value $0$ at $1$, so $W$ is nonempty.
For $p, q \in W$ and a real number $a$, evaluation at $1$ respects sums and multiples:
$$(p + aq)(1) = p(1) + a\,q(1) = 0 + a \cdot 0 = 0.$$
So condition 2 holds, and $W$ is a subspace, and therefore a vector space, with no axiom checked by hand.
For instance, $x - 1$ and $x^2 - 1$ lie in $W$, and so does $(x - 1) + 3(x^2 - 1) = 3x^2 + x - 4$, whose value at $1$ is $3 + 1 - 4 = 0$.

### Why each hypothesis is needed

The word "nonempty" in condition 2 cannot be dropped.
The empty set satisfies the closure condition, because there are no vectors $u$ and $v$ to test, but it has no zero vector, so it is not a subspace.

The scalar $a$ must range over all of $F$.
If we allow only $a \ge 0$ in $\mathbb{R}^2$, the first quadrant passes, since $u + av$ has nonnegative entries when $u$, $v$ and $a$ do.
But the first quadrant is not a subspace, because $(-1)(1, 1) = (-1, -1)$ is not in it.

In condition 3, the operations must be those of $V$.
The [[positive real numbers with product as addition|DQQ6NXK1SQ]] form a vector space, but with other operations than those of $\mathbb{R}$, so they are not a subspace of $\mathbb{R}$.

### What it gives you

The test turns the eight axioms into one line of algebra.
It shows at once that the [[null space|0PHDYNR24D]] of a matrix, the polynomials of degree at most $n$ and the continuous functions are vector spaces.
The test also works with a condition that fails: for $p(1) = 1$ in place of $p(1) = 0$, we get $(p + aq)(1) = 1 + a$, which is $2$ for $a = 1$, so that set is not a subspace.

### Generalizations

The same test, with a ring $R$ in place of $F$, characterizes the submodules of a [[module|0NZ8JA25WK]] over $R$.
The test for subgroups of a group has the same shape: a nonempty subset $H$ is a subgroup when $g h^{-1} \in H$ for all $g, h \in H$.

## Explanations

### L1 human

To show that a set of vectors is a subspace, you do not need to check all eight rules of a vector space.
Check that the set is not empty, and that $u + av$ stays in the set whenever $u$ and $v$ are in it.
For the line $y = 2x$, the points $(1, 2)$ and $(3, 6)$ give $(1, 2) + 2 \cdot (3, 6) = (7, 14)$, which is again on the line.
The rules of a vector space then come for free from the big space.

### L2 human

Why does one condition do the work of three?
The choice $a = 1$ gives closure under addition.
The choice $u = v = w$ and $a = -1$ gives $w + (-1)w = 0$, so the zero vector is in $W$.
Then $u = 0$ gives $0 + av = av$, which is closure under scaling.
The [[proof|N8XQ4315RR]] writes this out and then checks the axioms of a vector space for $W$.
Watch out: a proof by the test must use arbitrary $u$, $v$ and $a$; a check at a few sample vectors only finds failures.
