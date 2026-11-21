---
tag: 6M2R0ER3KV
kind: statement
role: theorem
name: Elimination of imaginaries
aliases: [elimination-of-imaginaries, elimination-of-imaginaries-in-acf, poizat-elimination-of-imaginaries, weak-elimination-of-imaginaries]
msc: ["03C07", "03C45", "03C60"]
topics: [SZRM3N6BXW]
audience: grad
uses: [120S3V3975, 0PF6TM8TWT, EYTTQZ0E1S, DKAGC639W9, 2NBBJADY5N]
about: [Q0HM88QQKN, 0PF6TM8TWT]
history:
  first_stated: "Poizat, 1983"
  notes: "Poizat proved elimination of imaginaries for algebraically closed fields in his 1983 paper Une théorie de Galois imaginaire, building on the eq-construction that Shelah introduced in 1978."
sources:
  - url: https://en.wikipedia.org/wiki/Imaginary_element
    locator: Definitions
  - book: isbn:9780521763240
  - book: isbn:9780198534372
---

## Statement

Let $T$ be a complete theory with a [[monster model|EYTTQZ0E1S]] $\mathbb{M}$, and let $\mathbb{M}^{\mathrm{eq}}$ be its structure of [[imaginary elements|120S3V3975]].
Write $\operatorname{dcl}$ and $\operatorname{acl}$ for [[definable and algebraic closure|DKAGC639W9]] in $\mathbb{M}^{\mathrm{eq}}$.

- $T$ has *elimination of imaginaries* if for each imaginary $e$ there is a finite tuple $\bar b$ of real elements with $e \in \operatorname{dcl}(\bar b)$ and $\bar b \in \operatorname{dcl}(e)$.
- $T$ has *weak elimination of imaginaries* if for each imaginary $e$ there is a real tuple $\bar b$ with $e \in \operatorname{dcl}(\bar b)$ and $\bar b \in \operatorname{acl}(e)$.
- $T$ has *uniform elimination of imaginaries* if for each $\emptyset$-definable equivalence relation $E$ on $\mathbb{M}^n$ there is a $\emptyset$-definable map $f : \mathbb{M}^n \to \mathbb{M}^k$ with $E(\bar x, \bar y) \leftrightarrow f(\bar x) = f(\bar y)$.

**Theorem (Poizat).** Let $p$ be $0$ or a prime.
The theory $\mathrm{ACF}_p$ of [[algebraically closed fields|0PF6TM8TWT]] of characteristic $p$, in the signature $\set{+, -, \cdot, 0, 1}$, has elimination of imaginaries.
It also has uniform elimination of imaginaries.

## Remarks

Elimination of imaginaries says that every definable set $X$ has a real code: a real tuple $\bar b$ such that the automorphisms fixing $X$ are exactly those fixing $\bar b$.
The proof is [[this proof|T6KS32FGAV]].

### Why each hypothesis is needed

- A field structure. The pure infinite set is strongly minimal, like $\mathrm{ACF}_p$, but the unordered pair $\set{a, b}$ has no real code: swapping $a$ and $b$ fixes the pair and no real element. In a field the pair is coded by $(a + b, a b)$.
- The pure field signature. Adding a predicate for a valuation ring gives the theory ACVF, whose value group and residue field are imaginary sorts. Haskell, Hrushovski and Macpherson showed that ACVF does not eliminate imaginaries in the field sort alone, and that it does after adding the *geometric sorts*.
- Algebraic closure enters the proof through strong minimality, which [[quantifier elimination|2NBBJADY5N]] gives. It is not necessary for the conclusion, as the converse below shows.

### Consequences

- Fields of definition. Let $\bar b$ be a real code of a definable set $X$. Then $X$ is definable over a subfield $k$ exactly when $\bar b$ lies in the perfect closure of $k$, since that closure is $\operatorname{dcl}(k)$ in $\mathrm{ACF}_p$.
- Quotients. For a $\emptyset$-definable group $G$ and a $\emptyset$-definable subgroup $H$, the coset space $G / H$ is in $\emptyset$-definable bijection with a definable set of tuples. This applies to quotients of algebraic groups.
- Galois theory. For a subfield $k$, each imaginary in $\operatorname{dcl}(k)$ is interdefinable with a tuple of the perfect closure of $k$, and each imaginary in $\operatorname{acl}(k)$ with a tuple of the algebraic closure of $k$. Poizat used this to give a [[Galois theory|WNQDKQYZ2R]] of imaginaries.

