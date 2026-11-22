---
tag: 4FV9TDGWWH
kind: statement
role: theorem
name: Conjugacy classes of GL_n over a finite field
aliases: [conjugacy-classes-of-gl-n-over-finite-fields, number-of-conjugacy-classes-of-gl-n-fq]
msc: ["20G40", "15A21"]
topics: [GEBYZKYV3D]
audience: grad
about: [0FCHE902D7, 0DEBXAJ5SA]
uses: [0FCHE902D7, 0DEBXAJ5SA, 0ZXZ82FTX2, 042JWAR3Q0, F7GJPMVBXA, 0JV30XN73Z, 0JQ1KNQW2K, 08BPSC6YTE, 0VK5V9P8G3, GXZGWZSJ2J]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy class equation
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: Over finite fields
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
    locator: General case and theory
---

## Statement

The conjugacy classes of the finite group $GL_n(\mathbb{F}_q)$ are the rational canonical forms of invertible matrices, and this turns the count of classes into a count of polynomial data.

Let $q$ be a prime power, let $\mathbb{F}_q$ be the [[finite field|0ZXZ82FTX2]] with $q$ elements, and let $n \ge 1$.
Let $G = GL_n(\mathbb{F}_q)$ be the [[general linear group|0FCHE902D7]], and let $c_n(q)$ be the number of its [[conjugacy classes|0DEBXAJ5SA]].
Let $\Phi$ be the set of monic irreducible polynomials in $\mathbb{F}_q[x]$ other than $x$.

1. Two matrices in $G$ are conjugate in $G$ if and only if they have the same [[invariant factors|F7GJPMVBXA]]. So the conjugacy classes of $G$ correspond bijectively to the [[rational canonical forms|042JWAR3Q0]] $C(d_1) \oplus \cdots \oplus C(d_r)$ of size $n$ with $d_r(0) \ne 0$.
2. Equivalently, the classes correspond bijectively to the maps $f \mapsto \lambda(f)$ that assign to each $f \in \Phi$ an [[integer partition|0JV30XN73Z]] $\lambda(f)$, possibly empty, with $\sum_{f \in \Phi} \deg f \cdot |\lambda(f)| = n$.
3. As formal power series in $u$, with $c_0(q) = 1$,
$$\sum_{n \ge 0} c_n(q)\, u^n = \prod_{k \ge 1} \frac{1 - u^k}{1 - q u^k}.$$
In particular $c_1 = q - 1$, $c_2 = q^2 - 1$, $c_3 = q^3 - q$ and $c_4 = q^4 - q$.
4. For $n = 2$, the $q^2 - 1$ classes are of the four types in the table.

| type | representative | number of classes | centralizer order | class size |
|---|---|---|---|---|
| scalar | $a I_2$, $a \ne 0$ | $q - 1$ | $(q^2 - 1)(q^2 - q)$ | $1$ |
| one eigenvalue, not scalar | $\begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix}$, $a \ne 0$ | $q - 1$ | $q(q - 1)$ | $q^2 - 1$ |
| two eigenvalues in $\mathbb{F}_q$ | $\operatorname{diag}(a, b)$, $a \ne b$, $ab \ne 0$ | $(q - 1)(q - 2)/2$ | $(q - 1)^2$ | $q(q + 1)$ |
| no eigenvalue in $\mathbb{F}_q$ | $C(f)$, $f$ irreducible of degree $2$ | $(q^2 - q)/2$ | $q^2 - 1$ | $q(q - 1)$ |

The class sizes add up to $|G|$, as the [[class equation|08BPSC6YTE]] requires.

## Remarks

### A first count by hand

Take $q = 3$, so $|GL_2(\mathbb{F}_3)| = (9 - 1)(9 - 3) = 48$.
The four types give $2$, $2$, $1$ and $3$ classes, in total $8 = 3^2 - 1$.
The irreducible quadratics are $x^2 + 1$, $x^2 + x + 2$ and $x^2 + 2x + 2$, and the only diagonal type is $\operatorname{diag}(1, 2)$.
The class sizes are $1$, $8$, $12$ and $6$, and the class equation checks:
$$2 \cdot 1 + 2 \cdot 8 + 1 \cdot 12 + 3 \cdot 6 = 48.$$
For $q = 2$ the group has order $6$ and $3$ classes, worked out in the [[three conjugacy classes of GL_2(F_2)|T87V16N2DB]].

