---
tag: RA380RWEC0
kind: topic
name: Bounded arithmetic
msc: ["03F30", "03F20"]
topics: [DYJ0KGTPMR]
---

## Summary

This topic is a part of [[mathematical logic|DYJ0KGTPMR]], and it asks what arithmetic looks like when every quantifier is bounded and every proof must be feasible.
The starting point is $\mathsf{I}\Delta_0$, Peano arithmetic with induction only for bounded formulas such as $\exists y \le x \, (y \cdot y = x)$.
Its definable sets are the linear-time hierarchy, and Parikh's theorem of 1971 shows that it cannot prove that $2^x$ exists.
Cook's equational theory $\mathsf{PV}$ of 1975 and Buss's theories $S^i_2$ and $T^i_2$ of 1985 then match proofs with polynomial-time computation.
The smash function $x \# y = 2^{\lvert x \rvert \cdot \lvert y \rvert}$ gives polynomial growth in the lengths, and Buss's witnessing theorem turns a proof of $\forall x \, \exists y \, A$ in $S^1_2$ into a polynomial-time algorithm.
From there the story turns to open problems.
The Krajicek-Pudlak-Takeuti theorem ties the collapse of the theories to the collapse of the polynomial hierarchy, and the Paris-Wilkie translation turns proofs into short propositional proofs.
Through it, lower bounds in proof complexity show which theories cannot prove the pigeonhole principle.
Whether the theories separate is still open, and Jeřábek's approximate counting shows how much probabilistic reasoning the weak theories can still carry out.

## Remarks

### Reading order

1. [[Bounded arithmetic|A2CFPP8JMN]]: how bounded formulas, lengths and the smash function fit together, and how the theories $\mathsf{I}\Delta_0$, $S^i_2$ and $T^i_2$ are built.
2. [[IΔ0 and the linear-time hierarchy|FYGWNXETVJ]]: which sets a bounded formula can define, such as the primes and the squares, and why they are exactly the linear-time hierarchy.
3. [[Parikh's theorem|YPQPC1WJMV]]: why a provable bounded search has a polynomial bound, and why $\mathsf{I}\Delta_0$ therefore cannot prove that $2^x$ is total.
4. [[Cook's theory PV|FMM44KFZQT]]: how to build a theory whose function symbols are exactly the polynomial-time algorithms, and what a [[feasibly constructive proof|H1B2VD0KVP]] is.
5. [[Buss's witnessing theorem|RH4R7GTTAX]]: how a proof in $S^1_2$ of a $\Sigma^b_1$ existence statement becomes a polynomial-time algorithm, and the converse.
6. [[Krajíček-Pudlák-Takeuti theorem|YP7KE8E6DC]]: how a proof of a $\forall \exists \forall$ sentence becomes a guessing game with few rounds, and why equal theories would collapse the polynomial hierarchy.
7. [[Paris-Wilkie translation|ZVD982MVST]]: how a bounded proof becomes a family of short constant-depth propositional proofs, so that proof complexity gives independence results.
8. [[Pigeonhole principles in bounded arithmetic|NJ18EZ5JBC]]: which weak theories prove which forms of the pigeonhole principle, and which cases are still open.
9. [[Separating the hierarchy of bounded arithmetic|PEJQDHHX8E]]: what is known about the open problem whether the theories $S^i_2$ and $T^i_2$ differ.
10. [[Approximate counting in bounded arithmetic|65K2S22DGZ]]: how the dual weak pigeonhole principle lets a weak theory measure the sizes of sets and reason about randomized algorithms.

### Prerequisites

1. [[Formal arithmetic and its fragments|QHCRN4JVG0]]: Robinson arithmetic, Peano arithmetic and its fragments by induction.
2. [[Structural proof theory|R10RMQCJQX]]: the sequent calculus and cut elimination, used in the witnessing proofs.
3. [[Natural independence results and fast-growing functions|T6FK1E7GJ1]]: provably total functions of stronger theories, for comparison.
4. [[P|GVT2NKN37K]] and [[NP|QQRA9GBW51]]: the complexity classes that the theories capture.
5. [[Polynomial hierarchy|TDQ7AXGM6P]]: the classes $\Sigma^p_i$ that match the formulas $\Sigma^b_i$.
