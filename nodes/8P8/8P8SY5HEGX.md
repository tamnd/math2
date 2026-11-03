---
tag: 8P8SY5HEGX
kind: definition
name: Space complexity
msc: [68Q15, 68Q04]
defines: FDNFGKEEJR
uses: [758EYCN27B, M7SDX137WE, YK3HD56R3G, 5MFZ4VNY6D, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Space_complexity
---

## Definition

Let $\Sigma$ be a finite alphabet.
Consider a [[multitape Turing machine|YK3HD56R3G]] $M$ with a read-only input tape and one or more read-write work tapes.
Suppose that $M$ is deterministic and halts on every input.
Let $w \in \Sigma^*$ be an input.
The space used by $M$ on $w$ is the number of distinct work-tape cells that the heads of $M$ visit while $M$ runs on $w$.
The *space complexity* of $M$ is the function $s_M \colon \N \to \N$ with
$$s_M(n) = \max \set{\text{space used by } M \text{ on } w : w \in \Sigma^*, \ \abs{w} = n}.$$
For a [[nondeterministic Turing machine|M7SDX137WE]] that halts on every branch, the maximum is also taken over all computation branches.
For a function $f \colon \N \to \N$, $\mathrm{DSPACE}(f)$ is the set of [[languages|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ decided by some deterministic machine $M$ with $s_M(n) = O(f(n))$, in [[big O notation|0TGV80E6A4]].
The class $\mathrm{NSPACE}(f)$ is defined in the same way with nondeterministic machines.

## Remarks

Example: the language $\set{0^k 1^k : k \in \N}$ lies in $\mathrm{DSPACE}(\log n)$.
A machine first checks that no $1$ comes before a $0$, then counts the $0$s and the $1$s in two binary counters and compares them.
Each counter holds a number at most $n$, so it needs at most $\floor{\log_2 n} + 1$ cells.

Non-example: a machine that runs forever on some input has no space complexity in this sense, because the definition asks that $M$ halts on every input.

The input tape is not counted.
This makes sublinear bounds such as $\log n$ meaningful.
For bounds $f(n) \ge n$, counting the input as well changes nothing up to a constant factor.
