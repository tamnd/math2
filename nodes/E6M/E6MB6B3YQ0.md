---
tag: E6MB6B3YQ0
kind: definition
name: Realizability
msc: ["03F50", "03F55", "03D80"]
defines: 4H35VQ16DC
uses: [RXHJPVMPJH, CK8ZQRN183, KZSB5E471K, 7B53ZGXXEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Realizability
---

## Definition

Let $\{e\}$ denote the partial [[computable function|KZSB5E471K]] with code $e \in \N$, and write $\{e\}(n)\downarrow$ when it is defined at $n$.
Fix a computable pairing of natural numbers with projections $(e)_0$ and $(e)_1$.
*Number realizability* is the relation "$e$ realizes $A$", written $e \Vdash A$, between a number $e$ and a closed formula $A$ of [[Heyting arithmetic|RXHJPVMPJH]].
It is defined by induction on $A$.

1. $e \Vdash (s = t)$ if $s = t$ is true. No number realizes $0 = 1$.
2. $e \Vdash A \wedge B$ if $(e)_0 \Vdash A$ and $(e)_1 \Vdash B$.
3. $e \Vdash A \vee B$ if either $(e)_0 = 0$ and $(e)_1 \Vdash A$, or $(e)_0 \ne 0$ and $(e)_1 \Vdash B$.
4. $e \Vdash A \to B$ if for every $n$ with $n \Vdash A$, $\{e\}(n)\downarrow$ and $\{e\}(n) \Vdash B$.
5. $e \Vdash \exists x\, A(x)$ if $(e)_1 \Vdash A(\overline{(e)_0})$, where $\overline{k}$ is the numeral of $k$.
6. $e \Vdash \forall x\, A(x)$ if for every $n$, $\{e\}(n)\downarrow$ and $\{e\}(n) \Vdash A(\overline{n})$.

A closed formula is *realizable* if some number realizes it.
Negation $\neg A$ is read as $A \to (0 = 1)$.

## Remarks

Soundness theorem (Kleene): if Heyting arithmetic proves a closed formula $A$, then $A$ is realizable.
Example: $\forall x\, \exists y\, (y = x + x)$ is realized by a code $e$ of a total function with $\{e\}(n) = \langle 2n, 0 \rangle$.
Indeed, $\{e\}(n)$ is defined, its first part is $2n$, and its second part realizes the true equation $2n = n + n$ by clause 1.
Non-example: let $H(x)$ say that the program $x$ halts on input $x$.
A realizer of $\forall x\, (H(x) \vee \neg H(x))$ would compute, from $x$, a bit telling whether $H(x)$ holds, and so solve the halting problem.
So this instance of the law of excluded middle is not realizable, and hence not provable in Heyting arithmetic.
Many variants exist, such as realizability by functions, by terms of a typed calculus, and in toposes.
