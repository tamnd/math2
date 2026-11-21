---
tag: 6DP6ESTNYR
kind: example
name: The type space of algebraically closed fields
msc: ["03C07", "03C60", "12F05"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [VDY4PG5WHN, A0VNTN725W]
uses: [VDY4PG5WHN, A0VNTN725W, 9V71Q3SD1G, MT8TDVPBXB, 0PF6TM8TWT, 00X2A9G9W3, 03NDVCSHSB, 0NQMZ89X4A, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Stone spaces
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $T = \mathrm{ACF}_0$, the theory of [[algebraically closed fields|0PF6TM8TWT]] of characteristic $0$, in the language $\set{+, -, \cdot, 0, 1}$.
We describe the [[Stone space|VDY4PG5WHN]] $S_1(\emptyset)$ of $T$.

1. The [[theory of algebraically closed fields|MT8TDVPBXB]] has quantifier elimination, so a complete type $p(x)$ is fixed by its atomic formulas $f(x) = 0$ with $f \in \Z[x]$.
2. Suppose $p$ contains $f(x) = 0$ for some nonzero $f$. Factor $f$ into [[irreducible polynomials|00X2A9G9W3]] in $\Z[x]$; since $p$ is complete, it contains $g(x) = 0$ for one irreducible factor $g$.
3. Two irreducible polynomials $g, h$ that are not multiples of each other satisfy $ug + vh = m$ for some $u, v \in \Z[x]$ and an integer $m \ne 0$, so they have no common root in characteristic $0$.
4. So $g$ is unique up to sign, and an element $a$ with $g(a) = 0$ satisfies $h(a) = 0$ exactly when $g$ divides $h$, since $g$ is the [[minimal polynomial|03NDVCSHSB]] of $a$ up to a scalar.
5. So all roots of $g$ have the same type $p_g$, and the formula $g(x) = 0$ isolates it: $[g(x) = 0] = \set{p_g}$.
6. Otherwise $p$ contains $f(x) \ne 0$ for every nonzero $f \in \Z[x]$. This is one type $p_\infty$, the type of a [[transcendental number|0NQMZ89X4A]] such as $\pi$ in $\C$.
7. A formula $\varphi(x) \in p_\infty$ is, by step 1, equivalent to a Boolean combination of equations $f_i(x) = 0$. Its truth value is the same at every element that is a root of none of the nonzero $f_i$. It holds at $\pi$, so it defines a cofinite set.
8. A cofinite set contains roots of all but finitely many irreducible $g$, so $[\varphi]$ contains infinitely many $p_g$.

So $S_1(\emptyset) = \set{p_g : g \text{ irreducible}} \cup \set{p_\infty}$, each $p_g$ is an [[isolated type|A0VNTN725W]], and $p_\infty$ is the only limit point.

## Remarks

The space is homeomorphic to $\set{0} \cup \set{1/k : k \ge 1}$ with the topology of $\R$: a countable discrete set with one point added at the end.
In characteristic $p$ the same argument works with $\mathbb{F}_p[x]$ in place of $\Z[x]$.
Over a parameter field $K$, the types are the types of the roots of the irreducible polynomials over $K$ and one transcendental type, so $\abs{S_1(K)} = \abs{K}$ for infinite $K$.
The field $\C$ realizes every point of $S_1(\emptyset)$, while $\overline{\Q}$ omits $p_\infty$.

## Explanations

### L1 human

Over the empty set, the field operations can only say which polynomial equations with integer coefficients a number solves.
So $\sqrt{2}$ and $-\sqrt{2}$ look the same, because both solve $x^2 - 2 = 0$ and they solve the same other equations.
Every transcendental number, such as $\pi$ or $e$, solves no equation, so all of them look the same too.

### L2 human

We check that $\sqrt{2}$ and $\pi$ have different types and that only one of them has an isolated type.

1. The formula $x \cdot x = 1 + 1$ is in $\operatorname{tp}(\sqrt{2})$ and not in $\operatorname{tp}(\pi)$.
2. The formula $x \cdot x = 1 + 1$ alone implies the whole type of $\sqrt{2}$, by step 5.
3. No formula implies the type of $\pi$, by steps 7 and 8.

The typical use is to read off the algebraic and transcendental types of a field.
The trap is to think that $\sqrt{2}$ and $\sqrt{3}$ have the same type because both are algebraic: they are roots of different irreducible polynomials.
