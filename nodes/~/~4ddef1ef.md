---
tag: ~4ddef1ef
kind: problem
name: Separating the hierarchy of bounded arithmetic
aliases: [separation-problem-bounded-arithmetic, finite-axiomatizability-of-s2]
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [~55a002f3, ~ad7bce8a, ~2d7d49f7, TDQ7AXGM6P, ~e2b71b10]
about: [~55a002f3, TDQ7AXGM6P]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Buss's first-order theories
  - url: https://en.wikipedia.org/wiki/Polynomial_hierarchy
    locator: lead section
history:
  posed_by: "Samuel R. Buss"
  notes: "Buss introduced the theories in his 1985 thesis and states the question as an open question in his survey Bounded Arithmetic and Propositional Proof Complexity."
---

## Problem

Buss's theories of [[bounded arithmetic|~55a002f3]] form the chain
$$S^1_2 \subseteq T^1_2 \subseteq S^2_2 \subseteq T^2_2 \subseteq \cdots \subseteq S_2 = \bigcup_i S^i_2 = \bigcup_i T^i_2.$$
Here $S^i_2$ has polynomial induction for $\Sigma^b_i$ formulas, and $T^i_2$ has ordinary induction for $\Sigma^b_i$ formulas.

**Problem (open).** Is any of these inclusions strict?

The problem has a weak and a strong form, and both are open.

1. Is $S^1_2 \ne S_2$? This holds if and only if at least one inclusion is strict.
2. Is $S_2$ not finitely axiomatizable? Each $S^i_2$ and each $T^i_2$ with $i \ge 1$ is finitely axiomatizable, so this holds if and only if infinitely many inclusions are strict.

A related open problem concerns the relativized theories with a new relation symbol $\alpha$.
Is there a fixed $k$ such that the theories $T^i_2(\alpha)$ are separated by $\forall \Sigma^b_k(\alpha)$ sentences?
In particular, is there a $\forall \Sigma^b_1(\alpha)$ sentence provable in $T_2(\alpha)$ but not in $T^2_2(\alpha)$?

## Remarks

### What is known

