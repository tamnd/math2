---
tag: 3RVB1T9YDT
kind: statement
role: theorem
name: Extended Goodstein's theorem
sources:
  - wikipedia: en:150062@r1368439001
    locator: Goodstein's theorem, section Proof of Goodstein's theorem > Extended Goodstein's theorem
    note: adopted
    mention: wikipedia://en/150062#Z2SW
    sections: [Statement]
inventory: [KS3YDTBRHQ]
---

## Statement

The above proof still works if the definition of the Goodstein sequence is changed so that the base-changing operation replaces each occurrence of the base $b$ with $b+2$ instead of $b+1$. More generally, let $b_1$, $b_2$, $b_3, \ldots$ be any non-decreasing sequence of integers with $b_1 \geq 2$. Then let the $(n+1)$st term $G_m(n+1)$ of the extended Goodstein sequence of $m$ be as follows:

- Take the hereditary base $b_n$ representation of $G_m(n)$.
- Replace each occurrence of the base $b_n$ with $b_{n+1}$.
- Subtract one.

A simple modification of the above proof shows that this sequence still terminates. For example, if $b_n = 4$ and if $b_{n+1} = 9$, then $f(3 \cdot 4^{4^4} + 4, 4) = 3 \omega^{\omega^\omega} + \omega= f(3 \cdot 9^{9^9} + 9, 9)$, hence the ordinal $f(3 \cdot 4^{4^4} + 4, 4)$ is strictly greater than the ordinal $f\big((3 \cdot 9^{9^9} + 9) - 1, 9\big).$

The extended version is in fact the one considered in Goodstein's original paper, where Goodstein proved that it is equivalent to the restricted ordinal theorem (i.e. the claim that [[transfinite induction|0ZHQMQ2C1N]] below ε<sub>0</sub> is valid), and gave a finitist proof for the case where $m \le b_1^{b_1^{b_1}}$ (equivalent to transfinite induction up to $\omega^{\omega^\omega}$).

The extended Goodstein's theorem without any restriction on the sequence *b<sub>n</sub>* is not formalizable in Peano arithmetic (PA), since such an arbitrary infinite sequence cannot be represented in PA. This seems to be what kept Goodstein from claiming back in 1944 that the extended Goodstein's theorem is unprovable in PA due to Gödel's second incompleteness theorem and Gentzen's proof of the consistency of PA using ε<sub>0</sub>-induction. However, inspection of Gentzen's proof shows that it only needs the fact that there is no primitive recursive strictly decreasing infinite sequence of ordinals, so limiting *b<sub>n</sub>* to primitive recursive sequences would have allowed Goodstein to prove an unprovability result. Furthermore, with the relatively elementary technique of the Grzegorczyk hierarchy, it can be shown that every primitive recursive strictly decreasing infinite sequence of ordinals can be "slowed down" so that it can be transformed to a Goodstein sequence where $b_n = n+1$, thus giving an alternative proof to the same result Kirby and Paris proved.
