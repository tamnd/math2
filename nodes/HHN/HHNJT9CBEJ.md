---
tag: HHNJT9CBEJ
kind: definition
name: Term rewriting for equational theories
msc: [68Q42, 08B05, 03B35]
defines: A6J731Y193
uses: [3YYKGWJJND, NCDZ969V7X, PKD440G2XW, F1M51B4MDG, WDHWCQ6Y2Y]
sources:
  - url: https://en.wikipedia.org/wiki/Rewriting
    locator: Term rewriting systems
---

## Definition

Let $\sigma$ be a signature and $X$ a set of variables.
Let $T(X)$ be the set of terms of $\sigma$ over $X$, as in the [[term algebra|3YYKGWJJND]].
A *term rewriting system* is a set $R$ of pairs $(l, r)$ of terms, written $l \to r$ and called rules.
Each rule must satisfy two conditions: $l$ is not a variable, and every variable of $r$ occurs in $l$.
For terms $s, t$, one writes $s \to_R t$ if there are a rule $l \to r$ in $R$ and a [[substitution|NCDZ969V7X]] $\tau$ with the following property.
The term $s$ contains $\tau(l)$ as a subterm, and $t$ is obtained from $s$ by replacing one occurrence of it by $\tau(r)$.
Let $\leftrightarrow_R^*$ be the smallest equivalence relation that contains $\to_R$.
The system $R$ *presents* the [[equational theory|F1M51B4MDG]] $E$ if, for all terms $s, t$, one has $s \leftrightarrow_R^* t$ if and only if $s \approx t$ belongs to $E$.
The system $R$ is *convergent* if:

1. it is terminating: there is no infinite chain $t_0 \to_R t_1 \to_R t_2 \to_R \cdots$;
2. it is [[confluent|EDHK5KSGHY]]: if $t \to_R^* u$ and $t \to_R^* v$, then $u \to_R^* w$ and $v \to_R^* w$ for some term $w$.

## Remarks

By [[Birkhoff's completeness theorem|WDHWCQ6Y2Y]], a system $R$ presents the theory axiomatised by the [[identities|PKD440G2XW]] $\set{l \approx r : (l \to r) \in R}$.
If $R$ is convergent, each term $t$ has a unique normal form $\operatorname{nf}(t)$, a term with no further rewrite step.
Then $s \approx t$ is in the theory if and only if $\operatorname{nf}(s) = \operatorname{nf}(t)$.
For a finite convergent system, this decides the equational theory.
Example: $R = \set{f(f(x)) \to x}$ is convergent: each step shortens the term, and the only overlap, in $f(f(f(x)))$, rewrites to $f(x)$ in both ways.
So $f^m(x) \approx f^n(x)$ holds in the theory of an involution exactly when $m$ and $n$ have the same parity.
Non-example: $R = \set{x \cdot y \to y \cdot x}$ presents the theory of a commutative operation but is not terminating, since $a \cdot b \to b \cdot a \to a \cdot b \to \cdots$.
The [[Knuth–Bendix completion|4JKD5FBJCS]] procedure tries to turn a set of identities into an equivalent convergent system.
