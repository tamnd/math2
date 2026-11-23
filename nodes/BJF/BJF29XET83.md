---
tag: BJF29XET83
kind: statement
role: theorem
name: Representability of recursive functions in Robinson arithmetic
aliases: [representability-theorem, representability-in-arithmetic]
msc: ["03F30", "03D20"]
topics: [QHCRN4JVG0]
audience: grad
uses: [TT8MXRTVBM, VM8TQ70CVJ, Q5MT8WY7JM, HBK5QHC1GC, Y0JTZXBRT5, 69234Z1V00, BM6P0C2AC2, 1DQ1M6ZWS4, TN9G24VABN, 3PRW76471J, X9WYNYE29C, YRV6SYK2BY, TKDKW5MENB, 4W0E9G7PPV]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - book: isbn:9781482237726
  - url: https://builds.openlogicproject.org/
    locator: Representability in Q
---

## Statement

The theorem says that the weak theory $\mathsf{Q}$ can compute every computable function, and that no reasonable theory computes more.
Let $T$ be a theory in the language $L_A$ that extends [[Robinson arithmetic|TT8MXRTVBM]] $\mathsf{Q}$.

A function $f : \mathbb{N}^k \to \mathbb{N}$ is *representable* in $T$ if there is a formula $\varphi(x_1, \ldots, x_k, y)$ such that for all $n_1, \ldots, n_k \in \mathbb{N}$,
$$T \vdash \forall y\,\bigl(\varphi(\overline{n_1}, \ldots, \overline{n_k}, y) \leftrightarrow y = \overline{f(n_1, \ldots, n_k)}\bigr).$$
A relation $R \subseteq \mathbb{N}^k$ is *representable* in $T$ if there is a formula $\psi(x_1, \ldots, x_k)$ such that $T \vdash \psi(\overline{n_1}, \ldots, \overline{n_k})$ when $(n_1, \ldots, n_k) \in R$, and $T \vdash \neg \psi(\overline{n_1}, \ldots, \overline{n_k})$ when $(n_1, \ldots, n_k) \notin R$.

**Theorem.**

1. Every total [[recursive function|HBK5QHC1GC]] is representable in $\mathsf{Q}$ by a $\Sigma_1$ formula, and hence in $T$.
2. Every recursive relation is representable in $\mathsf{Q}$, and hence in $T$.
3. If $T$ is [[consistent|VM8TQ70CVJ]] and recursively axiomatized, then every function and every relation that is representable in $T$ is recursive.

## Remarks

### A first representation: Cantor's pairing function

Cantor's pairing function codes a pair of numbers by one number:
$$\pi(a, b) = \frac{(a + b)(a + b + 1)}{2} + a.$$
For the pair $(3, 5)$ we get $\pi(3, 5) = \tfrac{8 \cdot 9}{2} + 3 = 36 + 3 = 39$.
The language has no division, so we write the graph as the $\Delta_0$ formula
$$\varphi(a, b, y) := y + y = (a + b) \cdot (a + b + \overline{1}) + a + a.$$
Check: $39 + 39 = 78$ and $8 \cdot 9 + 6 = 78$.

$\mathsf{Q}$ proves $\varphi(\overline{3}, \overline{5}, \overline{39})$ by computing both closed terms, which is what [[Σ1-completeness|69234Z1V00]] guarantees.
That is half of representability.
The other half asks $\mathsf{Q}$ to prove that no other $y$ satisfies $\varphi(\overline{3}, \overline{5}, y)$, and here $y$ is a variable, which may stand for a non-standard element.
$\mathsf{Q}$ has no induction, so the usual argument that $y + y = \overline{78}$ forces $y = \overline{39}$ is not available there.
[[The proof|4T3MSP1SPK]] solves this by building uniqueness into the formula itself.

### Why each hypothesis is needed

Part 1 needs a theory that can compute with both $+$ and $\cdot$.
[[Presburger arithmetic|4W0E9G7PPV]] is complete and true in $(\mathbb{N}, 0, S, +, <)$.
A formula that represents the recursive relation "$x$ is a square" in it would define that relation in $(\mathbb{N}, 0, S, +, <)$, and [[no formula does|TKDKW5MENB]].

Part 3 needs consistency, because in an inconsistent theory every formula represents every relation.
It also needs a recursive set of axioms.
The complete theory of $\mathfrak{N}$ is consistent, and it represents every relation definable in $\mathfrak{N}$, including the halting set, which is not recursive.

### The converse

Part 3 is the converse of Parts 1 and 2.
For a consistent recursively axiomatized extension $T$ of $\mathsf{Q}$, the functions representable in $T$ are exactly the total recursive functions.
In the same way, the relations representable in $T$ are exactly the recursive relations.

