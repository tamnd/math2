---
tag: GMR2HXZRMR
kind: proof
name: Proof that the tensor products of basis vectors form a basis
msc: [15A69]
proves: 0SH5VT8QYA
uses: [0G31VJ5YS5, 0YDRV01R8F, 0VTQTPQGAV, 0BJKVF90Z6, 0EVHJFTG9Z, 0R8X9XA83A, 0RJF668P1T]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/tensorprod.pdf
    locator: Theorem 4.9
---

## Proof

We use the construction $V \otimes W = L / N$ of the [[tensor product|0G31VJ5YS5]], where $v \otimes w$ is the class of the basis vector $[v, w]$ of $L$.

1. The elements of $N$ have class $0$. So $(v + v') \otimes w = v \otimes w + v' \otimes w$, $v \otimes (w + w') = v \otimes w + v \otimes w'$, and $(av) \otimes w = a (v \otimes w) = v \otimes (aw)$.
2. Each element of $V \otimes W$ is the class of a finite combination $\sum_k c_k [v_k, w_k]$. So it is $\sum_k c_k (v_k \otimes w_k)$, and the vectors $v \otimes w$ [[span|0BJKVF90Z6]] $V \otimes W$.
3. Let $v \in V$ and $w \in W$. Since $(e_i)$ and $(f_j)$ are [[bases|0VTQTPQGAV]], $v = \sum_i a_i e_i$ and $w = \sum_j b_j f_j$ with finitely many nonzero coefficients.
4. By step 1, $v \otimes w = \sum_{i,j} a_i b_j\, (e_i \otimes f_j)$. With step 2, the family $(e_i \otimes f_j)$ spans $V \otimes W$.
5. For independence, let $\sum_{(i,j)} c_{ij}\, (e_i \otimes f_j) = 0$, with only finitely many $c_{ij} \ne 0$. Fix $(k, l) \in I \times J$.
6. By [[the extension from a basis|0R8X9XA83A]], there are [[linear maps|0RJF668P1T]] $\alpha \colon V \to F$ with $\alpha(e_i) = \delta_{ik}$ and $\beta \colon W \to F$ with $\beta(f_j) = \delta_{jl}$. Here $\delta$ is $1$ for equal indices and $0$ otherwise.
7. The map $h(v, w) = \alpha(v) \beta(w)$ from $V \times W$ to $F$ is bilinear, since $\alpha$ and $\beta$ are linear.
8. By the [[universal property|0YDRV01R8F]], there is a linear map $\varphi \colon V \otimes W \to F$ with $\varphi(v \otimes w) = \alpha(v) \beta(w)$.
9. In particular $\varphi(e_i \otimes f_j) = \delta_{ik} \delta_{jl}$. Applying $\varphi$ to the relation of step 5 gives $c_{kl} = 0$.
10. Since $(k, l)$ was arbitrary, all $c_{ij}$ vanish. So the family is [[linearly independent|0EVHJFTG9Z]].
11. By steps 4 and 10, $(e_i \otimes f_j)_{(i,j) \in I \times J}$ is a basis of $V \otimes W$.

## Idea

Spanning comes from expanding $v$ and $w$ in their bases and using bilinearity. For independence, the universal property gives a linear functional that reads off one coefficient $c_{kl}$. It comes from the bilinear map that multiplies the $k$-th coordinate of $v$ by the $l$-th coordinate of $w$.
