---
tag: 8NHEZN3NW2
kind: proof
name: Proof of the basis of a cyclic subspace
msc: ["15A21", "15A04"]
topics: [GEBYZKYV3D]
audience: ug2
proves: 5VYBJYPYMW
methods: [0NTF6DMVAP]
uses: [42MMQBTP0M, 03NDVCSHSB, 0MES3KS0ZC, 0CRMGPAH83, 0KCQ9Y3QKA, 0ACX5QT8TE, 0YQSGNYE3K, 0VH1TC1PWF, XYR7GPH20K, 0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Companion matrix
  - book: isbn:9780135367971
    locator: Section 7.1
---

## Proof

We find an annihilating polynomial by a dimension count, reduce every $f(T) v$ by division with remainder, and read off the basis and the matrix.

1. Let $n = \dim V$. The $n + 1$ vectors $v, Tv, \dots, T^n v$ are linearly dependent, because $V$ has dimension $n$.
2. So there is a nonzero $g \in F[x]$ of degree at most $n$ with $g(T) v = 0$. Dividing $g$ by its leading coefficient, we may take $g$ monic.
3. So the set of monic polynomials $f$ with $f(T) v = 0$ is not empty. Let $m_v$ be one of least degree in this set.
4. Let $f \in F[x]$ with $f(T) v = 0$. By [[division with remainder|0MES3KS0ZC]], $f = q m_v + r$ with $r = 0$ or $\deg r < \deg m_v$.
5. Then $r(T) v = f(T) v - q(T) m_v(T) v = 0$, because $(q m_v)(T) = q(T) m_v(T)$ for a [[polynomial of an endomorphism|0E3MV6E6MG]].
6. If $r \ne 0$, then $r$ divided by its leading coefficient is monic, kills $v$, and has smaller degree than $m_v$. This contradicts the choice in step 3, so $r = 0$ and $m_v$ divides $f$.
7. Conversely, if $f = q m_v$, then $f(T) v = q(T) m_v(T) v = 0$. With step 6 this proves part 2.
8. Let $m'$ be another monic polynomial of least degree that kills $v$. By step 6, $m_v$ divides $m'$, and both are monic of the same degree, so $m' = m_v$. This proves part 1.
9. Let $k = \deg m_v$ and write $m_v = x^k + c_{k-1} x^{k-1} + \cdots + c_0$. Suppose that $\sum_{i < k} a_i T^i v = 0$ with some $a_i \ne 0$. Then $h = \sum_{i < k} a_i x^i$ is a nonzero polynomial of degree less than $k$ that kills $v$.
10. By step 6, $m_v$ divides $h$, which is impossible for a nonzero $h$ of smaller degree. So $v, Tv, \dots, T^{k-1} v$ are [[linearly independent|0CRMGPAH83]].
11. Let $f \in F[x]$ be arbitrary and write $f = q m_v + r$ as in step 4. By step 5, $f(T) v = r(T) v$, which is a combination of $v, Tv, \dots, T^{k-1} v$ because $\deg r < k$ or $r = 0$.
12. Since $Z(v; T)$ is the set of all $f(T) v$, steps 10 and 11 show that $v, Tv, \dots, T^{k-1} v$ is a [[basis|0KCQ9Y3QKA]] of $Z(v; T)$. This proves part 3.
13. For $w = f(T) v$ in $Z(v; T)$, we have $Tw = (x f)(T) v$, which lies in $Z(v; T)$. So $Z(v; T)$ is [[$T$-invariant|0ACX5QT8TE]].
14. Let $U$ be a $T$-invariant subspace with $v \in U$. By induction on $i$, $T^i v \in U$ for all $i \ge 0$, so $Z(v; T) \subseteq U$. This proves part 4.
15. Let $v \ne 0$, and put $b_i = T^{i-1} v$ for $1 \le i \le k$. Then $T b_i = b_{i+1}$ for $i < k$.
16. The last basis vector goes to $T b_k = T^k v = -c_0 b_1 - c_1 b_2 - \cdots - c_{k-1} b_k$, because $m_v(T) v = 0$.
17. The columns of the [[matrix of $T|_{Z(v; T)}$|0YQSGNYE3K]] are the coordinates of $T b_1, \dots, T b_k$. By steps 15 and 16 this matrix is the [[companion matrix|0VH1TC1PWF]] $C(m_v)$, which proves part 5.
18. By the [[theorem on companion matrices|XYR7GPH20K]], $C(m_v)$ has minimal and characteristic polynomial $m_v$. These polynomials do not depend on the basis, so they are the polynomials of $T|_{Z(v; T)}$. For $v = 0$ both equal $1$ on the zero space, which proves part 6.

## Idea

The vectors $v, Tv, T^2 v, \dots$ stay independent until the first one that depends on the earlier ones.
The dependence at that step is the annihilator $m_v$, and division with remainder by $m_v$ pushes every $f(T) v$ back to the earlier vectors.
In the basis that results, $T$ moves each vector to the next one and sends the last one to the combination given by $m_v$, which is exactly the shape of a companion matrix.

## Variants

The module proof is shorter.
The map $F[x] \to Z(v; T)$, $f \mapsto f(T) v$, is a surjective homomorphism of $F[x]$-modules, and its kernel is an ideal of $F[x]$.
Every ideal of $F[x]$ is principal, so the kernel is $(m_v)$, and $Z(v; T) \cong F[x]/(m_v)$.
The classes of $1, x, \dots, x^{k-1}$ form a basis of $F[x]/(m_v)$ by division with remainder, and their images give part 3 again.
