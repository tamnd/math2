---
tag: HKW429DSDK
kind: concept
name: Herbrand structure
aliases: [herbrand-base, herbrand-model, minimal-herbrand-model, term-model]
msc: ["03B10", "68V15"]
topics: [NJDME6F845]
audience: ug2
uses: [NFW38QJ3A7, 983GZBQYT4, 6D3WA7N2W4, 2RBQPV02AS]
sources:
  - wikipedia: en:12274200@r1326042931
    locator: Herbrand structure
    note: adopted
    mention: wikipedia://en/12274200
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: lead section
same_as:
  wikidata: Q1609475
  wikipedia: Herbrand structure
inventory: [K7J082HZ3K]
---

## Summary

A Herbrand structure is a structure made of names: its elements are the closed terms of the language, and each term stands for itself.
For $L = \{ 0, s, P \}$, the elements are $0, s(0), s(s(0)), \ldots$, the symbol $s$ sends $s^n(0)$ to $s^{n+1}(0)$, and the only free choice is which terms satisfy $P$.
In exact terms, let $L$ be a signature with at least one constant symbol, and let $H(L)$ be its [[Herbrand universe|NFW38QJ3A7]].
A Herbrand structure for $L$ is an $L$-[[structure|983GZBQYT4]] $\mathcal{H}$ with domain $H(L)$ such that
$$c^{\mathcal{H}} = c, \qquad f^{\mathcal{H}}(t_1, \ldots, t_n) = f(t_1, \ldots, t_n)$$
for every constant symbol $c$, every $n$-ary function symbol $f$ and all $t_1, \ldots, t_n \in H(L)$.
The relation symbols may be interpreted freely, so a Herbrand structure is fixed by the set of ground atoms that it makes true, a subset of the Herbrand base.
A Herbrand model of a set $\Sigma$ of sentences is a Herbrand structure that is a [[model|MVCH6N9SNW]] of $\Sigma$.
The [[formal definition|JAKSE2A1D4]] states this with the Herbrand base.

## Motivation

In general a structure is a set with meanings for the symbols, and the set has nothing to do with the language.
Herbrand's idea is to build a structure out of the language itself.
Then the value of a closed term is the term, and the only freedom left is which ground atoms are true.

