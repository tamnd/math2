---
tag: Z86VGP5RMG
kind: statement
role: theorem
name: Word problem for free lattices
msc: [06B25, "03D40"]
uses: [WP20S9NZ15, J2T75ATRV5, 6D3WA7N2W4, PPGD5KW8JC]
about: [WP20S9NZ15]
sources:
  - url: https://en.wikipedia.org/wiki/Free_lattice
---

## Statement

Let $X$ be a set and let $\mathrm{FL}(X)$ be the [[free lattice|WP20S9NZ15]] on $X$.
For lattice [[terms|6D3WA7N2W4]] $s$ and $t$ over $X$, write $s \le t$ when the value of $s$ is below the value of $t$ in $\mathrm{FL}(X)$.
Then $s \le t$ holds if and only if one of the following holds:

1. $s$ and $t$ are the same letter $x \in X$;
2. $s = s_1 \vee s_2$, and $s_1 \le t$ and $s_2 \le t$;
3. $t = t_1 \wedge t_2$, and $s \le t_1$ and $s \le t_2$;
4. $s$ is a letter $x \in X$, $t = t_1 \vee t_2$, and $x \le t_1$ or $x \le t_2$;
5. $s = s_1 \wedge s_2$, $t$ is a letter $x \in X$, and $s_1 \le x$ or $s_2 \le x$;
6. $s = s_1 \wedge s_2$, $t = t_1 \vee t_2$, and $s_1 \le t$ or $s_2 \le t$ or $s \le t_1$ or $s \le t_2$.

Consequently, equality of two lattice terms in $\mathrm{FL}(X)$ is [[decidable|PPGD5KW8JC]]: $s = t$ in $\mathrm{FL}(X)$ exactly when $s \le t$ and $t \le s$.

## Remarks

In each clause the comparisons on the right involve terms of smaller total length, so the clauses give a recursive algorithm to decide $s \le t$.
The "if" direction holds in every lattice.
The "only if" direction is the content of the theorem; clause 6 is [[Whitman's condition|5TNA2HBG7Y]].
Example: $x \wedge (y \vee z) \le (x \wedge y) \vee (x \wedge z)$ fails in $\mathrm{FL}(\set{x, y, z})$.
By clause 6 it would need one of $x \le (x \wedge y) \vee (x \wedge z)$, $y \vee z \le (x \wedge y) \vee (x \wedge z)$, $x \wedge (y \vee z) \le x \wedge y$ or $x \wedge (y \vee z) \le x \wedge z$, and the clauses refute each of them in turn.
So the distributive law is not an identity of all lattices.

## Explanations

### L1 human

Two lattice formulas, such as $x \wedge (y \vee x)$ and $x$, may look different but always give the same value.
This theorem gives a mechanical test for when this happens.
To compare two formulas, look at their outermost operations and reduce the question to smaller comparisons, until only letters are left.

### L2 human

The word problem asks whether two terms define the same element of a free algebra.
For finitely presented groups it can be undecidable, but for free lattices it has this explicit solution, due to Whitman.
The procedure also decides whether a lattice identity holds in all lattices.
Indeed, $s = t$ holds in every lattice exactly when $s = t$ in the free lattice on the letters of $s$ and $t$.
Whitman also used these rules to show that each element of $\mathrm{FL}(X)$ has a canonical form: a shortest term, unique up to commutativity and associativity.
