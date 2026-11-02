---
tag: MB1K62QDM4
kind: definition
name: Krull dimension of a noncommutative ring
msc: [16P40, 16P70]
defines: PP11DV3ZMQ
uses: [0B1261B5ED, 0NZ8JA25WK, 05WDSN597C, 0YSCSX5YZC, YQNZTQGP1X, AK1ZRCXR32, MVGBS3J1P7]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_dimension
    locator: For non-commutative rings
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $M$ be a right $R$-[[module|0NZ8JA25WK]].
The *Krull dimension* $\operatorname{Kdim} M$, when it exists, is an [[ordinal|0YSCSX5YZC]] or $-1$, defined by transfinite recursion as follows.

1. $\operatorname{Kdim} M = -1$ if and only if $M = 0$.
2. For an ordinal $\alpha \ge 0$, $\operatorname{Kdim} M \le \alpha$ if, for every descending chain $M_0 \supseteq M_1 \supseteq M_2 \supseteq \cdots$ of [[submodules|05WDSN597C]] of $M$, there is $N$ such that $\operatorname{Kdim}(M_i / M_{i+1}) < \alpha$ for all $i \ge N$.
3. $\operatorname{Kdim} M = \alpha$ if $\operatorname{Kdim} M \le \alpha$ and $\operatorname{Kdim} M \not\le \beta$ for every $\beta < \alpha$.

If no ordinal $\alpha$ satisfies $\operatorname{Kdim} M \le \alpha$, then $M$ has no Krull dimension.
The *right Krull dimension* of $R$ is $\operatorname{Kdim} R_R$, the Krull dimension of $R$ as a right module over itself.

## Remarks

From clause 2 with $\alpha = 0$, a module has Krull dimension $0$ exactly when it is nonzero and [[Artinian|YQNZTQGP1X]]: the factors of every descending chain are eventually $0$.

Example: $\operatorname{Kdim} \Z_\Z = 1$.
Take a descending chain $M_0 \supseteq M_1 \supseteq \cdots$ of subgroups of $\Z$.
If every $M_i = a_i\Z$ is nonzero, every factor $M_i / M_{i+1}$ is finite, hence Artinian.
Otherwise some $M_i = 0$, and all later factors are $0$.
So $\operatorname{Kdim} \Z \le 1$, and $\Z$ is not Artinian, so $\operatorname{Kdim} \Z = 1$.

Non-example: an infinite-dimensional vector space $V$ over a field has no Krull dimension.
Splitting a basis into infinitely many infinite parts gives a descending chain $V \supsetneq M_1 \supsetneq M_2 \supsetneq \cdots$ in which every factor is infinite-dimensional.
So an induction on $\alpha$ shows that $\operatorname{Kdim} V \le \alpha$ fails for every ordinal $\alpha$.

Every [[Noetherian module|AK1ZRCXR32]] has a Krull dimension.
For a commutative Noetherian ring, the Krull dimension defined here equals the classical [[Krull dimension|MVGBS3J1P7]] given by chains of prime ideals.
The definition is the deviation of the partially ordered set of submodules of $M$.
