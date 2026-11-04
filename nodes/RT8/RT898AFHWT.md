---
tag: RT898AFHWT
kind: statement
role: theorem
name: Seese's theorem
sources:
  - wikipedia: en:47857242@r1374729429
    locator: Logic of graphs, section Second order > Seese's theorem
    note: adopted
    mention: wikipedia://en/47857242#3UW8
    sections: [Statement]
inventory: [DEE4BGX392]
---

## Statement

The satisfiability problem for a sentence of monadic second-order logic is the problem of determining whether there exists at least one graph (possibly within a restricted family of graphs) for which the sentence is true. For arbitrary graph families, and arbitrary sentences, this problem is undecidable. However, satisfiability of MSO<sub>2</sub> sentences is decidable for the graphs of bounded treewidth, and satisfiability of MSO<sub>1</sub> sentences is decidable for graphs of bounded clique-width. The proof involves using Courcelle's theorem to build an automaton that can test the property, and then examining the automaton to determine whether there is any graph it can accept. As a partial converse, (Seese 1991) proved that, whenever a family of graphs has a decidable MSO<sub>2</sub> satisfiability problem, the family must have bounded treewidth. The proof is based on a theorem of Robertson and Seymour that the families of graphs with unbounded treewidth have arbitrarily large grid minors. Seese also conjectured that every family of graphs with a decidable MSO<sub>1</sub> satisfiability problem must have bounded clique-width. This has not been proven, but a weakening of the conjecture that extends MSO<sub>1</sub> with modular counting predicates is true.
