---
tag: 2MGJJTSRFD
kind: statement
role: theorem
name: Ordinal analysis of Π¹₁ comprehension
msc: ["03F15", "03F35", "03B30"]
topics: [XTTKZTYDSD]
audience: research
uses: [DC60FYCSPM, 5GS6DRJ5SY, E7WEFRMQTB, C72RBH0CDR, 3CNSYYX2HF, 5NVA2JRHPV, VM8TQ70CVJ, 0ZHQMQ2C1N, 5VNT564Y2W, NZWRK062WQ, M7D1HEJQVH]
about: [DC60FYCSPM, C72RBH0CDR]
history:
  first_stated: "1967"
  notes: "Takeuti gave a consistency proof of Π¹₁-comprehension with ordinal diagrams in the Annals of Mathematics in 1967; the methods of Buchholz and Pohlers are collected in Lecture Notes in Mathematics 897 (1981)."
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Theories with larger proof-theoretic ordinals
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Ordinal notation
---

## Statement

The theory $\Pi^1_1\text{-}\mathrm{CA}_0$ proves that the notations below $\psi_0(\Omega_2)$, the Bachmann-Howard ordinal, are well-ordered, and it can go much further, up to but not including $\psi_0(\Omega_\omega)$.

Let $\Pi^1_1\text{-}\mathrm{CA}_0$ be the subsystem of [[second-order arithmetic|DC60FYCSPM]] with the basic axioms, the induction axiom for sets, and the [[comprehension scheme|5GS6DRJ5SY]] for $\Pi^1_1$ formulas with set parameters.
Let $(\mathrm{OT}, \prec)$ be [[Buchholz's ordinal notation system|E7WEFRMQTB]], a [[primitive recursive|5NVA2JRHPV]] set of terms with a primitive recursive linear order, as in [[ordinal notation systems|3CNSYYX2HF]].
Let $\tau \in \mathrm{OT}$ be the term for $\psi_0(\Omega_\omega)$.
For $a \in \mathrm{OT}$, let $\mathrm{WO}(a)$ be the $\Pi^1_1$ sentence below, which says that $\prec$ restricted to the terms below $a$ is well-founded.

$$\forall X \, \Big[ \forall x \, \big( \forall y \, (y \prec x \to y \in X) \to x \in X \big) \to \forall x \, (x \prec a \to x \in X) \Big]$$

Then the following hold.

- (a) For every $a \in \mathrm{OT}$ with $a \prec \tau$, the theory $\Pi^1_1\text{-}\mathrm{CA}_0$ proves $\mathrm{WO}(a)$.
- (b) The theory $\Pi^1_1\text{-}\mathrm{CA}_0$ does not prove $\mathrm{WO}(\tau)$.
- (c) Primitive recursive arithmetic with quantifier-free [[transfinite induction|0ZHQMQ2C1N]] along $\prec$ restricted to the terms below $\tau$ proves the [[consistency|VM8TQ70CVJ]] of $\Pi^1_1\text{-}\mathrm{CA}_0$.

In particular, the [[proof-theoretic ordinal|C72RBH0CDR]] of $\Pi^1_1\text{-}\mathrm{CA}_0$ is $\psi_0(\Omega_\omega)$, in Buchholz's notation.

## Remarks

### Which ordinal and which notation

Here the proof-theoretic ordinal of a theory is the supremum of the order types of the primitive recursive well-orderings that the theory proves well-founded.
The functions $\psi_\nu$ are Buchholz's, with $\Omega_0 = 1$ and $\Omega_\nu = \aleph_\nu$ for $\nu \ge 1$.
Other systems use the letter $\psi$ for different functions, so the expression $\psi_0(\Omega_\omega)$ only has this meaning in Buchholz's system.
Part (c) speaks about one particular primitive recursive ordering, and the ordinal is the order type of that ordering.
Such a value is only meaningful for a natural notation, in which the terms and the order come from the collapsing functions.

### Why each hypothesis is needed

The restriction of induction to sets matters.
The theory $\Pi^1_1\text{-}\mathrm{CA}$, with the induction scheme for all formulas, proves more instances of $\mathrm{WO}$ and has a larger ordinal, so (b) fails for it.
Adding bar induction gives $\Pi^1_1\text{-}\mathrm{CA} + \mathrm{BI}$, whose ordinal is the [[Takeuti-Feferman-Buchholz ordinal|NZWRK062WQ]] $\psi_0(\varepsilon_{\Omega_\omega + 1})$, far above $\tau$.
The bound $\tau$ is sharp: part (a) reaches every term below $\tau$, and part (b) shows that $\tau$ itself is not reached.

### Consequences

The theory $\mathrm{ID}_{<\omega}$, the union of the theories of finitely [[iterated inductive definitions|5VNT564Y2W]], has the same ordinal $\psi_0(\Omega_\omega)$.
By (c) and [[Gödel's second incompleteness theorem|4PZM5GJTR5]], $\Pi^1_1\text{-}\mathrm{CA}_0$ does not prove quantifier-free transfinite induction along $\prec$ below $\tau$.
Since $\mathrm{WO}(\tau)$ implies each instance of this induction, because a quantifier-free formula defines a set, this gives a second proof of (b).
Combinatorial statements that imply $\mathrm{WO}(\tau)$ over a weak base theory are not provable in $\Pi^1_1\text{-}\mathrm{CA}_0$.
Friedman's extended Kruskal theorem, with the gap condition, and the graph minor theorem give such statements.

### The same ordinal, different theories

The ordinal does not determine the theory.
The first-order theory $\mathrm{ID}_{<\omega}$ has the ordinal $\psi_0(\Omega_\omega)$ but has no set variables at all.
So a theory that proves $\mathrm{WO}(a)$ for exactly the terms $a \prec \tau$ need not prove the same theorems as $\Pi^1_1\text{-}\mathrm{CA}_0$.

### Beyond Π¹₁-comprehension

Michael Rathjen extended the methods to stronger theories, among them the set theory $\mathrm{KPM}$, with [[Rathjen's psi function|M7D1HEJQVH]], and parameter-free $\Pi^1_2$-comprehension (Archive for Mathematical Logic, 2005).
His work on stable ordinals aims at full $\Pi^1_2$-comprehension.
No ordinal analysis of full second-order arithmetic is known, and it is the main open problem of the field.

### Watch out

Do not give $\Pi^1_1\text{-}\mathrm{CA}_0$ the ordinal $\psi_0(\varepsilon_{\Omega_\omega + 1})$.
That is the ordinal of $\Pi^1_1\text{-}\mathrm{CA} + \mathrm{BI}$ and of $\mathrm{ID}_\omega$, which differ from $\Pi^1_1\text{-}\mathrm{CA}_0$ in the induction they allow.
Do not read $\Omega_\omega$ as a countable ordinal either: it is the cardinal $\aleph_\omega$, and only the collapsed value $\psi_0(\Omega_\omega)$ is countable.

### Try it

Show that $\Pi^1_1\text{-}\mathrm{CA}_0$ proves $\mathrm{WO}(b)$, where $b$ is the term for the Bachmann-Howard ordinal $\psi_0(\Omega_2)$.

Answer: the term $\Omega_2 = \psi_2(0)$ lies in $C_0(\Omega_3)$ and is below $\Omega_3$, so $\psi_0(\Omega_2) \in C_0(\Omega_3)$ and hence $\psi_0(\Omega_2) < \psi_0(\Omega_3) \le \psi_0(\Omega_\omega)$.
So $b \prec \tau$, and part (a) gives $\mathrm{WO}(b)$.

## History

Gaisi Takeuti proved the consistency of $\Pi^1_1$-comprehension in "Consistency proofs of subsystems of classical analysis", Annals of Mathematics 86 (1967).
His proof used reductions of proofs in a Gentzen-style calculus, with ordinal diagrams as the measure of complexity.
Buchholz and Pohlers analyzed the theories $\mathrm{ID}_\nu$ with the $\Omega_{\mu+1}$-rule and with [[local predicativity|5C4YBXQV15]], and these results appear in Lecture Notes in Mathematics 897 (1981).
Buchholz's functions $\psi_\nu$ of 1986 gave the standard form of the ordinal, $\psi_0(\Omega_\omega)$.

## Explanations

### L1 human

A theory is a list of axioms, and its proof-theoretic ordinal measures how much induction it can prove.
For ordinary arithmetic the measure is $\varepsilon_0$.
The theory $\Pi^1_1\text{-}\mathrm{CA}_0$ lets us form sets described with one "for all sets" quantifier, and this is much stronger.
Its measure is the ordinal $\psi_0(\Omega_\omega)$, named with Buchholz's collapsing functions and a ladder of infinities $\Omega_1, \Omega_2, \dots$.
The theorem says that the theory can prove well-ordering for every notation below this one, and not for this one.

### L2 human

We see how (a) follows from the analysis of the theories $\mathrm{ID}_n$.

1. The ordinal of $\mathrm{ID}_n$ is $\psi_0(\Omega_{n+1})$, and $\mathrm{ID}_n$ proves that every term below $\psi_0(\Omega_{n+1})$ lies in the accessible part of $\prec$.
2. The ordinal of $\mathrm{ID}_{<\omega}$ is $\psi_0(\Omega_\omega)$, the supremum of the values $\psi_0(\Omega_{n+1})$, so every term $a \prec \tau$ lies below $\psi_0(\Omega_{n+1})$ for some $n$.
3. The theory $\Pi^1_1\text{-}\mathrm{CA}_0$ interprets $\mathrm{ID}_n$: each inductively defined set is the intersection of all sets closed under its operator.
4. Under this interpretation, "$a$ is in the accessible part" implies $\mathrm{WO}(a)$.

The typical use of the theorem is to show that a mathematical statement is not provable in $\Pi^1_1\text{-}\mathrm{CA}_0$, by deriving $\mathrm{WO}(\tau)$ from it.

### L3 human

The proofs of this theorem and of its relatives for $\mathrm{ID}_\nu$ created the modern tools of impredicative proof theory: collapsing functions, the $\Omega$-rule and local predicativity.
In reverse mathematics, $\Pi^1_1\text{-}\mathrm{CA}_0$ is the strongest of the "big five" subsystems, and many theorems of analysis and combinatorics are equivalent to it over a weak base.
The ordinal $\psi_0(\Omega_\omega)$ explains why some finite combinatorial statements, such as forms of the graph minor theorem, are not provable in this system.
The next steps are theories with $\Pi^1_2$-comprehension, where the cardinals $\Omega_\nu$ of the notation give way to ordinals with stronger reflection properties.
