---
tag: 0WCPH5Z7FA
kind: statement
role: proposition
name: Trace of a linear map is the trace of its matrix
msc: [15A04, 15A15]
uses: [0RPDTWY2JS, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$ with a basis $B$, and let $T \colon V \to V$ be a linear map.
Then the [[trace of $T$|0KZDNGA561]] equals the trace of the [[matrix of $T$|0YQSGNYE3K]] in $B$:
$$\tr T = \tr [T]_B.$$

## Remarks

The key fact is that similar matrices have the same trace, by $\tr(AB) = \tr(BA)$.
With a basis-free definition, the trace is the map $\End_F(V) \cong V^* \otimes V \to F$ induced by evaluation $f \otimes v \mapsto f(v)$.

## Explanations

### L1 human

We can compute the trace of a linear map in any basis that we like.
We write the matrix in that basis and add its diagonal entries.
Every basis gives the same number.
