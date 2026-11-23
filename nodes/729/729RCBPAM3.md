---
tag: 729RCBPAM3
kind: concept
name: Independence of axioms
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
uses: [1MGMQX43B8, 0Y0MQYST0M, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Independence_(mathematical_logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Independence_(mathematical_logic)
    locator: Complete (strong) independence
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Summary

To show that an axiom is really needed, give the symbols a new meaning in which the other axioms stay true and the rules keep truth, but the chosen axiom fails.
For example, read $\neg$ in the system L as "do nothing": then A1 and A2 stay tautologies, but the instance $(\neg q \to \neg q) \to ((\neg q \to q) \to q)$ of A3 becomes $(q \to q) \to ((q \to q) \to q)$, which is $1 \to (1 \to 0) = 0$ at $q = 0$.

Let $S$ be a [[Hilbert system|1MGMQX43B8]] with a set of axiom schemas and a set of rules of inference.
An axiom schema $\alpha$ of $S$ is *independent* when some instance of $\alpha$ is not derivable from the other axiom schemas with the rules of $S$.
A set of schemas is independent when each member is independent of the others.
The *matrix method* proves independence with a set of values $V$, a subset $D \subseteq V$ of designated values, and a function on $V$ for each connective.
Every instance of the other schemas must take a value in $D$ under every assignment, and every rule must lead from values in $D$ to values in $D$.
Then an instance of $\alpha$ that takes a value outside $D$ under some assignment is not derivable from the other schemas.

## Motivation

An axiom list for a logic is a choice, and it is natural to ask whether a shorter list would do.
To show that an axiom is needed, it is not enough to fail to find a derivation of it.
We need a property that all derivations from the other axioms share and that the axiom lacks.
A matrix gives such a property: "always takes a designated value".
Truth tables with two values give soundness, and tables with more values, or with unusual readings of the connectives, separate the axioms from each other.

The same idea, a model of the other axioms in which one statement fails, proves independence results across mathematics, from geometry to set theory.

## Notation

A matrix is written $\mathcal{M} = (V, D, f_\neg, f_\to)$, with the functions $f_\neg : V \to V$ and $f_\to : V \times V \to V$ for the connectives.
An assignment $h$ gives a value in $V$ to each variable, and it extends to all formulas by the functions.
A formula is $\mathcal{M}$-valid when it takes a value in $D$ under every assignment.
Other names for a matrix are logical matrix and characteristic table, and the designated values are also called distinguished values.

## Remarks

### Three matrices for L

In L, A3 is independent of A1 and A2: read $\to$ by the usual truth table and $\neg$ as the identity; see [[the independence of A3|16P6A7750Q]].
A1 is independent of A2 and A3, and A2 is independent of A1 and A3, by two matrices with three values; see [[the independence of A1 and A2|W5AW31K5TA]].
In the first of these, A1 fails at $p = u$, $q = 1$, since $u \to (1 \to u) = u \to 0 = 0$.
[[Peirce's law|GMSZ75D5WE]] is independent of the schemas K and S of the [[implicational propositional calculus|ZMVBAY7ZZD]].
The three-element [[Heyting algebra|NG943XNQWH]] with designated value $1$ validates K and S, and Peirce's law takes the value $\tfrac12$ there.

### Beyond logic

The [[parallel postulate|2PC3XY0PYZ]] is independent of the other axioms of plane geometry, since [[non-Euclidean geometry|SPCYMFN5V2]] gives models of the other axioms in which it fails.
The [[axiom of choice|0HTGB13FE2]] is independent of the axioms of Zermelo-Fraenkel set theory, assuming they are consistent, and so is the [[continuum hypothesis|0MN2MER9WN]].

### What is not independent

Frege's six axioms are not independent, since one of them follows from the others.
If $\varphi \to \varphi$ is added to L as a fourth axiom, the list is not independent, since $\varphi \to \varphi$ is derivable from A1 and A2.
The system with all [[tautologies|05006AJ7DZ]] as axioms is not independent either, since the tautology $p \to p$ is derivable from other tautologies, the instances of A1 and A2.
A matrix in which modus ponens does not preserve the designated values proves nothing: one such matrix validates A1 and A2 but refutes the derivable $p \to p$; see [[this non-example|SHCDQRD4ZK]].

### The rules you can use

The method is correct by induction on the length of a derivation.
If the other axioms are $\mathcal{M}$-valid and each rule preserves $D$, every formula derivable from the other axioms is $\mathcal{M}$-valid, so a schema with a non-valid instance is not derivable.
The two-valued [[truth table|05RSK4Q657]] matrix gives the [[soundness theorem for propositional logic|XD629S54CS]], but it cannot prove the independence of a tautology, since every tautology is valid in it.
Removing a dependent axiom does not change the set of theorems.
Independence of each axiom does not imply completeness, and completeness does not imply independence.

### Watch out

Do not check only the axioms: the matrix must also make each rule preserve the designated values.
Do not check the other axioms only on the old values $0$ and $1$: each must be designated under every assignment, including the new values.
Do not conclude that an axiom is independent because no derivation was found; only a matrix, a model or another proof of non-derivability shows independence.

### History

Łukasiewicz showed that Frege's third axiom is derivable from his other axioms, so Frege's list was not independent.
The parallel postulate is the classical example of an independent axiom, and the non-Euclidean geometries of the nineteenth century gave the models.
Gödel showed in 1938 that the axiom of choice and the continuum hypothesis are consistent with Zermelo-Fraenkel set theory.
Cohen showed in 1963 that their negations are also consistent with it.

### Try it

First, in the matrix with $\neg$ read as the identity, what is the value of $\neg \neg p \to p$?
It is $p \to p = 1$, so this matrix cannot show that $\neg \neg p \to p$ needs A3.

Second, does the matrix with $\neg$ read as the constant $1$ make A3 fail?
Yes: at $\varphi = 1$, $\psi = 0$ the instance is $(1 \to 1) \to ((1 \to 1) \to 0) = 0$.

## Explanations

### L1 human

An axiom is independent when the other axioms cannot prove it.
To show this, we change the meaning of the symbols.
In the new meaning, the other axioms stay always true and the rules keep truth, but the chosen axiom becomes false in some case.
Then the chosen axiom cannot follow from the others, since everything that follows from them stays true.

### L2 human

We show that the formula $\neg \neg p \to p$ is not derivable from A1 and A2 in L.
Read $\to$ by the usual truth table, read $\neg$ as the constant $1$, and take $1$ as the designated value.
A1 and A2 contain no $\neg$, so they are tautologies and always take the value $1$.
Modus ponens preserves the value $1$, by the truth table of $\to$.
At $p = 0$, the formula $\neg \neg p \to p$ takes the value $1 \to 0 = 0$.
So the formula is not derivable from A1 and A2, and every derivation of it in L uses A3.
The typical use of the method is to show that an axiom list is minimal, or that a theorem needs a given axiom.

### L3 human

The matrix method is the propositional case of a general principle.
A statement is independent of a theory when some model of the theory is not a model of the statement.
For a Hilbert system, the "models" are matrices, and the method needs soundness of the rules for the matrix.
In set theory the models are built by forcing and inner models, and in geometry by models of non-Euclidean geometry, but the logic of the argument is the same.

The matrices here are the first examples of [[many-valued logics|66NMTCQNQV]].
A matrix that validates a whole logic shows that a formula outside the logic is not a theorem.
For example, the three-element Heyting algebra validates intuitionistic logic, and Peirce's law fails in it.
