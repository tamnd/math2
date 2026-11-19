---
tag: PDH3HKXWAZ
kind: statement
role: theorem
name: Structure of the solution set of a linear system
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0GT4WWGWH2, 04KGXJG1A2, 0PHDYNR24D, 00YC1D652K, 0PYW26VNT6, 0W4FSW1TVB, 0EWQEYRVA8, E7SAHXQEVC]
about: [0GT4WWGWH2]
proofs: [6D2XRTWTCG]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Homogeneous systems
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]], let $A$ be an $m \times n$ matrix over $F$, and let $b \in F^m$.
Let $N = \set{x \in F^n : Ax = 0}$ be the solution set of the [[homogeneous system|04KGXJG1A2]], which is the [[null space|0PHDYNR24D]] of $A$.
Let $S = \set{x \in F^n : Ax = b}$ be the solution set of the [[system|0GT4WWGWH2]] $Ax = b$.

1. $N$ is a [[linear subspace|00YC1D652K]] of $F^n$.
2. (Superposition.) If $Ax_1 = b_1$ and $Ax_2 = b_2$, then $A(c_1 x_1 + c_2 x_2) = c_1 b_1 + c_2 b_2$ for all $c_1, c_2 \in F$.
3. If $p \in S$, then $S = p + N = \set{p + v : v \in N}$.
4. So $S$ is empty, or it is an [[affine subspace|0PYW26VNT6]] of $F^n$ with direction $N$.
5. $\dim N = n - \operatorname{rank} A$, so a nonempty $S$ has dimension $n - \operatorname{rank} A$.

## Remarks

### Why each hypothesis is needed

1. Part 3 needs $p \in S$; if the system is inconsistent, $S$ is empty and is not of the form $p + N$.
2. Part 1 needs the right side $0$: for $b \neq 0$ the set $S$ does not contain $0$, so it is not a subspace, as in [[a non-homogeneous system whose solution set is not a subspace|J291MKHE97]].
3. The equations must be linear: for $x^2 = 1$ the solutions $1$ and $-1$ have difference $2$, and $1 + 2 \cdot 2 = 5$ is not a solution.

### Consequences

1. A consistent system has a unique solution if and only if $N = \set{0}$, that is, $\operatorname{rank} A = n$.
2. The difference of two solutions of $Ax = b$ solves $Ax = 0$.
3. The [[parametric form|KQT68YPHD1]] $p + t_1 v_1 + \dots + t_k v_k$ is an instance of part 3, with $v_1, \dots, v_k$ a basis of $N$.
4. Over a field with $q$ elements, a consistent system has $|N| = q^{\dim N}$ solutions.

### Converse

Every affine subspace $p + N$ of $F^n$ is the solution set of some system: choose $A$ whose null space is $N$, for example with rows a basis of the vectors orthogonal to $N$ over $\R$, and put $b = Ap$.

### Generalizations

The same proof works for any [[linear map|0NRYHJPQG2]] $T \colon V \to W$: the solutions of $T(x) = w$ are empty or a coset $p + \ker T$.
This is the form used for linear differential equations, see [[the general solution of an inhomogeneous linear equation|0GHWEH6H15]].

### History

The rule "general solution $=$ particular solution $+$ homogeneous solution" is standard in Lay, Section 1.5, and in the theory of linear differential equations.

## Explanations

### L1 human

To find all solutions of a system, it is enough to find one solution.
Then add to it every solution of the same system with right side $0$.
For example, $x + y = 2$ has the solution $(1, 1)$, and $x + y = 0$ has the solutions $(t, -t)$.
So all solutions of $x + y = 2$ are $(1 + t, 1 - t)$.

### L2 human

We find all solutions of $x + 2y + z = 4$, $y - z = 1$ over $\R$.

1. A particular solution: put $z = 0$; then $y = 1$ and $x = 2$, so $p = (2, 1, 0)$.
2. The homogeneous system $x + 2y + z = 0$, $y - z = 0$: put $z = t$, then $y = t$ and $x = -3t$.
3. So $N = \set{t(-3, 1, 1) : t \in \R}$, a line through $0$.
4. By part 3, $S = \set{(2, 1, 0) + t(-3, 1, 1) : t \in \R}$.
5. Check: $(2 - 3t) + 2(1 + t) + t = 4$ and $(1 + t) - t = 1$.

The typical use is to split the solving into two easier tasks, or to describe the shape of the solution set.
A trap: the sum of two solutions of $Ax = b$ solves $Ax = 2b$, not $Ax = b$.

### L3 human

The map $x \mapsto Ax$ is a linear map $F^n \to F^m$, and $S$ is the fibre over $b$.
The fibres are the cosets of the kernel, so the nonempty fibres are the elements of the quotient space $F^n / N$.
The dimension formula is the rank-nullity theorem for this map.
