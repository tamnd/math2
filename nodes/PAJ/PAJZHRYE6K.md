---
tag: PAJZHRYE6K
kind: proof
name: Proof of quantifier elimination for Z-groups by the embedding test
msc: ["03C10", "03B25"]
topics: [1A9JSC5YG8]
audience: grad
proves: VKC9CR37FT
uses: [Q1CGE4DWXQ, A49BATWQEH, 007NPQX34K, C9494XYEMN]
methods: [0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Presburger_arithmetic
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Proof

We use the embedding test of [[the tests for quantifier elimination|Q1CGE4DWXQ]]; $L$ has the constant $0$.
Let $M, N$ be $\Z$-groups with a common substructure $A$, let $\bar a$ be a tuple in $A$, and let $\varphi(\bar a, y)$ be a conjunction of literals with $M \models \varphi(\bar a, b)$.
We find $c \in N$ with $N \models \varphi(\bar a, c)$.
We write $k$ for $k \cdot 1$ when $k \in \Z$.

### Normal form

1. Every term in $y$ with parameters in $A$ has the form $k y + t$ with $k \in \Z$ and $t \in A$. So each literal is $k y + t = 0$, $k y + t \neq 0$, $k y + t > 0$, $k y + t \le 0$, $D_n(k y + t)$ or $\neg D_n(k y + t)$. Literals with $k = 0$ have parameters in $A$ only, and they hold in $N$ because they hold in $M$.
2. Let $K$ be the [[least common multiple|007NPQX34K]] of the coefficients $k \neq 0$. Multiplying each literal by $K / \abs k$ turns $k y$ into $\pm K y$, with $D_n$ replaced by $D_{n K / \abs k}$. With $z = K y$ we get a conjunction $\psi(\bar a, z)$ of literals in $z$ with coefficient $\pm 1$, and $\varphi(\bar a, y) \leftrightarrow \psi(\bar a, K y)$ in every $\Z$-group.
3. Put $z_0 = K b$. Then $M \models \psi(\bar a, z_0) \land D_K(z_0)$. It suffices to find $d \in N$ with $N \models \psi(\bar a, d) \land D_K(d)$, since then $d = K c$ for some $c \in N$.

### Case 1: an equation

If $\psi$ contains $z = s$ or $-z = s$ with $s \in A$, then $z_0 = \pm s \in A$.
The literals $\psi(\bar a, z_0)$ and $D_K(z_0)$ have parameters in $A$, so they hold in $N$, and $d = z_0$ works.

### Case 2: no equation

1. Let $N_0$ be the least common multiple of $K$ and of all moduli $n$. Each element $w$ of a $\Z$-group has a residue $\rho(w) \in \set{0, \dots, N_0 - 1}$ with $D_{N_0}(w - \rho(w))$. For $w \in A$ this residue is the same in $M$ and in $N$.
2. Each congruence literal $D_n(\pm z + t)$ or its negation depends only on the residue of $z$, given the residue of $t$. Let $r = \rho(z_0)$. Every $d \in N$ with $\rho(d) = r$ satisfies the congruence literals and $D_K(d)$.
3. The other literals say $s_i < z$, $z < u_j$ and $z \neq v_l$, with $s_i, u_j, v_l \in A$ and $l = 1, \dots, m$; a literal $z \le t$ is rewritten as $z < t + 1$, using discreteness. Let $s$ be the largest $s_i$ and $u$ the smallest $u_j$; the order on $A$ is the same in $M$ and $N$.
4. Subcase: $u - s \le (m + 1) N_0$. In a $\Z$-group, $0 < x \le n$ implies $x = j$ for some integer $1 \le j \le n$, by discreteness. So $z_0 = s + j$ for an integer $j$, and $z_0 \in A$. Then $d = z_0$ works, as in Case 1.
5. Subcase: $u - s > (m + 1) N_0$, a condition on $A$ that also holds in $N$. Let $e \in N$ be the least element above $s$ with residue $r$; it is $s + j$ with $1 \le j \le N_0$. The elements $e, e + N_0, \dots, e + m N_0$ lie strictly between $s$ and $u$, have residue $r$, and are distinct, so one of them differs from all $v_l$. Take it as $d$.
6. If there is no upper bound, or no lower bound, or neither, the same argument works with the elements above $s$, below $u$, or above $0$.

In all cases $N \models \exists y \, \varphi(\bar a, y)$, so $T_\Z$ has quantifier elimination by the embedding test.

## Idea

After scaling, the variable appears with coefficient one.
A solution is then determined, up to finitely many exceptions, by its position between the bounds and by its residue modulo one common period.
If the interval between the bounds is short, the solution is a bound plus an integer and lies in $A$; if it is long, one period contains enough candidates in $N$.

## Variants

Cooper's procedure is the syntactic form of the same argument: it replaces $\exists z$ by a finite disjunction over the test points $s + j$ with $1 \le j \le N_0$, and it is used in [[the proof of Presburger's theorem|FSX4D0YCTJ]].
One can also use the extension test with an $\omega$-saturated $N$, realizing the cut and the residue of a new element over a finitely generated substructure.
