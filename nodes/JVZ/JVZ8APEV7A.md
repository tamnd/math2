---
tag: JVZ8APEV7A
kind: statement
role: theorem
name: The Lindenbaum-Tarski algebra of classical logic is a free Boolean algebra
aliases: [lindenbaum-tarski-algebra-is-boolean, lindenbaum-algebra-free-boolean-algebra]
msc: ["03G05", "03B05", "06E05"]
topics: [QYA4H5Y7VR]
audience: grad
about: [QC9M3Q8B8Q]
uses: [MGCVQXXQJH, 1MGMQX43B8, 0XADJKM699, DCSXXT4SER, 1MF0TVHDZD]
proofs: [TW6DDQ57CW]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "5. The algebraic counterparts of classical and intuitionistic logic"
  - book: isbn:9780387905785
---

## Statement

Let $P$ be a nonempty set of variables, and let $F$ be the set of formulas over $P$ in $\neg$ and $\to$.
Let $\vdash$ be derivability in the [[Hilbert system L|1MGMQX43B8]].
Let $T \subseteq F$, and let $\mathbf{L}_T = F/{\sim_T}$ be its [[Lindenbaum-Tarski algebra|MGCVQXXQJH]].

**Theorem.**

1. The relation $\sim_T$ is a [[congruence|DCSXXT4SER]] of the formula algebra $\langle F, \neg, \to \rangle$.
2. With $[\varphi] \le [\psi]$ iff $T \vdash \varphi \to \psi$, the quotient is a [[Boolean algebra|0XADJKM699]].
   Its meet, join and complement are $[\varphi \land \psi]$, $[\varphi \lor \psi]$ and $[\neg \varphi]$.
3. Its top is $1 = [\top]$, its bottom is $0 = [\bot]$, and $[\varphi] = 1$ iff $T \vdash \varphi$.
4. For $T = \emptyset$, the algebra $\mathbf{L}_\emptyset$ is [[free|1MF0TVHDZD]] over the map $p \mapsto [p]$.
   So for each Boolean algebra $B$ and each map $f \colon P \to B$, there is exactly one homomorphism $h \colon \mathbf{L}_\emptyset \to B$ with $h([p]) = f(p)$.

## Remarks

### Why each hypothesis is needed

1. The quotient is needed: on the formula algebra itself, $p \land q$ and $q \land p$ are different elements, so meet is not commutative; see [[this non-example|S563QJHDTK]].
2. The calculus must be classical. For the Hilbert system of intuitionistic logic, the law $\neg \neg p \to p$ is not derivable.
   The quotient is then a [[Heyting algebra|NG943XNQWH]] in which $[\neg \neg p] \ne [p]$, so it is not Boolean.
3. Part 4 needs $T = \emptyset$. For $T = \set{p}$, the map $p \mapsto 0$ into the two-element algebra has no extension, because $[p] = 1$ must go to $1$.

### Consequences

1. The theorem gives [[the algebraic completeness theorem|J2GTJ8FKF2]]: with an ultrafilter, an unprovable formula is refuted in the two-element algebra.
2. Each Boolean algebra $B$ is a quotient of some $\mathbf{L}_\emptyset$: take $P = B$ and $f = \mathrm{id}_B$.
3. For $n$ variables, completeness gives $|\mathbf{L}_\emptyset| = 2^{2^n}$; see [[the two-variable example|A7CTMV6M39]].

### Converse

Every Boolean algebra is isomorphic to $\mathbf{L}_T$ for some $T$.
Take $P = B$, $f = \mathrm{id}_B$, and let $T$ be the set of formulas $\varphi$ with $h([\varphi]) = 1$.
The map $h$ is onto, and $h([\varphi]) = h([\psi])$ iff $T \vdash \varphi \to \psi$ and $T \vdash \psi \to \varphi$.
So $\mathbf{L}_T \cong B$, and the Lindenbaum-Tarski algebras are, up to isomorphism, all the Boolean algebras.

### Generalizations

1. For intuitionistic logic, the same construction gives the free Heyting algebra; see [[the Heyting semantics proof|RQ0C4BC1KS]].
2. For a normal modal logic, it gives the free modal algebra of the corresponding variety; see [[this theorem|Z0S91AK9WG]].
3. For an [[algebraizable logic|CESWST3NWA]], the quotient of the formula algebra by the Leibniz congruence of each theory lies in the equivalent algebraic semantics.

## History

Lindenbaum used the quotient of formulas by provable equivalence in Łukasiewicz's seminar from 1926 to 1927.
Tarski later developed the method, and the algebra carries both names.

## Explanations

### L1 human

Group the formulas so that two formulas are in one group when the logic proves that each gives the other.
The theorem says that these groups behave like sets under union, intersection and complement.
For one letter $p$ there are four groups, like the four subsets of a two-element set.
The theorem also says that the groups of the letters are as independent as possible.

### L2 human

1. Take $P = \set{p, q}$ and $f(p) = \set{1}$, $f(q) = \set{2}$ in the power set of $\set{1, 2}$.
2. The homomorphism of part 4 sends $[p \land q]$ to $\set{1} \cap \set{2} = \emptyset$.
3. It sends $[p \lor q]$ to $\set{1, 2}$, and $[p \to q]$ to $\set{2} \cup \set{2} = \set{2}$.
4. It sends $[\neg p]$ to $\set{2}$.
5. So $[p \to q]$ and $[\neg p]$ have the same image, but they are different classes in $\mathbf{L}_\emptyset$.

The typical use is to compute values of formulas in any Boolean algebra by one homomorphism.
The trap: a homomorphism can merge classes, so equal images do not mean provably equivalent formulas.

### L3 human

The theorem says that the Boolean algebras form the [[variety|AJNZJD8442]] that corresponds to classical propositional logic.
The free algebra of a variety is the term algebra modulo the equations of the variety, and here the equations come from provable equivalences.
This is the first case of the correspondence between logics and classes of algebras that [[algebraic logic|Z3DE4R4RET]] studies.
