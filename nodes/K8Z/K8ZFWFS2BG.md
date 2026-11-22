---
tag: K8ZFWFS2BG
kind: proof
name: Proof that similarity does not depend on the field
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
proves: 5PVFX89NM7
methods: [0NTF6DMVAP]
uses: [042JWAR3Q0, 0VH1TC1PWF, F7GJPMVBXA, 027KDW2K72, XYR7GPH20K]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
    locator: General case and theory
  - book: isbn:9780135367971
    locator: Section 7.2
---

## Proof

We show that the rational canonical form of $A$ over $K$ is also its rational canonical form over $L$, and then we compare the forms of $A$ and $B$.

*Part 1.*

1. By the [[rational canonical form theorem|042JWAR3Q0]] over $K$, there are $P_A \in GL_n(K)$ and monic nonconstant $d_1 \mid \cdots \mid d_r$ in $K[x]$ with $A = P_A R P_A^{-1}$ and $R = C(d_1) \oplus \cdots \oplus C(d_r)$.
   These $d_i$ are the [[invariant factors|F7GJPMVBXA]] of $A$ over $K$.
2. Each $d_i$ is also monic and nonconstant as an element of $L[x]$.
   If $d_i e = d_{i+1}$ with $e \in K[x]$, then $e$ also lies in $L[x]$, so $d_1 \mid \cdots \mid d_r$ also holds in $L[x]$.
3. A [[companion matrix|0VH1TC1PWF]] $C(d_i)$ depends only on the coefficients of $d_i$, so $R$ is also a block matrix of companion matrices of the kind allowed in $M_n(L)$.
4. Since $P_A \in GL_n(K) \subseteq GL_n(L)$, the equation $A = P_A R P_A^{-1}$ also holds over $L$.
5. By the uniqueness part of the rational canonical form theorem over $L$, the matrix $R$ is the rational canonical form of $A$ over $L$.
   So the invariant factors of $A$ over $L$ are $d_1, \dots, d_r$, which proves part 1.

*Part 3.*

6. By the [[theorem on companion matrices|XYR7GPH20K]], the block $C(d_i)$ has minimal polynomial $d_i$.
7. A polynomial kills the block diagonal matrix $R$ exactly when it kills each block, so the minimal polynomial of $R$ is $\operatorname{lcm}(d_1, \dots, d_r) = d_r$.
8. Similar matrices have the same minimal polynomial, so the minimal polynomial of $A$ is $d_r$, both over $K$ and, by step 5, over $L$.

*Part 2.*

9. Apply steps 1 to 5 to $B$.
   This gives $B = P_B R' P_B^{-1}$ with $P_B \in GL_n(K)$, where $R'$ is the rational canonical form of $B$ over $K$ and also over $L$.
10. The matrices $A$ and $B$ are similar over $L$, and [[similarity|027KDW2K72]] is an equivalence relation, so they have the same rational canonical form over $L$.
    So $R = R'$.
11. Then
$$B = P_B R P_B^{-1} = P_B P_A^{-1} A P_A P_B^{-1}.$$
    Put $P = P_A P_B^{-1}$, which lies in $GL_n(K)$.
    Then $B = P^{-1} A P$, and part 2 is proved.

## Idea

The rational canonical form is computed by operations inside $K$, and it is unique over every field.
So the form over $K$ is already the form over $L$.
Two matrices that are similar over $L$ have equal forms over $L$, hence equal forms over $K$, and the transition matrices to the common form have entries in $K$.

## Variants

The [[theorem on the characteristic matrix|92VZF0QRM8]] gives a second proof.
The determinantal divisors are gcds of polynomials in $K[x]$, and a gcd computed by the Euclidean algorithm in $K[x]$ is also the gcd in $L[x]$.

For infinite $K$ there is a proof with no canonical forms.
Let $X_1, \dots, X_m$ be a $K$-basis of the solutions of the linear system $AX = XB$.
Gaussian elimination over $K$ shows that they are also an $L$-basis of the solutions over $L$, so the given $Q$ is an $L$-combination of them.
Then $f(t) = \det(t_1 X_1 + \cdots + t_m X_m)$ is a polynomial with coefficients in $K$, and it is nonzero at the coordinates of $Q$, so it is not the zero polynomial.
A nonzero polynomial over an infinite field has a nonzero value at some point of $K^m$, and that point gives an invertible $X \in M_n(K)$ with $AX = XB$.
The argument fails for finite $K$, where a nonzero polynomial such as $t^q - t$ over $\mathbb{F}_q$ can vanish at every point.
