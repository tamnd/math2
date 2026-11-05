---
tag: MSB2CV57BC
kind: statement
role: proposition
name: Canonical bundle formula
sources:
  - wikipedia: en:3073462@r1317488161
    locator: Elliptic surface, section Canonical bundle formula
    note: adopted
    mention: wikipedia://en/3073462#E22U
    sections: [Statement]
inventory: [G7Y95QMKQ6]
---

## Statement

To understand how elliptic surfaces fit into the classification of surfaces, it is important to compute the canonical bundle of a minimal elliptic surface *f*: *X* → *S*. Over the complex numbers, Kodaira proved the following **canonical bundle formula**:

$$K_X=f^*(L)\otimes O_S\big(\sum_i (m_i-1)D_i\big).$$

Here the multiple fibers of *f* (if any) are written as $f^*(p_i)=m_iD_i$, for an integer *m*<sub>*i*</sub> at least 2 and a divisor *D*<sub>*i*</sub> whose coefficients have greatest common divisor equal to 1, and *L* is some line bundle on the smooth curve *S*. If *S* is projective (or equivalently, compact), then the degree of *L* is determined by the holomorphic Euler characteristics of *X* and *S*: deg(*L*) = χ(*X*,*O*<sub>*X*</sub>) − 2χ(*S*,*O*<sub>*S*</sub>). The canonical bundle formula implies that *K*<sub>*X*</sub> is **Q**-linearly equivalent to the pullback of some **Q**-divisor on *S*; it is essential here that the elliptic surface *X* → *S* is minimal.

Building on work of Kenji Ueno, Takao Fujita (1986) gave a useful variant of the canonical bundle formula, showing how *K*<sub>*X*</sub> depends on the variation of the smooth fibers. Namely, there is a **Q**-linear equivalence

$$K_X\sim_{\bf Q}f^*(K_S+B_S+M_S),$$

where the **discriminant divisor** *B*<sub>*S*</sub> is an explicit effective **Q**-divisor on *S* associated to the singular fibers of *f*, and the **moduli divisor** *M*<sub>*S*</sub> is $(1/12)j^*O(1)$, where *j*: *S* → **P**<sup>1</sup> is the function giving the *j*-invariant of the smooth fibers. (Thus *M*<sub>*S*</sub> is a **Q**-linear equivalence class of **Q**-divisors, using the identification between the divisor class group Cl(*S*) and the Picard group Pic(*S*).) In particular, for *S* projective, the moduli divisor *M*<sub>*S*</sub> has nonnegative degree, and it has degree zero if and only if the elliptic surface is isotrivial, meaning that all the smooth fibers are isomorphic.

The discriminant divisor in Fujita's formula is defined by

$$B_S=\sum_{p\in S}(1-c(p))[p],$$

where *c*(*p*) is the **log canonical threshold** $\text{lct}(X,f^*(p))$. This is an explicit rational number between 0 and 1, depending on the type of singular fiber. Explicitly, the lct is 1 for a smooth fiber or type $I_{\nu}$, and it is 1/*m* for a multiple fiber ${}_mI_{\nu}$, 1/2 for $I_{\nu}^*$, 5/6 for II, 3/4 for III, 2/3 for IV, 1/3 for IV\*, 1/4 for III\*, and 1/6 for II\*.

The canonical bundle formula (in Fujita's form) has been generalized by Yujiro Kawamata and others to families of Calabi–Yau varieties of any dimension.
