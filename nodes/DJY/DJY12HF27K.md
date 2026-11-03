---
tag: DJY12HF27K
kind: definition
name: NL
msc: [68Q15]
defines: 7RH189REV7
uses: [FDNFGKEEJR, M7SDX137WE, ESPYW94XGR, 5MFZ4VNY6D, VRZ9H4EZ6V, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/NL_(complexity)
---

## Definition

Let $\Sigma$ be a finite alphabet.
The [[complexity class|ESPYW94XGR]] *NL* is
$$\mathrm{NL} = \mathrm{NSPACE}(\log n),$$
where $\mathrm{NSPACE}$ is defined through the [[space complexity|FDNFGKEEJR]] of [[nondeterministic Turing machines|M7SDX137WE]] with a read-only input tape.
So a [[language|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ lies in NL when some such machine decides it using $O(\log n)$ work-tape cells on every branch, for inputs of length $n$.

## Remarks

Example: directed reachability lies in $\mathrm{NL}$.
An input is a directed graph $G$ with $n$ vertices and two vertices $s, t$.
The machine stores the current vertex and a step counter, starts at $s$, and guesses an out-neighbour at each step.
It accepts when it reaches $t$ and rejects after $n$ steps, using $O(\log n)$ cells.
Some branch accepts exactly when $G$ has a path from $s$ to $t$.

Non-example: a machine that guesses a whole path and writes it on the work tape may use about $n \log n$ cells, so it does not show membership in $\mathrm{NL}$.

Directed reachability is NL-complete under logarithmic-space reductions.
One has $\mathrm{L} \subseteq \mathrm{NL} \subseteq \mathrm{P}$, where L is the class [[L|VRZ9H4EZ6V]] and P is the class [[P|GVT2NKN37K]].
NL is closed under complement, by the Immerman–Szelepcsényi theorem.
