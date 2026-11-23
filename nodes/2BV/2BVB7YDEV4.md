---
tag: 2BVB7YDEV4
kind: example
name: The Herbrand universe is an absolutely free algebra
msc: ["03B10", "08B20"]
topics: [NJDME6F845]
audience: ug2
instance_of: [TTTEV3NWWM]
uses: [NFW38QJ3A7, TTTEV3NWWM, 3YYKGWJJND, VZ21F10WRS, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Start with $L = \{ a, g \}$, where $a$ is a constant and $g$ is binary, and the algebra $\mathcal{A} = (\mathbb{N}, 1, +)$, where $a$ means $1$ and $g$ means addition.
Each closed term gets a value in $\mathcal{A}$:
$$a \mapsto 1, \qquad g(a, a) \mapsto 2, \qquad g(a, g(a, a)) \mapsto 3, \qquad g(g(a, a), a) \mapsto 3.$$
This value map is the only map from the closed terms to $\mathcal{A}$ that respects $a$ and $g$, and the general claim says that this happens for every algebra.

Let $L$ be a signature with at least one constant symbol and no relation symbols, and let $H(L)$ be its [[Herbrand universe|NFW38QJ3A7]].
Make $H(L)$ an $L$-algebra: a constant $c$ denotes the term $c$, and an $n$-ary function symbol $f$ acts by $(t_1, \ldots, t_n) \mapsto f(t_1, \ldots, t_n)$.
We show that this algebra is the [[absolutely free algebra|TTTEV3NWWM]] on the empty set of generators: for every $L$-algebra $\mathcal{A}$, there is exactly one homomorphism $H(L) \to \mathcal{A}$.

1. Existence.
   Let $h(t) = t^{\mathcal{A}}$, the value of the closed term $t$ in $\mathcal{A}$.
2. By the recursive definition of the value of a term, $h(c) = c^{\mathcal{A}}$ and $h(f(t_1, \ldots, t_n)) = f^{\mathcal{A}}(h(t_1), \ldots, h(t_n))$.
   These two equations say that $h$ is a homomorphism.
3. Uniqueness.
   Let $g \colon H(L) \to \mathcal{A}$ be any homomorphism.
   We show $g(t) = h(t)$ for every closed term $t$, by [[structural induction|12MQ2NJ29A]] on $t$.
4. For a constant $c$, we get $g(c) = c^{\mathcal{A}} = h(c)$, because a homomorphism preserves constants.
5. For $t = f(t_1, \ldots, t_n)$, we get $g(t) = f^{\mathcal{A}}(g(t_1), \ldots, g(t_n))$, because $g$ preserves $f$.
   By the induction hypothesis, this equals $f^{\mathcal{A}}(h(t_1), \ldots, h(t_n)) = h(t)$.

So $H(L)$ is the [[term algebra|3YYKGWJJND]] on no variables, and it is unique up to isomorphism among $L$-algebras with this property.

## Remarks

The example shows the algebraic side of the Herbrand universe: the closed terms form the most general algebra of the signature, and every other algebra is reached from it in exactly one way, by evaluation.
In the opening computation the map counts the occurrences of $a$, and two different terms have the value $3$.
So the homomorphism need not be injective; freeness is a property of $H(L)$, not of the maps out of it.

For $L = \{ 0, s \}$, the initial algebra is $(\mathbb{N}, 0, n \mapsto n + 1)$ up to isomorphism.
The unique homomorphism to an algebra $(A, a, f)$ is $n \mapsto f^n(a)$, and this is definition by recursion on $\mathbb{N}$.

For $L = \{ 0, 1, + \}$, the algebra $(\mathbb{N}, 0, 1, +)$ is not free, because the two different terms $1 + 1$ and $(0 + 1) + 1$ get the same value.
This is why [[Herbrand's theorem|VZ21F10WRS]] works with the terms themselves and not with their values.

## Explanations

### L1 human

The closed terms of a language form the most general algebra for that language.
No two different terms are forced to be equal.
Any other algebra for the language is reached from it in exactly one way: evaluate each term.

### L2 human

The typical use is to define a function on all closed terms by giving its values on the symbols.
For example, to count the occurrences of $g$ in a term of $L = \{ a, g \}$, take the algebra $(\mathbb{N}, 0, (m, n) \mapsto m + n + 1)$.
The unique homomorphism sends $a$ to $0$, and $g(a, a)$ to $0 + 0 + 1 = 1$, and $g(a, g(a, a))$ to $0 + 1 + 1 = 2$.
Freeness guarantees that this recursion defines exactly one function.
Watch out: the same recipe fails on an algebra that is not free, because there one element can have two different descriptions that lead to two different values.
