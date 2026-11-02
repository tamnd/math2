---
tag: ZV7VGE2SQ2
kind: statement
role: theorem
name: Grothendieck spectral sequence
msc: [18G40, 18G10]
uses: [Y9CZ3MTNF1, KAN07YC9T2, S1G61TDW0K, NPMC3K6J2F, F2CMPBHQ02, 5QRFTBF4PG, GG8AYV847V]
about: [GG8AYV847V, NPMC3K6J2F]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_spectral_sequence
same_as:
  wikidata: Q5610729
  wikipedia: Grothendieck spectral sequence
---

## Statement

Let $\mathcal{A}$, $\mathcal{B}$ and $\mathcal{C}$ be [[abelian categories|Y9CZ3MTNF1]], and assume that $\mathcal{A}$ and $\mathcal{B}$ have enough injectives.
Let $G \colon \mathcal{A} \to \mathcal{B}$ and $F \colon \mathcal{B} \to \mathcal{C}$ be left [[exact|S1G61TDW0K]] [[additive functors|KAN07YC9T2]].
Assume that $G$ sends every [[injective object|5QRFTBF4PG]] of $\mathcal{A}$ to an [[$F$-acyclic object|F2CMPBHQ02]] of $\mathcal{B}$.
Then for every object $X$ of $\mathcal{A}$ there is a first quadrant [[spectral sequence|GG8AYV847V]]
$$E_2^{p,q} = (R^p F)(R^q G)(X) \Longrightarrow R^{p+q}(F \circ G)(X),$$
natural in $X$, where $R^n$ denotes the right [[derived functors|NPMC3K6J2F]].

## Remarks

To prove it, take an injective resolution $X \to I^\bullet$ and a Cartan–Eilenberg resolution of the complex $G(I^\bullet)$.
Apply $F$, and compare the two spectral sequences of the resulting double complex.
Because $G(I^n)$ is $F$-acyclic, one of them collapses and computes $R^n(F \circ G)(X)$; the other has the stated $E_2$ page.
Without the acyclicity hypothesis the derived functor of $F \circ G$ is not computed by this double complex, and the statement can fail.
One example is the [[Leray spectral sequence|8BMQ90EJPR]], where $G = f_*$ for a continuous map $f$ and $F$ is the global sections functor.
Another is the [[Lyndon–Hochschild–Serre spectral sequence|VC3QNG6TKR]], where $G$ and $F$ take invariants under a normal subgroup and under the quotient group.
The low degree terms of the spectral sequence give the exact sequence $0 \to R^1 F(G X) \to R^1(F G)(X) \to F(R^1 G(X)) \to R^2 F(G X) \to R^2(F G)(X)$.

## Explanations

### L1 human

If a functor is done in two steps, its derived functors are related to the derived functors of the two steps.
The relation is not a simple formula but a spectral sequence: a table of groups that, after several corrections, gives the answer.
The one condition is that the first step sends the simple building blocks, the injective objects, to objects that the second step treats as simple.

### L2 human

In practice the theorem is used in low degrees, through the five-term exact sequence.
It is also used when the $E_2$ page vanishes outside one row or column, so that $R^n(F \circ G)$ can be read off directly.
In the language of [[derived categories|5ST7NVJFSM]] it says that $R(F \circ G) \cong RF \circ RG$.
