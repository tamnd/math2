---
tag: 4M5T9TGSFW
kind: definition
name: L
msc: [68Q15]
defines: VRZ9H4EZ6V
uses: [FDNFGKEEJR, ESPYW94XGR, 5MFZ4VNY6D, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/L_(complexity)
---

## Definition

Let $\Sigma$ be a finite alphabet.
The [[complexity class|ESPYW94XGR]] *L* is
$$\mathrm{L} = \mathrm{DSPACE}(\log n),$$
where $\mathrm{DSPACE}$ is defined through the [[space complexity|FDNFGKEEJR]] of deterministic Turing machines with a read-only input tape.
So a [[language|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ lies in L when some such machine decides it using $O(\log n)$ work-tape cells on inputs of length $n$.

## Remarks

Example: the language of balanced strings of brackets over $\set{(, )}$ lies in $\mathrm{L}$.
A machine scans the input once and keeps the current depth in a binary counter, rejecting if the depth becomes negative.
It accepts if the depth is $0$ at the end, and the counter needs $O(\log n)$ cells.

Non-example: a machine that first copies its input to a work tape uses $n$ cells.
That machine does not show membership in L, since $n$ is not $O(\log n)$.

A machine in logarithmic space has only polynomially many configurations on inputs of length $n$.
So it halts within polynomially many steps, and $\mathrm{L} \subseteq$ [[P|GVT2NKN37K]].
Omer Reingold proved that connectivity in undirected graphs lies in $\mathrm{L}$.
