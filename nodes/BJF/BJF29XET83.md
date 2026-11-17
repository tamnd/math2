---
tag: BJF29XET83
kind: statement
role: theorem
name: Representability of recursive functions in Robinson arithmetic
aliases: [representability-theorem, representability-in-arithmetic]
msc: ["03F30", "03D20"]
topics: [QHCRN4JVG0]
audience: grad
uses: [TT8MXRTVBM, VM8TQ70CVJ, Q5MT8WY7JM, HBK5QHC1GC, Y0JTZXBRT5, 69234Z1V00, BM6P0C2AC2, 1DQ1M6ZWS4, TN9G24VABN, 3PRW76471J, X9WYNYE29C, YRV6SYK2BY, TKDKW5MENB, ~14d8268c]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - book: isbn:9781482237726
  - url: https://builds.openlogicproject.org/
    locator: Representability in Q
---

## Statement

Let $T$ be a theory in the language $L_A$ that extends [[Robinson arithmetic|TT8MXRTVBM]] $\mathsf{Q}$.

A function $f : \N^k \to \N$ is *representable* in $T$ if there is a formula $\varphi(x_1, \ldots, x_k, y)$ such that for all $n_1, \ldots, n_k \in \N$,
$$T \vdash \forall y\,\bigl(\varphi(\overline{n_1}, \ldots, \overline{n_k}, y) \leftrightarrow y = \overline{f(n_1, \ldots, n_k)}\bigr).$$
A relation $R \subseteq \N^k$ is *representable* in $T$ if there is a formula $\psi(x_1, \ldots, x_k)$ such that $T \vdash \psi(\overline{n_1}, \ldots, \overline{n_k})$ when $(n_1, \ldots, n_k) \in R$, and $T \vdash \neg \psi(\overline{n_1}, \ldots, \overline{n_k})$ when $(n_1, \ldots, n_k) \notin R$.

**Theorem.**

1. Every total [[recursive function|HBK5QHC1GC]] is representable in $\mathsf{Q}$ by a $\Sigma_1$ formula, and hence in $T$.
2. Every recursive relation is representable in $\mathsf{Q}$, and hence in $T$.
3. If $T$ is [[consistent|VM8TQ70CVJ]] and recursively axiomatized, then every function and every relation that is representable in $T$ is recursive.

## Remarks

### Why each hypothesis is needed

- Part 1 needs a theory that can compute with $+$ and $\cdot$. The theory $\mathsf{Pr}$ of [[Presburger arithmetic|~14d8268c]] is complete and true in $(\N, 0, S, +, <)$. A formula representing the recursive relation "$x$ is a square" in $\mathsf{Pr}$ would define it in $(\N, 0, S, +, <)$, and [[no formula does|TKDKW5MENB]].
- Part 3 needs consistency: in an inconsistent theory every formula represents every relation. It needs a recursive set of axioms, since the complete theory of $\mathfrak{N}$ is consistent and represents every relation definable in $\mathfrak{N}$, including the halting set.

### Converse

Part 3 is the converse of Parts 1 and 2.
For a consistent recursively axiomatized extension $T$ of $\mathsf{Q}$, the functions representable in $T$ are exactly the total recursive functions.
The relations representable in $T$ are exactly the recursive relations.

### Consequences

- *Weak representability.* A set $A \subseteq \N$ is weakly representable in $T$ if there is $\psi(x)$ with $T \vdash \psi(\overline{n})$ exactly when $n \in A$. The sets weakly representable in $\mathsf{Q}$ are exactly the [[computably enumerable|TN9G24VABN]] sets. A c.e. set is defined by a $\Sigma_1$ formula, which works by [[Σ1-completeness|69234Z1V00]] and the truth of $\mathsf{Q}$ in $\mathfrak{N}$. Conversely, a search through the proofs of $\mathsf{Q}$ enumerates $\set{n : \mathsf{Q} \vdash \psi(\overline{n})}$.
- *Definability versus representability.* A relation is [[definable|1DQ1M6ZWS4]] in $\mathfrak{N}$ when a formula is true exactly on it; it is representable in $T$ when $T$ proves the formula on it and refutes it off it.
- Every relation representable in $\mathsf{Q}$ is definable in $\mathfrak{N}$ by the same formula, since $\mathfrak{N} \models \mathsf{Q}$.
- The converse fails: the halting set is definable by a $\Sigma_1$ formula but is not recursive, so it is not representable in $\mathsf{Q}$.
- The function $n \mapsto$ (code of the result of substituting $\overline{n}$ in the formula with code $n$) is recursive, hence representable. This gives the [[diagonal lemma|3PRW76471J]], and with it [[Gödel's incompleteness theorems|X9WYNYE29C]] and [[Tarski's undefinability theorem|YRV6SYK2BY]].
- $\mathsf{Q}$ is essentially undecidable: no consistent extension of $\mathsf{Q}$ is decidable.

### Generalizations

The same proof works for every theory that proves the facts about numerals used in the proof, such as the theory $\mathsf{R}$ of [[weak theories of arithmetic|Q5MT8WY7JM]].
Part 1 for primitive recursive functions holds with formulas whose totality $\forall \vec{x}\, \exists y\, \varphi$ is provable in $\mathsf{I}\Sigma_1$.

## Explanations

### L1 human

A function is representable in a theory when the theory can compute it: for each input, the theory proves that a certain formula picks out exactly the right output.
The theorem says that the very weak theory $\mathsf{Q}$ can compute every computable function in this sense.
Conversely, a reasonable theory cannot compute more than the computable functions, since one can search through its proofs.
This link between proofs and computation is the starting point of Gödel's incompleteness theorems.

### L2 human

We represent the function $f(n) = 2n$ in $\mathsf{Q}$ by the formula $\varphi(x, y) := (y = x + x)$, which is $\Delta_0$.

1. Fix $n$. By $\mathsf{Q}4$ and $\mathsf{Q}5$ applied to numerals, $\mathsf{Q} \vdash \overline{n} + \overline{n} = \overline{2n}$.
2. So $\mathsf{Q} \vdash \forall y\,(y = \overline{n} + \overline{n} \leftrightarrow y = \overline{2n})$, by the equality axioms.
3. For $n = 3$: $\mathsf{Q} \vdash \forall y\,(y = \overline{3} + \overline{3} \leftrightarrow y = \overline{6})$.

For a function defined by a search, such as "the least prime above $n$", the formula that defines the graph in $\mathfrak{N}$ need not represent the function, and [[the proof|4T3MSP1SPK]] has to modify it.
A trap is to confuse "$T \vdash \varphi(\overline{n}, \overline{f(n)})$ for each $n$" with representability: the theory must also exclude every other output, inside a single formula with a free variable $y$.

### L3 human

Two notions of representability appear in the books, and both follow from the theorem.
The version above, with $\forall y$, is sometimes called functional or strong representability.
The weaker version asks for $T \vdash \varphi(\overline{n}, \overline{f(n)})$ and $T \vdash \neg \varphi(\overline{n}, \overline{m})$ for $m \ne f(n)$, which is representability of the graph as a relation.
For extensions of $\mathsf{Q}$ a function is representable in one sense exactly when it is in the other, because $\mathsf{Q}$ can list the numbers below a numeral and compare every number with a numeral; the strong form uses $\varphi(x, y) \land \forall z < y\, \neg \varphi(x, z)$.
The proof shows that the representing formula can be taken $\Sigma_1$, which places the whole computation in the part of arithmetic where $\mathsf{Q}$ is complete.
