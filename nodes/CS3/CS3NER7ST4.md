---
tag: CS3NER7ST4
kind: statement
role: theorem
name: Arason–Pfister Hauptsatz
msc: ["11E81", "11E04"]
uses: [53EK4D07PV, 7HMTK6P4W7, KFVY0RPGF2, 0RBQS1JJCR]
about: [53EK4D07PV]
sources:
  - url: https://en.wikipedia.org/wiki/Pfister_form
---

## Statement

Let $F$ be a field of characteristic not $2$ and let $n \ge 0$.
Let $q$ be a nonzero anisotropic nondegenerate [[quadratic form|0RBQS1JJCR]] over $F$.
Assume that the class of $q$ in the [[Witt ring|KFVY0RPGF2]] $W(F)$ lies in the $n$-th power $I^n(F)$ of the [[fundamental ideal|53EK4D07PV]].
Then $\dim q \ge 2^n$.

## Remarks

The bound is sharp: an anisotropic $n$-fold [[Pfister form|7HMTK6P4W7]] lies in $I^n(F)$ and has dimension exactly $2^n$.
Moreover an anisotropic form in $I^n(F)$ of dimension $2^n$ is similar to an $n$-fold Pfister form.
The proof by Arason and Pfister uses Pfister forms and their behaviour over function fields of quadrics.
Example: for $n = 1$, a nonzero anisotropic form of even dimension has dimension at least $2$, which is clear.
For $n = 2$, a $2$-dimensional form in $I^2(F)$ has trivial discriminant, so it is $\langle a, -a \rangle$, which is hyperbolic; hence anisotropic forms in $I^2(F)$ have dimension at least $4$.
A consequence is that $\bigcap_{n} I^n(F) = 0$, since each nonzero Witt class contains an anisotropic form of some fixed dimension.

## Explanations

### L1 human

The powers of the fundamental ideal sort quadratic forms by how "deep" they are.
The theorem says that deep forms must be large: a form in the $n$-th layer that has no nontrivial zeros needs at least $2^n$ variables.
Pfister forms show that this many variables can be enough.

### L2 human

Hauptsatz is German for main theorem.
The theorem gives the separation property $\bigcap_n I^n(F) = 0$, which is needed to use the graded ring $\bigoplus_n I^n(F)/I^{n+1}(F)$ to study the Witt ring.
Together with the Milnor conjecture on quadratic forms, it means that a quadratic form is determined up to Witt equivalence by invariants with values in Galois cohomology.
