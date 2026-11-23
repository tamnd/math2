---
tag: PEJQDHHX8E
kind: problem
name: Separating the hierarchy of bounded arithmetic
aliases: [separation-problem-bounded-arithmetic, finite-axiomatizability-of-s2]
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [A2CFPP8JMN, RH4R7GTTAX, YP7KE8E6DC, TDQ7AXGM6P, V8WD1F0NS2]
about: [A2CFPP8JMN, TDQ7AXGM6P]
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

Buss's theories of [[bounded arithmetic|A2CFPP8JMN]] form one long chain:

$$S^1_2 \subseteq T^1_2 \subseteq S^2_2 \subseteq T^2_2 \subseteq S^3_2 \subseteq \cdots \subseteq S_2 = \bigcup_i S^i_2 = \bigcup_i T^i_2.$$

Here $S^i_2$ has polynomial induction for $\Sigma^b_i$ formulas, and $T^i_2$ has ordinary induction for $\Sigma^b_i$ formulas.
Next to it stands the [[polynomial hierarchy|TDQ7AXGM6P]], and the levels match:

| Level $i$ | Sets defined by $\Sigma^b_i$ formulas | $\Sigma^b_i$-definable functions of $S^i_2$ |
|---|---|---|
| $1$ | $\mathrm{NP}$ | $\mathrm{FP}$ |
| $2$ | $\Sigma^p_2$ | $\mathrm{FP}^{\mathrm{NP}}$ |
| $3$ | $\Sigma^p_3$ | $\mathrm{FP}^{\Sigma^p_2}$ |

Nobody knows whether $\mathrm{P} \subseteq \mathrm{NP} \subseteq \Sigma^p_2 \subseteq \cdots$ is a proper chain, and nobody knows it for the theories either.

**Problem (open).** Is any inclusion of the chain of theories strict?

The problem has a weak and a strong form, and both are open.

1. Is $S^1_2 \ne S_2$?
   This holds if and only if at least one inclusion is strict.
2. Is $S_2$ not finitely axiomatizable?
   Each $S^i_2$ and each $T^i_2$ with $i \ge 1$ is finitely axiomatizable, so this holds if and only if infinitely many inclusions are strict.

## Remarks

### Why the two forms are what they are

The second equivalence deserves a line of proof.
If $S_2$ has a finite set of axioms, they all lie in some $T^i_2$, because the chain is increasing.
Then $T^i_2$ proves all of $S_2$, and every inclusion from $T^i_2$ on is an equality.
Conversely, if the chain is constant from $T^i_2$ on, then $S_2 = T^i_2$, which is finitely axiomatizable.

$S_2$ and [[$\mathsf{I}\Delta_0 + \Omega_1$|V8WD1F0NS2]] prove the same theorems up to the translation of languages.
So the strong form is also a question of weak arithmetic: is $\mathsf{I}\Delta_0 + \Omega_1$ finitely axiomatizable?

### What is known

Buss proved the inclusions: $T^i_2$ proves $\Sigma^b_i$-$\mathrm{PIND}$, and $S^{i+1}_2$ proves $\Sigma^b_i$-$\mathrm{IND}$.
He also proved that $S^{i+1}_2$ is conservative over $T^i_2$ for $\forall \exists \Sigma^b_{i+1}$ sentences.
So a sentence that separates $S^{i+1}_2$ from $T^i_2$ must be more complex than that.

