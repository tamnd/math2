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

Let L be the [[Hilbert system|ET1HPME8VV]] over the connectives $\neg$ and $\to$, with three axiom schemas and [[modus ponens|0Y0MQYST0M]]:
$$\begin{aligned} &\text{A1: } \varphi \to (\psi \to \varphi), \\ &\text{A2: } (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \\ &\text{A3: } (\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi). \end{aligned}$$
We check the four conditions of a [[Frege system|J2BAR09TPF]] one at a time.

1. *A finite complete basis.*
   The set $\{ \neg, \to \}$ is finite, and it is [[functionally complete|FPJFV3R8QP]].
2. *Schematic rules.*
   Each of A1, A2 and A3 is a rule with $k = 0$ premises once the Greek letters are read as propositional variables.
   Modus ponens is the rule $p, \ p \to q \,/\, q$ with $k = 2$, and an axiom of L is then a substitution instance of a schema.
3. *Soundness.*
   Each axiom is a tautology.
   For A1, the formula is false only if $\varphi$ is true and $\psi \to \varphi$ is false, and the second needs $\varphi$ false.
   A2 passes the same kind of check on its $8$ rows and A3 on its $4$ rows, and modus ponens is sound by the truth table of $\to$.
4. *Implicational completeness.*
   Let $\psi_1, \dots, \psi_m \models \chi$.
   Then $\theta = \psi_1 \to (\psi_2 \to \dots (\psi_m \to \chi) \dots)$ is a tautology, so the [[completeness theorem|81ZNY1XKYJ]] for L gives an L-proof of $\theta$.
   Write the hypotheses $\psi_1, \dots, \psi_m$ after it and apply modus ponens $m$ times, peeling one hypothesis at each step, to reach $\chi$.

So L is a Frege system.

## Remarks

Step 4 shows a general fact.
A sound system with modus ponens over a functionally complete basis is implicationally complete as soon as it proves every tautology.
The deduction theorem is not needed for this direction, only modus ponens.

The argument says nothing about short proofs.
The usual proof of the completeness theorem, by Kalmár's method, builds a case for each of the $2^n$ assignments of $n$ variables, so the proof of $\theta$ that it gives can be exponentially long.
Short proofs are a separate question, and by [[Reckhow's theorem|YAHHWZ7XRH]] the answer for L is the same, up to a polynomial, as for every other Frege system.

What if you drop A3?
Then the system is still sound, but it cannot prove $\neg \neg p \to p$, so step 4 fails, and the remaining system is not a Frege system.

## Explanations

### L1 human

The three axioms and modus ponens of a first logic course form a Frege system.
The axioms are patterns with letters, and each pattern stands for infinitely many axioms.
For example, $p \to (q \to p)$ and $\neg r \to ((s \to r) \to \neg r)$ are both instances of A1.

### L2 human

We derive $q$ from the hypotheses $p$ and $p \to q$ by the method of step 4.

1. Since $p, p \to q \models q$, the formula $\theta = p \to ((p \to q) \to q)$ is a tautology.
2. The completeness theorem gives an L-proof of $\theta$.
3. Write the hypothesis $p$ and apply modus ponens to get $(p \to q) \to q$.
4. Write the hypothesis $p \to q$ and apply modus ponens to get $q$.

The typical use of the example is to read results about Frege systems as results about the Hilbert systems of textbooks.
Watch out: implicational completeness asks for derivations from hypotheses, not only for proofs of tautologies, and for L the two agree only because of step 4.
