---
tag: GMSZ75D5WE
kind: statement
role: theorem
name: Peirce's law
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
about: [ZMVBAY7ZZD, 0NMG7W7Q11]
uses: [0NMG7W7Q11, 05006AJ7DZ, H31CS3HK5P, 1MGMQX43B8]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: Failure in non-classical models of intuitionistic logic
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Axiom system
---

## Statement

Peirce's law is a classical law that uses implication only, and it is both true and derivable.

Let $\varphi$ and $\psi$ be propositional formulas.
Peirce's law is the formula
$$((\varphi \to \psi) \to \varphi) \to \varphi.$$

1. It is a [[tautology|05006AJ7DZ]]: for every [[truth assignment|H31CS3HK5P]] $v$, the formula takes the value $1$.
2. It is a theorem of the [[Hilbert system|1MGMQX43B8]] L: $\vdash ((\varphi \to \psi) \to \varphi) \to \varphi$.

## Remarks

### Implication alone, but not intuitionistic

The law contains only the connective [[implication|0NMG7W7Q11]], but it does not follow from the laws of implication that hold in [[intuitionistic logic|Q11N8X99FK]].
Its truth depends on the classical fact that each formula takes the value $0$ or $1$.
The proof is in [[the proof of Peirce's law|1QFGDY6NV9]], and its derivation in L uses the axiom A3 through the law T8.

### Why the classical setting is needed

The statement has no hypotheses on $\varphi$ and $\psi$, but it depends on the two-valued semantics.
Take the three-element [[Heyting algebra|NG943XNQWH]] $0 < \tfrac12 < 1$ with $a \to b = 1$ when $a \le b$, and $a \to b = b$ otherwise.
With $p = \tfrac12$ and $q = 0$ we get
$$p \to q = 0, \qquad (p \to q) \to p = 0 \to \tfrac12 = 1, \qquad ((p \to q) \to p) \to p = 1 \to \tfrac12 = \tfrac12.$$
In this algebra the axioms K, $\varphi \to (\psi \to \varphi)$, and S, $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$, always take the value $1$.
Also [[modus ponens|0Y0MQYST0M]] preserves the value $1$.
So Peirce's law is not derivable from K and S with modus ponens, and it is not a theorem of intuitionistic logic.

### What it gives you

Adding Peirce's law to K and S, with modus ponens, gives the [[implicational propositional calculus|ZMVBAY7ZZD]].
That system derives exactly the tautologies that use only $\to$, so Peirce's law plays the role that excluded middle plays in systems with negation.
Over intuitionistic logic, adding Peirce's law as an axiom schema gives classical logic.
With $\psi := \bot$ and $\neg \varphi$ read as $\varphi \to \bot$, the law becomes $(\neg \varphi \to \varphi) \to \varphi$, called consequentia mirabilis.
A worked use is [[the derivation that uses Peirce's law|GEQWJPR0ZV]].

### The converse

The converse $\varphi \to ((\varphi \to \psi) \to \varphi)$ is also a theorem of L, since it is the instance of A1 with $\varphi \to \psi$ in the place of the second letter.
So $(\varphi \to \psi) \to \varphi$ and $\varphi$ are logically equivalent, for all formulas $\varphi$ and $\psi$.
The converse holds in intuitionistic logic too, since A1 does.

### Generalizations

Peirce's law holds in every [[Boolean algebra|0XADJKM699]], with $a \to b = \neg a \lor b$, because Boolean algebras validate exactly the classical tautologies.
A Heyting algebra in which Peirce's law holds for all elements is a Boolean algebra.

### Watch out

A formula with only $\to$ need not be intuitionistically valid.
Peirce's law is the standard counterexample, and the Heyting algebra above shows the failure with $p = \tfrac12$, $q = 0$.

## History

The law is named after Charles Sanders Peirce, who stated it in his work on the algebra of logic.
There it is the fifth of his basic "icons", and he tied it to the principle of excluded middle.

## Explanations

### L1 human

Peirce's law says: if "$p$ implies $q$" implies $p$, then $p$ is true.
A check by cases shows why.
If $p$ is true, there is nothing to show.
If $p$ is false, then "$p$ implies $q$" is true, so the assumption "($p$ implies $q$) implies $p$" would make $p$ true, which is not the case.
So the assumption is false, and the whole implication is true.

### L2 human

We fill in the truth table for $p$ and $q$.

1. $v(p) = 1$, $v(q) = 1$: $v(p \to q) = 1$, $v((p \to q) \to p) = 1$, and the law has value $1 \to 1 = 1$.
2. $v(p) = 1$, $v(q) = 0$: $v(p \to q) = 0$, $v((p \to q) \to p) = 1$, and the law has value $1 \to 1 = 1$.
3. $v(p) = 0$, $v(q) = 1$: $v(p \to q) = 1$, $v((p \to q) \to p) = 0$, and the law has value $0 \to 0 = 1$.
4. $v(p) = 0$, $v(q) = 0$: $v(p \to q) = 1$, $v((p \to q) \to p) = 0$, and the law has value $0 \to 0 = 1$.

The typical use is in implication-only logic, where the law does the work of excluded middle in proofs by cases.
The table also shows where the third value breaks it: rows 3 and 4 need $p$ to be exactly $0$ or exactly $1$.

### L3 human

Peirce's law marks the line between classical and intuitionistic implication.
Under the Curry-Howard correspondence, intuitionistic proofs are typed lambda terms, and Peirce's law has no closed term in the simply typed lambda calculus.
Its proof terms appear with control operators such as call/cc, which is how classical logic enters computation.
The countermodel in the three-element Heyting algebra is also a model of the Gödel logics in [[many-valued logic|66NMTCQNQV]], where the same failure occurs.
