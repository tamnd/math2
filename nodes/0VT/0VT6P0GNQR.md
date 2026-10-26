---
tag: 0VT6P0GNQR
kind: concept
name: Gram–Schmidt process
msc: [15A63, 65F25]
uses: [09VYHEF2VT, 0EVHJFTG9Z, 0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Description
same_as:
  wikidata: Q475239
  wikipedia: Gram–Schmidt process
---

## Summary

Let $V$ be an inner product space over $\R$ or $\C$, and let $v_1, \dots, v_k \in V$ be [[linearly independent|0CRMGPAH83]].
The *Gram–Schmidt process* defines vectors $u_1, \dots, u_k$ by $u_1 = v_1$ and, for $2 \le j \le k$,
$$u_j = v_j - \sum_{i=1}^{j-1} \frac{\langle v_j, u_i \rangle}{\langle u_i, u_i \rangle} u_i.$$
Then the vectors $e_j = u_j / \norm{u_j}$ form an [[orthonormal family|0RW9TNNT87]] with the same [[span|0DTY8B9HMS]] as $v_1, \dots, v_j$ for each $j$.

## Remarks

Each step subtracts from $v_j$ its projections on the earlier vectors $u_i$.
For $v_1 = (1, 1)$ and $v_2 = (1, 0)$ in $\R^2$, it gives $u_1 = (1, 1)$ and $u_2 = (1/2, -1/2)$.
In floating point arithmetic, the modified Gram–Schmidt process is more stable.
In matrix form, the process gives the [[QR decomposition|0ERWG4NXQ9]].

## Explanations

### L1 human

The Gram–Schmidt process turns any independent list of vectors into a list of perpendicular unit vectors.
It treats the vectors one at a time, and it removes from each one its components along the earlier ones.
Then it scales each result to length one.
