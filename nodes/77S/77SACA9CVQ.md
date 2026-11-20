---
tag: 77SACA9CVQ
kind: statement
role: theorem
name: Fitting decomposition of an endomorphism
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: grad
about: [0ACX5QT8TE, 063D5Z2C70]
uses: [0S23E6YE83, 041JTZCK9Q, 0M8MHYERTY, 0EP59ESQ94]
sources:
  - url: https://en.wikipedia.org/wiki/Fitting_lemma
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n$, and let $T \colon V \to V$ be linear.

1. The [[kernels|0S23E6YE83]] $\ker T^j$ increase with $j$, and the images $\operatorname{im} T^j$ decrease with $j$. Both chains are constant from some index $k \le n$ on.
2. $V = \ker T^n \oplus \operatorname{im} T^n$, a [[direct sum|0XYYT5KNTX]] of $T$-[[invariant subspaces|0ACX5QT8TE]].
3. The [[restriction|0KN7EPH7Z0]] of $T$ to $\ker T^n$ is [[nilpotent|063D5Z2C70]], and the restriction of $T$ to $\operatorname{im} T^n$ is invertible.
4. The decomposition is unique: if $V = K \oplus I$ with $T$-invariant $K$ and $I$, $T|_K$ nilpotent and $T|_I$ invertible, then $K = \ker T^n$ and $I = \operatorname{im} T^n$.

We call $\ker T^n$ the Fitting null component and $\operatorname{im} T^n$ the Fitting one component of $T$.

## Remarks

### Why each hypothesis is needed

- Finite dimension is needed for the chains to stop. The derivative $D$ on $\R[x]$ has $\ker D^j$ the polynomials of degree less than $j$. This chain never stops.
- The shift $(x_1, x_2, \dots) \mapsto (x_2, x_3, \dots)$ on sequences is surjective, so all its images are the whole space, but its kernels grow without end.
- The power must be large enough. For $T = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $\ker T = \operatorname{im} T = F e_1$, so $\ker T + \operatorname{im} T$ is not $V$.

### Consequences

- Apply the theorem to $T - \lambda \id_V$. Then $\ker (T - \lambda \id_V)^n$ is the [[generalized eigenspace|0AJ035ZTZE]] $V_\lambda$, and $V = V_\lambda \oplus \operatorname{im} (T - \lambda \id_V)^n$.
- This gives the [[dimension of the generalized eigenspace|PHZ684KGWS]]: $\dim V_\lambda$ is the algebraic multiplicity of $\lambda$.
- $T$ is invertible exactly when $\ker T^n = 0$, and $T$ is nilpotent exactly when $\operatorname{im} T^n = 0$.
- $T$ restricted to $\operatorname{im} T^n$ is invertible, so $\operatorname{rank} T^m = \operatorname{rank} T^n$ for all $m \ge n$.

### Converse

Part 4 is a converse: any splitting of $V$ into a nilpotent part and an invertible part is the Fitting decomposition.

### Generalizations

The same statement holds for an endomorphism of a module of finite length over any ring; this is [[Fitting's lemma|F52B2JMEHY]].
There the index $n$ is replaced by an index from which both chains are constant.
For a nilpotent Lie algebra acting on a module, there is a [[Fitting decomposition for Lie modules|7MCBYWNF32]], which belongs to Lie theory.

## History

Fitting proved the module version, and it shows that an indecomposable module of finite length has a local endomorphism ring.
The linear algebra case appears in Axler, Chapter 8, as the decomposition $V = \ker T^n \oplus \operatorname{im} T^n$.

## Explanations

### L1 human

Apply a matrix again and again.
Some vectors eventually go to zero, and they form one part of the space.
The other part is what is left after many applications, and the matrix moves it around without losing anything.
The whole space is the sum of these two parts, with no overlap.

### L2 human

Let $T = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 2 \end{pmatrix}$ over $\R$, so $n = 3$.

1. $T^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 2 \\ 0 & 0 & 4 \end{pmatrix}$ and $T^3 = \begin{pmatrix} 0 & 0 & 6 \\ 0 & 0 & 4 \\ 0 & 0 & 8 \end{pmatrix}$.
2. $\ker T = \R e_1$, while $\ker T^2 = \ker T^3 = \operatorname{span}(e_1, e_2)$. So the chain stops at $k = 2$.
3. $\operatorname{im} T^3$ is the line spanned by $(3, 2, 4)$, which is also $\operatorname{im} T^2$.
4. $(3, 2, 4)$ is not in $\operatorname{span}(e_1, e_2)$, so $\R^3 = \operatorname{span}(e_1, e_2) \oplus \R (3, 2, 4)$.
5. On $\operatorname{span}(e_1, e_2)$, $T e_1 = 0$ and $T e_2 = e_1$, so $T$ is nilpotent there.
6. $T(3, 2, 4) = (6, 4, 8) = 2 (3, 2, 4)$, so $T$ acts as multiplication by $2$ on the line, which is invertible.

The typical use is to split off the invertible part of $T$ and study the nilpotent part alone.
The trap is to use $\ker T \oplus \operatorname{im} T$: here $\ker T = \R e_1$ lies inside $\operatorname{im} T$, so this sum is not direct.

### L3 human

In module language, $V$ is an $F[t]$-module, and the decomposition separates the $t$-primary part from the part where $t$ acts invertibly.
It is the special case $p = t$ of the [[primary decomposition|49ZHBMYKVE]], with the other primary parts grouped together.
For modules of finite length, Fitting's lemma gives the Krull-Schmidt theorem on the uniqueness of decompositions into indecomposable modules.
