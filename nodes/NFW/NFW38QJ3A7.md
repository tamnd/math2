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

The Herbrand universe of a language is the set of everything the language can name without variables.
Take a constant $0$ and a unary function symbol $s$: the names are $0$, $s(0)$, $s(s(0))$, and so on, and these strings themselves are the elements.
In exact terms, let $L$ be a [[signature|WDVVEYD6AT]] with at least one constant symbol; if $L$ has none, we first add one new constant symbol $c_0$.
The Herbrand universe $H(L)$ is the set of closed [[terms|6D3WA7N2W4]] of $L$, the terms that contain no variable.
It is the smallest set that contains every constant symbol of $L$ and contains $f(t_1, \ldots, t_n)$ whenever $f$ is an $n$-ary function symbol and $t_1, \ldots, t_n \in H(L)$.
The Herbrand base $B(L)$ is the set of closed atomic formulas $R(t_1, \ldots, t_n)$, with $R$ a relation symbol of $L$ and $t_1, \ldots, t_n \in H(L)$.
The [[formal definition|JKP0XNXRPB]] builds $H(L)$ level by level.

## Motivation

To show that a set of sentences has a model, we must find a domain for the model.
A signature gives us no objects at all, only symbols, and the only things it can point to are its closed terms.
Herbrand's idea was to use these names as the objects.
For universal sentences without equality, this idea always works: such a set has a model if and only if it has a model whose domain is $H(L)$.

