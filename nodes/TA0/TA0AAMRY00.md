---
tag: TA0AAMRY00
kind: example
name: Stages of the accessible part of an order of type ω+1
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [5C4YBXQV15]
uses: [5C4YBXQV15, CRP7Z3M9XD, 45GQ3KQVT3, DBD64TH52D, 0YSCSX5YZC, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_logic
    locator: Least fixed-point logic
  - url: https://en.wikipedia.org/wiki/Well-founded_relation
    locator: Induction and recursion
---

## Example

We compute the stages of an inductive definition, in the notation of the page on [[local predicativity|5C4YBXQV15]]: $I^\alpha = \Gamma(I^{<\alpha})$ and $I^{<\alpha} = \bigcup_{\beta < \alpha} I^\beta$.
Let $\prec'$ be the order on $\mathbb{N}$ with $n \prec' m$ if and only if ($m = 0$ and $n \ge 1$) or ($1 \le n < m$).
So $1 \prec' 2 \prec' 3 \prec' \cdots$, and $0$ lies above all the other numbers.
Let $A(X, x) = \forall y \, (y \prec' x \to X(y))$, as for the [[accessible part|CRP7Z3M9XD]], and let $\Gamma(S) = \set{x : A(S, x)}$.
So $x \in \Gamma(S)$ exactly when all $\prec'$-predecessors of $x$ are in $S$.

1. Predecessors. The number $1$ has no predecessors. A number $m \ge 2$ has the predecessors $1, \dots, m - 1$. The number $0$ has the predecessors $1, 2, 3, \dots$.
2. Stage $0$. $I^{<0} = \emptyset$, and only $1$ has all its predecessors in $\emptyset$. So $I^0 = \set{1}$.
3. Finite stages. We show $I^k = \set{1, \dots, k + 1}$ by induction on $k$. Assume it for all $j < k$, with $k \ge 1$. Then $I^{<k} = \set{1, \dots, k}$.
4. A number $m \ge 1$ is in $\Gamma(\set{1, \dots, k})$ if and only if $m - 1 \le k$, by step 1. The number $0$ is not, because its predecessor $k + 1$ is missing. So $I^k = \set{1, \dots, k + 1}$.
5. Stage $\omega$. $I^{<\omega} = \set{1, 2, 3, \dots}$ contains all predecessors of every number, so $I^\omega = \mathbb{N}$.
6. Later stages. $\Gamma(\mathbb{N}) = \mathbb{N}$, so $I^\alpha = \mathbb{N}$ for every $\alpha \ge \omega$, by induction on $\alpha$.
7. The fixed point. $\mathbb{N}$ is a fixed point of $\Gamma$, and it is the [[least fixed point|DBD64TH52D]], because every fixed point $S$ contains each stage, by induction on $\alpha$. So $I = \mathbb{N}$.
8. Stages of the elements. The stage of $m \ge 1$ is $m - 1$, and the stage of $0$ is $\omega$, by steps 2 to 5.
9. Closure ordinal. The least $\alpha$ with $I^\alpha \subseteq I^{<\alpha}$ is $\omega + 1$: the stage $I^\omega$ adds $0$, and $I^{\omega+1}$ adds nothing. This is the order type of $(\mathbb{N}, \prec')$.

## Remarks

The example shows that the stage of an element is the order type of its predecessors.
This holds for every well-order.
An element $x$ is in $I^\alpha$ exactly when every $y \prec' x$ has a stage below $\alpha$.
So the stage of $x$ is the least ordinal above all stages of its predecessors, and induction along the order gives the order type.
For the usual order $<$ on $\mathbb{N}$ the stages are $I^n = \set{0, \dots, n}$, and the closure ordinal is $\omega$.
For an order with an infinite descending chain, the elements on the chain never enter, because the [[well-founded part|0DQPNJNPYK]] does not contain them.
A recursive well-order of type $\alpha$ gives a recursive operator whose closure ordinal is $\alpha$.
So the stages of recursive operators reach every recursive [[ordinal|0YSCSX5YZC]].
This is why $\Omega$ stands for the least non-recursive ordinal in the analysis of $\mathrm{ID}_1$.
Each stage $I^\alpha$ is defined from the earlier stages only, and this is the local predicativity of the stage hierarchy.

## Explanations

### L1 human

Imagine a queue in which a person may enter only after everyone in front of them has entered.
The numbers $1, 2, 3, \dots$ stand in a line, and the number $0$ stands behind all of them.
At step $0$ the first person, $1$, enters; at step $1$ the person $2$ enters, and so on.
The person $0$ must wait until all the others are in, so $0$ enters only after infinitely many steps.
The number of steps that the whole queue needs is "infinity plus one", the ordinal $\omega + 1$.

### L2 human

We repeat the computation for an order of type $\omega + 2$.
Let $n \prec'' m$ if and only if ($m \in \set{0, 1}$ and $n \ge 2$) or ($m = 0$ and $n = 1$) or ($2 \le n < m$).
So $2 \prec'' 3 \prec'' 4 \prec'' \cdots \prec'' 1 \prec'' 0$.

1. Only $2$ has no predecessors, so $I^0 = \set{2}$.
2. $I^k = \set{2, \dots, k + 2}$ for each $k < \omega$, by the induction of steps 3 and 4.
3. $I^{<\omega} = \set{2, 3, 4, \dots}$. This set contains all predecessors of $1$, but not the predecessor $1$ of $0$. So $I^\omega = \set{1, 2, 3, \dots}$.
4. $I^{\omega+1} = \mathbb{N}$, because now $1$ is in.
5. So the stage of $1$ is $\omega$, the stage of $0$ is $\omega + 1$, and the closure ordinal is $\omega + 2$.

The typical use of stages is to measure an inductive definition by an ordinal, and in proof theory to bound the length of a derivation of $t \in I$.
The trap is the convention: with $I^0 = \Gamma(\emptyset)$, the least element has stage $0$, and the closure ordinal is the order type, not the order type plus one.
