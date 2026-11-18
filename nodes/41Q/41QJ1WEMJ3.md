---
tag: 41QJ1WEMJ3
kind: definition
defines: 1Q046J0AW2
name: Bounded-depth Frege
aliases: [bounded-depth-frege, ac0-frege, constant-depth-frege]
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [J2BAR09TPF, 3V24CYWDT6, QG78SX3DK1]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
---

## Definition

Read formulas over $\neg$, $\land$, $\lor$ as circuits of unbounded fan-in.
A maximal block of the same binary connective, such as $\varphi_1 \lor \varphi_2 \lor \cdots \lor \varphi_k$, counts as one gate, and negations are pushed to the variables by De Morgan's laws.

The *depth* of a formula is defined by induction.

1. A literal $x$ or $\neg x$ has depth $0$.
2. A formula $\varphi_1 \lor \cdots \lor \varphi_k$, with $k \ge 2$ and no $\varphi_i$ itself a disjunction, has depth $1 + \max_i \mathrm{depth}(\varphi_i)$. Conjunctions are treated in the same way.
3. The depth of $\neg \varphi$ is the depth of $\varphi$.

Fix a [[Frege system|J2BAR09TPF]] $\mathcal F$ over $\neg$, $\land$, $\lor$.
For $d \ge 1$, a *depth-$d$ Frege proof* is an $\mathcal F$-proof in which every line has depth at most $d$.
A family of proofs $(\pi_n)$ is a *bounded-depth Frege* family if there is a constant $d$ such that every $\pi_n$ is a depth-$d$ Frege proof.

The measure is size, the number of symbols, as for Frege systems.
The system $\mathrm{AC}^0$-Frege is the class of bounded-depth Frege systems, named after the circuit class [[AC0|QG78SX3DK1]] of constant-depth, polynomial-size circuits.

## Notation

Writers use $\mathrm{AC}^0$-Frege, $\mathrm{F}_d$, $\mathrm{Frege}_d$ or "depth-$d$ $\mathrm{LK}$" for these systems.
Many writers use the sequent calculus LK with unbounded fan-in connectives instead of a Frege system.
The two choices give the same sizes up to a polynomial and the same depths up to an additive constant.
Some writers count depth from $1$ for literals, so the depth of a CNF is $2$ or $3$ depending on the convention.

## Remarks

### Examples

- [[Substitution instances of a fixed proof|N95EDP0DFS]]: replacing the variables of a fixed proof by formulas of depth at most $e$ gives proofs of depth at most a constant plus $e$. So such families are bounded-depth Frege families.
- [[Resolution as the sequent calculus with atomic cuts|BJ4T6B8Q2M]]: resolution refutations are proofs whose lines are clauses, so resolution sits at the lowest level of the hierarchy.

### Non-examples

- [[Buss's Frege proofs of the pigeonhole principle|PXBV25AQM8]] use counting formulas of depth growing like $\log n$. So they do not form a bounded-depth family.
- A general Frege proof of the [[Tseitin formulas|JXTCC6KXNG]] by Gaussian elimination writes parities of many variables. Such parities need large depth or exponential size, by the theorem that [[parity is not in AC0|W6T7X0QCFH]].

### Basic properties

- A depth-$d$ Frege proof is also a depth-$(d+1)$ Frege proof, so depth-$(d+1)$ Frege p-simulates depth-$d$ Frege.
- Every bounded-depth Frege system is p-simulated by Frege systems.
- *Ajtai's theorem.* Bounded-depth Frege has no polynomial-size proofs of the [[pigeonhole formulas|RJ571F7FF0]]; see [[Ajtai's theorem|Q0ERK64J78]]. The exponential form $2^{n^{\varepsilon_d}}$ is due to Krajíček, Pudlák and Woods, and to Pitassi, Beame and Impagliazzo.
- *Method.* The lower bounds use random restrictions and switching lemmas, as for the circuit lower bounds for $\mathrm{AC}^0$. A restriction simplifies every line of a small proof to a shallow decision tree, and a consistent assignment of such trees to the lines cannot exist for a proof of the pigeonhole principle.
- *Bounded arithmetic.* The theory $I\Delta_0(R)$ with a new relation symbol $R$ corresponds to bounded-depth Frege: its proofs of bounded formulas translate into families of polynomial-size bounded-depth Frege proofs, by the translation of Paris and Wilkie. So Ajtai's theorem shows that $I\Delta_0(R)$ does not prove the pigeonhole principle for $R$. See [[bounded arithmetic|RA380RWEC0]].
- *Counting gates.* Adding parity or counting modulo $p$ to the lines gives $\mathrm{AC}^0[p]$-Frege. No superpolynomial lower bound for $\mathrm{AC}^0[p]$-Frege is known; this is an open problem.

### History

Ajtai proved the first superpolynomial lower bound for bounded-depth Frege in 1988, with methods of nonstandard models of arithmetic.
Krajíček, Pudlák and Woods, and independently Pitassi, Beame and Impagliazzo, proved exponential lower bounds in the early 1990s by combinatorial switching lemmas.

### Common errors

- The depth bound is a constant for the whole family. A proof whose depth grows with $n$, even slowly, is not a bounded-depth family.
- Lower bounds for depth $d$ say nothing about Frege systems in general. The pigeonhole formulas are hard in every fixed depth and easy in Frege.
- The depth convention must be stated: some writers count literals as depth $1$.

## Explanations

### L1 human

A formula has a depth: the number of times "and" and "or" alternate as one reads it from the outside to the variables.
A bounded-depth Frege proof uses only formulas of depth at most a fixed number, such as $3$.
Such proofs cannot easily count, and they need exponential size to prove that $n + 1$ pigeons do not fit into $n$ holes.
For example, $(x \land y) \lor (\neg x \land z)$ has depth $2$: an "or" of two "and"s of literals.

### L2 human

We compute the depth of three formulas.

1. A clause $x \lor \neg y \lor z$ is one $\lor$-gate over literals, so its depth is $1$.
2. A CNF $(x \lor y) \land (\neg x \lor z)$ is an $\land$-gate over clauses, so its depth is $2$.
3. The negation $\neg((x \lor y) \land (\neg x \lor z))$ becomes $(\neg x \land \neg y) \lor (x \land \neg z)$ by De Morgan's laws, a DNF of depth $2$.

The typical use is to fix $d$, and to prove lower bounds that hold for depth $d$ and become weaker as $d$ grows.
A trap: depth and size are separate measures, and both must be bounded.

### L3 human

Bounded-depth Frege is the proof system whose lines are $\mathrm{AC}^0$ circuits written as formulas.
Its lower bounds are the proof analogue of the lower bounds for $\mathrm{AC}^0$ circuits, and they use the same switching lemmas.
The next steps, $\mathrm{AC}^0[p]$-Frege and $\mathrm{TC}^0$-Frege, have no known superpolynomial lower bounds, although the corresponding circuit lower bounds for $\mathrm{AC}^0[p]$ are known.
