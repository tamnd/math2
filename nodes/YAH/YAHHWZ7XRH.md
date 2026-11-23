---
tag: YAHHWZ7XRH
kind: statement
role: theorem
name: Reckhow's theorem on Frege systems
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
uses: [J2BAR09TPF, 3V24CYWDT6]
about: [J2BAR09TPF, ANSV13M4FS]
proofs: [36ZDZA100X]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
history:
  first_stated: "1976"
  notes: "Robert Reckhow, PhD thesis, University of Toronto, 1976. Published with Stephen Cook in The relative efficiency of propositional proof systems, Journal of Symbolic Logic, 1979."
---

## Statement

Suppose one textbook system has the rule "from $\varphi$ and $\psi$ infer $\varphi \land \psi$" and another does not.
The second can still derive $p \land q$ from $p$ and $q$ in some fixed number $c$ of lines, so each use of the rule costs it at most $c$ lines.
Reckhow's theorem says that this local repair always works: any two Frege systems simulate each other with only polynomial loss.

Let $\mathcal F_1$ and $\mathcal F_2$ be [[Frege systems|J2BAR09TPF]].
Then $\mathcal F_2$ [[p-simulates|3V24CYWDT6]] $\mathcal F_1$, so any two Frege systems are p-equivalent.
This holds also when $\mathcal F_1$ and $\mathcal F_2$ use different finite functionally complete sets of connectives, after a fixed polynomial-time translation of formulas into the connectives of $\mathcal F_2$.

When the two systems use the same connectives, there is a constant $c$ with the following property.
Every $\mathcal F_1$-proof with $m$ lines and size $S$ becomes an $\mathcal F_2$-proof of the same formula with at most $c m$ lines and size at most $c S^2$.
The measures are the number of lines and the size in symbols.

## Remarks

### Why each hypothesis is needed

$\mathcal F_2$ must be implicationally complete.
A system that proves every tautology but cannot derive from hypotheses gives no derived rule to stand in for a rule of $\mathcal F_1$.

$\mathcal F_1$ must have finitely many rules.
The constant $c$ is the largest length of finitely many fixed derivations, one for each rule, and with infinitely many rules no single $c$ need exist.

The rules of $\mathcal F_1$ must be sound.
An unsound rule, such as "from $p \to q$ and $q$ infer $p$", has no derivation in the sound system $\mathcal F_2$.

### What it gives you

The size $s_{\mathcal F}(\tau)$ is fixed by $\tau$ up to a polynomial, whatever Frege system $\mathcal F$ you choose.
So "Frege systems prove the pigeonhole formulas in polynomial size" is a statement about the class, and you need not name the rules.
For the same reason, the open problem of [[lower bounds for Frege systems|ANSV13M4FS]] is one question, not a question for each system.

Here is a worked use.
If some Frege system $\mathcal F_1$ over $\{ \neg, \to \}$ proves a family $\tau_n$ with size $n^4$, then the Hilbert system L proves it with size at most $c \, n^8$, by the quadratic bound.
So a superpolynomial lower bound in L would be a superpolynomial lower bound for every Frege system.

### The converse

The theorem already gives simulation in both directions.
A system that p-simulates every Frege system need not be a Frege system, and [[extended Frege|5YSE04SHFH]] is the standard example.

### Generalizations

The same proof shows that all extended Frege systems are p-equivalent, and that the sequent calculus with cut and natural deduction are p-equivalent to Frege systems.
For [[bounded-depth Frege|41QJ1WEMJ3]], the translation raises the depth of each line by at most a constant, so depth $d$ in one system becomes depth $d + O(1)$ in another.

### Watch out

The case of different connectives is not a copy of the same-connective case.
Writing $\varphi \leftrightarrow \psi$ as $(\varphi \land \psi) \lor (\neg \varphi \land \neg \psi)$ copies both sides, so a nest of $n$ biconditionals grows to size at least $2^n$.
Reckhow's proof avoids this blow-up by first rebalancing each formula, and a naive translation would not give a p-simulation.

## History

Robert Reckhow proved the theorem in his 1976 doctoral thesis at the University of Toronto, written under Stephen Cook.
It appeared in the 1979 paper of Cook and Reckhow in the Journal of Symbolic Logic, which also introduced the general notion of a propositional proof system.

## Explanations

### L1 human

There are many textbook proof systems with different axioms and rules.
The theorem says that the choice hardly matters.
A proof in one system can be rewritten in any other, and its length grows by at most a fixed polynomial.
For example, a proof of $100$ lines becomes a proof of at most $100 c$ lines, for a constant $c$ that depends only on the two systems.

### L2 human

We apply the idea of the [[proof|36ZDZA100X]] to one rule.
Let $\mathcal F_1$ have the rule $p, q \,/\, p \land q$, and let $\mathcal F_2$ lack it.
Since $p, q \models p \land q$, the system $\mathcal F_2$ has a fixed derivation $D$ of $p \land q$ from $p$ and $q$, say with $c$ lines.
In an $\mathcal F_1$-proof, replace each use of the rule with $\varphi$, $\psi$ for $p$, $q$ by $D$ under the same substitution.
Each use now costs at most $c$ lines, so the line count grows by a factor of at most $c$.
The typical use of the theorem is to say "Frege" without naming the rules.

### L3 human

The theorem shows that the Frege class does not depend on the choice of rules, in the same way that the circuit class $\mathrm{NC}^1$ does not depend on the choice of gates.
Its proof is the propositional form of the fact that one Hilbert calculus derives the rules of another, with the extra work of counting sizes.
So proof complexity measures tautologies against classes of systems: Frege, [[extended Frege|5YSE04SHFH]] and [[bounded-depth Frege|41QJ1WEMJ3]] of each depth.
