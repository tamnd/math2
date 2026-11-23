---
tag: NSEE4QP6JV
kind: example
name: The chain-antichain principle implies the ascending or descending sequence principle
msc: ["03B30", "03F35", "06A05"]
topics: [BY8AAFN7C5]
audience: research
instance_of: [E3X5B175ZR]
uses: [E3X5B175ZR, XQENB067R3, 0QV2JS9RJ3, 0FRXBVVR03, 03HF498P1J]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Additional systems
  - url: https://en.wikipedia.org/wiki/Ramsey%27s_theorem
    locator: Reverse mathematics
---

## Example

A linear order on $\mathbb{N}$ and the usual order of the numbers either agree or disagree on each pair, and a partial order can record exactly where they agree.
We use this to prove $\mathrm{CAC} \to \mathrm{ADS}$ over [[RCA0|XQENB067R3]], an arrow of the [[reverse mathematics zoo|E3X5B175ZR]] found by Hirschfeldt and Shore.
Let $(L, \prec)$ be a [[linear order|0FRXBVVR03]] with $L \subseteq \mathbb{N}$ infinite, and write $x \preceq y$ for "$x \prec y$ or $x = y$".
An *ascending sequence* is an infinite set $S \subseteq L$ with $x \prec y$ for all $x < y$ in $S$, and a *descending sequence* is one with $y \prec x$ for all $x < y$ in $S$.
$\mathrm{ADS}$ says that every such $(L, \prec)$ has an ascending or a descending sequence.
We argue in $\mathsf{RCA}_0 + \mathrm{CAC}$.

1. Define $x \trianglelefteq y$ if and only if $x \le y$ and $x \preceq y$.
   The relation exists by $\Delta^0_1$ comprehension, since its definition has no unbounded quantifier.
2. $\trianglelefteq$ is reflexive, because $x \le x$ and $x \preceq x$.
3. $\trianglelefteq$ is antisymmetric, because $x \trianglelefteq y$ and $y \trianglelefteq x$ give $x \le y \le x$.
4. $\trianglelefteq$ is transitive, because both $\le$ and $\preceq$ are transitive.
   So $(L, \trianglelefteq)$ is an infinite [[partial order|0QV2JS9RJ3]].
5. By $\mathrm{CAC}$ there is an infinite set $C \subseteq L$ that is a chain or an [[antichain|03HF498P1J]] for $\trianglelefteq$.
6. Let $C$ be a chain and let $x < y$ be in $C$.
   Then $y \trianglelefteq x$ fails because $y \le x$ fails, so $x \trianglelefteq y$, and $x \prec y$ since $x \ne y$; so $C$ is ascending.
7. Let $C$ be an antichain and let $x < y$ be in $C$.
   Then $x \trianglelefteq y$ fails while $x \le y$ holds, so $x \preceq y$ fails, and $y \prec x$ because $\prec$ is linear; so $C$ is descending.

Steps 6 and 7 cover both cases, so $(L, \prec)$ has an ascending or a descending sequence, which is $\mathrm{ADS}$.

## Remarks

The relation of step 1 is the intersection of two linear orders, the order of the numbers and the order $\prec$.
A chain is a set where the two orders agree, and an antichain is a set where they disagree.
Hirschfeldt and Shore asked whether $\mathrm{ADS}$ implies $\mathrm{CAC}$, and Lerman, Solomon and Towsner showed that it does not.
The same proof with a finite form of $\mathrm{CAC}$ gives a classical theorem.
A partial order with $n^2 + 1$ elements has a chain or an antichain with $n + 1$ elements, by Dilworth's theorem.
So a list of $n^2 + 1$ distinct numbers has an increasing or a decreasing sub-list of length $n + 1$, which is the Erdős-Szekeres theorem.
Watch out for step 7: it uses that $\prec$ is linear, and for a partial order $\prec$ an incomparable pair would give neither direction.

## Explanations

### L1 human

Write a list of different numbers, for example $5, 2, 8, 1, 9, 3$.
Two positions agree when the later number is larger, and they disagree when it is smaller.
A set of positions that all agree gives a rising sub-list, such as $5, 8, 9$.
A set of positions that all disagree gives a falling sub-list, such as $5, 2, 1$.
The chain-antichain principle finds an endless set of one of the two kinds.

### L2 human

Order $\mathbb{N}$ by putting the even numbers first in increasing order and then the odd numbers in decreasing order:
$$0 \prec 2 \prec 4 \prec \cdots \prec 5 \prec 3 \prec 1.$$
For even $x < y$ we have $x \prec y$, so $x \trianglelefteq y$, and the even numbers form a chain.
For odd $x < y$ we have $y \prec x$, so neither $x \trianglelefteq y$ nor $y \trianglelefteq x$, and the odd numbers form an antichain.
Check with step 6 and step 7: the even numbers ascend and the odd numbers descend, as they should.
The typical use is to show that a principle about linear orders is no stronger than a principle about partial orders.
The trap is to think that the chain must be an ascending sequence in the order of the numbers too; it is, but only because step 1 built that order into $\trianglelefteq$.
