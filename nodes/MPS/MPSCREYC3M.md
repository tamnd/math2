---
tag: MPSCREYC3M
kind: example
name: First-order Peano arithmetic as a theory
msc: ["03B10", "03F30"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [92SWXST1ZM]
uses: [92SWXST1ZM, FZRMYTQFRR, DKFGQTRYZE, 0QFT7Z76N5, 1QD0KDDGYJ, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Peano arithmetic as first-order theory
  - book: isbn:9781482237726
    locator: Chapter 3
---

## Example

Let $\sigma = \set{0, S, +, \cdot}$ with arities $0, 1, 2, 2$.
Peano arithmetic $\mathrm{PA}$ is the set of the following $\sigma$-sentences.

- (A1) $\forall x \, \neg (S(x) = 0)$.
- (A2) $\forall x \, \forall y \, (S(x) = S(y) \to x = y)$.
- (A3) $\forall x \, (x + 0 = x)$.
- (A4) $\forall x \, \forall y \, (x + S(y) = S(x + y))$.
- (A5) $\forall x \, (x \cdot 0 = 0)$.
- (A6) $\forall x \, \forall y \, (x \cdot S(y) = x \cdot y + x)$.
- (Ind) For each formula $\varphi$ with $\operatorname{FV}(\varphi) \subseteq \set{x, y_1, \dots, y_k}$, the sentence $\forall y_1 \cdots \forall y_k \, \big( (\varphi[0/x] \land \forall x \, (\varphi \to \varphi[S(x)/x])) \to \forall x \, \varphi \big)$.

We check that $\mathrm{PA}$ is a [[first-order theory|92SWXST1ZM]] and that $\N$ is a model.

1. In (A1) to (A6) every variable is bound by a quantifier in front, so each is a [[sentence|DKFGQTRYZE]].
2. In (Ind), the term $0$ has no variables, so no capture occurs in $\varphi[0/x]$. A free occurrence of $x$ never lies in the scope of a quantifier on $x$, so no capture occurs in $\varphi[S(x)/x]$ either.
3. The free variables of the three parts lie in $\set{x, y_1, \dots, y_k}$. The variable $x$ is not free in $\varphi[0/x]$, it is bound by $\forall x$ in the other two parts, and the prefix binds $y_1, \dots, y_k$. So each instance is a sentence.
4. So $\mathrm{PA}$ is a set of $\sigma$-sentences, that is, a theory, by the [[definition|FZRMYTQFRR]].
5. There is one instance of (Ind) for each formula $\varphi$ and each list of its parameters, so $\mathrm{PA}$ is infinite. It is [[countable|01TQB88H4C]], since $\sigma$ is finite.
6. In $\N$ with the usual $0$, successor, sum and product, axioms (A1) to (A6) are the usual facts about these operations.
7. For an instance of (Ind), fix values of $y_1, \dots, y_k$ and let $A$ be the set of $n \in \N$ that satisfy $\varphi$ at $x = n$. The hypothesis says $0 \in A$ and that $n \in A$ implies $n + 1 \in A$. By induction in $\N$, $A = \N$, so $\N$ satisfies the instance.

So $\mathrm{PA}$ is a countably infinite first-order theory, and $\N$ is a model of it.

## Remarks

The second-order [[Peano axioms|0QFT7Z76N5]] have one induction axiom about all subsets of $\N$.
The [[induction schema|1QD0KDDGYJ]] replaces it with one sentence for each formula, which covers only the definable subsets.
So $\mathrm{PA}$ has nonstandard models, which are not isomorphic to $\N$, by the compactness theorem.
The set $\mathrm{PA}$ is decidable: one can check by an algorithm whether a string is an axiom.
By Gödel's first incompleteness theorem, $\mathrm{PA}$ is not complete, if it is consistent.

## Explanations

### L1 human

Peano arithmetic writes the basic facts about $0$, "the next number", addition and multiplication as formal sentences.
For example, (A3) says $x + 0 = x$ for every $x$.
The induction rule cannot be one sentence in first-order logic, so there is one sentence for each property that a formula can express.
The natural numbers satisfy all these sentences.

### L2 human

We write the instance of (Ind) for the formula $\varphi = (0 + x = x)$, with no parameters.

1. $\varphi[0/x]$ is $0 + 0 = 0$.
2. $\varphi[S(x)/x]$ is $0 + S(x) = S(x)$.
3. The instance is $\big(0 + 0 = 0 \land \forall x \, (0 + x = x \to 0 + S(x) = S(x))\big) \to \forall x \, (0 + x = x)$.
4. From (A3), $0 + 0 = 0$. From (A4), $0 + S(x) = S(0 + x)$, which is $S(x)$ when $0 + x = x$.
5. So $\mathrm{PA}$ proves $\forall x \, (0 + x = x)$, a law that is not among (A1) to (A6).

The typical use of the schema is to prove general laws, such as commutativity of $+$, inside $\mathrm{PA}$.
A trap: the schema has infinitely many axioms, so $\mathrm{PA}$ is not a finite list, and in fact it is not finitely axiomatizable.
