---
tag: AR0D7V1J8T
kind: statement
role: theorem
name: Root system of a semisimple Lie algebra
msc: ["17B20", "17B22"]
uses: [KJKH7NJGGP, EY9DN7QAX1, BB098JPWGA, TWVQT18JXE, AVVV93CASN, 6TCXJA0FF9]
about: [EY9DN7QAX1, AVVV93CASN]
sources:
  - url: https://en.wikipedia.org/wiki/Semisimple_Lie_algebra
---

## Statement

Let $\mathfrak{g}$ be a finite-dimensional [[semisimple Lie algebra|EY9DN7QAX1]] over $\C$, and let $\mathfrak{h}$ be a [[Cartan subalgebra|BB098JPWGA]].
Let $\Phi \subseteq \mathfrak{h}^*$ be the set of roots from the [[root space decomposition|KJKH7NJGGP]].
For $\lambda \in \mathfrak{h}^*$, let $t_\lambda \in \mathfrak{h}$ be the element with $B(t_\lambda, h) = \lambda(h)$ for all $h \in \mathfrak{h}$, where $B$ is the [[Killing form|TWVQT18JXE]].
Put $(\lambda, \mu) = B(t_\lambda, t_\mu)$, and let $E_\Q$ be the $\Q$-span of $\Phi$.
Then:

1. the form $(\cdot, \cdot)$ takes rational values on $E_\Q$ and is positive definite there;
2. $\Phi$ is a reduced [[root system|AVVV93CASN]] in the Euclidean space $E = \R \otimes_\Q E_\Q$, and $\dim_\R E = \dim_\C \mathfrak{h}$;
3. up to isomorphism, this root system does not depend on the choice of $\mathfrak{h}$;
4. $\mathfrak{g}$ is simple if and only if $\Phi$ is irreducible.

## Remarks

The proof studies, for each root $\alpha$, the subalgebra $\mathfrak{g}_\alpha \oplus \mathfrak{g}_{-\alpha} \oplus [\mathfrak{g}_\alpha, \mathfrak{g}_{-\alpha}]$, which is isomorphic to $\mathfrak{sl}_2(\C)$.
The weights of $\mathfrak{g}$ under this copy of $\mathfrak{sl}_2(\C)$ are integers, which gives the integrality of $\langle \beta, \alpha \rangle$, and the symmetry of the weights of $\mathfrak{sl}_2$-modules gives $s_\alpha(\Phi) = \Phi$.
Item 3 follows from the [[conjugacy of Cartan subalgebras|6TCXJA0FF9]].
For $\mathfrak{sl}_{n+1}(\C)$, the roots $\varepsilon_i - \varepsilon_j$ form the root system $A_n$.
Two semisimple Lie algebras over $\C$ are isomorphic if and only if their root systems are isomorphic, so the root system is a complete invariant.

## Explanations

### L1 human

Each semisimple complex Lie algebra carries a finite symmetric set of vectors, its roots.
The theorem says that these vectors always satisfy the axioms of a root system.
This turns the study of the Lie algebra into the study of a finite geometric object.

### L2 human

This is the bridge between Lie algebras and combinatorics.
Together with the classification of root systems by Dynkin diagrams and the existence result of Serre, it gives the classification of the simple Lie algebras over $\C$.
