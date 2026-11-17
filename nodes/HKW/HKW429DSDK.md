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

Let $L$ be a signature with at least one constant symbol, and let $H(L)$ be its [[Herbrand universe|NFW38QJ3A7]], the set of closed terms.
A Herbrand structure for $L$ is an $L$-[[structure|983GZBQYT4]] $\mathcal{H}$ with domain $H(L)$ in which each constant symbol and each function symbol denotes itself: $c^{\mathcal{H}} = c$ and $f^{\mathcal{H}}(t_1, \ldots, t_n) = f(t_1, \ldots, t_n)$.
The relation symbols may be interpreted freely, so a Herbrand structure is determined by the set of closed atomic formulas that it makes true, a subset of the Herbrand base.
A Herbrand model of a set $\Sigma$ of sentences is a Herbrand structure that is a model of $\Sigma$.
Herbrand structures matter because a set of universal sentences without equality has a model if and only if it has a [[Herbrand model|B9C9NTWHZJ]], which reduces satisfiability to questions about closed terms.

## Motivation

A structure is a set together with meanings for the symbols, and in general the set has nothing to do with the language.
Herbrand's idea is to build a structure from the language itself: the elements are the closed terms, and each term denotes itself.
Then the value of a closed term is the term, and the only freedom left is which closed atoms are true.
For universal sentences this freedom is enough, and the problem of finding a model becomes a problem about sets of ground atoms.
This is the semantic basis of [[Herbrand's theorem|VZ21F10WRS]], of resolution theorem proving and of the semantics of logic programs.

## Notation

A Herbrand structure is often identified with a subset $I \subseteq B(L)$ of the Herbrand base, called a Herbrand interpretation: $R(t_1, \ldots, t_n)$ is true if and only if it lies in $I$.
The terms "Herbrand structure", "Herbrand interpretation" and "term model" are used with small differences; "term model" also names the structure of the Henkin construction, which is a quotient of the set of terms.
This page leaves out the equality symbol, or interprets it as identity of terms.

## Remarks

### Examples

1. [[The Herbrand models of a recursive pair of clauses|FHCDYBZPHC]]: for $\Sigma = \set{P(0), \forall x \, (P(x) \to P(s(s(x))))}$ in $L = \set{0, s, P}$, the Herbrand models are the sets $I$ that contain every $P(s^{2n}(0))$, and the least one contains exactly these atoms.
2. [[A Herbrand model built from a finite model|73MVVFTCY7]]: from the two-element model $(\set{0, 1}, a = 0, f(n) = 1 - n, R = \neq)$ of $\set{\forall x \, R(x, f(x)), \forall x \, \neg R(x, x)}$, the Herbrand structure with $R(f^m(a), f^n(a))$ true exactly when $m + n$ is odd is a model.
3. For $L = \set{a, b, P}$ with constants only, there are $4$ Herbrand structures, one for each subset of $\set{P(a), P(b)}$.
4. For $L = \set{0, s}$ with no relation symbols, there is exactly one Herbrand structure, a copy of $(\N, 0, n \mapsto n + 1)$.

### Non-examples

1. [[A satisfiable set without a Herbrand model|3MKF3CSB9E]]: $\set{\exists x \, P(x), \neg P(c)}$ in $L = \set{c, P}$ has the model $(\set{0, 1}, c = 0, P = \set{1})$, but no Herbrand model. The condition that fails is universality: $\exists x \, P(x)$ is not universal.
2. The structure $(\N, 0, n \mapsto n + 1)$ for $L = \set{0, s}$ is not a Herbrand structure: the condition that fails is that its elements are numbers, not terms. It is isomorphic to the Herbrand structure, by the evaluation map.
3. The structure with domain $H(\set{0, s})$ and $s$ interpreted as the identity map is not a Herbrand structure: the condition that fails is that $s(0)$ must denote the term $s(0)$, and here it denotes $0$.

### Basic properties

1. In a Herbrand structure $\mathcal{H}$, every closed term denotes itself: $t^{\mathcal{H}} = t$, by induction on $t$.
2. For a term $t$ with variables and an assignment $s$ in $\mathcal{H}$, $t^{\mathcal{H}}[s]$ is the closed term obtained from $t$ by replacing each variable $x$ by $s(x)$.
3. A Herbrand structure satisfies a universal sentence $\forall x_1 \cdots \forall x_n \, \varphi$, with $\varphi$ quantifier-free, if and only if it satisfies every ground instance $\varphi[t_1/x_1, \ldots, t_n/x_n]$ with $t_i \in H(L)$.
4. A set of universal sentences without equality has a model if and only if it has a Herbrand model. This is the [[theorem on Herbrand models|B9C9NTWHZJ]].
5. A set of definite Horn clauses always has a least Herbrand model: the intersection of all its Herbrand models.

### History

Jacques Herbrand used structures built from terms in his 1930 thesis, in the proof of the theorem that now bears his name.
Van Emden and Kowalski showed in 1976 that the meaning of a logic program is its least Herbrand model, and this made Herbrand models central in logic programming.

### Common errors

- Assuming that every satisfiable set has a Herbrand model. This holds for universal sentences without equality, and fails for $\set{\exists x \, P(x), \neg P(c)}$ and for $\set{c = d}$.
- Treating equality as a free relation. In a Herbrand structure, $c = d$ is false for distinct constant symbols $c$ and $d$, because $=$ means identity of terms.
- Forgetting the constant symbol. Without one, $H(L)$ is empty, and there is no Herbrand structure until a constant is added.

## Explanations

### L1 human

A Herbrand structure is a world made of names.
Each object of the world is a name, such as $0$ or $s(s(0))$, and each name stands for itself.
The only thing left to decide is which basic statements about names are true, such as "$P(s(0))$".
For rules of the form "for all $x$, ..." without "there exists", a world of names is always enough, if any world works at all.

### L2 human

We compute the value of a term with variables in a Herbrand structure for $L = \set{a, f, g}$.
Let $t = g(x, f(y))$ and let $s(x) = f(a)$ and $s(y) = a$.

1. $x^{\mathcal{H}}[s] = f(a)$ and $y^{\mathcal{H}}[s] = a$, by the clause for variables.
2. $f(y)^{\mathcal{H}}[s] = f^{\mathcal{H}}(a) = f(a)$, because $f$ denotes the term-building map.
3. $t^{\mathcal{H}}[s] = g^{\mathcal{H}}(f(a), f(a)) = g(f(a), f(a))$.

So the value is the term $t$ with $x$ and $y$ replaced by $f(a)$ and $a$.
The typical use is to reduce a universal sentence to its ground instances.
A trap is to evaluate $g(f(a), f(a))$ further; in a Herbrand structure it is already a final value.

### L3 human

Herbrand structures are the free structures of the signature: every $L$-structure $\mathcal{M}$ receives a unique map $t \mapsto t^{\mathcal{M}}$ from $H(L)$ that preserves constants and functions.
Universal sentences without equality are preserved under substructures, and the image of this map is a substructure of $\mathcal{M}$; the Herbrand model is the pullback of that image.
With equality, the right replacement is a quotient of $H(L)$ by a congruence, as in the Henkin construction of the completeness proof.
Herbrand's theorem combines the Herbrand model theorem with compactness: a universal sentence is unsatisfiable if and only if finitely many of its ground instances are propositionally unsatisfiable.
