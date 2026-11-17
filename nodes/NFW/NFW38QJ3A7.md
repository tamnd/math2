---
tag: NFW38QJ3A7
kind: concept
name: Herbrand universe
msc: ["03B10", "08B20"]
topics: [NJDME6F845]
audience: ug2
specializes: [3YYKGWJJND]
uses: [6D3WA7N2W4, WDVVEYD6AT, 3YYKGWJJND, TTTEV3NWWM]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: lead section
---

## Summary

Let $L$ be a [[signature|WDVVEYD6AT]] with at least one constant symbol; if $L$ has none, we add one constant symbol $c_0$ first.
The Herbrand universe $H(L)$ of $L$ is the set of closed [[terms|6D3WA7N2W4]] of $L$, the terms that contain no variables.
It is the smallest set that contains every constant symbol of $L$ and contains $f(t_1, \ldots, t_n)$ whenever $f$ is an $n$-ary function symbol and $t_1, \ldots, t_n \in H(L)$.
The Herbrand base $B(L)$ is the set of closed atomic formulas $R(t_1, \ldots, t_n)$ with $R$ a relation symbol of $L$ and $t_1, \ldots, t_n \in H(L)$.
The Herbrand universe is the domain of the [[Herbrand structures|HKW429DSDK]], and through them it reduces questions about all structures to questions about terms.

## Motivation

To find a model of a set of sentences, we need some domain to start from.
The only objects that a signature itself provides are the things it can name: the closed terms.
Herbrand's idea was to use the names as the objects.
For universal sentences without equality this is enough: such a set has a model if and only if it has a model whose domain is $H(L)$.
This turns the search for a model into a search over the ground instances of the sentences, which is the basis of [[Herbrand's theorem|VZ21F10WRS]] and of resolution theorem proving.

## Notation

Common symbols are $H(L)$, $H_L$, $U_L$ and $\mathcal{U}$; some books say "Herbrand domain".
The Herbrand base is written $B(L)$, $B_L$ or $\mathcal{B}$.
Closed terms are also called ground terms, and closed atomic formulas are called ground atoms.
The Herbrand base never contains equations: the equality symbol is left out, or $L$ is assumed to have no equality.

## Remarks

### Examples

1. [[One constant and one unary function symbol|7XKWHMNGQH]]: for $L = \set{0, s}$, $H(L) = \set{0, s(0), s(s(0)), \ldots}$, a copy of $\N$.
2. [[One constant and one binary function symbol|3B4C9Q5K2H]]: for $L = \set{a, g}$, the closed terms correspond to the full binary trees, and the number of terms with $n$ occurrences of $g$ is the $n$-th Catalan number.
3. For $L = \set{a, b}$ with two constants and no function symbols, $H(L) = \set{a, b}$ is finite.
4. For $L = \set{a, f, g}$ with $f$ and $g$ unary, the closed terms are the words over $\set{f, g}$ applied to $a$, so there are $2^n$ terms of depth $n$.
5. For $L = \set{0, s, P}$ with $P$ unary, the Herbrand base is $\set{P(0), P(s(0)), P(s(s(0))), \ldots}$.

### Non-examples

1. [[A signature without constants|5Y0RH5JH4T]], such as $L = \set{f, P}$: the condition that fails is the existence of a closed term, so the set of closed terms is empty; adding a constant repairs this.
2. The term $s(x)$ is not in $H(\set{0, s})$: the condition that fails is that it contains the variable $x$.
3. For $L = \set{0, 1, +}$, the set $\N$ is not $H(L)$: the elements of $H(L)$ are terms, and $1 + 1$ and $(0 + 1) + 1$ are different terms with the same value $2$.

### Basic properties

1. $H(L)$ is nonempty, by the convention on constants.
2. $H(L)$ is finite if and only if $L$ has no function symbol of arity at least $1$. It is countable when $L$ is countable.
3. Each element of $H(L)$ is either a constant symbol or $f(t_1, \ldots, t_n)$ for exactly one $f$ and one tuple $(t_1, \ldots, t_n)$, by unique readability of terms.
4. With the operations $(t_1, \ldots, t_n) \mapsto f(t_1, \ldots, t_n)$, the set $H(L)$ is the [[term algebra|3YYKGWJJND]] on no variables, the [[absolutely free algebra|TTTEV3NWWM]] on no generators; see the [[worked example|2BVB7YDEV4]].
5. For every $L$-structure $\mathcal{M}$, the evaluation map $t \mapsto t^{\mathcal{M}}$ is the unique map $H(L) \to M$ that sends $c$ to $c^{\mathcal{M}}$ and $f(t_1, \ldots, t_n)$ to $f^{\mathcal{M}}(t_1^{\mathcal{M}}, \ldots, t_n^{\mathcal{M}})$.

### History

Jacques Herbrand introduced the domain of terms in his 1930 thesis, "Recherches sur la théorie de la démonstration", in the proof of the result now called Herbrand's theorem.
The name "Herbrand universe" became standard in automated theorem proving, for example in the 1965 paper of John Alan Robinson that introduced resolution.

### Common errors

- Identifying a closed term with its value. In $H(L)$, the terms $1 + 1$ and $2$ are different elements, even when a structure gives them the same value.
- Forgetting the constant. Without a constant symbol, a signature has no closed terms, and $H(L)$ would be empty.
- Putting equations into the Herbrand base. Herbrand structures interpret equality as identity of terms, so the equations are not free to choose.

## Explanations

### L1 human

The Herbrand universe is the list of all objects that a language can name without variables.
Start from the names of constants, and apply the function symbols again and again.
With a name $0$ and a "next" symbol $s$, the list is $0$, $s(0)$, $s(s(0))$, and so on.
The objects of the universe are these names themselves, not the numbers that they might stand for.

### L2 human

We list the first levels of $H(L)$ for $L = \set{a, f, g}$, with $f$ unary and $g$ binary.

1. Level $0$: $H_0 = \set{a}$.
2. Level $1$: add $f(t)$ and $g(t, u)$ for $t, u \in H_0$. So $H_1 = \set{a, f(a), g(a, a)}$.
3. Level $2$: $H_2 = \set{a} \cup \set{f(t) : t \in H_1} \cup \set{g(t, u) : t, u \in H_1}$, with $1 + 3 + 9 = 13$ elements.

The universe is the union $H_0 \subseteq H_1 \subseteq H_2 \subseteq \cdots$.
The typical use is to build Herbrand structures and to list the ground instances of a universal sentence.
A trap is to apply the function symbols only to the new terms of the previous level; mixed terms such as $g(a, f(a))$ are also needed.

### L3 human

For a signature with function symbols only, $H(L)$ is the initial object in the category of $L$-algebras: every algebra receives exactly one homomorphism from it.
For an equational theory $E$, the initial model is the quotient of $H(L)$ by the congruence of provable equations; this is the semantics of abstract data types.
Herbrand's theorem reduces the unsatisfiability of a universal sentence to the propositional unsatisfiability of finitely many of its instances over $H(L)$, which makes first-order validity semi-decidable by enumeration of instances.