So the search for a model becomes a search among the ground instances of the sentences, which are formulas of propositional logic in disguise.
This is the basis of [[Herbrand's theorem|VZ21F10WRS]] and of [[resolution|ZDW6N1PGJ7]] theorem proving.
The structures built on $H(L)$ are the [[Herbrand structures|HKW429DSDK]], and the theorem on their models is [[universal sentences have Herbrand models|B9C9NTWHZJ]].

## Notation

Books write $H(L)$, $H_L$, $U_L$ or $\mathcal{U}$, and some say "Herbrand domain".
The Herbrand base is written $B(L)$, $B_L$ or $\mathcal{B}$.
Closed terms are also called ground terms, and closed atomic formulas are called ground atoms.
The Herbrand base never contains equations, because the equality symbol is a logical symbol and not a relation symbol of $L$.
Watch the notation $s^n(0)$: it is a string with $n$ copies of $s$, not the number $n$.

## Remarks

### Building the universe level by level

Start with $L = \{ a, f, g \}$, where $a$ is a constant, $f$ is unary and $g$ is binary.
Level $0$ holds only the constant:
$$H_0 = \{ a \}.$$
Level $1$ adds $f(t)$ and $g(t, u)$ for all $t, u \in H_0$:
$$H_1 = \{ a, \ f(a), \ g(a, a) \}.$$
Level $2$ applies the symbols to all of $H_1$, so it holds $a$, the $3$ terms $f(t)$ and the $3 \cdot 3 = 9$ terms $g(t, u)$ with $t, u \in H_1$:
$$|H_2| = 1 + 3 + 9 = 13.$$
Check: $H_1 \subseteq H_2$, because $f(a)$ and $g(a, a)$ appear again among the new terms.
The universe is the union $H_0 \subseteq H_1 \subseteq H_2 \subseteq \cdots$, and every closed term of height $k$ lies in $H_k$.

### Three small universes

With [[one constant and one unary function symbol|7XKWHMNGQH]], $L = \{ 0, s \}$, the universe is $\{ s^n(0) : n \in \mathbb{N} \}$, a copy of the natural numbers.
With [[one constant and one binary function symbol|3B4C9Q5K2H]], $L = \{ a, g \}$, the closed terms are the full binary trees, and the number of terms with $n$ occurrences of $g$ is the Catalan number $C_n$: $1, 1, 2, 5, 14, \ldots$.
With two constants and no function symbols, $L = \{ a, b \}$, the universe is the finite set $\{ a, b \}$.

The base depends on the relation symbols.
For $L = \{ 0, s, P \}$ with $P$ unary, the Herbrand base is $\{ P(0), P(s(0)), P(s(s(0))), \ldots \}$.
A choice of true atoms in it is the same thing as a subset of $\mathbb{N}$.

### What is not a Herbrand universe

[[A signature without constant symbols|5Y0RH5JH4T]], such as $L = \{ f, P \}$, has no closed terms at all, since every term contains a variable.
The empty set cannot be the domain of a structure, and that is why the definition adds a constant $c_0$ first.
The term $s(x)$ is not an element of $H(\{ 0, s \})$, because it contains the variable $x$.
For $L = \{ 0, 1, + \}$, the set $\mathbb{N}$ is not $H(L)$: the terms $1 + 1$ and $(0 + 1) + 1$ are two different elements of $H(L)$, though both have the value $2$ in the natural numbers.

### The rules you can use

The set $H(L)$ is nonempty, by the convention on constants.
When $L$ has finitely many constants, $H(L)$ is finite exactly when $L$ has no function symbol of arity $1$ or more, because one such symbol $f$ already gives the infinite chain $a, f(a), f(f(a)), \ldots$.
It is countable when $L$ is countable, since each $H_k$ is then countable.

Each element of $H(L)$ is either a constant symbol or $f(t_1, \ldots, t_n)$ for exactly one $f$ and one tuple of closed terms, by the unique readability of terms.
So $H(L)$, with the maps $(t_1, \ldots, t_n) \mapsto f(t_1, \ldots, t_n)$, is the [[term algebra|3YYKGWJJND]] on no variables, the [[absolutely free algebra|TTTEV3NWWM]] on no generators.
[[The worked example|2BVB7YDEV4]] proves this.
For every structure $\mathcal{M}$, the evaluation map $t \mapsto t^{\mathcal{M}}$ is the unique map $H(L) \to M$ that sends $c$ to $c^{\mathcal{M}}$ and $f(t_1, \ldots, t_n)$ to $f^{\mathcal{M}}(t_1^{\mathcal{M}}, \ldots, t_n^{\mathcal{M}})$.

### Watch out

A closed term is not its value.
In $H(\{ 0, 1, + \})$, the terms $1 + 1$ and $(0 + 1) + 1$ are distinct, even though every structure that reads $+$ as addition gives them the same value.

Do not forget the mixed terms when you build a level.
Applying $g$ only to the newest terms of $H_1$ misses $g(a, f(a))$, which has one old argument and one new one.

Do not put relation symbols into the universe.
$P(0)$ is an element of the base $B(L)$, a formula, and not an element of $H(L)$.

### History

Jacques Herbrand worked with the domain of terms in his 1930 thesis, "Recherches sur la théorie de la démonstration", in the proof of the result now called Herbrand's theorem.
The name "Herbrand universe" is standard in automated theorem proving, where resolution, introduced by John Alan Robinson in 1965, builds on Herbrand's theorem.

### Try it

List $H_2$ for $L = \{ a, f \}$ with $f$ unary.
The answer is $\{ a, f(a), f(f(a)) \}$, and in general $H_k$ has $k + 1$ elements.

How many elements does $H_2$ have for $L = \{ a, g \}$ with $g$ binary?
Here $H_1 = \{ a, g(a, a) \}$, so $H_2$ holds $a$ and the $2 \cdot 2 = 4$ terms $g(t, u)$ with $t, u \in H_1$, which makes $5$.

## Explanations

### L1 human

The Herbrand universe is the list of all objects that a language can name without variables.
Start from the names of the constants, and apply the function symbols again and again.
With a name $0$ and a "next" symbol $s$, the list is $0$, $s(0)$, $s(s(0))$, and so on.
The objects of the universe are these names themselves, not the numbers that the names might stand for.
So $s(s(0))$ is a string of symbols, and only a structure can decide that it means $2$.

### L2 human

Here is a typical use: list the ground instances of the universal sentence $\forall x \, (P(x) \to P(s(x)))$ for $L = \{ 0, s, P \}$.
The universe is $\{ s^n(0) : n \in \mathbb{N} \}$, so we put each closed term in place of $x$:
$$P(0) \to P(s(0)), \qquad P(s(0)) \to P(s^2(0)), \qquad P(s^2(0)) \to P(s^3(0)), \qquad \ldots$$
Each instance is a formula without variables, and its atoms are elements of the base $B(L)$.
If we read each atom as a propositional variable, the instances become an infinite set of propositional formulas.
This is how Herbrand's method turns a first-order question into a propositional one.
Watch out: the instances use the terms, not numbers, so $P(s^2(0))$ is an atom of the base and not a statement about the number $2$.

### L3 human

When $L$ has no relation symbols, $H(L)$ is the [[initial algebra|R76EC56V9R]] of the signature: every $L$-algebra receives exactly one homomorphism from it.
For an equational theory $E$, the initial model of $E$ is the quotient of $H(L)$ by the congruence of equations that $E$ proves, and this is the semantics of abstract data types.
Herbrand's theorem reduces the unsatisfiability of a universal sentence to the propositional unsatisfiability of finitely many of its instances over $H(L)$.
Since these instances can be listed one by one, first-order validity is semi-decidable, which is the starting point of the sub-areas on proof systems and on completeness.
