---
tag: J2BAR09TPF
kind: definition
defines: 1MGMQX43B8
name: Frege system
aliases: [frege-proof-system]
msc: ["03F20", "03B05"]
topics: [CBAF7J051K]
audience: research
uses: [3V24CYWDT6, ET1HPME8VV, TDZVCWYJ9F, 1HK0VYWTV7, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Definition

In a first logic course you prove $p \to p$ in five lines from the axiom schemas A1 and A2 by two uses of modus ponens, as in [[lines and size of a proof of p → p in L|72XT4SG3VZ]].
A Frege system is any proof system of that shape: a finite list of sound schematic rules, strong enough to derive every consequence.

Let $K$ be a finite [[functionally complete|TDZVCWYJ9F]] set of connectives, such as $K = \{ \neg, \land, \lor, \to \}$, and let $\models$ be [[logical consequence|1HK0VYWTV7]] for formulas over $K$.

1. A *Frege rule* is a pair written $\varphi_1, \dots, \varphi_k \,/\, \psi$, with $k \ge 0$ and formulas $\varphi_1, \dots, \varphi_k, \psi$ over $K$.
   A rule with $k = 0$ is an *axiom schema*.
2. An *instance* of the rule is $\varphi_1\sigma, \dots, \varphi_k\sigma \,/\, \psi\sigma$, for one [[substitution|NCDZ969V7X]] $\sigma$ of formulas for variables, applied to all $k + 1$ formulas at once.
3. A rule is *sound* if $\varphi_1, \dots, \varphi_k \models \psi$.
4. A *Frege system* $\mathcal F$ is a finite set of sound Frege rules over $K$ that is *implicationally complete*: whenever $\psi_1, \dots, \psi_m \models \chi$, there is an $\mathcal F$-derivation of $\chi$ from $\psi_1, \dots, \psi_m$.
5. An *$\mathcal F$-derivation* of $\chi$ from $\Gamma$ is a list $\chi_1, \dots, \chi_m = \chi$ in which each $\chi_i$ is in $\Gamma$ or is the conclusion of an instance of a rule whose premises are among $\chi_1, \dots, \chi_{i-1}$.
   An *$\mathcal F$-proof* is a derivation from $\Gamma = \emptyset$.

The *number of lines* of a proof is $m$, and its *size* is $\lvert \chi_1 \rvert + \dots + \lvert \chi_m \rvert$.
A Frege system is a [[propositional proof system|3V24CYWDT6]]: send a correct proof to its last line, and every other string to a fixed tautology.

## Notation

Books write $\mathcal F$, $F$ or $\mathbf{F}$ for a Frege system and $\mathcal F \vdash \tau$ for provability.
The least size of an $\mathcal F$-proof of $\tau$ is $s_{\mathcal F}(\tau)$, and the least number of lines is $k_{\mathcal F}(\tau)$.
In logic the same systems are called [[Hilbert systems|ET1HPME8VV]] or Hilbert-style systems, and "Frege system" is the name used in proof complexity.

## Remarks

### Reading the definition

Each rule is a schema, so one rule covers infinitely many steps.
Modus ponens is the rule $p, \ p \to q \,/\, q$, and its instance under $\sigma(p) = r \land s$, $\sigma(q) = \neg r$ is
$$r \land s, \quad (r \land s) \to \neg r \ / \ \neg r.$$
Checking that a line is an instance is a pattern match against finitely many fixed rules, so a proof is checked in polynomial time.
Soundness makes every provable formula a tautology.
Implicational completeness asks for more than proofs of all tautologies, because it asks for derivations from hypotheses, and the simulations between systems need exactly that.

### Examples

The [[Hilbert system L|BDAZGNZBJ5]], with schemas A1 to A3 and modus ponens over $\{ \neg, \to \}$, is a Frege system.
In it, the [[proof of p → p|72XT4SG3VZ]] has $5$ lines and size $41$, counting variables and connectives.
If you put a formula $\varphi$ of size $s$ for $p$, the same $5$ lines prove $\varphi \to \varphi$ with size $23s + 18$.
So the number of lines can stay fixed while the size grows, and a result must say which of the two it counts.

### What is not a Frege system

[[Resolution is not a Frege system|ZE7RCEAVND]].
It has no axioms, so it proves no formula from no hypotheses, and from $\{p\}$ it cannot derive $\{p, q\}$, so it is not implicationally complete.
The system with only A1, A2 and modus ponens is sound, but it does not prove Peirce's law $((p \to q) \to p) \to p$, so completeness fails.
A system with the rule "from $p \to q$ and $q$ infer $p$" fails soundness, as the [[unsound example|5WQDFMR91G]] shows.

### The rules you can use

All Frege systems are p-equivalent, even over different sets of connectives, by [[Reckhow's theorem|YAHHWZ7XRH]].
So "Frege" names a class, and a bound for one Frege system holds for all of them up to a polynomial.
The propositional sequent calculus with cut and natural deduction are p-equivalent to Frege systems too.
Cut-free sequent calculus is much weaker; see the [[complexity of cut elimination|B5F5HB4YK7]].
[[Extended Frege|5YSE04SHFH]] adds abbreviations and p-simulates every Frege system.

### Where Frege stands

Frege systems prove the [[pigeonhole formulas|RJ571F7FF0]] in polynomial size, by [[Buss's theorem|VRX23FZV21]].
Resolution needs exponential size on the same formulas, and [[bounded-depth Frege|41QJ1WEMJ3]] needs superpolynomial size.
So Frege is exponentially stronger than both.
No superpolynomial lower bound on Frege size is known; see [[lower bounds for Frege systems|ANSV13M4FS]].

### Watch out

A substitution acts on the whole rule at once.
From $p$ and $q \to r$ you may not apply modus ponens, because that would need $\sigma(p) = q$ in one premise and $\sigma(p) = p$ in the other.
The second trap is to call a system with few lines short.
The $5$-line proof of $\varphi \to \varphi$ has size about $23 \lvert \varphi \rvert$, so for long $\varphi$ it is not small in size.

### History

Cook and Reckhow defined Frege systems in their papers of 1974 and 1979.
Reckhow proved in his 1976 thesis that all Frege systems p-simulate each other, and the result appeared in the 1979 paper.
The name honors Gottlob Frege, whose Begriffsschrift of 1879 gave the first such calculus.

### Try it

First, how many lines and what size has the proof of $(q \to q) \to (q \to q)$ obtained from the $5$-line proof of $p \to p$?
Put $\varphi = q \to q$, of size $s = 3$, so the proof has $5$ lines and size $23 \cdot 3 + 18 = 87$.

Second, is "from $p \land q$ infer $p$" a sound Frege rule?
Yes, because every assignment that makes $p \land q$ true makes $p$ true.

## Explanations

### L1 human

A Frege system is the kind of proof system found in a first logic course.
It has a few axiom patterns and rules such as "from $A$ and $A \to B$, conclude $B$".
A proof is a list of formulas, each an axiom or the result of a rule.
Proof complexity counts how many lines, or how many symbols, the shortest list needs.
For example, $p \to p$ needs $5$ lines in the usual system of three axioms with modus ponens.

### L2 human

We check that modus ponens is a sound Frege rule and measure one instance.
The rule is $p, \ p \to q \,/\, q$, with $k = 2$.
It is sound, because an assignment that makes $p$ and $p \to q$ true makes $q$ true, by the truth table of $\to$.
Take $\sigma(p) = r \land s$ and $\sigma(q) = \neg r$.
The premises of the instance have $3$ and $6$ symbols, not counting parentheses, and the conclusion $\neg r$ has $2$.
So one step of a Frege proof can carry formulas of any size, and size and lines must be counted apart.
The typical use is to fix one Frege system and measure tautologies in it, since by Reckhow's theorem the choice changes sizes by at most a polynomial.

### L3 human

Frege systems are the propositional form of ordinary reasoning with formulas, and they sit high in the hierarchy of proof systems.
Their lines are Boolean formulas, so they match the circuit class $\mathrm{NC}^1$, as resolution matches clauses and [[extended Frege|5YSE04SHFH]] matches circuits.
Bounding the depth of the lines gives [[bounded-depth Frege|41QJ1WEMJ3]], which matches $\mathrm{AC}^0$.
In [[bounded arithmetic|RA380RWEC0]], Frege systems match theories whose reasoning is in $\mathrm{NC}^1$, such as the theory $\mathrm{VNC}^1$ of Cook and Nguyen.
