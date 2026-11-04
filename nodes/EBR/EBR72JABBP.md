---
tag: EBR72JABBP
kind: statement
role: lemma
name: Solutions of a nonhomogeneous polynomial operator equation
msc: [15A06, 39A06]
uses: [0S23E6YE83]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_recurrence_rigorous.ptx#L77
    locator: source/s_recurrence_rigorous.ptx:77
---

## Statement

Let $V$ be a vector space of functions (for example, of sequences), and let $A$ be a linear operator on $V$.
Let $p(A) = c_0 A^k + c_1 A^{k-1} + \dots + c_k$ be a polynomial in $A$ with $c_0 \ne 0$ and $c_k \ne 0$.
Let $g \in V$, and let $W$ be the set of all $f \in V$ with $p(A) f = 0$.
Suppose $f_0 \in V$ satisfies $p(A) f_0 = g$.
Then every $f \in V$ with $p(A) f = g$ can be written as $f = f_0 + f_1$ with $f_1 \in W$.

## Remarks

Proof: the operator $p(A)$ is linear, so $p(A)(f - f_0) = g - g = 0$. Put $f_1 = f - f_0$.
The set $W$ is the [[kernel|0S23E6YE83]] of $p(A)$, and so a subspace of $V$.
The conditions $c_0 \ne 0$ and $c_k \ne 0$ are not used in this argument.
Example: for $u_{n+1} - 2u_n = 1$, the constant $-1$ is one solution, and $W$ is spanned by $2^n$.
