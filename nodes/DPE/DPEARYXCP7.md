---
tag: DPEARYXCP7
kind: proof
name: Proof that AB − BA = I has no solution in characteristic 0
msc: ["15A15", "15A27"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: E2P5TNE0G9
methods: [0J0XBKG64S]
uses: [0Y4NF1DRKD, 0GJWQZCPZM, 07PTPSZPME]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
---

## Proof

We take the trace of both sides and get $0$ on the left and $n$ on the right.
Suppose, for a contradiction, that $A$ and $B$ are $n \times n$ matrices over $F$ with $AB - BA = I_n$.

1. Equal matrices have equal traces, so $\operatorname{tr}(AB - BA) = \operatorname{tr} I_n$.
2. By [[linearity of the trace|0GJWQZCPZM]], $\operatorname{tr}(AB - BA) = \operatorname{tr}(AB) - \operatorname{tr}(BA)$.
3. By the [[cyclic property|0Y4NF1DRKD]], $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, so the left side of step 1 is $0$.
4. By the [[definition of the trace|07PTPSZPME]], $\operatorname{tr} I_n = 1 + \cdots + 1 = n \cdot 1_F$, with $n$ terms.
5. The field $F$ has characteristic $0$ and $n \ge 1$, so $n \cdot 1_F \neq 0$.
6. Steps 1, 3 and 5 give $0 = n \cdot 1_F \neq 0$, a contradiction, so no such $A$ and $B$ exist.

## Idea

The trace kills every commutator but not the identity.
In characteristic $0$, $\operatorname{tr} I_n = n$ is not $0$, and the two sides of the equation cannot have the same trace.

## Variants

The same proof works over any commutative ring $R$ in which $n \cdot 1_R \neq 0$, since steps 1 to 4 use only linearity and the cyclic property.
It shows more generally that $AB - BA = cI_n$ forces $nc = 0$.
The argument fails exactly when $n \cdot 1_F = 0$, that is, when the characteristic $p$ divides $n$, and then solutions exist; see [[this example|KZD8TFB85C]] for $p = n = 2$.
