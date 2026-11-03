---
tag: Q7NFY5N96E
kind: statement
role: theorem
name: Leptin's theorem
msc: [43A07, 43A30, 22D15]
uses: [AHV05ZBCYW, CEAT9BESKK, ZYNY2VFECQ, 3JA4EF163Q, CDYXTW3PJF]
about: [CEAT9BESKK, 3JA4EF163Q]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_algebra
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] and let $A(G)$ be its [[Fourier algebra|3JA4EF163Q]].
Call $G$ [[amenable|CEAT9BESKK]] if there is a left-invariant [[mean|ZYNY2VFECQ]] on $L^\infty(G)$.
Then $G$ is amenable if and only if $A(G)$ has a bounded [[approximate identity|CDYXTW3PJF]].
This means a net $(u_\alpha)$ in $A(G)$ with $\sup_\alpha \norm{u_\alpha}_A < \infty$ and $\norm{u_\alpha v - v}_A \to 0$ for every $v \in A(G)$.

## Remarks

The idea of the proof in one direction: if $G$ is amenable, it satisfies the Følner or Reiter condition.
For a compact set $K$ and $\varepsilon > 0$ there is a set or function that is almost invariant under translation by $K$.
For a Følner set $F$, the function $u = \mu(F)^{-1} \mathbf{1}_F * \check{\mathbf{1}}_F$, where $\check{\mathbf{1}}_F(x) = \mathbf{1}_F(x^{-1})$, lies in $A(G)$ with norm at most $1$ and is close to $1$ on $K$.
These functions form an approximate identity bounded by $1$.
The converse direction uses a bounded approximate identity to build an invariant mean.

Example: for a compact group $G$ the constant function $1$ lies in $A(G)$ and is a unit, so the theorem is immediate.
For $G = \R$, the functions $u_n = \frac{1}{2n} \mathbf{1}_{[-n, n]} * \mathbf{1}_{[-n, n]}$ are the triangle functions $u_n(x) = \max(0, 1 - \abs{x}/(2n))$.
They satisfy $\norm{u_n}_A \le 1$ and tend to $1$ uniformly on compact sets.

Non-example: for the free group $F_2$ on two generators, which is not amenable, $A(F_2)$ has no bounded approximate identity.

## Explanations

### L1 human

Amenability is a property of groups that says, roughly, that one can average over the group in a translation-invariant way.
The Fourier algebra is an algebra of functions on the group with pointwise multiplication.
Leptin's theorem says that the group is amenable exactly when this algebra has an approximate unit of bounded size.
Such an approximate unit is a family of functions close to $1$ that, by multiplication, approximates every function of the algebra.

### L2 human

The theorem translates amenability of $G$ into a Banach algebra property of $A(G)$.
It is dual to the fact that $L^1(G)$ always has a bounded approximate identity: on the Fourier side, this property characterizes amenability.
It is the starting point of the study of $A(G)$ as a Banach algebra.
For instance, Forrest and Runde showed that $A(G)$ is an amenable Banach algebra if and only if $G$ has an abelian subgroup of finite index.
Weaker approximation properties of $A(G)$, such as weak amenability in the sense of Cowling and Haagerup, give invariants of non-amenable groups.
