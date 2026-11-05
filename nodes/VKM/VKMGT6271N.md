---
tag: VKMGT6271N
kind: statement
role: proposition
name: Projective bundle formula
sources:
  - wikipedia: en:4282051@r1374097989
    locator: Chow group, section Examples > Projective bundle formula
    note: adopted
    mention: wikipedia://en/4282051#KB3O
    sections: [Statement]
inventory: [TTFCA5Q4MJ]
---

## Statement

Given a vector bundle $E \to X$ of rank $r$ over a smooth proper scheme $X$ over a field, the Chow ring of the associated projective bundle $\mathbb{P}(E)$ can be computed using the Chow ring of $X$ and the Chern classes of $E$. If we let $\zeta = c_1(\mathcal O_{\mathbb{P}(E)}(1))$ and $c_1,\ldots, c_r$ the Chern classes of $E$, then there is an isomorphism of rings

$$CH^\bullet(\mathbb{P}(E)) \cong \frac{CH^\bullet(X)[\zeta]}{\zeta^r + c_1\zeta^{r-1} + c_2\zeta^{r-2} + \cdots + c_r}$$

For example, the Chow ring of a Hirzebruch surface can be readily computed using the projective bundle formula. Recall that it is constructed as $F_a = \mathbb{P}(\mathcal{O}\oplus\mathcal{O}(a))$ over $\mathbb{P}^1$. Then, the only non-trivial Chern class of this vector bundle is $c_1 = aH$. This implies that the Chow ring is isomorphic to

$$CH^\bullet(F_a) \cong \frac{CH^\bullet(\mathbb{P}^1)[\zeta]}{(\zeta^2 + aH\zeta)} \cong \frac{\mathbf Z[H,\zeta]}{(H^2, \zeta^2+aH\zeta)}$$
