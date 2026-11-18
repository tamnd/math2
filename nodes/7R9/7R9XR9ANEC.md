---
tag: 7R9XR9ANEC
kind: example
name: DPLL does not automate general resolution
msc: ["03F20", "68Q17", "68W40"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: WBECDG163W
    note: "DPLL runs in time at least the least tree-like resolution size, which can be exponentially larger than the least resolution size, so it is not an automating algorithm for general resolution."
uses: [6JSH907W5R, K7R9D390SP, 889KFFK1N3, WBECDG163W]
sources:
  - url: https://en.wikipedia.org/wiki/DPLL_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Automatability
---

## Example

Run the [[DPLL algorithm|K7R9D390SP]] on an unsatisfiable CNF $F$, with any rule for choosing the branching variable.

1. The run is a binary tree. Each node branches on a variable, and each leaf is a partial assignment that falsifies a clause of $F$.
2. Label each leaf with that clause, and each inner node with the resolvent of the labels of its children on the branching variable, or with one of them when the variable is missing. The labels form a tree-like [[resolution|6JSH907W5R]] refutation of $F$, as in [[A tree-like refutation from a DPLL run|889KFFK1N3]].
3. So the number of steps of the run is at least the number of nodes of this tree, which is at least the least tree-like size $S_T(F \vdash \square)$.
4. There are CNFs $F_n$ with resolution refutations of polynomial size whose least tree-like size is exponential in a power of $\abs{F_n}$. Bonet, Esteban, Galesi and Johannsen gave such a separation of tree-like and dag-like resolution, and Ben-Sasson, Impagliazzo and Wigderson made it nearly optimal.
5. On $F_n$, every DPLL run takes exponential time, while $\abs{F_n} + S(F_n \vdash \square)$ is polynomial.

So DPLL, with any branching rule, is not an algorithm that [[automatizes|WBECDG163W]] general resolution.

## Remarks

- The argument uses only the lower bound $S_T$ on the running time, not the details of the branching rule. It applies to every algorithm whose runs give tree-like refutations.
- DPLL with clause learning, as in CDCL solvers, gives dag-like refutations, so step 3 does not apply to it. But the [[Atserias-Müller theorem|W7FP9TZMVP]] shows that no algorithm automates resolution in polynomial time unless P = NP.
- Whether tree-like resolution is automatizable in polynomial time is open. Alekhnovich and Razborov showed that it is not, unless FPT = W[P].

## Explanations

### L1 human

DPLL is a method that tries values for the letters of a formula, one at a time, and goes back when it fails.
Its record of work is a proof of a special tree shape.
Some formulas have short proofs only of other shapes, so DPLL needs a long time on them even though short proofs exist.

### L2 human

The key step is that a DPLL run is itself a tree-like refutation.
So its time is at least the least tree-like size, whatever the algorithm does inside each node.
A trap is to blame a bad branching rule: on the separating formulas every rule is slow, because the best tree is already large.
