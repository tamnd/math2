---
tag: 8YNE1HTZEP
kind: statement
role: proposition
name: Kernels and images of commuting maps are invariant
msc: ["15A04"]
topics: [Z6S6PWMJPH]
audience: ug1
about: [0ACX5QT8TE]
uses: [0EP59ESQ94, 0BNEXSKNRV, 02YFME3RGW]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9780135367971
    locator: Section 6.4
---

## Statement

A map that commutes with $T$ has a kernel and an image that $T$ keeps, and this gives many invariant subspaces of $T$ for free.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].

1. If $S \colon V \to V$ is linear and $S T = T S$, then $\ker S$ and $\operatorname{im} S$ are [[$T$-invariant|0ACX5QT8TE]].
2. For each polynomial $p \in F[x]$, the subspaces $\ker p(T)$ and $\operatorname{im} p(T)$ are invariant under $q(T)$ for every $q \in F[x]$, and in particular under $T$.
3. If $U$ and $W$ are $T$-invariant subspaces, then $U + W$ and $U \cap W$ are $T$-invariant.

Here $p(T)$ is the [[value of $p$ at $T$|0E3MV6E6MG]].

## Remarks

### Why the maps must commute

Part 1 fails without the hypothesis $ST = TS$.
On $F^2$, let $T(a, b) = (b, 0)$ and $S(a, b) = (0, a)$.
Then $\ker S$ and $\operatorname{im} S$ are both the line $F e_2$, but $T(e_2) = e_1$ leaves that line.
The two maps do not commute, since
$$ST(e_2) = S(e_1) = e_2, \qquad TS(e_2) = T(0) = 0.$$
Part 2 is the case $S = p(T)$ of part 1, and it needs no extra hypothesis, because two polynomials in the same map always commute.

### What it gives you

Most invariant subspaces in the sub-area come from part 2.
With $p = x - \lambda$, the [[eigenspace|0G0RFPG8HR]] $E_\lambda = \ker(T - \lambda \id_V)$ is invariant.
With $p = (x - \lambda)^k$, the [[generalized eigenspace|0AJ035ZTZE]] is invariant.
With $p = x^k$, the kernels $\ker T^k$ and the images $\operatorname{im} T^k$ are invariant, which is the start of the [[Fitting decomposition|77SACA9CVQ]].
If $S$ commutes with $T$, then so does $S - \mu \id_V$, and part 1 shows that $T$ keeps each eigenspace $\ker(S - \mu \id_V)$ of $S$.
This is the main step of [[simultaneous diagonalization|0FK17N4DKA]].

### The converse

The converse of part 2 is false: an invariant subspace need not be a kernel or an image of a polynomial in $T$.
Take $T = \id_V$ with $\dim V = 2$.
Every line is invariant, but each $p(T) = p(1) \id_V$ has kernel $\{0\}$ or $V$ and image $V$ or $\{0\}$.

### Generalizations

The proof uses nothing about fields, so the statement holds for modules over any commutative ring.
For a commuting family $\mathcal{F}$ of maps, the kernel and the image of each member are invariant under every member.

## Explanations

### L1 human

Suppose two machines act on the same space, and the order in which they act does not matter.
Then the vectors that the first machine sends to zero form a region that the second machine never leaves.
A polynomial in a map, such as $T^2 - 3T$, always commutes with the map itself.
So its kernel is a region that $T$ never leaves.

### L2 human

Let $T(a, b, c) = (a + b, \; b, \; 2c)$ on $\R^3$, and let $p(x) = (x - 1)^2$.
First compute $T - \id$, then apply it twice:
$$(T - \id)(a, b, c) = (b, 0, c), \qquad (T - \id)^2(a, b, c) = (T - \id)(b, 0, c) = (0, 0, c).$$
So $\ker p(T)$ is the plane $c = 0$, and $\operatorname{im} p(T)$ is the line $\R e_3$.
Check: $T(a, b, 0) = (a + b, b, 0)$ stays in the plane, and $T(0, 0, c) = (0, 0, 2c)$ stays on the line.
This is the typical use: kernels of factors of the characteristic or minimal polynomial give invariant subspaces without any guessing.
Watch out: part 1 says nothing about a map $S$ that does not commute with $T$, as the example with $e_2$ above shows.

### L3 human

In the language of modules, $V$ is an $F[x]$-module through $T$, and each $p(T)$ is a module endomorphism.
Kernels and images of module endomorphisms are submodules, which is the statement.
More generally, every map in the commutant of $T$ is a module endomorphism, so its kernel and image are $T$-invariant.
The [[kernels lemma|ACBNK1VFVG]] sharpens part 2: for coprime $p$ and $q$, the invariant subspace $\ker (pq)(T)$ splits as $\ker p(T) \oplus \ker q(T)$.
