---
tag: 97YPZ0YHEB
kind: example
name: Vector spaces over the rationals are categorical in every uncountable cardinal
aliases: [rational-vector-spaces-are-uncountably-categorical]
msc: ["03C35", "15A03"]
topics: [6XEXRME4C1]
audience: grad
instance_of: [1JJCGNX240]
uses: [1JJCGNX240, 000AYPA9AJ, 0KCQ9Y3QKA, 0EBACQFAZW, ZR7Y5C235P]
sources:
  - url: https://en.wikipedia.org/wiki/Categorical_theory
    locator: Examples
  - book: isbn:9780387987606
---

## Example

Let $L$ be the signature with a binary function $+$, a unary function $-$, a constant $0$, and a unary function $\lambda_q$ for each $q \in \Q$.
Let $T$ be the $L$-theory with the axioms of a [[vector space|000AYPA9AJ]] over $\Q$, where $\lambda_q(x)$ means $q x$, and the axiom $\exists x \, (x \ne 0)$.
The models of $T$ are the nonzero vector spaces over $\Q$, and the isomorphisms are the $\Q$-linear bijections.
We show that $T$ is $\kappa$-categorical for every uncountable [[cardinal|0EBACQFAZW]] $\kappa$, and that it is not $\aleph_0$-categorical.

1. Every model is infinite. Let $v \ne 0$. If $q v = q' v$, then $(q - q') v = 0$, so $q = q'$, because $v \ne 0$. So $q \mapsto q v$ is injective on $\Q$.
2. Let $V$ have a [[basis|0KCQ9Y3QKA]] $B$ of cardinality $d$. Each vector is a finite linear combination of elements of $B$ with rational coefficients, so $\abs{V} \le \max(d, \aleph_0)$.
3. Also $\abs{V} \ge d$, since $B \subseteq V$, and $\abs{V} \ge \aleph_0$ by step 1. So $\abs{V} = \max(d, \aleph_0)$.
4. Let $\kappa$ be uncountable and $\abs{V} = \kappa$. Then $\max(d, \aleph_0) = \kappa > \aleph_0$, so $d = \kappa$.
5. Let $V$ and $W$ have size $\kappa$, with bases $B$ and $C$. By step 4, $\abs{B} = \abs{C} = \kappa$, so there is a bijection $g : B \to C$.
6. The map $g$ extends to a linear map $f : V \to W$, and $f$ is bijective, because it maps a basis onto a basis. A linear bijection preserves $+$, $-$, $0$ and each $\lambda_q$, so $f$ is an isomorphism of $L$-structures.
7. A model of size $\kappa$ exists: the space of finitely supported functions from $\kappa$ to $\Q$ has a basis of size $\kappa$, so it has size $\kappa$ by step 3.
8. Not $\aleph_0$-categorical: $\Q$ and $\Q^2$ are countable models of dimension $1$ and $2$. An isomorphism would be a linear bijection, which keeps the dimension, so they are not isomorphic.

## Remarks

The countable models are the spaces of dimension $1, 2, 3, \dots$ and $\aleph_0$, so $T$ has exactly $\aleph_0$ countable models.
The signature is countable and $T$ has no finite models, so the [[Łoś-Vaught test|ZR7Y5C235P]] with $\kappa = \aleph_1$ shows that $T$ is complete.
The same theory, written in the signature of groups, is the theory of nontrivial torsion-free divisible abelian groups.
If $\Q$ is replaced by a finite field $F$, an infinite space of dimension $d$ has size $d$, so the theory of infinite $F$-vector spaces is totally categorical.
If $\Q$ is replaced by a field $F$ of infinite size $\lambda$, step 3 becomes $\abs{V} = \max(d, \lambda)$, and the theory is $\kappa$-categorical exactly for $\kappa > \lambda$.

## Explanations

### L1 human

A vector space over the fractions is determined by the number of independent directions it has.
When the space is uncountably large, this number equals the size of the space.
So two spaces of the same uncountable size have the same number of directions, and one can be turned into the other.
For countable spaces this fails: a line and a plane are both countable, but a line has one direction and a plane has two.

### L2 human

We compare $V = \Q$ and $W = \Q^2$ in step 8.

1. Both are countable, since $\Q$ and $\Q \times \Q$ are countable.
2. The vector $1$ spans $V$, so $\dim V = 1$. The vectors $(1, 0)$ and $(0, 1)$ form a basis of $W$, so $\dim W = 2$.
3. Suppose $f : V \to W$ is an isomorphism. Every $w \in W$ is $f(v)$ for some $v = q \cdot 1$, so $w = q f(1)$.
4. Then $W$ is spanned by $f(1)$, so $\dim W \le 1$, which contradicts step 2.

The typical use of the example is to show that a theory can have many countable models and still be complete.
A trap is to count cardinalities only: $V$ and $W$ have the same size, and still they are not isomorphic.
