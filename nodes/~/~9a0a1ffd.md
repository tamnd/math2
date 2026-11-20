---
tag: ~9a0a1ffd
kind: statement
role: theorem
name: Embeddings preserve quantifier-free formulas
aliases: [embeddings-preserve-existential-formulas]
msc: ["03C07", "03C40"]
topics: [AY09KYSW81]
audience: ug2
about: [SCRB74SWQN, 676H7EGTKJ]
uses: [SCRB74SWQN, 676H7EGTKJ, 1WTCZB4DVB, HYJ10AF6RT, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Substructure_(mathematics)
    locator: Submodel
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Statement

Let $\mathcal{M}$ and $\mathcal{N}$ be $L$-structures with domains $M$ and $N$, and let $h \colon M \to N$ be an [[embedding|SCRB74SWQN]].
For a tuple $\bar{a} = (a_1, \dots, a_n)$ in $M$, write $h(\bar{a}) = (h(a_1), \dots, h(a_n))$.
A [[formula|HYJ10AF6RT]] is *quantifier-free* when it has no quantifiers.
It is *existential* when it has the form $\exists y_1 \cdots \exists y_k \, \psi$ with $\psi$ quantifier-free, and *universal* when it has the form $\forall y_1 \cdots \forall y_k \, \psi$ with $\psi$ quantifier-free.
Then the following hold for every tuple $\bar{a}$ in $M$.

1. For every [[term|6D3WA7N2W4]] $t(x_1, \dots, x_n)$: $h(t^{\mathcal{M}}(\bar{a})) = t^{\mathcal{N}}(h(\bar{a}))$.
2. For every quantifier-free formula $\varphi(x_1, \dots, x_n)$: $\mathcal{M} \models \varphi(\bar{a})$ if and only if $\mathcal{N} \models \varphi(h(\bar{a}))$.
3. For every existential formula $\varphi(x_1, \dots, x_n)$: if $\mathcal{M} \models \varphi(\bar{a})$, then $\mathcal{N} \models \varphi(h(\bar{a}))$.
4. For every universal formula $\varphi(x_1, \dots, x_n)$: if $\mathcal{N} \models \varphi(h(\bar{a}))$, then $\mathcal{M} \models \varphi(\bar{a})$.

In particular, let $\mathcal{M} \subseteq \mathcal{N}$ be a [[substructure|676H7EGTKJ]].
Then quantifier-free formulas with parameters in $M$ have the same truth value in $\mathcal{M}$ and in $\mathcal{N}$, existential sentences go up from $\mathcal{M}$ to $\mathcal{N}$, and universal sentences go down from $\mathcal{N}$ to $\mathcal{M}$.

## Remarks

### Why each hypothesis is needed

- Injectivity is needed for part 2. The ring homomorphism $\Z \to \Z/2\Z$ sends $0$ and $2$ to the same element, so the formula $\neg(x = y)$ holds of $(0, 2)$ in $\Z$ and fails of the images.
- Reflection of relations is needed for part 2. For the identity map from the graph with no edge on $\set{1, 2}$ to the graph with one edge, the formula $\neg E(x, y)$ holds of $(1, 2)$ before and fails after; see [[this non-example|~3e0fe003]].
- The quantifier pattern is needed in parts 3 and 4. For the inclusion $(\Z, <) \subseteq (\Q, <)$, the existential formula $\exists z \, (x < z \land z < y)$ holds of $(0, 1)$ in $\Q$ but not in $\Z$, so existential formulas need not go down.
- For the inclusion $(\N, <) \subseteq (\Z, <)$, the universal formula $\forall y \, \neg(y < x)$ holds of $0$ in $\N$ but not in $\Z$, so universal formulas need not go up.

### Consequences

- A substructure of a model of a universal theory is a model of the theory. So subgroups of groups in $\set{\cdot, {}^{-1}, e}$ are groups, and substructures of commutative rings are commutative rings.
- If $\mathcal{M}$ embeds into $\mathcal{N}$ and $\mathcal{M}$ has an element with $\psi(x)$ for a quantifier-free $\psi$, then so does $\mathcal{N}$. For example, a group with an element of order $2$ embeds only into groups with an element of order $2$.
- If $h$ is an isomorphism, then parts 3 and 4 apply to $h$ and to $h^{-1}$, and a further induction gives [[isomorphism invariance of truth|NDTJ2E895C]].
- A field that embeds into an algebraically closed field need not be algebraically closed: the sentence "every monic polynomial of degree $2$ has a root" is not universal.

### Converse

The converse of part 2 holds.
If $h \colon M \to N$ is any map such that every atomic formula $\varphi$ satisfies $\mathcal{M} \models \varphi(\bar{a}) \iff \mathcal{N} \models \varphi(h(\bar{a}))$, then $h$ is an embedding.
The atomic formula $x_1 = x_2$ gives injectivity, $f(x_1, \dots, x_n) = x_{n+1}$ gives the condition for $f$, $c = x_1$ gives the condition for $c$, and $R(x_1, \dots, x_n)$ gives the condition for $R$.
The converse of part 3 for theories is the [[Łoś-Tarski theorem|9RN0KYXNT1]]: a theory whose class of models is closed under substructures is equivalent to a universal theory.

### Generalizations

- A homomorphism preserves every positive existential formula, that is, a formula built from atomic formulas with $\land$, $\lor$ and $\exists$; the proof is the same induction with one direction only.
- An [[elementary embedding|CGH8C8EA9N]] is a map for which part 2 holds for all formulas.
- The same statement holds for many-sorted structures, sort by sort.

## Explanations

### L1 human

An embedding is a faithful copy of one structure inside another.
A statement that talks only about the copied elements and uses no "for all" or "there exists" has the same truth value before and after copying.
For example, $2 + 3 = 5$ is true in the integers, and it stays true in the fractions.
A statement with "there exists" can become true in the bigger structure: no integer lies strictly between $0$ and $1$, but the fraction $1/2$ does.

### L2 human

We test the four parts on the inclusion $h \colon \Z \to \Q$ of rings, with $L = \set{+, -, \cdot, 0, 1}$.

1. Part 1: for the term $t(x) = x \cdot x + 1$ and $a = 3$, $t^{\Z}(3) = 10$ and $t^{\Q}(3) = 10$.
2. Part 2: the formula $x \cdot x = 1 + 1$ fails at every integer and at every rational number.
3. Part 3: the existential formula $\exists y \, (y + y = x)$ holds of $4$ in $\Z$ (with $y = 2$), and so it holds of $4$ in $\Q$.
4. Part 4: the formula $\forall y \, \neg(y + y = x)$ fails of $3$ in $\Q$ (with $y = 3/2$); it holds of $3$ in $\Z$, so universal formulas can fail to go up.

The typical use is to transfer equations and universal axioms between a structure and its substructures.
A trap is to apply part 2 to a formula with a quantifier; the extra elements of $\mathcal{N}$ can change its value.

### L3 human

The theorem places embeddings in a hierarchy of maps: homomorphisms preserve positive existential formulas, embeddings preserve quantifier-free formulas, and elementary embeddings preserve all formulas.
Each preservation result has a converse at the level of theories: Lyndon's theorem for positive formulas and homomorphic images, and the [[Łoś-Tarski theorem|9RN0KYXNT1]] for universal formulas and substructures; they are treated in the sub-area on [[preservation theorems|JYJHB4YBAH]].
Quantifier elimination makes part 2 apply to every formula; so in a theory with quantifier elimination, every embedding between models is elementary.
This is the idea behind model completeness in the sub-area on [[quantifier elimination|1A9JSC5YG8]].
