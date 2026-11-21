---
tag: BFK4T1WK38
kind: example
name: Divisible torsion-free abelian groups have quantifier elimination
aliases: [quantifier-elimination-for-modules-and-abelian-groups, divisible-torsion-free-abelian-groups-quantifier-elimination]
msc: ["03C10", "03C60", "20K15"]
topics: [1A9JSC5YG8]
audience: grad
instance_of: [7FDDXV3JK7]
uses: [Q1CGE4DWXQ, 082GHNPJ53, ZXVBEPMTCN, PEMNN32A43, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $L = \set{0, +, -}$ and let $T$ be the theory of nontrivial, [[torsion-free|PEMNN32A43]], [[divisible|ZXVBEPMTCN]] [[abelian groups|082GHNPJ53]].
Its models are the nonzero [[vector spaces|000AYPA9AJ]] over $\Q$.
We show that $T$ has quantifier elimination by the one-quantifier test of [[the tests for quantifier elimination|Q1CGE4DWXQ]].
Let $\varphi(\bar x, y)$ be a conjunction of literals.

1. Every term is equal modulo $T$ to $k y + t(\bar x)$ with $k \in \Z$ and $t$ a term in $\bar x$. So each literal is $k y = t$ or $k y \neq t$. Literals with $k = 0$ do not mention $y$, and we can move them outside $\exists y$.
2. Case 1: some literal is an equation $k y = t$ with $k \neq 0$. In a model, $y = t / k$ exists and is unique, by divisibility and torsion-freeness.
3. Another literal $k' y = t'$ holds at $y = t / k$ if and only if $k' t = k t'$, since multiplication by $k$ is injective. The same holds for $k' y \neq t'$ with $\neq$.
4. So in Case 1, $\exists y \, \varphi$ is equivalent modulo $T$ to the conjunction of the literals $k' t = k t'$ and $k' t \neq k t'$, one for each other literal.
5. Case 2: all literals with $k \neq 0$ are inequations $k_j y \neq t_j$. Each excludes at most one value of $y$, by torsion-freeness.
6. A nonzero vector space over $\Q$ is infinite, so some $y$ avoids the finitely many excluded values. Hence $\exists y \, \varphi$ is equivalent modulo $T$ to true, together with the literals moved out in step 1.

So $T$ has quantifier elimination.

## Remarks

The example shows the simplest pattern of elimination: solve an equation if there is one, otherwise use that each inequation excludes few values.
It gives that $T$ is complete, since the quantifier-free sentences are $0 = 0$ and its negation, and that the definable subsets of a model in one variable are finite or cofinite.

When the theory changes, the result changes in this way.

- Torsion-free abelian groups that are not divisible: $(\Z, 0, +, -)$ has no quantifier elimination, since $\exists y \, (x = y + y)$ defines the even numbers, an infinite and coinfinite set.
- Divisible ordered abelian groups: with the order added, quantifier elimination still holds, and solutions of inequalities are found as midpoints and by going beyond the bounds.
- Infinite vector spaces over a finite field $\mathbb F_p$, as groups of exponent $p$: the same steps work, with $k$ taken modulo $p$.
- Abelian groups in general: Szmielew's invariants determine [[the complete theories|Y0753DF5R9]], and for modules over a ring, the Baur-Monk theorem reduces every formula to a Boolean combination of positive primitive formulas and invariant sentences.

## Explanations

### L1 human

In the rational numbers with addition, a question like "is there $y$ with $2y = x$ and $3y \neq z$?" can be answered without searching for $y$.
The only candidate is $y = x / 2$, so the question is the same as "$3x \neq 2z$".
If there is no equation, almost every $y$ works, and the answer is yes.

### L2 human

We eliminate the quantifier in $\exists y \, (2 y = x \land 3 y \neq z \land y \neq w)$.

1. The equation $2 y = x$ gives $y = x / 2$.
2. The literal $3 y \neq z$ becomes $3 x \neq 2 z$, after multiplying by $2$.
3. The literal $y \neq w$ becomes $x \neq 2 w$.
4. So the formula is equivalent to $3 x \neq 2 z \land x \neq 2 w$.
5. Check: $x = 2$, $z = 3$, $w = 0$ gives $y = 1$, $3 \neq 3$ fails, and indeed $6 \neq 6$ fails.

The typical use is as the model case for quantifier elimination in linear algebra.
A trap is to forget torsion-freeness: in a group with elements of order $2$, the equation $2 y = x$ can have several solutions.
