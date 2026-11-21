---
tag: T6KS32FGAV
kind: proof
name: Proof of elimination of imaginaries in algebraically closed fields
aliases: [proof-of-elimination-of-imaginaries-in-acf, proof-of-poizat-elimination-of-imaginaries]
msc: ["03C07", "03C60"]
topics: [SZRM3N6BXW]
audience: grad
proves: 6M2R0ER3KV
uses: [120S3V3975, 2NBBJADY5N, PNGY60EBDJ, DKAGC639W9, EYTTQZ0E1S, 7WH24MZZQ8, 0W4X9G6263, 0SDC934R52, 1NR3HAWG9D]
methods: [0ASJVEFA9J, H840D9TM2X, 0NTF6DMVAP, TFQ1845T84]
sources:
  - url: https://en.wikipedia.org/wiki/Imaginary_element
    locator: Definitions
  - book: isbn:9780521763240
  - book: isbn:9780198534372
---

## Proof

Let $\mathbb{M}$ be a [[monster model|EYTTQZ0E1S]] of $\mathrm{ACF}_p$, and work in $\mathbb{M}^{\mathrm{eq}}$, with $\operatorname{dcl}$ and $\operatorname{acl}$ computed there.
We use the automorphism criterion of the monster model, as in [[types as orbits|7WH24MZZQ8]]: for a small set $A$, an element $c$ is in $\operatorname{dcl}(A)$ exactly when every automorphism fixing $A$ pointwise fixes $c$.
Likewise, $c$ is in $\operatorname{acl}(A)$ exactly when $c$ has finitely many images under these automorphisms; see [[algebraic and definable closure|DKAGC639W9]].

### Step 1: points in the algebraic closure

1. By [[quantifier elimination for ACF|2NBBJADY5N]], each definable subset of $\mathbb{M}$ is finite or cofinite, so $\mathrm{ACF}_p$ is [[strongly minimal|PNGY60EBDJ]]. This holds for sets defined with imaginary parameters too, since such a set is also defined with a real representative.
2. The set $\operatorname{acl}(\emptyset) \cap \mathbb{M}$ contains the algebraic closure of the prime field, which is infinite.
3. Claim: for each small $B \subseteq \mathbb{M}^{\mathrm{eq}}$ and each nonempty $B$-definable $X \subseteq \mathbb{M}^n$, some point of $X$ lies in $\operatorname{acl}(B)$. We prove it by induction on $n$.
4. Case $n = 1$, $X$ finite. Each point of $X$ has finitely many images under automorphisms fixing $B$, since these permute $X$. So each point is in $\operatorname{acl}(B)$.
5. Case $n = 1$, $X$ cofinite. The infinite set of step 2 lies in $\operatorname{acl}(B)$, and only finitely many of its points miss $X$.
6. Case $n > 1$. The projection $Y$ of $X$ to the first coordinate is nonempty and $B$-definable, so by the case $n = 1$ it has a point $a \in \operatorname{acl}(B)$.
7. The fiber $X_a = \set{\bar c : (a, \bar c) \in X}$ is nonempty and $(B \cup \set{a})$-definable. By induction it has a point $\bar c \in \operatorname{acl}(B a) = \operatorname{acl}(B)$, and then $(a, \bar c) \in X$.

### Step 2: weak elimination

1. Let $e = \bar a / E$ be an imaginary, for a $\emptyset$-definable equivalence relation $E$ on $\mathbb{M}^n$.
2. The class $X = \set{\bar x : E(\bar x, \bar a)}$ is nonempty and $e$-definable, by $\pi_E(\bar x) = e$.
3. By step 1 with $B = \set{e}$, some $\bar b \in X$ lies in $\operatorname{acl}(e)$.
4. Then $e = \pi_E(\bar b)$, so $e \in \operatorname{dcl}(\bar b)$.

### Step 3: codes of finite sets

1. Let $F = \set{\bar c_1, \dots, \bar c_k}$ be a finite set of $n$-tuples. Let $P_F = \prod_{j = 1}^{k} (Y + c_{j 1} X_1 + \dots + c_{j n} X_n)$, and let $\bar d$ be its tuple of coefficients in a fixed order of monomials.
2. If an automorphism $\sigma$ maps $F$ onto $F$, it permutes the factors of $P_F$, so it fixes $\bar d$.
3. If $\sigma$ fixes $\bar d$, then $P_{\sigma F} = P_F$. The ring $\mathbb{M}[Y, X_1, \dots, X_n]$ is a [[UFD|0W4X9G6263]], by the theory of [[polynomial rings|0SDC934R52]], and each factor is irreducible and monic in $Y$. So the factors of $P_F$ are determined, and $\sigma F = F$.

### Step 4: elimination

1. Take $e$ and $\bar b$ as in step 2. Let $F$ be the set of images of $\bar b$ under the automorphisms fixing $e$. It is finite, since $\bar b \in \operatorname{acl}(e)$.
2. Let $\bar d$ be the code of $F$ from step 3. Each automorphism fixing $e$ maps $F$ onto $F$, so it fixes $\bar d$, and $\bar d \in \operatorname{dcl}(e)$.
3. Let $\sigma$ fix $\bar d$. By step 3, $\sigma F = F$, so $\sigma \bar b = \tau \bar b$ for some automorphism $\tau$ fixing $e$.
4. Then $\sigma(e) = \pi_E(\sigma \bar b) = \pi_E(\tau \bar b) = \tau(e) = e$. So $e \in \operatorname{dcl}(\bar d)$.
5. So $e$ and the real tuple $\bar d$ are interdefinable, and $\mathrm{ACF}_p$ eliminates imaginaries.

### Step 5: uniformity

1. Fix $E$ on $\mathbb{M}^n$. For each class $e$, steps 2 to 4 give $\emptyset$-definable maps $g$ and $h$ with $\bar d = g(e)$ and $e = h(\bar d)$. By [[compactness|1NR3HAWG9D]], finitely many pairs $(g_i, h_i)$ cover all classes, each pair on a $\emptyset$-definable set of classes.
2. Pad the values of the $g_i$ with $0$ to a common length, and add a block that writes $i$ in binary with the constants $0$ and $1$. The resulting map $f$ satisfies $E(\bar x, \bar y) \leftrightarrow f(\bar x) = f(\bar y)$.

This proves the theorem.

## Idea

Strong minimality and the infinite algebraic closure of the prime field give each imaginary a real tuple algebraic over it.
The finitely many conjugates of that tuple form a finite set, which is a single imaginary again.
A field codes finite sets by the coefficients of a product of linear forms, and unique factorization makes this code exact.

## Variants

- The same steps 1 and 2 prove weak elimination of imaginaries for every strongly minimal theory with infinite $\operatorname{acl}(\emptyset)$. Steps 3 and 4 show that weak elimination plus codes for finite sets gives full elimination, in any theory.
- For finite sets of single elements, step 3 is the classical fact that the elementary symmetric functions of $c_1, \dots, c_k$ determine the set $\set{c_1, \dots, c_k}$, as the roots of $\prod_j (Y - c_j)$.
- For real closed fields, definable choice gives a shorter proof: each class has a canonical representative, definable from the class.
