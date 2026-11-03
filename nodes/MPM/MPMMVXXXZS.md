---
tag: MPMMVXXXZS
kind: definition
name: Knuth–Bendix completion
msc: [68Q42, 68V15, 03D03]
defines: 4JKD5FBJCS
uses: [A6J731Y193, Y83TQF6V6A, EDHK5KSGHY, WWKVNYM6AX, 0DQPNJNPYK]
sources:
  - url: https://en.wikipedia.org/wiki/Knuth–Bendix_completion_algorithm
---

## Definition

Let $T$ be the set of terms over a signature and a set of variables.
Let $E$ be a finite set of equations $s \approx t$ between terms.
Let $>$ be a *reduction order* on $T$, that is, a strict order with these properties.
It is [[well-founded|0DQPNJNPYK]], and $s > t$ implies $C[s] > C[t]$ for every context $C$ and $\sigma(s) > \sigma(t)$ for every substitution $\sigma$.
Let $l_1 \to r_1$ and $l_2 \to r_2$ be rules with disjoint variables.
Let $p$ be a position of $l_1$ where the subterm $l_1|_p$ is not a variable and has a most general unifier $\sigma$ with $l_2$.
Then the pair $(\sigma(r_1), \sigma(l_1)[\sigma(r_2)]_p)$ is a *critical pair*.
The *Knuth–Bendix completion* procedure, with input $E$ and $>$, maintains a set $R$ of rules of a [[term rewriting system|A6J731Y193]]:

1. To orient an equation $s \approx t$ with $s \ne t$: add $s \to t$ to $R$ if $s > t$, add $t \to s$ if $t > s$, and stop with failure otherwise.
2. Start with $R = \emptyset$ and orient every equation of $E$.
3. For each critical pair $(s, t)$ of rules of $R$, compute normal forms $s'$ of $s$ and $t'$ of $t$ with respect to $R$.
   If $s' \ne t'$, orient $s' \approx t'$.
4. Repeat step 3 until every critical pair of $R$ has equal normal forms, and then stop with output $R$.

## Remarks

If the procedure stops with output $R$, then $R$ is terminating, since $l > r$ for every rule, and [[confluent|EDHK5KSGHY]].
Indeed, a terminating term rewriting system whose critical pairs are joinable is locally confluent, and [[Newman's lemma|WWKVNYM6AX]] gives confluence.
Moreover $s \approx t$ follows from $E$ if and only if $s$ and $t$ have the same normal form with respect to $R$.
Example: for the group axioms $e \cdot x \approx x$, $x^{-1} \cdot x \approx e$, $(x \cdot y) \cdot z \approx x \cdot (y \cdot z)$ and a suitable reduction order, completion stops with ten rules, among them $x \cdot x^{-1} \to e$, $(x^{-1})^{-1} \to x$ and $(x \cdot y)^{-1} \to y^{-1} \cdot x^{-1}$.
Non-example: for $E = \set{x \cdot y \approx y \cdot x}$ the procedure fails in step 1 for every reduction order, since $x \cdot y > y \cdot x$ would give $y \cdot x > x \cdot y$ by the substitution exchanging $x$ and $y$.
The procedure can also run forever, adding infinitely many rules.
Practical versions also simplify and delete rules during the run.
