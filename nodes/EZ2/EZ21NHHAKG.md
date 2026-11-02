---
tag: EZ21NHHAKG
kind: statement
role: theorem
name: Varieties as categories of algebras over a monad
msc: ["18C05", "18C15", "08C05"]
uses: [AJNZJD8442, WV3BPYCHVG, N353JF8RBK, FF6XXA6D1A, DF5N0PK3ZS, QG1ZXRC8EH, FEPRJR3MND]
about: [AJNZJD8442, FEPRJR3MND]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Statement

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras of a finitary signature, regarded as a category with homomorphisms.
Let $U \colon \mathcal{V} \to \mathbf{Set}$ be the [[forgetful functor|WV3BPYCHVG]] and let $F \colon \mathbf{Set} \to \mathcal{V}$ be the [[free functor|N353JF8RBK]], its left adjoint.
Let $\mathbb{T} = (U F, \eta, \mu)$ be the [[monad|FF6XXA6D1A]] on $\mathbf{Set}$ [[induced by this adjunction|DF5N0PK3ZS]], and let $\mathbf{Set}^{\mathbb{T}}$ be its [[Eilenberg–Moore category|FEPRJR3MND]] of [[$\mathbb{T}$-algebras|QG1ZXRC8EH]].
Then the comparison functor $K \colon \mathcal{V} \to \mathbf{Set}^{\mathbb{T}}$, which sends an algebra $A$ to the $\mathbb{T}$-algebra $(U A, U \varepsilon_A)$ where $\varepsilon_A \colon F U A \to A$ is the counit, is an isomorphism of categories.

## Remarks

The underlying set of $U F(X)$ is the set of terms in the variables $X$ modulo the identities of $\mathcal{V}$.
The map $U \varepsilon_A \colon U F U A \to U A$ evaluates such a term at elements of $A$.
Conversely, a $\mathbb{T}$-algebra $h \colon U F(X) \to X$ defines each basic operation $f$ of arity $n$ by $f(x_1, \ldots, x_n) = h(f(x_1, \ldots, x_n))$.
On the right, $h$ is applied to the term $f(x_1, \ldots, x_n)$.
The unit and associativity laws of $h$ force the identities of $\mathcal{V}$ to hold.
Another proof applies Beck's monadicity theorem: $U$ creates coequalizers of $U$-split pairs.

Example: for the variety of monoids, $U F(X)$ is the set $X^*$ of words.
A $\mathbb{T}$-algebra structure $X^* \to X$ is the same as a monoid structure on $X$: it sends a word to the product of its letters.

The monads that arise in this way are finitary, and every finitary monad on $\mathbf{Set}$ arises from a variety, possibly with infinitely many operations of each finite arity.
Monads that are not finitary describe infinitary structures; for instance, the algebras of the ultrafilter monad on $\mathbf{Set}$ are the compact Hausdorff spaces.

## Explanations

### L1 human

A variety, such as groups or rings, is usually described by operations and equations.
The theorem gives another description: only the free algebras and the way to evaluate formal expressions are needed.
An algebra of the variety is then a set with a rule that turns every formal expression in its elements into an element, consistently.

### L2 human

The result says that the forgetful functor of a variety is monadic, in the strict sense that the comparison functor is an isomorphism, not only an equivalence.
It explains why constructions on varieties, such as limits computed on underlying sets and the existence of colimits, follow from general monad theory.
Together with [[Lawvere theories|NTJ94H2CNS]], it gives three equivalent views of a variety: by a presentation, by a Lawvere theory, and by a finitary monad on $\mathbf{Set}$.
The [[Kleisli category|D9YHA46YWM]] of the same monad is equivalent to the full subcategory of free algebras.
