---
tag: ~b9a2abfd
kind: example
name: A rational matrix with no Jordan form over the rationals
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
not_instance_of:
  - target: ~f6e144c3
    note: the characteristic polynomial x² − 2 does not split over Q, so the method stops at its first step
illustrates: [085HQ5G5TE]
uses: [~f6e144c3, 0VH1TC1PWF, 0VSSPAFM2C]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Matrices with entries in a field
---

## Example

Let $A = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix} = C(x^2 - 2)$ over $\mathbb{Q}$, a [[companion matrix|0VH1TC1PWF]].

1. $\chi_A = x^2 - (\operatorname{tr} A) x + \det A = x^2 - 2$.
2. $x^2 - 2$ has no rational root, since $\sqrt 2$ is irrational. So $\chi_A$ does not split over $\mathbb{Q}$, and $A$ has no eigenvalue in $\mathbb{Q}$.
3. A Jordan matrix over $\mathbb{Q}$ is triangular with rational diagonal, so its characteristic polynomial has rational roots. So $A$ is similar over $\mathbb{Q}$ to no Jordan matrix.
4. Over $\mathbb{R}$, $\chi_A = (x - \sqrt 2)(x + \sqrt 2)$. The vectors $(\sqrt 2, 1)$ and $(-\sqrt 2, 1)$ satisfy $A(\sqrt 2, 1) = (2, \sqrt 2) = \sqrt 2 \, (\sqrt 2, 1)$ and $A(-\sqrt 2, 1) = (2, -\sqrt 2) = -\sqrt 2 \, (-\sqrt 2, 1)$.
5. So over $\mathbb{R}$ the Jordan form is $J_1(\sqrt 2) \oplus J_1(-\sqrt 2)$.

## Remarks

Over $\mathbb{Q}$, $A$ is already in rational canonical form, with the single invariant factor $x^2 - 2$.
So the rational canonical form, and not the Jordan form, is the right normal form when $\chi_A$ does not split.
Replacing $2$ by $4$ gives $\chi = (x - 2)(x + 2)$, which splits over $\mathbb{Q}$, and then the Jordan form is $\operatorname{diag}(2, -2)$ over $\mathbb{Q}$.

## Explanations

### L1 human

The eigenvalues of this matrix are the square roots of $2$, and they are not fractions.
So with only fractions you cannot write its Jordan form.
With real numbers you can, and the form is diagonal.

### L2 human

The first step of the method is to find the roots of the characteristic polynomial in the field.
Here there are none, so the method gives no answer over $\mathbb{Q}$.
The two-sided check $A v = \lambda v$ in step 4 shows that the real eigenvectors exist.