- The inclusions hold. $T^i_2$ proves $\Sigma^b_i$-$\mathrm{PIND}$, and $S^{i+1}_2$ proves $\Sigma^b_i$-$\mathrm{IND}$ (Buss). The L2 explanation below checks the first inclusion.
- At the bottom level, $S^0_2 \ne T^0_2$ (Takeuti). Apart from this case, no two theories of the chain are known to be different.
- $S^{i+1}_2$ is conservative over $T^i_2$ for $\forall \Sigma^b_{i+1}$ sentences (Buss). So a separation of $S^{i+1}_2$ from $T^i_2$ needs sentences of higher complexity.
- By [[Buss's witnessing theorem|~ad7bce8a]], a $\forall \Sigma^b_i$ theorem of $T^i_2$ whose search problem is not in $\square^p_i$ would separate $S^i_2$ from $T^i_2$. For $i = 1$, a problem in $\mathrm{PLS}$ outside $\mathrm{FP}$ would suffice, but this implies $\mathrm{P} \ne \mathrm{NP}$.
- If $T^i_2 = S^{i+1}_2$, then the [[polynomial hierarchy|TDQ7AXGM6P]] collapses, by the [[Krajíček-Pudlák-Takeuti theorem|~2d7d49f7]]. Buss showed that then also $T^i_2 = S_2$, and that $T^i_2$ proves the collapse.
- $S_2$ is finitely axiomatizable if and only if $S_2$ proves that the polynomial hierarchy collapses (Buss; Zambella).
- With a new symbol $\alpha$, the hierarchy does not collapse: Krajíček, Pudlák and Takeuti proved that $S_2(\alpha)$ is not finitely axiomatizable.
- The relativized theories $S^1_2(\alpha)$, $T^1_2(\alpha)$ and $T^2_2(\alpha)$ are separated by their $\forall \Sigma^b_1(\alpha)$ consequences. Above $T^2_2(\alpha)$, no $\forall \Sigma^b_1(\alpha)$ separation is known.

### Why the problem is hard

A proof that $S_2$ is not finitely axiomatizable is an independence result: it shows that $S_2$ does not prove that the polynomial hierarchy collapses.
By the Krajíček-Pudlák-Takeuti theorem, a proof that the polynomial hierarchy is infinite would separate $T^i_2$ from $S^{i+1}_2$ for every $i$.
That proof would give $\mathrm{P} \ne \mathrm{NP}$, so this route is beyond present methods.
The finite axiomatizability of $S_2$ is also equivalent to the finite axiomatizability of [[$\mathsf{I}\Delta_0 + \Omega_1$|~e2b71b10]], a question of weak arithmetic.

### Common errors

- To think that the theories are known to be different because the levels of the polynomial hierarchy look different. Both separations are open, and a separation of the levels would give a separation of the theories.
- To expect a $\forall \Sigma^b_{i+1}$ sentence that separates $S^{i+1}_2$ from $T^i_2$. The conservation theorem excludes this.

## History

Buss introduced the theories in his 1985 thesis.
Takeuti separated $S^0_2$ from $T^0_2$.
Krajíček, Pudlák and Takeuti connected the problem with the polynomial hierarchy in 1991.
Buss in 1995, and Zambella independently, showed that the collapse of the theories is equivalent to the provable collapse of the polynomial hierarchy.

## Explanations

### L1 human

Buss made a ladder of systems of axioms for numbers.
Each step on the ladder allows a stronger kind of proof by induction.
Every theorem of a lower step is a theorem of all higher steps.
The question is whether each step proves new theorems, or whether from some step on nothing new is proved.
Nobody knows the answer, even for the first two steps.

### L2 human

We check the first kind of inclusion: $T^i_2$ proves $\Sigma^b_i$-$\mathrm{PIND}$.

1. Let $A(x)$ be $\Sigma^b_i$. Assume $A(0)$ and $\forall x \, (A(\floor{x/2}) \to A(x))$. Fix $a$; we show $A(a)$.
2. Let $B(y) := A(\floor{a / 2^{\abs a - y}})$ for $y \le \abs a$. The number $\floor{a / 2^{\abs a - y}}$ consists of the first $y$ binary digits of $a$.
3. $B(y)$ is $\Sigma^b_i$: the shift by $\abs a - y$ digits is given by a term of the language, and $A$ is $\Sigma^b_i$.
4. $B(0)$ is $A(0)$, since $a < 2^{\abs a}$.
5. Step: halving the first $y + 1$ digits of $a$ gives the first $y$ digits. So the hypothesis of step 1 turns $B(y)$ into $B(y + 1)$.
6. $\Sigma^b_i$-$\mathrm{IND}$ on $y$ gives $B(\abs a)$, which is $A(a)$.
7. For $a = 13 = 1101_2$, the induction passes through $0, 1, 3, 6, 13$, which is $\abs{13} + 1 = 5$ values.

The typical use is to place a new principle in the chain: one proves it in some $T^i_2$, and asks whether $S^i_2$ or a lower theory proves it.
A trap is to read the converse from this argument: ordinary induction would need about $a$ steps, and $\mathrm{PIND}$ gives only about $\abs a$.

### L3 human

The problem is the proof-theoretic form of the question whether the polynomial hierarchy is infinite.
Each level $\Sigma^b_i$ of formulas matches the level $\Sigma^p_i$ of the hierarchy, and each theory has its class of provably total search problems.
For $\forall \Sigma^b_1$ sentences, $S^1_2$ corresponds to polynomial-time functions, and both $T^1_2$ and $S^2_2$ correspond to polynomial local search.

Known separations are relativized, and they come from combinatorial principles such as [[weak pigeonhole principles|~55b2a273]] or from lower bounds through the [[Paris-Wilkie translation|~c9c38d6d]].
[[Approximate counting|~a1e5c7e9]] proves most of these principles, so theories of approximate counting mark the present limit of the methods.
The unrelativized problem would need new ideas, in the same way as the separation of complexity classes.
