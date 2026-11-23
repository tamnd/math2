---
tag: N95EDP0DFS
kind: example
name: Substitution instances of a fixed proof have bounded depth
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
instance_of: [41QJ1WEMJ3]
uses: [41QJ1WEMJ3, J2BAR09TPF, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
---

## Example

Take a fixed Frege proof of $p \lor \neg p$, and replace $p$ everywhere by $x_1 \land x_2 \land \cdots \land x_n$.
The result is a proof of $(x_1 \land \cdots \land x_n) \lor \neg x_1 \lor \cdots \lor \neg x_n$ with the same number of lines, and its depth stays bounded as $n$ grows.

In detail, fix a [[Frege system|J2BAR09TPF]] $\mathcal F$ over $\neg, \land, \lor$, and a fixed $\mathcal F$-proof $\pi$ of $p \lor \neg p$.
Let $c$ be the largest depth of a line of $\pi$, and let $\ell$ be its number of lines.
For $n \ge 1$, let $\varphi_n = x_1 \land x_2 \land \cdots \land x_n$, a formula of depth $1$.

1. Apply the [[substitution|NCDZ969V7X]] $p \mapsto \varphi_n$ to every line of $\pi$.
   The result $\pi_n$ is an $\mathcal F$-proof of $\varphi_n \lor \neg \varphi_n$, since the rules of $\mathcal F$ are closed under substitution.
2. $\pi_n$ has $\ell$ lines, the same number for every $n$.
3. In each line of $\pi$, the literals $p$ and $\neg p$ sit at depth $0$, and they are replaced by $\varphi_n$ and $\neg \varphi_n$, which have depth $1$.
   So the gate tree of the line grows by at most one level, and merging blocks of the same connective can only lower it.
   Every line of $\pi_n$ has depth at most $c + 1$.
4. Each occurrence of $p$ becomes a formula with $2n - 1$ symbols, so each line grows by a factor of at most $2n$.
   So $\pi_n$ has size $O(n)$.

So $(\pi_n)$ is a [[bounded-depth Frege|41QJ1WEMJ3]] family of depth $c + 1$ and linear size.

*Depth of the conclusion.* By De Morgan's laws, $\neg \varphi_n$ is $\neg x_1 \lor \cdots \lor \neg x_n$, of depth $1$.
So $\varphi_n \lor \neg \varphi_n$ is an $\lor$-gate over one $\land$-gate and $n$ literals, of depth $2$.

## Remarks

### Why it works

The same argument works for every fixed proof and every substitution by formulas of depth at most $e$.
The depth of each line grows by at most $e$, so the family has depth at most $c + e$.
So every family of substitution instances of one fixed proof, by formulas of bounded depth, is a bounded-depth family.

### Watch out

The hard tautologies for bounded-depth Frege, such as the [[pigeonhole formulas|RJ571F7FF0]], are not of this kind.
They form a family in which the number of variables and the structure both grow, and no fixed proof covers them.
A short fixed proof of a schema, such as $p \lor \neg p$, gives bounded depth for free; the lower bounds are about families that need new reasoning for each $n$.

## Explanations

### L1 human

A short proof that "$p$ or not $p$" stays short when $p$ is replaced by a longer formula.
If the formula has small depth, the proof also keeps a small depth.
For example, with $p$ replaced by "$x_1$ and $x_2$ and $x_3$", the proof has the same number of lines and depth at most $1$ more.

### L2 human

We compute the depth of one substituted line.

1. Suppose $\pi$ contains the line $\neg p \lor (p \land q)$, of depth $2$.
2. Replace $p$ by $\varphi_n$, and the new line is $\neg \varphi_n \lor (\varphi_n \land q)$.
3. $\neg \varphi_n$ is the disjunction $\neg x_1 \lor \cdots \lor \neg x_n$, which merges with the outer $\lor$.
4. $\varphi_n \land q$ is the conjunction $x_1 \land \cdots \land x_n \land q$, which merges with the inner $\land$.
5. So the new line has depth $2$.

Here the depth does not grow at all, because the blocks merge.
The typical use of the example is to show that the depth bound is a property of a family, measured uniformly in $n$.
