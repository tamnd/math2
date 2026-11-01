---
tag: CAEHMSX9RT
kind: statement
role: theorem
name: Steinitz's theorem on algebraically closed fields
msc: [12F20, 12F05]
uses: [02SJG1HC32, 1ZB13N78XW, D7TR0YWR9H, E45PA267S4, 0MCXX29HWY, 01VQ7C4FTB, 0JTGRV4WT4]
about: [0PF6TM8TWT, D7TR0YWR9H]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraically_closed_field
---

## Statement

Let $K$ and $L$ be [[algebraically closed fields|02SJG1HC32]], and let $P_K$ and $P_L$ be their prime subfields.
Then $K$ and $L$ are isomorphic if and only if they have the same [[characteristic|1ZB13N78XW]] and $\operatorname{trdeg}_{P_K} K = \operatorname{trdeg}_{P_L} L$, where $\operatorname{trdeg}$ is the [[transcendence degree|D7TR0YWR9H]].

## Remarks

If the characteristics agree, then $P_K \cong P_L$, and a bijection between [[transcendence bases|E45PA267S4]] $B$ of $K$ and $B'$ of $L$ gives an isomorphism $P_K(B) \cong P_L(B')$.
Since $K$ and $L$ are [[algebraic closures|0MCXX29HWY]] of these fields, the isomorphism extends to $K \cong L$ by [[uniqueness of the algebraic closure|01VQ7C4FTB]].
The converse holds because an isomorphism preserves the characteristic and maps a transcendence basis to a transcendence basis.
For an uncountable algebraically closed field, the transcendence degree over the prime field equals the [[cardinality|0JTGRV4WT4]] of the field.
So two uncountable algebraically closed fields of the same characteristic and the same cardinality are isomorphic; for example, $\C$ is isomorphic to an algebraic closure of $\Q(x_i : i \in \R)$.

## Explanations

### L1 human

An algebraically closed field is determined by two numbers: its characteristic and how many free variables it has.
Everything else follows by adding all roots of all polynomials.
For instance, $\C$ and the algebraic closure of the field of $p$-adic numbers are isomorphic as fields, although their topologies are very different.

### L2 human

The theorem shows that the algebraic closure $\overline{\Q}$ and $\C$ are not isomorphic: one has transcendence degree $0$, the other has transcendence degree the continuum.
It is the field-theoretic source of the fact that the theory of algebraically closed fields of a fixed characteristic is categorical in each uncountable cardinality.
Its proof uses the existence of transcendence bases and the uniqueness of algebraic closures, both of which rest on Zorn's lemma.
