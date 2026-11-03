---
tag: GAGWR57ZT0
kind: definition
name: Relevant and irrelevant operators
msc: [82B28, 82B27]
defines: FQV4QYXFC1
uses: [H0B5TN4139, 047NDTEPCV, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Renormalization_group
---

## Definition

Let $\mathcal K$ be an open subset of $\R^n$, a space of coupling constants.
Let $(R_b)_{b > 1}$ be a family of renormalization group maps $R_b \colon \mathcal K \to \mathcal K$ with $R_b \circ R_{b'} = R_{bb'}$.
Let $K^*$ be a common [[fixed point|H0B5TN4139]] of all $R_b$, and assume each $R_b$ is differentiable at $K^*$.
Let $A_b$ be the [[Jacobian matrix|047NDTEPCV]] of $R_b$ at $K^*$.
Assume that the matrices $A_b$ have a common basis of eigenvectors $e_1, \dots, e_n$ with real [[eigenvalues|0BQAA2BK3Q]] $\lambda_i(b) = b^{y_i}$.
The number $y_i$ is the *RG eigenvalue* of the direction $e_i$, and the perturbation $K^* + h e_i$, or the operator coupled to $e_i$, is called:

1. *relevant* if $y_i > 0$;
2. *irrelevant* if $y_i < 0$;
3. *marginal* if $y_i = 0$.

## Remarks

The semigroup law gives $A_b A_{b'} = A_{bb'}$, so $\lambda_i(b) \lambda_i(b') = \lambda_i(bb')$.
A continuous solution of this equation with $\lambda_i(b) > 0$ is a power $b^{y_i}$, which explains the form of the eigenvalues.
To first order, $R_b(K^* + h e_i) = K^* + b^{y_i} h e_i$, so a relevant component grows and an irrelevant one decays under iteration.

Example: at the critical fixed point of the two-dimensional Ising model, the thermal direction has $y_t = 1$ and the magnetic direction has $y_h = 15/8$.
Both are relevant, and the correlation length exponent is $\nu = 1/y_t = 1$.

Non-example: a direction with $y_i = 0$ is neither relevant nor irrelevant; its fate is decided by the higher-order terms of $R_b$, as for the marginal coupling in the [[Berezinskii–Kosterlitz–Thouless transition|MN952HPZ50]].

When there is no marginal direction, the relevant directions span the directions transverse to the critical surface at $K^*$, and the irrelevant directions are tangent to it.
