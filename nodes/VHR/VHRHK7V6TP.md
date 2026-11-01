---
tag: VHRHK7V6TP
kind: definition
name: Artinian module
msc: ["16P20", "13E10"]
defines: YQNZTQGP1X
uses: [0894J980RK, 09VDS2W1E8, 0RGZ10DFPG]
sources:
  - url: https://en.wikipedia.org/wiki/Artinian_module
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $M$ be a left [[module|09VDS2W1E8]] over $R$.
The module $M$ is *Artinian* if the set of its [[submodules|0RGZ10DFPG]], ordered by inclusion, satisfies the descending chain condition.
That is, for every chain $N_1 \supseteq N_2 \supseteq \cdots$ of submodules of $M$, there is an index $k$ with $N_n = N_k$ for all $n \ge k$.

## Remarks

Equivalently, every nonempty set of submodules of $M$ has a minimal element for inclusion.
Example: a finite-dimensional vector space $V$ over a field is Artinian, because a strictly decreasing chain of subspaces has at most $\dim V + 1$ terms.
Non-example: $\Z$ as a $\Z$-module is not Artinian, because $2\Z \supsetneq 4\Z \supsetneq 8\Z \supsetneq \cdots$ never stops.
Example: for a prime $p$, the Prüfer group $\Z[1/p]/\Z$ is an Artinian $\Z$-module, since its proper subgroups form the chain $0 \subset \frac{1}{p}\Z/\Z \subset \frac{1}{p^2}\Z/\Z \subset \cdots$.
That chain also shows that it is not a [[Noetherian module|AK1ZRCXR32]].
Submodules, quotients and extensions of Artinian modules are Artinian.

## Explanations

### L1 human

An Artinian module is a module with no endless decreasing chain of submodules.
It is the mirror image of a Noetherian module.
