---
tag: 8R31F7BQGY
kind: statement
role: theorem
name: Realizing types
aliases: [realizing-types-in-elementary-extensions]
msc: ["03C07", "03C50"]
topics: [Z772KEC9BY]
audience: grad
about: [9V71Q3SD1G, CGH8C8EA9N]
uses: [9V71Q3SD1G, VA7AK1R5AN, 8WZF9SBP39, 1NR3HAWG9D, 0G0ASKNA6Z]
history:
  notes: "The result is a direct consequence of the compactness theorem, which Gödel obtained for countable languages in 1930 and Maltsev extended to arbitrary languages in 1936."
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
    locator: Definitions
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Statement

Let $\mathcal{M}$ be an $L$-structure with domain $M$.
For each $i$ in an index set $I$, let $A_i \subseteq M$ and let $p_i(\bar{x}_i)$ be a set of $L_{A_i}$-formulas in finitely many free variables.
Assume that each $p_i$ is *finitely satisfiable in $\mathcal{M}$*: every finite subset of $p_i$ is satisfied by some tuple of $\mathcal{M}$.
Then there is an elementary extension $\mathcal{N} \succeq \mathcal{M}$ and, for each $i \in I$, a tuple $\bar{b}_i$ of $\mathcal{N}$ that realizes $p_i$.
The extension can be chosen with $\abs{N} \le \abs{M} + \abs{L} + \abs{I} + \aleph_0$.

In particular, every [[type|9V71Q3SD1G]] over a set $A \subseteq M$ is realized in some [[elementary extension|8WZF9SBP39]] of $\mathcal{M}$.

## Remarks

### Why each hypothesis is needed

- Finite satisfiability in $\mathcal{M}$ cannot be weakened to consistency with the theory of $\mathcal{M}$ without parameters: $\set{0 < x, \; x < 1}$ is not realized in any elementary extension of $(\Z, <)$; see [[a set that is a type in one order and not in another|FQXCHW7DDG]].
- Each $p_i$ gets its own tuple $\bar{b}_i$. One tuple cannot realize $p_1 \cup p_2$ unless this union is finitely satisfiable, as for $p_1 = \set{x < 0}$ and $p_2 = \set{x > 0}$.
- The word "elementary" matters: an extension that is only a superstructure need not keep the truths of $\mathcal{M}$, and then the types over $A$ lose their meaning.

### Consequences

- Every structure $\mathcal{M}$ has an elementary extension that realizes every complete type over $M$, of size at most $2^{\abs{M} + \abs{L} + \aleph_0}$; this is the first step of the [[existence of saturated models|GSQ833HAZT]].
- An infinite structure has a proper elementary extension: realize $\set{x \ne m : m \in M}$.
- The theory of $(\N, 0, 1, +, \cdot, <)$ has a nonstandard model: realize the [[type of an infinite natural number|Q0H5CJGCAY]].

### Converse

The converse holds.
If $\mathcal{N} \succeq \mathcal{M}$ realizes $p$ and $q \subseteq p$ is finite, then $\mathcal{N} \models \exists \bar{x} \bigwedge q$.
This is an $L_A$-sentence, so $\mathcal{M} \models \exists \bar{x} \bigwedge q$ by elementarity, and $q$ is satisfied in $\mathcal{M}$.
So the types over $A$ are exactly the sets of $L_A$-formulas that are realized in elementary extensions of $\mathcal{M}$.

### Generalizations

A single type over $M$ is also realized in an ultrapower of $\mathcal{M}$, and every type over a countable set is realized in each countably incomplete ultrapower; see [[saturation of ultraproducts|DYXQP8WS63]].
Iterating the theorem along a chain gives $\kappa^+$-saturated elementary extensions.

## History

The result is a direct consequence of the [[compactness theorem|1NR3HAWG9D]].
Gödel obtained compactness for countable languages in 1930, and Maltsev extended it to arbitrary languages in 1936.

## Explanations

### L1 human

Suppose a list of wishes about an element is such that every finite part of the list can be met inside a structure.
The theorem says that the structure can be enlarged, without changing any of its first-order truths, so that one new element meets the whole list.
For example, the rational numbers can be enlarged to an ordered set with an element above every integer.

### L2 human

We realize $p(x) = \set{x > n : n \in \Z}$ over $A = \Z$ in an elementary extension of $\mathcal{M} = (\Q, <)$.

1. A finite subset of $p$ mentions finitely many integers, and their maximum plus $1$ satisfies it in $\Q$.
2. So $p$ is finitely satisfiable in $\mathcal{M}$, and the theorem gives $\mathcal{N} \succeq \mathcal{M}$ with an element $b$ above all integers.
3. The extension $\mathcal{N}$ is still a dense linear order without endpoints, since these axioms are true in $\mathcal{M}$.

The typical use is to add an element with prescribed first-order properties while keeping the theory.
The trap is to ask for an extension of $\mathcal{M}$ that is not elementary: then the new structure may lose properties such as density.

### L3 human

In topological terms, a type over $A$ is a point or a closed set of the [[Stone space|VDY4PG5WHN]] $S_n(A)$, and the theorem says that every point is realized somewhere.
The models that realize every type over every small set inside themselves are the [[saturated models|RMTZ5J64FX]].
The same compactness argument with an ultrafilter gives the ultrapower version, and with a chain it gives the [[monster model|EYTTQZ0E1S]] used in stability theory.