### Why each hypothesis is needed

The field must be finite for the counts in parts 3 and 4.
Over an infinite field there are infinitely many classes, since the scalar matrices $a I_n$ with $a \ne 0$ are pairwise not conjugate.
Part 1 holds over every field with the same proof, because conjugacy in $GL_n(F)$ is similarity over $F$.

The condition $d_r(0) \ne 0$ in part 1 is what makes the matrix invertible.
Without it the list also contains singular rational canonical forms, such as the zero matrix, which are not elements of $G$.

### What it gives you

The number $c_n(q)$ is a polynomial in $q$ with integer coefficients and leading term $q^n$.
For example, $GL_3(\mathbb{F}_2)$, a group of order $168$, has $c_3(2) = 8 - 2 = 6$ classes.

The centralizer of $A \in G$ is the group of units of the algebra of [[matrices that commute with A|GXZGWZSJ2J]].
For a cyclic $A$ this algebra is $\mathbb{F}_q[A] \cong \mathbb{F}_q[x]/(\chi_A)$, so its units are easy to count.
By the [[class size formula|0VK5V9P8G3]], the class of $A$ then has $|G| / |C_G(A)|$ elements, where $|G|$ comes from the [[order of the general linear group|0JQ1KNQW2K]].

### Generalizations

The same method counts the similarity classes in all of $M_n(\mathbb{F}_q)$.
Drop the condition $d_r(0) \ne 0$ in part 1 and allow $f = x$ in part 2, and the generating function becomes $\prod_{k \ge 1} 1/(1 - q u^k)$.
Its coefficient of $u^2$ is $q^2 + q$, which matches the [[similarity classes of 2 × 2 matrices|H6R274A93F]].

### Watch out

In the third type the pair $a, b$ is unordered.
The matrices $\operatorname{diag}(a, b)$ and $\operatorname{diag}(b, a)$ are conjugate by the permutation matrix that swaps $e_1$ and $e_2$, so they give one class, not two.
Counting ordered pairs would give $(q - 1)(q - 2)$ classes of this type, and for $q \ge 3$ the total would exceed $q^2 - 1$.

## Explanations

### L1 human

Two invertible matrices over a finite field are conjugate exactly when they have the same rational canonical form.
So counting conjugacy classes means counting rational canonical forms.
For $2 \times 2$ matrices over a field with $q$ elements there are $q^2 - 1$ classes.
With $q = 3$ that gives $8$ classes in a group of $48$ matrices.

### L2 human

Here is a typical use: count the conjugacy classes of $GL_3(\mathbb{F}_q)$ from part 3.
Each factor of the product is
$$\frac{1 - v}{1 - q v} = 1 + (q - 1) v + (q - 1) q v^2 + (q - 1) q^2 v^3 + \cdots, \qquad v = u^k.$$
A term $u^3$ comes from $u^3$ in the factor $k = 1$, from $u \cdot u^2$ in the factors $k = 1$ and $k = 2$, or from $u^3$ in the factor $k = 3$.
So
$$c_3 = (q - 1) q^2 + (q - 1)^2 + (q - 1) = (q - 1)(q^2 + q) = q^3 - q.$$
For $q = 2$ this gives $6$, the number of classes of the group of order $168$.
The generating function turns a question about a finite group into arithmetic with power series.

### L3 human

The conjugacy classes of $GL_n(\mathbb{F}_q)$ are indexed by partition-valued functions on $\Phi$.
The centralizer of a class is the unit group of the endomorphism ring of the module $\bigoplus_f \bigoplus_i \mathbb{F}_q[x]/(f^{\lambda_i(f)})$, so its order depends only on the degrees $\deg f$ and the partitions $\lambda(f)$.
The [[centralizer theorem|GXZGWZSJ2J]] gives the dimension of that ring, and the units of the ring give the class size.
This indexing is the starting point of the character theory of $GL_n(\mathbb{F}_q)$ in the representation theory of finite groups.
