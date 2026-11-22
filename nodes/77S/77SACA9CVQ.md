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

Every linear map on a finite-dimensional space splits the space into a part where it is nilpotent and a part where it is invertible.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n$, and let $T \colon V \to V$ be linear.

1. The [[kernels|0S23E6YE83]] $\ker T^j$ increase with $j$ and the images $\operatorname{im} T^j$ decrease with $j$, and both chains are constant from some index $k \le n$ on.
2. $V = \ker T^n \oplus \operatorname{im} T^n$, a [[direct sum|0XYYT5KNTX]] of two $T$-[[invariant subspaces|0ACX5QT8TE]].
3. The [[restriction|0KN7EPH7Z0]] of $T$ to $\ker T^n$ is [[nilpotent|063D5Z2C70]], and the restriction of $T$ to $\operatorname{im} T^n$ is invertible.
4. The decomposition is unique: if $V = K \oplus I$ with $K$ and $I$ both $T$-invariant, $T|_K$ nilpotent and $T|_I$ invertible, then $K = \ker T^n$ and $I = \operatorname{im} T^n$.

The space $\ker T^n$ is called the Fitting null component of $T$, and $\operatorname{im} T^n$ the Fitting one component.

## Remarks

### A first example

Take the $3 \times 3$ matrix
$$T = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$
over $\R$.
It sends $e_2$ to $e_1$ and $e_1$ to $0$, so it is nilpotent on the plane $\operatorname{span}(e_1, e_2)$.
It also sends $(3, 2, 4)$ to $(6, 4, 8)$, twice itself, so it is invertible on that line.
The plane and the line together give $\R^3$, and they are the two Fitting components of $T$.
The powers of $T$ find them without any guessing, as the worked problem in the explanations shows.

### Why each hypothesis is needed

Finite dimension is what makes the chains stop.
The derivative $D$ on $\R[x]$ has $\ker D^j$ equal to the polynomials of degree less than $j$, and this chain grows forever.
The left shift $(x_1, x_2, \dots) \mapsto (x_2, x_3, \dots)$ on real sequences is onto, so all its images are the whole space, while its kernels grow without end; the kernels and the images then meet in a nonzero space, and no splitting exists.

The power must also be high enough.
For $T = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ we have $\ker T = \operatorname{im} T = F e_1$, so $\ker T + \operatorname{im} T$ is only a line.
With the power $n = 2$, $\ker T^2 = F^2$ and $\operatorname{im} T^2 = 0$, and the theorem holds.

### What it gives you

Apply the theorem to $T - \lambda \id_V$ for an eigenvalue $\lambda$.
Then $\ker (T - \lambda \id_V)^n$ is the [[generalized eigenspace|0AJ035ZTZE]] $V_\lambda$, and
$$V = V_\lambda \oplus \operatorname{im} (T - \lambda \id_V)^n,$$
with $T - \lambda$ invertible on the second summand.
This is the main step in the proof of the [[dimension of the generalized eigenspace|PHZ684KGWS]]: the characteristic polynomial of $T$ factors along the two summands, and $\lambda$ is not a root of the second factor.
Two more facts are read off at once: $T$ is invertible exactly when $\ker T^n = 0$, and $T$ is nilpotent exactly when $\operatorname{im} T^n = 0$.
Since $T$ is invertible on $\operatorname{im} T^n$, we also get $\operatorname{rank} T^m = \operatorname{rank} T^n$ for every $m \ge n$.

### The converse

Part 4 is the converse statement.
Any splitting of $V$ into an invariant part where $T$ is nilpotent and an invariant part where $T$ is invertible is the Fitting decomposition.

### Generalizations

The same statement holds for an endomorphism of a module of finite length over any ring, where $n$ is replaced by an index from which both chains are constant; this is [[Fitting's lemma|F52B2JMEHY]].
For a nilpotent Lie algebra acting on a module there is a [[Fitting decomposition for Lie modules|7MCBYWNF32]], which belongs to Lie theory.

## History

The result is named after Hans Fitting, who proved the version for modules of finite length.
One of its uses in module theory is that an indecomposable module of finite length has a local endomorphism ring.

## Explanations

### L1 human

Apply a matrix again and again.
Some vectors reach zero after a few steps, and they form one part of the space.
The other part is what remains after many steps, and on it the matrix only moves vectors around, without losing any of them.
The whole space is the sum of these two parts, and they meet only at zero.

### L2 human

Let us find the Fitting components of the matrix $T$ of the first example, with $n = 3$.

1. Compute the powers:
$$T^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 2 \\ 0 & 0 & 4 \end{pmatrix}, \qquad T^3 = \begin{pmatrix} 0 & 0 & 6 \\ 0 & 0 & 4 \\ 0 & 0 & 8 \end{pmatrix}.$$
2. Read off the kernels: $\ker T = \R e_1$, while $\ker T^2 = \ker T^3 = \operatorname{span}(e_1, e_2)$, so the kernel chain stops at $k = 2$.
3. Read off the images: $\operatorname{im} T^3$ is the line spanned by $(3, 2, 4)$, which is also $\operatorname{im} T^2$.
4. The vector $(3, 2, 4)$ is not in $\operatorname{span}(e_1, e_2)$, so $\R^3 = \operatorname{span}(e_1, e_2) \oplus \R (3, 2, 4)$.
5. On the plane, $T e_1 = 0$ and $T e_2 = e_1$, so $T$ is nilpotent there.
6. On the line, $T(3, 2, 4) = (6, 4, 8) = 2 (3, 2, 4)$, so $T$ is multiplication by $2$, which is invertible.

The typical use is to split off the invertible part of $T$ and study the nilpotent part alone.
The trap is to use $\ker T \oplus \operatorname{im} T$ instead: here $\operatorname{im} T = \operatorname{span}(e_1, (1, 1, 2))$ contains $\ker T = \R e_1$, so this sum is not direct.

### L3 human

In module language, $V$ is a module over $F[t]$, and the decomposition separates the part where $t$ acts nilpotently from the part where $t$ acts invertibly.
It is the [[primary decomposition|49ZHBMYKVE]] for the prime $t$, with all the other primary parts grouped together.
For modules of finite length, Fitting's lemma is the main tool in the proof of the Krull-Schmidt theorem on the uniqueness of decompositions into indecomposable modules.