### What it gives you

A set $A \subseteq \mathbb{N}$ is weakly representable in $T$ if some $\psi(x)$ has $T \vdash \psi(\overline{n})$ exactly when $n \in A$.
The sets weakly representable in $\mathsf{Q}$ are exactly the [[computably enumerable|TN9G24VABN]] sets.
A $\Sigma_1$ definition of a c.e. set works by Σ1-completeness and because $\mathsf{Q}$ is true in $\mathfrak{N}$.
Conversely, a search through the proofs of $\mathsf{Q}$ lists $\{ n : \mathsf{Q} \vdash \psi(\overline{n}) \}$.

The map that sends $n$ to the code of the result of substituting $\overline{n}$ into the formula with code $n$ is recursive, hence representable.
This gives the [[diagonal lemma|3PRW76471J]], and with it [[Gödel's incompleteness theorems|X9WYNYE29C]] and [[Tarski's undefinability theorem|YRV6SYK2BY]].
It also shows that $\mathsf{Q}$ is essentially undecidable: no consistent extension of $\mathsf{Q}$ is decidable.

### Watch out: definable is not representable

A relation is [[definable|1DQ1M6ZWS4]] in $\mathfrak{N}$ when a formula is true exactly on it.
It is representable in $T$ when $T$ proves the formula on it and refutes the formula off it.
Every relation representable in $\mathsf{Q}$ is definable in $\mathfrak{N}$ by the same formula, since $\mathfrak{N} \models \mathsf{Q}$.
The converse fails: the halting set is defined by a $\Sigma_1$ formula, but it is not recursive, so by Part 3 no formula represents it in $\mathsf{Q}$.

### Generalizations

The same proof works for every theory that proves the facts about numerals that the proof uses, such as the theory $\mathsf{R}$ among the [[weak theories of arithmetic|Q5MT8WY7JM]].
For primitive recursive functions, the representing formulas can be chosen so that $\mathsf{I}\Sigma_1$ proves their totality $\forall \vec{x}\, \exists y\, \varphi$.

## History

Gödel in 1931 showed that every primitive recursive relation is representable in his formal system, which was enough for the incompleteness theorem.
Tarski, Mostowski and Robinson, in their book Undecidable Theories of 1953, proved that every recursive function is representable in $\mathsf{Q}$ and in the weaker theory $\mathsf{R}$.

## Explanations

### L1 human

A function is representable in a theory when the theory can compute it.
For each input, the theory proves that a certain formula picks out exactly the right output.
The theorem says that the very weak theory $\mathsf{Q}$ can compute every computable function in this sense.
Conversely, a reasonable theory cannot compute more than the computable functions, since one can search through its proofs.
This link between proofs and computation is the starting point of Gödel's incompleteness theorems.

### L2 human

We represent the doubling function $f(n) = 2n$ in $\mathsf{Q}$ by the $\Delta_0$ formula $\varphi(x, y) := (y = x + x)$.
Fix $n$.
By $\mathsf{Q}4$ and $\mathsf{Q}5$ applied to numerals, $\mathsf{Q} \vdash \overline{n} + \overline{n} = \overline{2n}$.
The equality axioms then give, for $n = 3$,
$$\mathsf{Q} \vdash \forall y\,(y = \overline{3} + \overline{3} \leftrightarrow y = \overline{6}).$$
Here uniqueness came free, because $y$ stands alone on one side of the equation.
For the pairing function above, or for a function defined by a search such as "the least prime above $n$", it does not, and [[the proof|4T3MSP1SPK]] has to modify the formula.
The trap is to take "$T \vdash \varphi(\overline{n}, \overline{f(n)})$ for each $n$" as representability, since the theory must also exclude every other output.

### L3 human

Books use two notions of representability for functions, and the theorem gives both.
The version above, with $\forall y$, is called functional or strong representability.
The weaker version asks only for $T \vdash \varphi(\overline{n}, \overline{f(n)})$ and $T \vdash \neg \varphi(\overline{n}, \overline{m})$ for $m \ne f(n)$, which is representability of the graph as a relation.
For extensions of $\mathsf{Q}$ the two agree, because the formula $\varphi(x, y) \land \forall z < y\, \neg \varphi(x, z)$ turns a weak representation into a strong one.
The proof uses that $\mathsf{Q}$ can list the numbers below a numeral and compare every element with a numeral.
The representing formula can be taken $\Sigma_1$, which places the whole computation in the part of arithmetic where $\mathsf{Q}$ is complete.
