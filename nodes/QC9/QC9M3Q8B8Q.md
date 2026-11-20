---
tag: QC9M3Q8B8Q
kind: concept
name: Lindenbaum–Tarski algebra
aliases: [lindenbaum-tarski-algebra, lindenbaum-algebra]
msc: ["03G05", "03B05"]
topics: [QYA4H5Y7VR]
audience: grad
uses: [1MGMQX43B8, 0XADJKM699, 0G8VEZ3WTK, DCSXXT4SER]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "5. The algebraic counterparts of classical and intuitionistic logic"
  - url: https://en.wikipedia.org/wiki/Leibniz_operator
    locator: Formulation
same_as:
  wikidata: Q841805
  wikipedia: Lindenbaum–Tarski algebra
---

## Summary

Let $\Gamma$ be a set of formulas of classical propositional logic over a nonempty set $P$ of variables.
Put $\varphi \sim_\Gamma \psi$ iff $\Gamma \vdash \varphi \to \psi$ and $\Gamma \vdash \psi \to \varphi$.
The *Lindenbaum-Tarski algebra* of $\Gamma$ is the set of classes $[\varphi]$ of this [[equivalence relation|0G8VEZ3WTK]], with $\neg [\varphi] = [\neg \varphi]$, $[\varphi] \to [\psi] = [\varphi \to \psi]$, and $\land$, $\lor$, $0$, $1$ induced by the defined connectives; see [[the definition|MGCVQXXQJH]].
It is a [[Boolean algebra|0XADJKM699]], and for $\Gamma = \emptyset$ it is the free Boolean algebra on the classes of the variables, by [[this theorem|~b1e6292b]].
It matters because it is the bridge from proofs to algebra: completeness theorems become statements about homomorphisms out of this algebra.

## Motivation

The formulas $p \land q$ and $q \land p$ are different strings, but every proof treats them in the same way.
Identifying provably equivalent formulas removes this difference, and the connectives then act on the classes.
The result satisfies the laws of the intended algebras of the logic, because each law corresponds to a provable equivalence.
A formula that is not provable gives a class different from $1$, and a homomorphism to the two-element algebra that sends this class to $0$ is a countermodel.
This is [[the algebraic completeness proof|~ca5a7c20]].

## Notation

We write $[\varphi]$ or $[\varphi]_\Gamma$ for the class of $\varphi$, and $\mathbf{L}_\Gamma$ or $\mathbf{Fm}/{\sim_\Gamma}$ for the algebra.
The order is $[\varphi] \le [\psi]$ iff $\Gamma \vdash \varphi \to \psi$.
In this sub-area the base calculus is the [[Hilbert system L|1MGMQX43B8]] with $\neg$ and $\to$, and $\varphi \lor \psi := \neg \varphi \to \psi$, $\varphi \land \psi := \neg(\varphi \to \neg \psi)$.
Some texts call it the Lindenbaum algebra.

## Remarks

### Examples

1. One variable, $\Gamma = \emptyset$: the classes are $[p \land \neg p]$, $[p]$, $[\neg p]$, $[p \lor \neg p]$, so the algebra has four elements and two atoms.
2. [[Two variables, empty theory|~7674071f]]: sixteen classes, one for each Boolean function of two arguments.
3. [[Two variables and the theory $\set{p}$|~1d3a2c08]]: four classes, because $p$ becomes equal to $1$.
4. Intuitionistic logic: the same construction gives a [[Heyting algebra|NG943XNQWH]], used in the [[algebraic completeness proof for intuitionistic logic|RQ0C4BC1KS]].
5. A normal modal logic gives a modal algebra; see [[the algebraic completeness of normal modal logics|~b53b6d4a]].

### Non-examples

1. [[The formula algebra|~a5ffa607]] without the quotient: $p \land q \ne q \land p$ as terms, so $\land$ is not commutative.
2. The quotient by equality of truth value under one fixed valuation is the two-element algebra, not the Lindenbaum-Tarski algebra; it collapses classes that the logic separates, such as $[p]$ and $[q]$ when $p$ and $q$ get the same value.

### Basic properties

1. The relation $\sim_\Gamma$ is a [[congruence|DCSXXT4SER]] of the formula algebra, and the quotient is a Boolean algebra, by [[this theorem|~b1e6292b]].
2. $[\varphi] = 1$ iff $\Gamma \vdash \varphi$.
3. $\Gamma$ is consistent iff $0 \ne 1$ in its algebra.
4. For $\Gamma = \emptyset$ the algebra is free on $\set{[p] : p \in P}$, again by [[this theorem|~b1e6292b]].
5. For finitely many variables $p_1, \dots, p_n$ and $\Gamma = \emptyset$, the algebra has $2^{2^n}$ elements; this uses [[the completeness theorem|~ca5a7c20]] to separate the classes.

### History

Lindenbaum used the method in Łukasiewicz's logic seminar from the academic year 1926 to 1927.
Tarski later made the method widely known and extended it to other logics.
The Leibniz operator of abstract algebraic logic extends the same quotient construction to arbitrary logics.

### Common errors

1. Forgetting the theory. The algebra depends on $\Gamma$: adding $p$ to $\Gamma$ merges $[p]$ with $1$.
2. Claiming that the algebra is finite for every set of variables. With infinitely many variables it is infinite, and with countably many variables it is the countable atomless Boolean algebra.
3. Proving that the quotient is a Boolean algebra by the completeness theorem and then deducing completeness from the quotient. That argument is circular; [[the proof|~40619dba]] uses only derivations in L.

## Explanations

### L1 human

Two sentences can look different and still say the same thing, such as "it rains and it is cold" and "it is cold and it rains".
The Lindenbaum-Tarski algebra puts all sentences that the logic proves equivalent into one box.
Each box is one element, and "and", "or" and "not" act on the boxes.
With one letter $p$ there are exactly four boxes: the box of $p$, of "not $p$", of "always true" and of "always false".
With two letters there are sixteen boxes.

### L2 human

A worked example with one variable and the theory $\Gamma = \emptyset$.

1. Every formula in $p$ alone has one of four truth tables, given by its values at $p = 0$ and $p = 1$.
2. Formulas with the same truth table are provably equivalent, by the [[completeness theorem|81ZNY1XKYJ]] applied to $\varphi \to \psi$ and $\psi \to \varphi$.
3. Formulas with different truth tables are not provably equivalent, by [[soundness|XD629S54CS]].
4. So there are four classes, $0 = [\neg(p \to p)]$, $[p]$, $[\neg p]$ and $1 = [p \to p]$.
5. The order is $0 < [p], [\neg p] < 1$, and $[p] \land [\neg p] = 0$, $[p] \lor [\neg p] = 1$.

The typical use is in completeness proofs: one works in the Lindenbaum-Tarski algebra and then maps it to a simpler algebra.
The trap: the order $[\varphi] \le [\psi]$ is defined by $\Gamma \vdash \varphi \to \psi$, not by "$\varphi$ is a subformula of $\psi$".

### L3 human

The construction works for any logic with a well-behaved equivalence, and it is the model of the Leibniz congruence: the largest congruence of the formula algebra compatible with a theory.
For classical, intuitionistic and normal modal logics, the Lindenbaum-Tarski algebras of all theories are exactly the algebras of the logic, up to isomorphism, when the set of variables is large enough, which is the start of [[algebraizability|~d9ad8170]].
In categorical logic the same algebra appears as the poset reflection of the syntactic category of the logic.
For first-order logic, the quotient keeps the quantifiers as operators and gives a [[cylindric algebra|1MDT9BF81H]] or a [[polyadic algebra|~8ae1836e]].