### Converse

The converse direction does not characterize algebraically closed fields: real closed fields and differentially closed fields of characteristic $0$ also eliminate imaginaries.
Weak elimination does not imply elimination: the theory of an infinite set has weak elimination of imaginaries, while unordered pairs have no real code.
An equivalence relation with infinitely many infinite classes has neither form; see [[this example|ZRJHD4RSXG]].

### Generalizations

- Uniformity. If $T$ has elimination of imaginaries and two distinct $\emptyset$-definable elements, then $T$ has uniform elimination of imaginaries, by compactness.
- Strongly minimal theories. A [[strongly minimal theory|PNGY60EBDJ]] with infinite $\operatorname{acl}(\emptyset)$ has weak elimination of imaginaries, by the first steps of the proof.
- Ordered structures. $\mathrm{RCF}$, and every [[o-minimal|DTWHAW1N0V]] expansion of an ordered group with a $\emptyset$-definable positive element, eliminates imaginaries, by definable choice: each nonempty set definable over $A$ has a point in $\operatorname{dcl}(A)$, uniformly in definable families.
- $\mathrm{DCF}_0$, the theory of [[differentially closed fields|KPCN3KHG50]], eliminates imaginaries.

## History

Shelah introduced $T^{\mathrm{eq}}$ in his 1978 book on classification theory.
Poizat proved elimination of imaginaries for algebraically closed fields in 1983, in his paper *Une théorie de Galois imaginaire*.
Haskell, Hrushovski and Macpherson later found the geometric sorts that eliminate imaginaries in algebraically closed valued fields.

## Explanations

### L1 human

Many objects in algebra are sets of points, like a finite set of points or a line.
The theorem says that, in an algebraically closed field, each such set has a name made of finitely many field elements.
For two points $2$ and $3$, the name of the set $\set{2, 3}$ is the pair $(5, 6)$, the sum and the product.
Every symmetry of the field that keeps the set in place keeps its name in place, and the converse also holds.

### L2 human

We find a real code for the set $X = \set{(1, 2), (3, 4)}$ in $\mathbb{C}^2$, as in step 3 of the proof.

1. Form the polynomial $P(Y, X_1, X_2) = (Y + 1 X_1 + 2 X_2)(Y + 3 X_1 + 4 X_2)$.
2. Expand: $P = Y^2 + (4 X_1 + 6 X_2) Y + 3 X_1^2 + 10 X_1 X_2 + 8 X_2^2$.
3. The coefficients $(4, 6, 3, 10, 8)$ do not depend on the order of the two points.
4. Conversely, $\mathbb{C}[Y, X_1, X_2]$ is a UFD, so the factorization into linear factors of the form $Y + c_1 X_1 + c_2 X_2$ is unique, and the coefficients give back $X$.

The typical use is to replace a definable family of sets by a definable set of tuples.
A trap is to code $X$ by the coordinatewise symmetric functions $(1 + 3, 1 \cdot 3, 2 + 4, 2 \cdot 4)$: the set $\set{(1, 4), (3, 2)}$ has the same values.

### L3 human

Elimination of imaginaries places the eq-construction inside the home sort, so that interpretable sets, quotients and canonical bases are all definable sets of tuples.
For algebraically closed fields, it is the model theoretic form of the algebraic fact that each subvariety of affine space has a smallest field of definition, up to perfect closure.
In valued fields, the right home is a finite list of geometric sorts, and in the stability theory of [[stable theories|T7JW5QY6KR]] one often works in $T^{\mathrm{eq}}$ from the start.
The next steps in the theory are the [[hyperimaginaries|NQPCDVV3NB]] of simple theories and the elimination of imaginaries in ACVF.