At the bottom, [[Buss's witnessing theorem|RH4R7GTTAX]] shows what a separation would take.
Every polynomial local search problem ($\mathrm{PLS}$) is provably total in $T^1_2$, by Buss and Krajíček.
If some $\mathrm{PLS}$ problem has no polynomial-time algorithm, then $S^1_2$ does not prove its totality, and $S^1_2 \ne T^1_2$.
But a $\mathrm{PLS}$ problem outside $\mathrm{FP}$ already gives $\mathrm{P} \ne \mathrm{NP}$.

From the other side, the [[Krajíček-Pudlák-Takeuti theorem|YP7KE8E6DC]] says that $T^i_2 = S^{i+1}_2$ implies a collapse of the polynomial hierarchy.
Zambella, and Buss in related work, sharpened this: $S_2$ is finitely axiomatizable if and only if $S_2$ proves that the polynomial hierarchy collapses.

### Relativized separations

With a new relation symbol $\alpha$ for an oracle, the hierarchy is known to be strict.
The relativized Krajicek-Pudlak-Takeuti theorem, combined with an oracle relative to which the polynomial hierarchy is infinite, shows that $S_2(\alpha)$ is not finitely axiomatizable.

At the bottom level the separation even uses simple sentences.
Relative to a suitable oracle some $\mathrm{PLS}$ problem has no polynomial-time algorithm.
So, by witnessing, a $\forall \Sigma^b_1(\alpha)$ sentence separates $S^1_2(\alpha)$ from $T^1_2(\alpha)$.
Combinatorial principles such as the [[weak pigeonhole principles|NJ18EZ5JBC]] give further relativized separations.

### Why the problem is hard

A proof that $S_2$ is not finitely axiomatizable is an independence result: it shows that $S_2$ does not prove that the polynomial hierarchy collapses.
The direct route goes through complexity.
A proof that the polynomial hierarchy is infinite would separate $T^i_2$ from $S^{i+1}_2$ for every $i$.
That proof would give $\mathrm{P} \ne \mathrm{NP}$, so this route is beyond present methods.
The relativized proofs do not transfer, because they use the freedom to choose the oracle, and the unrelativized theories have no free symbol to choose.

### Watch out

Do not think that the theories are known to differ because the levels of the hierarchy look different.
Both separations are open, and a separation of the classes would give a separation of the theories.
Do not look for a $\forall \exists \Sigma^b_{i+1}$ sentence that separates $S^{i+1}_2$ from $T^i_2$, since Buss's conservation theorem excludes it.

### Try it

1. Suppose someone proves $T^3_2 = S^4_2$.
   What follows for the polynomial hierarchy?
   Answer: it collapses, by the Krajíček-Pudlák-Takeuti theorem with $i = 3$.
2. Can a $\forall \exists \Sigma^b_2$ sentence separate $S^2_2$ from $T^1_2$?
   Answer: no, because $S^2_2$ is conservative over $T^1_2$ for these sentences.

## History

Buss introduced the theories $S^i_2$ and $T^i_2$ in his 1985 thesis and asked whether they differ.
Krajíček, Pudlák and Takeuti connected the problem with the polynomial hierarchy in 1991.
Buss and Zambella, independently, related the finite axiomatizability of $S_2$ to a collapse of the polynomial hierarchy that $S_2$ proves.

## Explanations

### L1 human

Buss made a ladder of systems of axioms for numbers.
Each step on the ladder allows a stronger kind of proof by induction.
Every theorem of a lower step is a theorem of all higher steps.
The question is whether each step proves new theorems, or whether from some step on nothing new is proved.
Nobody knows the answer, even for the first two steps.

### L2 human

We check the first kind of inclusion: $T^i_2$ proves $\Sigma^b_i$-$\mathrm{PIND}$ for $i \ge 1$.
Let $A(x)$ be $\Sigma^b_i$, assume $A(0)$ and $\forall x \, (A(\lfloor x/2 \rfloor) \to A(x))$, and fix $a$.
Write $a_y$ for the number formed by the first $y$ binary digits of $a$, and induct on $y \le \lvert a \rvert$ with the formula $B(y) := A(a_y)$.
$T^i_2$ can define $y \mapsto a_y$, with values at most $a$, so $B$ is equivalent in $T^i_2$ to a $\Sigma^b_i$ formula.
The base $B(0)$ is $A(0)$, because $a_0 = 0$.
The step holds because $a_y = \lfloor a_{y+1} / 2 \rfloor$, so the hypothesis turns $B(y)$ into $B(y + 1)$.
Induction gives $B(\lvert a \rvert)$, which is $A(a)$.
For $a = 13 = 1101_2$, the numbers $a_y$ are these:

$$a_0 = 0, \quad a_1 = 1, \quad a_2 = 3, \quad a_3 = 6, \quad a_4 = 13.$$

The typical use is to place a new principle in the chain: prove it in some $T^i_2$, and ask whether a lower theory proves it.
Watch out: the argument does not run backwards, since ordinary induction to $a$ needs about $a$ steps and polynomial induction gives only about $\lvert a \rvert$.

### L3 human

The problem is the proof-theoretic form of the question whether the polynomial hierarchy is infinite.
Each level $\Sigma^b_i$ of formulas matches the level $\Sigma^p_i$ of the hierarchy, and each theory has its class of provably total search problems.
For $\forall \Sigma^b_1$ sentences, $S^1_2$ corresponds to polynomial-time functions, and both $T^1_2$ and $S^2_2$ correspond to polynomial local search.

The known separations are relativized, and they come from combinatorial principles or from lower bounds through the [[Paris-Wilkie translation|ZVD982MVST]].
Theories of [[approximate counting|65K2S22DGZ]] sit inside this picture: $T^2_2$ proves the dual weak pigeonhole principle for polynomial-time functions, which is the axiom of $\mathsf{APC}_1$.
The unrelativized problem would need new ideas, in the same way as the separation of the complexity classes.
