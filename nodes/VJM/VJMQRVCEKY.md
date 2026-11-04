---
tag: VJMQRVCEKY
kind: statement
role: theorem
name: Structure theorem for commutative semigroups
msc: [20M10]
sources:
  - wikipedia: en:27799@r1363055110
    locator: Semigroup, section Structure theorem for commutative semigroups
    note: adopted
    mention: wikipedia://en/27799#IT1W
    sections: [Statement]
inventory: [8TEDRHYKJP]
---

## Statement

There is a structure theorem for commutative semigroups in terms of semilattices. A semilattice (or more precisely a meet-semilattice) $(L, \le)$ is a [[partially ordered set|0QV2JS9RJ3]] where every pair of elements $a, b \in L$ has a greatest lower bound, denoted $a \land b$. The operation ∧ makes *L* into a semigroup that satisfies the additional idempotence law $a \land a = a$.

Given a homomorphism $f : S \to L$ from an arbitrary semigroup to a semilattice, each inverse image $S_{a} = f^{-1}\{a\}$ is a (possibly empty) semigroup. Moreover, *S* becomes **graded** by *L*, in the sense that $S_{a}S_{b} \subseteq S_{a\land b}$.

If *f* is onto, the semilattice *L* is isomorphic to the quotient of *S* by the equivalence relation ~ such that $x \sim y$ if and only if $f(x) = f(y)$. This equivalence relation is a semigroup congruence, as defined above.

Whenever we take the quotient of a commutative semigroup by a congruence, we get another commutative semigroup. The structure theorem says that for any commutative semigroup *S*, there is a finest congruence ~ such that the quotient of *S* by this equivalence relation is a semilattice. Denoting this semilattice by *L*, we get a homomorphism *f* from *S* onto *L*. As mentioned, *S* becomes graded by this semilattice.

Furthermore, the components *S*<sub>*a*</sub> are all Archimedean semigroups. An Archimedean semigroup is one where given any pair of elements *x*, *y*, there exists an element *z* and $n > 0$ such that $x^{n} = yz$.

The Archimedean property follows immediately from the ordering in the semilattice *L*, since with this ordering we have $f(x) \le f(y)$ if and only if $x^{n} = yz$ for some *z* and $n > 0$.
