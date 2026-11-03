---
tag: Q86TANYYX4
kind: statement
role: theorem
name: Bianchi classification
msc: [17B05, 17B81, 83F05]
uses: [5JJYBJ6A8K, T9WAK2FH31, HBVZGRKCWQ, 1ZAT1Z967A, TQC9E2PE0T]
about: [5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Bianchi_classification
same_as:
  wikidata: Q2976541
  wikipedia: Bianchi classification
---

## Statement

Every real [[Lie algebra|5JJYBJ6A8K]] $L$ of dimension $3$ is isomorphic to a Lie algebra of one of the following Bianchi types.

1. Types I to VII: $L = \R x \ltimes_A \R^2$, a [[semidirect product|T9WAK2FH31]] with abelian ideal $\R^2$.
   Here $x$ acts on $\R^2$ by a real $2 \times 2$ matrix $A$, as follows.
   1. type I: $A = 0$, so $L$ is abelian;
   2. type II: $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, so $L$ is the [[Heisenberg algebra|HBVZGRKCWQ]];
   3. type III: $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$;
   4. type IV: $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$;
   5. type V: $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$;
   6. type $\mathrm{VI}_h$: $A$ has two distinct nonzero real eigenvalues, with $\mathrm{VI}_0$ given by $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$;
   7. type $\mathrm{VII}_h$: $A$ has two non-real eigenvalues, with $\mathrm{VII}_0$ given by $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
2. Type VIII: $L \cong \mathfrak{sl}_2(\R)$, the real [[special linear Lie algebra|1ZAT1Z967A]].
3. Type IX: $L \cong \mathfrak{so}_3(\R)$, the real [[orthogonal Lie algebra|TQC9E2PE0T]].

In types VI and VII a real parameter $h$ labels the classes of $A$ up to conjugation and scaling.
The normalization of $h$ differs between authors.
Algebras of different types, or of the same family with different admissible values of $h$, are not isomorphic.

## Remarks

The proof follows the dimension of the derived algebra $L' = [L, L]$.
If $L' = L$, then $L$ is simple, and its complexification is $\mathfrak{sl}_2(\C)$; the two real forms are $\mathfrak{sl}_2(\R)$ and $\mathfrak{so}_3(\R)$.
The Killing form is indefinite on the first and negative definite on the second, so they are not isomorphic.
Otherwise $L$ is solvable and has a $2$-dimensional abelian ideal, so it is a semidirect product $\R \ltimes_A \R^2$.
Replacing $x$ by $cx + v$ with $c \ne 0$ and $v \in \R^2$ replaces $A$ by $cA$, and a change of basis of $\R^2$ conjugates $A$.
So the type depends only on $A$ up to conjugation and nonzero scaling, which is what the list enumerates.
Types I, II, $\mathrm{VI}_0$, $\mathrm{VII}_0$, VIII and IX are the unimodular ones, where every $\operatorname{ad} y$ has trace zero.

## Explanations

### L1 human

Bianchi listed all three-dimensional real Lie algebras.
There are nine types, labelled with Roman numerals, two of which are one-parameter families.
Types VIII and IX are the simple ones: the Lie algebras of $SL_2(\R)$ and of the rotation group.
The others are built from a plane and one extra direction that acts on the plane by a matrix.

### L2 human

The list is the real counterpart of the classification of $3$-dimensional complex Lie algebras.
Over $\R$, a $2 \times 2$ real matrix can have complex eigenvalues, which gives the extra family $\mathrm{VII}_h$, and $\mathfrak{sl}_2(\C)$ has two real forms.
In general relativity, the Bianchi types classify spatially homogeneous cosmological models by the Lie algebra of their $3$-dimensional isometry group acting simply transitively.
The unimodular types form class A and the others class B.
