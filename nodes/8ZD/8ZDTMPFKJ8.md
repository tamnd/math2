---
tag: 8ZDTMPFKJ8
kind: example
name: The module of a scalar matrix
msc: ["15A21", "13C05"]
topics: [GEBYZKYV3D]
audience: grad
instance_of: [KGVTFBZX59]
illustrates: [R5X8SNHBGG]
uses: [KGVTFBZX59, R5X8SNHBGG, 06DW9BAWB1, 0ACX5QT8TE]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_theorem_for_finitely_generated_modules_over_a_principal_ideal_domain
    locator: Corollaries
---

## Example

Let $F$ be a field, let $c \in F$ and $n \ge 1$, and let $A = c I_n$, where $I_n$ is the [[identity matrix|06DW9BAWB1]].
We find the structure of the [[module|KGVTFBZX59]] $F^n_A$, in which $x$ acts as $A$.

1. Since $(c I_n)^k = c^k I_n$ for every $k$, a polynomial $f$ acts by $f \cdot v = f(c I_n) v = f(c) v$.
2. In particular $(x - c) \cdot v = 0$ for every $v$, and no nonzero constant kills a nonzero vector, so the annihilator of the module is the ideal $(x - c)$.
3. Every subspace $U$ is closed under $v \mapsto f(c) v$, so every subspace is a submodule. This agrees with the fact that every subspace is [[invariant|0ACX5QT8TE]] under $c I_n$.
4. Evaluation at $c$ gives an isomorphism of $F[x]/(x - c)$ with $F$, on which $x$ acts as multiplication by $c$.
5. Hence $F^n_A = F e_1 \oplus \cdots \oplus F e_n \cong (F[x]/(x - c))^n$.
6. For $n \ge 2$ the module is not cyclic, because each cyclic submodule $F[x] v = F v$ has dimension at most $1$.

## Remarks

### The other extreme from a cyclic module

A [[companion matrix|0ZCWPNZTQ3]] gives a module with one summand, and a scalar matrix gives one with as many summands as the dimension allows.
In the language of invariant factors, $c I_n$ has the $n$ invariant factors $x - c, \dots, x - c$, and its minimal polynomial $x - c$ is as small as possible.
For $c = 0$ the module is $F^n$ with $x$ acting as $0$.

### Many summands, many decompositions

The splitting in step 5 is not unique.
Any basis $v_1, \dots, v_n$ of $F^n$ gives $F^n_A = F v_1 \oplus \cdots \oplus F v_n$, and the structure theorem only says that the summands are determined up to isomorphism.

## Explanations

### L1 human

A scalar matrix multiplies every vector by the same number.
So a polynomial acting on a vector also just multiplies it by a number: the value of the polynomial at that number.
Every line through the origin is kept by the map, and the space splits into $n$ copies of one simple piece.

### L2 human

Here is a typical computation.
Take $A = 2 I_2$ over $\mathbb{Q}$ and $v = (1, 3)$.
Then $(x^2 - 1) \cdot v = (2^2 - 1) v = (3, 9)$.
Also $(x - 2) \cdot v = 0$, so $v$ has annihilator $(x - 2)$ and $\mathbb{Q}[x] v = \mathbb{Q} v$.
The example shows that the number of cyclic summands can be as large as $n$.
Watch out: "every subspace is a submodule" does not mean that the module is simple, since for $n \ge 2$ it splits into $n$ nonzero summands.
