---
tag: VZ21F10WRS
kind: statement
role: theorem
name: Herbrand's theorem
msc: [03B10, 03F05, 03B35]
uses: [GCPQGMJYEV, 6D3WA7N2W4, QN7M1JCGT9, WDVVEYD6AT]
about: [QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand's_theorem
same_as:
  wikidata: Q1930577
  wikipedia: Herbrand's theorem
---

## Statement

Consider first-order logic without equality over a [[signature|WDVVEYD6AT]] $\sigma$ with at least one constant symbol.
Let $\varphi = \forall x_1 \cdots \forall x_n \, \psi(x_1, \dots, x_n)$ be a sentence in [[Skolem normal form|GCPQGMJYEV]], with $\psi$ quantifier-free.
Then $\varphi$ is unsatisfiable if and only if there are finitely many tuples $\bar t_1, \dots, \bar t_k$ of closed [[terms|6D3WA7N2W4]] with the following property.
The conjunction $\psi(\bar t_1) \land \cdots \land \psi(\bar t_k)$ is unsatisfiable as a propositional formula, with its atomic sentences read as propositional variables.

## Remarks

The instances $\psi(\bar t)$ with closed terms $\bar t$ are the ground instances of $\varphi$.
For the proof, suppose every finite set of ground instances is propositionally [[satisfiable|QN7M1JCGT9]].
By propositional compactness, all ground instances are satisfiable at once by some assignment.
This assignment defines a Herbrand structure, whose elements are the closed terms, and this structure is a model of $\varphi$.
The other direction holds because $\varphi$ implies each of its ground instances.
Example: let $\varphi = \forall x \, (P(x) \land \neg P(f(x)))$ with a constant $c$.
The instances for $x = c$ and $x = f(c)$ contain $\neg P(f(c))$ and $P(f(c))$, so their conjunction is unsatisfiable, and so is $\varphi$.
If $\sigma$ has no constant symbol, one adds one; without closed terms there are no ground instances.

## Explanations

### L1 human

The theorem reduces a question about all possible structures to a question about finitely many concrete cases.
To show that a universal sentence is contradictory, it is enough to plug in finitely many concrete terms and find a contradiction by truth tables.
This is the basis of many automatic theorem provers.

### L2 human

Combined with Skolemization, the theorem gives a semi-decision procedure for validity in first-order logic.
To test whether $\chi$ is valid, put $\neg \chi$ in Skolem normal form and search through larger and larger sets of ground instances.
If $\chi$ is valid, the search ends; by [[Church's theorem|VA6BNNY2YC]] it cannot always end when $\chi$ is not valid.
The theorem is closely related to the [[compactness theorem|1NR3HAWG9D]] and to [[Gödel's completeness theorem|WQ1ZE255SF]].
With equality, the same holds after adding the equality axioms for $\sigma$ to $\varphi$.
