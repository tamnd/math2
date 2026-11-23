---
tag: JAKSE2A1D4
kind: definition
name: Herbrand structure
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
defines: HKW429DSDK
uses: [JKP0XNXRPB, Y6C40MHZZC, CWQV9PTCB3]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Definition

A Herbrand structure is a structure whose elements are the closed terms of the language, with each constant and function symbol read as itself.

Let $L$ be a signature with at least one constant symbol, and let $H(L)$ and $B(L)$ be its [[Herbrand universe and Herbrand base|JKP0XNXRPB]].
A Herbrand structure for $L$ is an $L$-[[structure|Y6C40MHZZC]] $\mathcal{H}$ such that:

1. the domain of $\mathcal{H}$ is $H(L)$;
2. $c^{\mathcal{H}} = c$ for every constant symbol $c$ of $L$;
3. $f^{\mathcal{H}}(t_1, \ldots, t_n) = f(t_1, \ldots, t_n)$ for every $n$-ary function symbol $f$ of $L$ and all $t_1, \ldots, t_n \in H(L)$.

Each relation symbol $R$ of arity $n$ may have any interpretation $R^{\mathcal{H}} \subseteq H(L)^n$.
For a set $I \subseteq B(L)$, the Herbrand structure $\mathcal{H}_I$ has
$$R^{\mathcal{H}_I} = \{ (t_1, \ldots, t_n) : R(t_1, \ldots, t_n) \in I \}.$$
A Herbrand model of a set $\Sigma$ of $L$-sentences is a Herbrand structure that is a [[model|CWQV9PTCB3]] of $\Sigma$.

## Notation

The set $I$ is called a Herbrand interpretation.
The map $I \mapsto \mathcal{H}_I$ is a bijection from the subsets of $B(L)$ to the Herbrand structures for $L$.

## Remarks

Condition 1 makes the names the objects, and it needs a constant symbol so that $H(L)$ is nonempty.
Conditions 2 and 3 fix the meaning of every constant and function symbol, so two Herbrand structures for $L$ differ only in their relations.
That is why a Herbrand structure is the same thing as a set of ground atoms.

Take $L = \{ a, b, P \}$ with two constants and one unary relation symbol.
Then $H(L) = \{ a, b \}$ and $B(L) = \{ P(a), P(b) \}$, so there are $4$ Herbrand structures.
The structure $\mathcal{H}_I$ with $I = \{ P(a) \}$ is a Herbrand model of $\{ P(a), \neg P(b) \}$, and it is the only one.

A structure with domain $\{ a, b \}$ in which both constants denote $a$ fails condition 2, because $b$ must denote the term $b$.
The equality symbol means identity, as in every structure, so distinct closed terms are never equal in a Herbrand structure.
The concept page [[Herbrand structure|HKW429DSDK]] gives more examples and the main theorem.

## Explanations

### L1 human

Take all the names that the language can form as the objects, and let each name stand for itself.
Then choose which basic facts about the names are true.
Each choice gives one Herbrand structure.

### L2 human

The typical use is to look for a model of a set of clauses among the subsets of $B(L)$.
For $L = \{ a, b, P \}$ and the clauses $P(a) \lor P(b)$ and $\neg P(a)$, test the four subsets:
$$\emptyset, \quad \{ P(a) \}, \quad \{ P(b) \}, \quad \{ P(a), P(b) \}.$$
The first fails $P(a) \lor P(b)$, the second and the fourth fail $\neg P(a)$, and $\{ P(b) \}$ satisfies both.
Watch out: do not let $a$ and $b$ name the same element to save work, because then the structure is not a Herbrand structure.
