---
tag: ~dbbd338b
kind: example
name: The accessible part of an order as an inductive definition
msc: ["03F15", "03F35"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [5VNT564Y2W]
uses: [~cd19a8f1, 0DQPNJNPYK, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Theories_of_iterated_inductive_definitions
    locator: ID<sub>1</sub>
  - url: https://en.wikipedia.org/wiki/Well-founded_relation
    locator: Induction and recursion
---

## Example

Let $\prec$ be a binary relation on $\mathbb{N}$ given by a formula $x \prec y$ of arithmetic.
Let $A(X, x) = \forall y \, (y \prec x \to X(y))$.
We check that $A$ gives a predicate $I_A$ of $\mathrm{ID}_1$ in the sense of the [[definition|~cd19a8f1]], and we compute $I_A$ in three cases.

1. Positivity. Written without $\to$, the formula is $\forall y \, (\neg (y \prec x) \vee X(y))$. The negation stands only on $y \prec x$, so $X$ occurs positively.
2. Meaning. In the standard model, $I_A$ is the least set $S$ such that $x \in S$ whenever all $\prec$-predecessors of $x$ are in $S$. This set is the accessible part, or [[well-founded part|0DQPNJNPYK]], of $\prec$.
3. Transfinite induction. Let $F(x)$ be any formula with $\forall x \, (\forall y \, (y \prec x \to F(y)) \to F(x))$. This hypothesis is $\forall x \, (A(F, x) \to F(x))$, so $(\mathrm{ID}^2_A)$ gives $\forall x \, (I_A(x) \to F(x))$. So $\mathrm{ID}_1$ proves [[transfinite induction|0ZHQMQ2C1N]] along $\prec$ restricted to $I_A$, for every formula.
4. Case $\prec$ is $<$ on $\mathbb{N}$. We prove $\forall x \, I_A(x)$ in $\mathrm{ID}_1$ by complete induction on $x$. Assume $I_A(y)$ for all $y < x$. This is $A(I_A, x)$, so $(\mathrm{ID}^1_A)$ gives $I_A(x)$. So $I_A = \mathbb{N}$.
5. Case $y \prec x$ if and only if $y = x + 1$. This relation has the infinite descending chain $0 \succ 1 \succ 2 \succ \cdots$. Take $F(x)$ to be $x \ne x$. Then $A(F, x)$ is $\forall y \, (y = x + 1 \to y \ne y)$, which is false. So $A(F, x) \to F(x)$ holds, and $(\mathrm{ID}^2_A)$ gives $\forall x \, \neg I_A(x)$. So $I_A = \emptyset$.
6. Case $\prec$ is the empty relation. Then $A(X, x)$ is true for every $X$, and $(\mathrm{ID}^1_A)$ gives $I_A(x)$ for all $x$. Every element is accessible at once, because it has no predecessors.

## Remarks

The example shows the main use of $\mathrm{ID}_1$ in ordinal analysis.
If $\prec$ is the order of an ordinal notation system, then every notation in $I_A$ supports transfinite induction for all formulas.
The lower bound for the ordinal of $\mathrm{ID}_1$ comes from proofs of $I_A(a)$ for the notations $a$ below the [[Bachmann-Howard ordinal|~fcf34cb0]].
For a relation with an infinite descending chain, every element of the chain stays outside $I_A$, when the chain is definable: apply the argument of step 5 to the formula "$x$ is not on the chain".
The [[stages|~a1b984d8]] of the definition can need infinitely many rounds, even for simple orders.

## Explanations

### L1 human

Think of a ladder where you can stand on a rung only if every rung below it is safe.
The bottom rung has nothing below it, so it is safe.
Then the next rung is safe, and so on: for the usual order of numbers, every rung becomes safe.
If the ladder goes down forever, no rung ever becomes safe, because there is always one more rung below to check.
The accessible part is the set of safe rungs.

### L2 human

We find the accessible part of the relation $\prec$ on $\set{0, 1, 2}$ with $1 \prec 0$, $2 \prec 1$ and $1 \prec 2$.

1. The element $0$ is accessible only if $1$ is accessible.
2. The element $1$ is accessible only if $2$ is accessible, and $2$ is accessible only if $1$ is accessible.
3. The empty set is closed under $A$: $A(\emptyset, x)$ holds only when $x$ has no predecessor, and each of $0, 1, 2$ has a predecessor.
4. By minimality the accessible part is contained in $\emptyset$, so it is empty. The cycle $1 \prec 2 \prec 1$ blocks $1$ and $2$, and $0$ depends on $1$.

The typical use is the transfinite induction of step 3.
The trap is to use only the closure axiom: it shows that elements are accessible, and the minimality scheme is needed to show that an element is not accessible.
