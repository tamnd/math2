---
tag: BDAZGNZBJ5
kind: example
name: The Hilbert system L is a Frege system
msc: ["03F20", "03B05"]
topics: [CBAF7J051K]
audience: research
instance_of: [J2BAR09TPF]
uses: [ET1HPME8VV, 81ZNY1XKYJ, FPJFV3R8QP, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

Let L be the [[Hilbert system|ET1HPME8VV]] with connectives $\neg$ and $\to$, axiom schemas A1, A2, A3 and the rule [[modus ponens|0Y0MQYST0M]].
We check the four conditions of a [[Frege system|J2BAR09TPF]].

1. *Finite basis.* The set $\set{\neg, \to}$ is finite, and it is [[functionally complete|FPJFV3R8QP]].
2. *Schematic rules.* Each of A1, A2, A3 is a rule with $k = 0$ premises, and modus ponens is the rule $\dfrac{p \quad p \to q}{q}$ with $k = 2$. The Greek letters of the schemas become propositional variables, and an axiom instance is a substitution instance.
3. *Soundness.* A1, A2 and A3 are tautologies, by a check of their truth tables. Modus ponens is sound, since every assignment that makes $p$ and $p \to q$ true makes $q$ true.
4. *Implicational completeness.* Let $\psi_1, \dots, \psi_m \models \chi$. Then the formula $\theta = \psi_1 \to (\psi_2 \to \cdots (\psi_m \to \chi) \cdots)$ is a tautology. By the [[completeness theorem|81ZNY1XKYJ]] for L, there is an L-proof of $\theta$. Add the hypotheses $\psi_1, \dots, \psi_m$ and apply modus ponens $m$ times. This gives an L-derivation of $\chi$ from $\psi_1, \dots, \psi_m$.

So L is a Frege system.

## Remarks

Step 4 shows a general fact.
A sound system with modus ponens over a functionally complete basis is implicationally complete as soon as it proves every tautology.
The deduction theorem is not needed for this direction.

The completeness theorem gives a proof of $\theta$, but its proof by Kalmár's method has about $2^n$ cases for $n$ variables.
So this argument says nothing about short proofs.
By [[Reckhow's theorem|YAHHWZ7XRH]], L is p-equivalent to every other Frege system.

## Explanations

### L1 human

The three axioms and modus ponens of a first logic course form a Frege system.
The axioms are patterns with letters, and each pattern gives many axioms.
For example, $p \to (q \to p)$ and $(r \land s) \to (\neg r \to (r \land s))$ are both instances of A1 after the connectives are written out.

### L2 human

We derive $q$ from the hypotheses $p$ and $p \to q$ by the method of step 4.

1. $p, p \to q \models q$, so $\theta = p \to ((p \to q) \to q)$ is a tautology.
2. The completeness theorem gives an L-proof of $\theta$.
3. Add the hypothesis $p$ and apply modus ponens: this gives $(p \to q) \to q$.
4. Add the hypothesis $p \to q$ and apply modus ponens: this gives $q$.

The typical use of the example is to read results about Frege systems as results about textbook Hilbert systems.
A trap: implicational completeness needs derivations from hypotheses, not only proofs of tautologies.
For L the two agree, by the argument of step 4.
