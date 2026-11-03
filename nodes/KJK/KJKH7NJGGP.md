---
tag: KJKH7NJGGP
kind: statement
role: theorem
name: Root space decomposition
msc: ["17B20", "17B22"]
uses: [EY9DN7QAX1, BB098JPWGA, TWVQT18JXE, KZ7RZC8XC4, 07JBSZE0V4]
about: [EY9DN7QAX1, BB098JPWGA]
sources:
  - url: https://en.wikipedia.org/wiki/Semisimple_Lie_algebra
---

## Statement

Let $F$ be an algebraically closed field of characteristic $0$.
Let $\mathfrak{g}$ be a finite-dimensional [[semisimple Lie algebra|EY9DN7QAX1]] over $F$, with a [[Cartan subalgebra|BB098JPWGA]] $\mathfrak{h}$.
Let $B$ be the [[Killing form|TWVQT18JXE]] of $\mathfrak{g}$.
For a linear form $\alpha$ in the [[dual space|07JBSZE0V4]] $\mathfrak{h}^*$, let $\mathfrak{g}_\alpha = \set{x \in \mathfrak{g} : [h, x] = \alpha(h) x \text{ for all } h \in \mathfrak{h}}$ be the [[weight space|KZ7RZC8XC4]] of $\alpha$ for the adjoint action of $\mathfrak{h}$.
Let $\Phi$ be the set of the nonzero $\alpha \in \mathfrak{h}^*$ with $\mathfrak{g}_\alpha \ne 0$; its elements are the roots.
Then:

1. $\mathfrak{h}$ is abelian and $\mathfrak{g}_0 = \mathfrak{h}$;
2. $\Phi$ is finite and $\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi} \mathfrak{g}_\alpha$;
3. $\dim \mathfrak{g}_\alpha = 1$ for each $\alpha \in \Phi$;
4. $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subseteq \mathfrak{g}_{\alpha + \beta}$ for all $\alpha, \beta \in \mathfrak{h}^*$;
5. $B(\mathfrak{g}_\alpha, \mathfrak{g}_\beta) = 0$ unless $\alpha + \beta = 0$, and the restriction of $B$ to $\mathfrak{h}$ is nondegenerate;
6. $\Phi$ spans $\mathfrak{h}^*$, and $-\alpha \in \Phi$ whenever $\alpha \in \Phi$.

## Remarks

The elements $\operatorname{ad} h$, $h \in \mathfrak{h}$, are semisimple and commute, so they can be diagonalized at the same time; this gives the decomposition in 2.
Item 4 follows from the Jacobi identity, and item 5 from the invariance of $B$.
Item 3 and the rest come from the copy of $\mathfrak{sl}_2$ spanned by $\mathfrak{g}_\alpha$, $\mathfrak{g}_{-\alpha}$ and $[\mathfrak{g}_\alpha, \mathfrak{g}_{-\alpha}]$, and from the representation theory of $\mathfrak{sl}_2$.
For $\mathfrak{g} = \mathfrak{sl}_n(F)$ with $\mathfrak{h}$ the diagonal matrices of trace $0$, the root spaces are the lines $F E_{ij}$ with $i \ne j$.
The root of $E_{ij}$ is $\varepsilon_i - \varepsilon_j$, where $\varepsilon_i$ reads off the $i$-th diagonal entry.
The hypothesis of semisimplicity is needed: for a nilpotent Lie algebra $\mathfrak{g}$, the whole of $\mathfrak{g}$ is a Cartan subalgebra and there are no roots.

## Explanations

### L1 human

The theorem cuts a semisimple Lie algebra into a commutative core $\mathfrak{h}$ and a finite number of lines.
On each line, the core acts by multiplication by a scalar that depends linearly on the element of the core.
These linear functions are the roots, and they record the whole bracket in a compact form.

### L2 human

The root space decomposition is the first step of the structure theory of semisimple Lie algebras.
From it one shows that the roots form a root system, which leads to the classification by Dynkin diagrams.
The same method with an arbitrary finite-dimensional module in place of $\mathfrak{g}$ gives the weight space decomposition of representations.