For universal sentences without equality this freedom is enough: such a set has a model if and only if it has a Herbrand model, by the theorem that [[universal sentences have Herbrand models|B9C9NTWHZJ]].
So the problem of finding a model becomes a problem about sets of ground atoms.
This is the semantic basis of [[Herbrand's theorem|VZ21F10WRS]], of [[resolution|ZDW6N1PGJ7]] theorem proving and of the semantics of logic programs.

## Notation

A Herbrand structure is often identified with a set $I \subseteq B(L)$ of ground atoms, called a Herbrand interpretation: the atom $R(t_1, \ldots, t_n)$ is true exactly when it lies in $I$.
We write $\mathcal{H}_I$ for the Herbrand structure of $I$.
The phrase "term model" overlaps with "Herbrand structure", but it also names the structure of the [[Henkin construction|RY8KRKR097]], which is a quotient of a set of terms.
Equality, when it is present, means identity of terms in a Herbrand structure, as it does in every structure.

## Remarks

### A first Herbrand model

Take $L = \{ 0, s, P \}$ and the two sentences
$$P(0), \qquad \forall x \, (P(x) \to P(s(s(x)))).$$
Choose $I = \{ P(0), P(s^2(0)), P(s^4(0)), \ldots \}$, the atoms with an even number of $s$.
The first sentence holds, because $P(0) \in I$.
For the second, give $x$ the value $s^n(0)$; then $s(s(x))$ has the value $s^{n+2}(0)$, and if $n$ is even, so is $n + 2$.
So $\mathcal{H}_I$ is a Herbrand model, and [[the full analysis of these clauses|FHCDYBZPHC]] shows that it is the least one.

The same computation works for every term with variables.
For an assignment $s$ in $\mathcal{H}$, the value $t^{\mathcal{H}}[s]$ is the closed term that we get from $t$ by putting $s(x)$ in place of each variable $x$.
For example, with $s(x) = f(a)$ and $s(y) = a$, the term $g(x, f(y))$ has the value $g(f(a), f(a))$, and that term is already a final value.

### More examples

[[A Herbrand model built from a finite model|73MVVFTCY7]] starts from the two-element model of $\{ \forall x \, R(x, f(x)), \forall x \, \neg R(x, x) \}$ in which $f$ swaps $0$ and $1$.
Copying its true atoms gives the Herbrand model in which $R(f^m(a), f^n(a))$ holds exactly when $m + n$ is odd.

For $L = \{ a, b, P \}$ with constants only, $H(L) = \{ a, b \}$, and there are $4$ Herbrand structures, one for each subset of $\{ P(a), P(b) \}$.
For $L = \{ 0, s \}$ with no relation symbols, there is exactly one Herbrand structure, a copy of $(\mathbb{N}, 0, n \mapsto n + 1)$.

### When no Herbrand model exists

[[A satisfiable set without a Herbrand model|3MKF3CSB9E]] is $\{ \exists x \, P(x), \neg P(c) \}$ in $L = \{ c, P \}$.
It has the model with domain $\{ 0, 1 \}$, $c = 0$ and $P = \{ 1 \}$, but $H(L) = \{ c \}$, and no choice of $P$ on $\{ c \}$ satisfies both sentences.
The condition that fails is universality: the witness $1$ is not the value of any closed term.

Equality gives a second failure.
The set $\{ c = d \}$ has a one-element model, but in every Herbrand structure $c$ and $d$ are two different terms, so $c = d$ is false.

Two structures that look close to Herbrand structures are not.
The structure $(\mathbb{N}, 0, n \mapsto n + 1)$ for $\{ 0, s \}$ has numbers as elements, not terms, though it is isomorphic to the Herbrand structure through the evaluation map.
The structure with domain $H(\{ 0, s \})$ and $s$ read as the identity map fails the condition $s^{\mathcal{H}}(0) = s(0)$, since it sends $0$ to $0$.

### The rules you can use

In a Herbrand structure every closed term denotes itself, $t^{\mathcal{H}} = t$, by induction on $t$.
So a Herbrand structure satisfies a universal sentence $\forall x_1 \cdots \forall x_n \, \varphi$, with $\varphi$ quantifier-free, if and only if it satisfies every ground instance $\varphi[t_1/x_1, \ldots, t_n/x_n]$ with $t_i \in H(L)$.
The reason is that the assignments in $\mathcal{H}$ are exactly the choices of closed terms for the variables.

A set of universal sentences without equality has a model if and only if it has a Herbrand model; this is the [[theorem on Herbrand models|B9C9NTWHZJ]].
A set of definite [[Horn clauses|QR92EZDTKF]] always has a least Herbrand model, the intersection of all its Herbrand models.
The family is never empty, because the whole base $B(L)$ is a Herbrand model of such a set.

### Watch out

Not every satisfiable set has a Herbrand model.
The theorem needs universal sentences without equality, and both $\{ \exists x \, P(x), \neg P(c) \}$ and $\{ c = d \}$ break it.

Equality is not a free relation in a Herbrand structure.
For distinct constant symbols $c$ and $d$, the sentence $c = d$ is false in every Herbrand structure, because $=$ means identity and the terms differ.

Do not forget the constant symbol.
Without one, $H(L)$ is empty, and no Herbrand structure exists until a constant is added.

### History

Jacques Herbrand worked with structures built from terms in his 1930 thesis, in the proof of the theorem that now bears his name.
Maarten van Emden and Robert Kowalski showed in 1976 that the meaning of a logic program is its least Herbrand model, and this made Herbrand models central in logic programming.

### Try it

How many Herbrand structures are there for $L = \{ a, b, R \}$ with $R$ binary?
The base is $\{ R(a, a), R(a, b), R(b, a), R(b, b) \}$, so there are $2^4 = 16$.

Is the Herbrand structure for $\{ 0, s, P \}$ with $I = B(L)$ a model of $\forall x \, (P(x) \to P(s(x)))$?
Yes: every atom is true, so every implication has a true conclusion.

## Explanations

### L1 human

A Herbrand structure is a world made of names.
Each object of the world is a name, such as $0$ or $s(s(0))$, and each name stands for itself.
The only thing left to decide is which basic statements about names are true, such as $P(s(0))$.
For rules of the form "for all $x$, ..." without "there exists" and without "equals", a world of names is always enough, if any world works at all.

### L2 human

Here is a typical problem: does $\Sigma = \{ P(a), \ \forall x \, (P(x) \to Q(f(x))), \ \forall x \, \neg Q(x) \}$ have a model?
All three sentences are universal and have no equality, so it is enough to search the Herbrand structures.
Put the terms $a$ and $f(a)$ in place of $x$ to get three ground instances:
$$P(a), \qquad P(a) \to Q(f(a)), \qquad \neg Q(f(a)).$$
Read as propositional formulas in the atoms $P(a)$ and $Q(f(a))$, they cannot all be true: the first two give $Q(f(a))$, and the third denies it.
So no Herbrand structure is a model, and by the theorem $\Sigma$ has no model at all.
Watch out: this reasoning needs the theorem's hypotheses, and it fails for a set with $\exists$ until the set is Skolemized.

### L3 human

The closed terms form the free structure of the signature: every $L$-structure $\mathcal{M}$ receives a unique map $t \mapsto t^{\mathcal{M}}$ from $H(L)$ that preserves constants and functions.
Its image is the [[substructure|676H7EGTKJ]] of $\mathcal{M}$ generated by the constants, and universal sentences are preserved under substructures.
The Herbrand model of the theorem is the pullback of that image along the evaluation map.
With equality, the right replacement is a quotient of $H(L)$ by a congruence, as in the Henkin construction of the completeness proof.
Herbrand's theorem combines the theorem on Herbrand models with the [[compactness theorem for propositional logic|4X9126SEMM]]: a universal sentence without equality is unsatisfiable if and only if finitely many of its ground instances are propositionally unsatisfiable.
