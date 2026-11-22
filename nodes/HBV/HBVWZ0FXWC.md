---
tag: HBVWZ0FXWC
kind: example
name: Eigenvalues of the shift operators on sequences
msc: ["15A18", "47A10"]
topics: [6R1D6QPY3S]
audience: ug2
instance_of: [0BQAA2BK3Q, 0N6960W0BV]
not_instance_of:
  - target: 0J5EMJRRFM
    note: The space of sequences is infinite-dimensional, so the shifts have no characteristic polynomial
illustrates: [08CJB2NQ92]
uses: [0ZND7NQ970, 0B5H4208Z9, 0AYEPBQMAW]
sources:
  - url: https://en.wikipedia.org/wiki/Shift_operator
    locator: Sequences
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Example

Let $F$ be a field and let $V = F^{\mathbb{N}}$ be the vector space of all sequences $x = (x_0, x_1, x_2, \dots)$ with entries in $F$.
The [[shift operators|MRJ5JPW9HN]] are the left shift $L$ and the right shift $R$:
$$L(x_0, x_1, x_2, \dots) = (x_1, x_2, x_3, \dots), \qquad R(x_0, x_1, x_2, \dots) = (0, x_0, x_1, \dots).$$
Both are linear, because they move entries and do not combine them.
We find all eigenvalues of each shift.

*The left shift.*

1. Let $\lambda \in F$ and let $v = (1, \lambda, \lambda^2, \dots)$, so that $v \ne 0$ because its first entry is $1$.
   Then
$$Lv = (\lambda, \lambda^2, \lambda^3, \dots) = \lambda (1, \lambda, \lambda^2, \dots) = \lambda v.$$
2. So every $\lambda \in F$ is an [[eigenvalue|0ZND7NQ970]] of $L$, and $v$ is an [[eigenvector|0B5H4208Z9]] for it.
3. Conversely, let $Lx = \lambda x$.
   Comparing entry $k$ gives $x_{k+1} = \lambda x_k$ for every $k$, so $x_k = \lambda^k x_0$ by induction, and $x = x_0 v$.
4. So the [[eigenspace|0AYEPBQMAW]] of $L$ for $\lambda$ is the line spanned by $v$.

*The right shift.*

5. Suppose $Rx = \lambda x$.
   Entry $0$ gives $0 = \lambda x_0$, and entry $k + 1$ gives $x_k = \lambda x_{k+1}$ for every $k \ge 0$.
6. If $\lambda = 0$, the second equation reads $x_k = 0$ for every $k$, so $x = 0$.
7. If $\lambda \ne 0$, the first equation gives $x_0 = 0$.
   Then $x_{k+1} = \lambda^{-1} x_k$ gives $x_k = 0$ for every $k$ by induction.
8. In both cases $x = 0$, so $R$ has no eigenvalue at all.

## Remarks

The two shifts are as different as possible: $L$ has every scalar as an eigenvalue, and $R$ has none.
The result for $R$ holds over every field, also over $\mathbb{C}$.
Over $\mathbb{C}$ in finite dimension this cannot happen, because every operator on a nonzero finite-dimensional complex space has an eigenvalue.
So the [[existence of an eigenvalue over an algebraically closed field|08CJB2NQ92]] needs the finite dimension.

The shifts break another rule of finite dimension.
We have $LR = \id$, since $L(0, x_0, x_1, \dots) = (x_0, x_1, \dots)$, but $RL(x) = (0, x_1, x_2, \dots)$, so $RL \ne \id$.
For square matrices a one-sided inverse is always two-sided.

The answer also depends on the space.
On the space $\ell^2$ of square-summable complex sequences, the sequence $(1, \lambda, \lambda^2, \dots)$ lies in $\ell^2$ exactly when $|\lambda| < 1$.
So there the eigenvalues of $L$ are the points of the open unit disc.
For operators on such spaces the [[spectrum of an operator|XXXSST2DR5]] can be larger than the set of eigenvalues.

## Explanations

### L1 human

The left shift forgets the first term of a sequence and moves every other term one place forward.
A geometric sequence such as $1, 2, 4, 8, \dots$ becomes $2, 4, 8, 16, \dots$, which is $2$ times the old one.
So the geometric sequences are eigenvectors of the left shift, one for each ratio.
The right shift puts a $0$ in front, and no nonzero sequence is a multiple of its own right shift.

### L2 human

The two shifts show what changes in infinite dimension.
Watch out: you cannot compute these eigenvalues with a determinant, because there is no characteristic polynomial on an infinite-dimensional space.
The only tool is the definition, applied entry by entry, as in steps 3 and 5.
The same method finds the eigenvectors of any linear recurrence: the solutions of $x_{k+1} = \lambda x_k$ are the geometric sequences.
