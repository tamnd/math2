---
tag: GMYSQTH3Z7
kind: definition
name: Cellular algebra
msc: [16G10, 20C08]
defines: 76DF4G7J9S
uses: [3CTW1P4HBP, 0310REJJY8, 0KCQ9Y3QKA, ZBQ4KRC98K]
sources:
  - url: https://en.wikipedia.org/wiki/Cellular_algebra
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] with identity and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $R$.
A *cell datum* for $A$ consists of four pieces of data.
They are a finite partially ordered set $\Lambda$, a finite set $M(\lambda)$ for each $\lambda \in \Lambda$, and an $R$-linear map $* \colon A \to A$.
The fourth is an injective map $(\lambda, S, T) \mapsto C^{\lambda}_{S,T} \in A$, defined for $\lambda \in \Lambda$ and $S, T \in M(\lambda)$.
The data must satisfy:

1. The elements $C^{\lambda}_{S,T}$, for $\lambda \in \Lambda$ and $S, T \in M(\lambda)$, form an $R$-[[basis|0KCQ9Y3QKA]] of $A$.
2. The map $*$ is an anti-involution, that is $(ab)^* = b^* a^*$ and $(a^*)^* = a$ for all $a, b \in A$, and $(C^{\lambda}_{S,T})^* = C^{\lambda}_{T,S}$.
3. For all $a \in A$, $\lambda \in \Lambda$ and $S, T \in M(\lambda)$,
$$a\, C^{\lambda}_{S,T} \equiv \sum_{S' \in M(\lambda)} r_a(S', S)\, C^{\lambda}_{S',T} \pmod{A(< \lambda)},$$
where $r_a(S', S) \in R$ does not depend on $T$, and $A(< \lambda)$ is the $R$-span of the $C^{\mu}_{U,V}$ with $\mu < \lambda$.

The algebra $A$ is *cellular* if it has a cell datum, and the basis in clause 1 is then a *cellular basis*.

## Remarks

Example: $A = M_n(R)$, with $\Lambda = \set{\lambda}$, $M(\lambda) = \set{1, \dots, n}$, $C^{\lambda}_{i,j} = E_{ij}$ and $*$ the transpose.
The check of clause 3: for $a = (a_{kl})$, $a E_{ij} = \sum_k a_{ki} E_{kj}$, whose coefficients $a_{ki}$ do not depend on $j$, and $A(< \lambda) = 0$.
Non-example of a datum: the same basis of $M_2(R)$ with $*$ the identity map fails clause 2, since $(E_{12} E_{21})^* = E_{11}$ but $E_{21}^* E_{12}^* = E_{22}$.
Non-example of an algebra: the upper triangular $2 \times 2$ matrices over a field are not cellular.
Graham and Lehrer showed that the [[Cartan matrix|ZBQ4KRC98K]] of a cellular algebra over a field is symmetric.
This algebra has the Cartan matrix $\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, which is not symmetric.
Applying $*$ to clause 3 gives the mirror condition for right multiplication.
