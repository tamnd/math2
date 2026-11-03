---
tag: 82N5ZEWENZ
kind: definition
name: Rewriting system
msc: [68Q42, 03D03]
defines: Y83TQF6V6A
uses: [05AVARPXA2, 05J9NWX07X, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Rewriting
    locator: Abstract rewriting systems
---

## Definition

An *abstract rewriting system* is a pair $(A, \to)$ of a set $A$ and a [[binary relation|05AVARPXA2]] $\to$ on $A$, called the *rewrite relation* or *reduction*.
For $a, b \in A$:

1. $a \to^* b$ means that $b$ is reachable from $a$ in zero or more steps; $\to^*$ is the reflexive and [[transitive closure|05J9NWX07X]] of $\to$;
2. $a \leftrightarrow^* b$ means that $a$ and $b$ are related by the smallest [[equivalence relation|0G8VEZ3WTK]] containing $\to$;
3. $a$ is a *normal form* if there is no $c \in A$ with $a \to c$.
   Then $b$ is a normal form *of* $a$ if $a \to^* b$ and $b$ is a normal form.

The system is *terminating*, or *strongly normalizing*, if there is no infinite chain $a_0 \to a_1 \to a_2 \to \cdots$.

## Remarks

Example: $A = \set{a, b}^*$ with $u \to v$ when $v$ arises from $u$ by replacing one occurrence of $ba$ by $ab$.
It is terminating, since each step lowers the number of pairs of positions $i < j$ with a $b$ at $i$ and an $a$ at $j$.
The normal forms are the words $a^m b^n$.
Non-example of termination: $A = \set{x, y}$ with $x \to y$ and $y \to x$, which has the infinite chain $x \to y \to x \to \cdots$ and no normal form.
A *string rewriting system* over an alphabet $\Sigma$ is a set of pairs of words $l \to r$, inducing $u l v \to u r v$ on $\Sigma^*$; a term rewriting system rewrites terms in the same way.
