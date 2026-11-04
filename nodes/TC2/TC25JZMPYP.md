---
tag: TC25JZMPYP
kind: statement
role: proposition
name: Semi-standard tableaux hook length formula
sources:
  - wikipedia: en:41497810@r1357150947
    locator: Hook length formula, section Semi-standard tableaux hook length formula
    note: adopted
    mention: wikipedia://en/41497810#AG3S
    sections: [Statement]
inventory: [BCMKTWSTAG]
---

## Statement

The Schur polynomial $s_\lambda(x_1,\ldots,x_k)$ is the generating function of semistandard Young tableaux with shape $\lambda$ and entries in $\{1,\ldots,k\}$. Specializing this to $x_i = 1$ gives the number of semi-standard tableaux, which can be written in terms of hook lengths:

> $$s_\lambda(1,\ldots,1)\ =\ \prod_{(i,j)\in \mathrm{Y}(\lambda)}\frac{k-i+j}{h_\lambda(i,j)}.$$

The Young diagram $\lambda$ corresponds to an irreducible representation of the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_k(\mathbb C)$, and the Schur polynomial is also the character of the [[diagonal matrix|044JNC7ZAA]] $\mathrm{diag}(x_1,\ldots,x_k)$ acting on this representation. The above specialization is thus the dimension of the irreducible representation, and the formula is an alternative to the more general Weyl dimension formula.

We may refine this by taking the principal specialization of the Schur function in the variables $1,t,t^2\!,t^3\!, \ldots$ :

$$s_{\lambda}(1,t,t^2,\ldots) \ =\ \frac{t^{n\left( \lambda\right)}}{\prod_{(i,j)\in Y(\lambda)}(1-t^{h_{\lambda}(i,j)})} ,$$

where $n(\lambda) = \sum_i (i{-}1)\lambda_i = \sum_i \tbinom{\lambda_i'}{2}$ for the conjugate partition $\lambda'$.
