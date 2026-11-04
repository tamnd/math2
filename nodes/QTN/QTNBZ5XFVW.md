---
tag: QTNBZ5XFVW
kind: statement
role: lemma
name: Van Kampen lemma
sources:
  - wikipedia: en:18871460@r1368818220
    locator: Van Kampen diagram, section Van Kampen lemma
    note: adopted
    mention: wikipedia://en/18871460#X9AW
    sections: [Statement]
inventory: [NSB389H3KX]
---

## Statement

A key basic result in the theory is the so-called *Van Kampen lemma* which states the following:

1. Let $\mathcal D\,$ be a Van Kampen diagram over the presentation (†) with boundary label *w* which is a word (not necessarily freely reduced) in the alphabet *A* ∪ *A*<sup>−1</sup>. Then *w*=1 in *G*.
1. Let *w* be a freely reduced word in the alphabet *A* ∪ *A*<sup>−1</sup> such that *w*=1 in *G*. Then there exists a reduced Van Kampen diagram $\mathcal D\,$ over the presentation (†) whose boundary label is freely reduced and is equal to *w*.

First observe that for an element *w* ∈ *F*(*A*) we have *w* = 1 in *G* if and only if *w* belongs to the normal closure of *R* in *F*(*A*) that is, if and only if w can be represented as

$w=u_1s_1u_1^{-1}\cdots u_n s_nu_{n}^{-1} \text{ in } F(A),$ (♠)

where *n* ≥ 0 and where *s<sub>i</sub>* ∈ *R*<sub>∗</sub> for *i* = 1, ..., *n*.

Part 1 of Van Kampen's lemma is proved by induction on the area of $\mathcal D\,$. The inductive step consists in "peeling" off one of the boundary regions of $\mathcal D\,$ to get a Van Kampen diagram $\mathcal D'\,$ with boundary cycle *w* and observing that in *F*(*A*) we have

$$w=usu^{-1} w',\,$$

where *s*∈*R*<sub>∗</sub> is the boundary cycle of the region that was removed to get $\mathcal D'\,$ from $\mathcal D\,$.

The proof of part two of Van Kampen's lemma is more involved. First, it is easy to see that if *w* is freely reduced and *w* = 1 in *G* there exists some Van Kampen diagram $\mathcal D_0\,$ with boundary label *w*<sub>0</sub> such that *w* = *w*<sub>0</sub> in *F*(*A*) (after possibly freely reducing *w*<sub>0</sub>). Namely consider a representation of *w* of the form (♠) above. Then make $\mathcal D_0\,$ to be a wedge of *n* "lollipops" with "stems" labeled by *u<sub>i</sub>* and with the "candys" (2-cells) labelled by *s<sub>i</sub>*. Then the boundary label of $\mathcal D_0\,$ is a word *w*<sub>0</sub> such that *w* = *w*<sub>0</sub> in *F*(*A*). However, it is possible that the word *w*<sub>0</sub> is not freely reduced. One then starts performing "folding" moves to get a sequence of Van Kampen diagrams $\mathcal D_0, \mathcal D_1, \mathcal D_2,\dots\,$ by making their boundary labels more and more freely reduced and making sure that at each step the boundary label of each diagram in the sequence is equal to *w* in *F*(*A*). The sequence terminates in a finite number of steps with a Van Kampen diagram $\mathcal D_k\,$ whose boundary label is freely reduced and thus equal to *w* as a word. The diagram $\mathcal D_k\,$ may not be reduced. If that happens, we can remove the reduction pairs from this diagram by a simple surgery operation without affecting the boundary label. Eventually this produces a reduced Van Kampen diagram $\mathcal D\,$ whose boundary cycle is freely reduced and equal to *w*.
