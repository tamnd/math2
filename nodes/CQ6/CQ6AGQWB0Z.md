---
tag: CQ6AGQWB0Z
kind: statement
role: theorem
name: Beilinson's theorem
sources:
  - wikipedia: en:63070573@r1369241780
    locator: Derived noncommutative algebraic geometry, section Beilinson's theorem
    note: adopted
    mention: wikipedia://en/63070573#LZFA
    sections: [Statement]
inventory: [QT5PQQFQ0W]
---

## Statement

Beilinson provided the first example of a full strong exceptional collection. In the derived category $D^b(\mathbb{P}^n)$ the line bundles $\mathcal{O}(-n), \mathcal{O}(-n+1), \ldots, \mathcal{O}(-1), \mathcal{O}$ form a full strong exceptional collection. He proves the theorem in two parts. First showing these objects are an exceptional collection and second by showing the diagonal $\mathcal{O}_\Delta$ of $\mathbb{P}^n \times \mathbb{P}^n$ has a resolution whose compositions are tensors of the pullback of the exceptional objects.

**Technical Lemma**

An exceptional collection of sheaves $E_1, E_2, \ldots, E_r$ on $X$ is full if there exists a resolution

$$0 \to p_1^*E_1 \otimes p_2^*F_1 \to \cdots \to p_1^*E_n \otimes p_2^*F_n \to \mathcal{O}_\Delta \to 0$$

in $D^b(X\times X)$ where $F_i$ are arbitrary coherent sheaves on $X$.

Another way to reformulate this lemma for $X = \mathbb{P}^n$ is by looking at the Koszul complex associated to

> $$\bigoplus_{i=0}^n \mathcal{O}(-D_i) \xrightarrow{\phi} \mathcal{O}$$

where $D_i$ are hyperplane divisors of $\mathbb{P}^n$. This gives the exact complex

> $$0 \to \mathcal{O}\left(-\sum_{i=1}^n D_i \right) \to \cdots \to \bigoplus_{i \neq j}\mathcal{O}(-D_i - D_j) \to \bigoplus_{i=1}^n\mathcal{O}(-D_i) \to \mathcal{O} \to 0$$

which gives a way to construct $\mathcal{O}(-n-1)$ using the sheaves $\mathcal{O}(-n),\ldots,\mathcal{O}(-1),\mathcal{O}$, since they are the sheaves used in all terms in the above exact sequence, except for

$$\mathcal{O}\left(-\sum_{i=0}^n D_i \right) \cong \mathcal{O}(-n-1)$$

which gives a derived equivalence of the rest of the terms of the above complex with $\mathcal{O}(-n-1)$. For $n=2$ the Koszul complex above is the exact complex

> $$0 \to \mathcal{O}(-3) \to \mathcal{O}(-2)\oplus\mathcal{O}(-2) \to \mathcal{O}(-1)\oplus\mathcal{O}(-1) \to \mathcal{O} \to 0$$

giving the quasi isomorphism of $\mathcal{O}(-3)$ with the complex

> $$0 \to \mathcal{O}(-2)\oplus\mathcal{O}(-2) \to \mathcal{O}(-1)\oplus\mathcal{O}(-1) \to \mathcal{O} \to 0$$
