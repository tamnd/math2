---
tag: MXSPFETKMM
kind: example
name: Types of reals over the rationals
msc: ["03C07", "06A05"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [9V71Q3SD1G]
uses: [9V71Q3SD1G, 2W4S2H4VYA, 7FDDXV3JK7, 08J2M1JYAG, 0NCJ5WXN6Z, 8WZF9SBP39]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Example

Let $\mathcal{R} = (\R, <)$ and $A = \Q$.
We describe the complete $1$-[[types|9V71Q3SD1G]] over $\Q$ in $\mathcal{R}$ and find the ones that $\mathcal{R}$ realizes.

1. The order $(\R, <)$ is a [[dense linear order|2W4S2H4VYA]] without endpoints, and this theory has [[quantifier elimination|7FDDXV3JK7]].
2. So a complete type $p(x)$ over $\Q$ is fixed by its atomic formulas $x < q$, $x = q$ and $q < x$ for $q \in \Q$.
3. If $x = q \in p$ for some $q$, then $p$ is the type of the rational number $q$.
4. Otherwise $p$ fixes the set $C_p = \set{q \in \Q : q < x \in p}$, a downward closed set of rationals, and $p$ is fixed by $C_p$.
5. For an irrational $r$, the type $\operatorname{tp}(r/\Q)$ has $C = \set{q : q < r}$, a cut with no largest element whose complement has no smallest element.
6. Two different irrationals $r < s$ have different types, since some rational $q$ with $r < q < s$ gives $x < q$ in the first type only.
7. Four kinds of types are not realized: $+\infty$ with $C = \Q$, $-\infty$ with $C = \emptyset$, and for each $q \in \Q$ the types $q^+$ with $C = \set{q' : q' \le q}$ and $q^-$ with $C = \set{q' : q' < q}$, without $x = q$.
8. Each of them is a type: a finite part of $q^+$ says $q < x < q'$ for finitely many $q' > q$, and a real number close to $q$ satisfies it.
9. No real realizes $q^+$: a real $r$ with $q < r$ has a rational $q'$ with $q < q' < r$, and then $x < q'$ fails at $r$.

So $S_1(\Q)$ has $2^{\aleph_0}$ points, and $\mathcal{R}$ realizes all of them except $\pm\infty$ and the types $q^{\pm}$.

## Remarks

The rational order $(\Q, <)$ is an [[elementary substructure|8WZF9SBP39]] of $\mathcal{R}$, so the types over $\Q$ are the same in both structures.
The rational order realizes only the types of rationals, so it omits $2^{\aleph_0}$ types over a countable set.
This is why $(\Q, <)$ is saturated but not $\aleph_1$-saturated.

In the real field $(\R, +, \cdot, <)$ the picture changes: the type of $\sqrt{2}$ over $\Q$ contains $x \cdot x = 1 + 1 \wedge 0 < x$, and this one formula implies the whole type.
So the same element can have an isolated type in a richer language and a non-isolated type in the pure order.

## Explanations

### L1 human

Over the rationals, the order can only say which rationals lie below a real number.
So the type of a real number is its position among the fractions.
For example, $\sqrt{2}$ is above $1.41$ and below $1.42$, and its type is the list of all such facts.
An element "just above $0$" is above $0$ and below every positive fraction, and no real number is like that.

### L2 human

We check that $\sqrt{2}$ and $\sqrt{3}$ have different types over $\Q$ in $(\R, <)$.

1. The rational number $3/2$ satisfies $\sqrt{2} < 3/2 < \sqrt{3}$, since $(3/2)^2 = 9/4$ lies between $2$ and $3$.
2. So the formula $x < 3/2$ is in $\operatorname{tp}(\sqrt{2}/\Q)$ and not in $\operatorname{tp}(\sqrt{3}/\Q)$.

The typical use is to see that $(\R, <)$ has many more types over $\Q$ than $(\Q, <)$ realizes.
The trap is to think that the type $0^+$ is realized by a small real number: every positive real is above some positive rational.
