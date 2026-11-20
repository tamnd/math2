---
tag: J2GTJ8FKF2
kind: statement
role: theorem
name: Algebraic completeness of classical propositional logic
aliases: [algebraic-completeness-classical-logic, boolean-completeness-propositional-logic]
msc: ["03G05", "03B05"]
topics: [QYA4H5Y7VR]
audience: grad
about: [QC9M3Q8B8Q, 09K9MWD2QQ]
uses: [JVZ8APEV7A, 0XADJKM699, 0WG43AC0EV, CQM84EW10G]
proofs: [H9KKH3C52K]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "5. The algebraic counterparts of classical and intuitionistic logic"
  - book: isbn:9780387905785
---

## Statement

Let $F$ be the set of formulas in $\neg$ and $\to$ over a nonempty set $P$ of variables, and let $\vdash$ be derivability in [[L|1MGMQX43B8]].
For a [[Boolean algebra|0XADJKM699]] $B$, a *$B$-valuation* is a map $v \colon F \to B$ with $v(\neg \varphi) = \neg v(\varphi)$ and $v(\varphi \to \psi) = \neg v(\varphi) \lor v(\psi)$.
Let $\mathbf{2}$ be the [[two-element Boolean algebra|0WG43AC0EV]].

**Theorem.** For $T \subseteq F$ and $\varphi \in F$, these three conditions are equivalent.

1. $T \vdash \varphi$.
2. For every Boolean algebra $B$ and every $B$-valuation $v$ with $v(T) \subseteq \set{1}$, $v(\varphi) = 1$.
3. For every $\mathbf{2}$-valuation $v$ with $v(T) \subseteq \set{1}$, $v(\varphi) = 1$.

## Remarks

### Why each hypothesis is needed

1. The proof of 3 implies 1 needs an [[ultrafilter|CQM84EW10G]] of the Lindenbaum-Tarski algebra of $T$ that omits $[\varphi]$.
   This is an instance of the [[ultrafilter lemma|3MKZST79MK]], which is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]].
   For finite $P$ the algebra is finite, and no choice principle is needed.
2. The valuations must respect the connectives. A map that sends $p$, $\neg p$ and $p \to p$ to $0$ in $\mathbf{2}$ is not a valuation, and it refutes the theorem $p \to p$.
3. The algebras must be Boolean. In the three-element [[Heyting algebra|NG943XNQWH]] the provable formula $p \lor \neg p$ can take a value below $1$; see [[this non-example|YBT5KSQ2GC]].

### Consequences

1. With $T = \emptyset$, condition 3 says that $\varphi$ is a tautology, so this is the [[completeness theorem for propositional logic|81ZNY1XKYJ]].
2. The equations true in all Boolean algebras are the equations true in $\mathbf{2}$.
   So $\mathbf{2}$ generates the variety of Boolean algebras.
3. Compactness: if $T \vdash \varphi$, then a finite part of $T$ derives $\varphi$, because derivations are finite.
   So condition 3 for $T$ implies condition 3 for some finite subset of $T$.
4. The same ultrafilter argument embeds every Boolean algebra into a power set algebra; this is [[Stone's representation theorem|S4QJ395PA5]].

### Converse

The direction from 1 to 2 is soundness, and it is part of the theorem.
Each condition is equivalent to each other one, so there is no further converse.

### Generalizations

1. Intuitionistic logic is complete for [[Heyting algebras|NG943XNQWH]]; see [[the Heyting semantics theorem|JM1XJXWZYH]].
   No finite Heyting algebra suffices for it.
2. A normal modal logic is complete for its variety of modal algebras; see [[this theorem|Z0S91AK9WG]].
3. Infinite-valued Łukasiewicz logic is complete for MV-algebras and already for $[0, 1]$; see [[Chang's completeness theorem|QM0F33QE9P]].

## Explanations

### L1 human

The theorem says that a formula can be proved exactly when it is always true.
"Always true" means: true for every choice of true and false for its letters.
To show that a formula with no proof is not always true, the proof builds one row of the truth table where the formula is false.
For example, $p \to q$ has no proof, and the row $p$ true, $q$ false makes it false.

### L2 human

1. Take $\varphi = p \to q$ and $T = \emptyset$.
2. In the Lindenbaum-Tarski algebra, $[p \to q] \ne 1$, since $p \to q$ is not a theorem.
3. Its complement is $\neg[p \to q] = [p] \land [\neg q]$.
4. The set $U$ of classes above $[p] \land [\neg q]$ is an ultrafilter, because $[p] \land [\neg q]$ is an atom.
5. The homomorphism $\chi_U$ to $\mathbf{2}$ sends $[p]$ to $1$ and $[q]$ to $0$.
6. So the valuation $p \mapsto 1$, $q \mapsto 0$ gives $p \to q$ the value $0$.

The typical use: one proves completeness for a class of algebras by a quotient and a homomorphism.
The trap: a filter that is not an ultrafilter does not give a homomorphism to $\mathbf{2}$.

### L3 human

The proof has two parts that recur in [[algebraic logic|Z3DE4R4RET]].
The first part says that the logic is complete for the class of all its Lindenbaum-Tarski algebras, which is formal.
The second part reduces that class to simple members, here to $\mathbf{2}$ by the ultrafilter lemma.
In universal algebra terms, the second part says that every Boolean algebra is a subdirect product of copies of $\mathbf{2}$.
In model theory terms, it is the propositional case of the Henkin construction.
