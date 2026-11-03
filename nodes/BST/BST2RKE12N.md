---
tag: BST2RKE12N
kind: statement
role: theorem
name: Baker–Gill–Solovay theorem
msc: [68Q15, 03D15]
uses: [Z5CCVBME2V, GVT2NKN37K, QQRA9GBW51, T9NTRY93ZT]
about: [Z5CCVBME2V, MFN5GYZH5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Oracle_machine
---

## Statement

Let $A \subseteq \set{0,1}^*$ be a language.
Let $\mathrm{P}^A$ and $\mathrm{NP}^A$ be the classes of languages decided in polynomial time by deterministic, respectively nondeterministic, [[oracle machines|Z5CCVBME2V]] with oracle $A$.

1. There is a language $A$ with $\mathrm{P}^A = \mathrm{NP}^A$.
2. There is a language $B$ with $\mathrm{P}^B \ne \mathrm{NP}^B$.

## Remarks

For part 1 one can take for $A$ any [[PSPACE|T9NTRY93ZT]]-complete language, such as the [[true quantified Boolean formula|WV2N01B4YV]] problem.
Then $\mathrm{NP}^A \subseteq \mathrm{NPSPACE} = \mathrm{PSPACE} \subseteq \mathrm{P}^A$, since a polynomial-space machine can answer the oracle queries itself.
For part 2 one builds $B$ in stages by diagonalisation, so that the language $\set{1^n : B \text{ contains a string of length } n}$ is in $\mathrm{NP}^B$ but escapes each polynomial-time oracle machine in turn.
A machine running in time less than $2^n$ cannot query all strings of length $n$.
The construction places a string in $B$ at a length where the machine has not looked.

A proof technique *relativizes* when it stays valid after every machine is given the same oracle.
Simulation and diagonalisation, as in the [[time hierarchy theorem|A6D1D67GHA]], relativize.
The theorem shows that no relativizing argument can settle the [[P versus NP problem|MFN5GYZH5Z]], since such an argument would give the same answer for every oracle.

## Explanations

### L1 human

An oracle is a black box that answers membership questions about a fixed set in one step.
The theorem gives one black box that makes P and NP equal and another that makes them different.
So any proof of $\mathrm{P} \ne \mathrm{NP}$ or of $\mathrm{P} = \mathrm{NP}$ must use some property of real computation that fails once black boxes are allowed.
This explains why the simple methods from computability theory do not solve the problem.

### L2 human

The result, from 1975, was the first of several barriers to proving separations of complexity classes.
Later barriers are the [[natural proofs barrier|THPBBYSDP1]] of Razborov and Rudich and the algebrization barrier of Aaronson and Wigderson.
Some results do not relativize: [[IP = PSPACE|W29Y13KD1T]] holds for real machines, but there are oracles relative to which the two classes differ.
Relativized worlds remain a useful test: a proposed proof that relativizes cannot separate classes that some oracle makes equal.
