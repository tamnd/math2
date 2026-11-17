---
tag: 2BVB7YDEV4
kind: example
name: The Herbrand universe is an absolutely free algebra
msc: ["03B10", "08B20"]
topics: [NJDME6F845]
audience: ug2
instance_of: [TTTEV3NWWM]
uses: [~b97c4e92, TTTEV3NWWM, 3YYKGWJJND, VZ21F10WRS, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Let $L$ be a signature with at least one constant symbol and no relation symbols, and let $H(L)$ be its [[Herbrand universe|~b97c4e92]], the set of closed terms of $L$.
Make $H(L)$ an $L$-algebra: a constant $c$ denotes the term $c$, and an $n$-ary function symbol $f$ acts by $(t_1, \ldots, t_n) \mapsto f(t_1, \ldots, t_n)$.
We show that this algebra is the [[absolutely free algebra|TTTEV3NWWM]] on the empty set of generators: for every $L$-algebra $\mathcal{A}$, there is exactly one homomorphism $H(L) \to \mathcal{A}$.

1. Existence: let $h(t) = t^{\mathcal{A}}$, the value of the closed term $t$ in $\mathcal{A}$.
2. By the recursive definition of term values, $h(c) = c^{\mathcal{A}}$ and $h(f(t_1, \ldots, t_n)) = f^{\mathcal{A}}(h(t_1), \ldots, h(t_n))$.
3. So $h$ is a homomorphism.
4. Uniqueness: let $g \colon H(L) \to \mathcal{A}$ be a homomorphism. We show $g(t) = h(t)$ by [[structural induction|12MQ2NJ29A]] on $t$.
5. For a constant, $g(c) = c^{\mathcal{A}} = h(c)$, because $g$ preserves constants.
6. For $t = f(t_1, \ldots, t_n)$, $g(t) = f^{\mathcal{A}}(g(t_1), \ldots, g(t_n))$, because $g$ preserves $f$.
7. By the induction hypothesis, this is $f^{\mathcal{A}}(h(t_1), \ldots, h(t_n)) = h(t)$.

So $H(L)$ is the [[term algebra|3YYKGWJJND]] on no variables, and it is unique up to isomorphism among $L$-algebras with this property.

## Remarks

The example shows the algebraic side of the Herbrand universe: a closed term is the same thing as an element of the initial algebra.
For $L = \set{0, s}$, the initial algebra is $(\N, 0, n \mapsto n + 1)$ up to isomorphism, and the unique homomorphism to an algebra $(A, a, f)$ is $n \mapsto f^n(a)$; this is definition by recursion.
For $L = \set{0, 1, +}$, the algebra $(\N, 0, 1, +)$ is not free, because $1 + 1$ and $(0 + 1) + 1$ are different terms with the same value.
This is why [[Herbrand's theorem|VZ21F10WRS]] works with terms and not with their values.

## Explanations

### L1 human

The closed terms of a language form the most general algebra for that language.
Any other algebra for the language is reached from it in exactly one way: evaluate each term.
No two different terms are forced to be equal.

### L2 human

We compute the unique homomorphism $h \colon H(L) \to \mathcal{A}$ for $L = \set{a, g}$ with $g$ binary and $\mathcal{A} = (\N, 1, +)$.

1. $h(a) = 1$.
2. $h(g(a, a)) = 1 + 1 = 2$.
3. $h(g(a, g(a, a))) = 1 + 2 = 3$, and $h(g(g(a, a), a)) = 2 + 1 = 3$.

So $h$ counts the occurrences of $a$, and different terms can have the same image.
The typical use is to define a function on terms by giving its values on the symbols.
A trap is to think that $h$ is injective; the freeness is a property of $H(L)$, not of the map to $\mathcal{A}$.
