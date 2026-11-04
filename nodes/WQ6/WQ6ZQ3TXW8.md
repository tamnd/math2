---
tag: WQ6ZQ3TXW8
kind: statement
role: theorem
name: Bestvina–Handel theorem for irreducible automorphisms
sources:
  - wikipedia: en:20304533@r1321087158
    locator: Train track map, section Main result for irreducible automorphisms > Bestvina–Handel theorem for irreducible automorphisms
    note: adopted
    mention: wikipedia://en/20304533#PWOB
    sections: [Statement]
inventory: [N404J0NYTA]
---

## Statement

The following result was obtained by Bestvina and Handel in their 1992 paper where train track maps were originally introduced:

Let *φ* ∈ Out(*F*<sub>*k*</sub>) be irreducible. Then there exists a train track representative of *φ*.

For a topological representative *f*:*Γ*→*Γ* of an automorphism *φ* of *F*<sub>*k*</sub> the *transition matrix* *M*(*f*) is an *r*x*r* matrix (where *r* is the number of topological edges of *Γ*) where the entry *m*<sub>*ij*</sub> is the number of times the path *f*(*e*<sub>*j*</sub>) passes through the edge *e*<sub>*i*</sub> (in either direction). If *φ* is irreducible, the transition matrix *M*(*f*) is *irreducible* in the sense of the Perron&ndash;Frobenius theorem and it has a unique Perron–Frobenius eigenvalue *λ*(*f*) ≥ 1 which is equal to the spectral radius of *M*(*f*).

One then defines a number of different *moves* on topological representatives of *φ* that are all seen to either decrease or preserve the Perron–Frobenius eigenvalue of the transition matrix. These moves include: subdividing an edge; valence-one homotopy (getting rid of a degree-one vertex); valence-two homotopy (getting rid of a degree-two vertex); collapsing an invariant forest; and folding. Of these moves the valence-one homotopy always reduced the Perron–Frobenius eigenvalue.

Starting with some topological representative *f* of an irreducible automorphism *φ* one then algorithmically constructs a sequence of topological representatives

*f* = *f*<sub>1</sub>, *f*<sub>2</sub>, *f*<sub>3</sub>,...

of *φ* where *f*<sub>*n*</sub> is obtained from *f*<sub>*n*−1</sub> by several moves, specifically chosen. In this sequence, if *f*<sub>*n*</sub> is not a train track map, then the moves producing *f*<sub>*n*+1</sub> from *f*<sub>*n*</sub> necessarily involve a sequence of folds followed by a valence-one homotopy, so that the Perron–Frobenius eigenvalue of *f*<sub>*n*+1</sub> is strictly smaller than that of *f*<sub>*n*</sub>. The process is arranged in such a way that Perron–Frobenius eigenvalues of the maps *f*<sub>*n*</sub> take values in a discrete substet of $\mathbb R$. This guarantees that the process terminates in a finite number of steps and the last term *f*<sub>*N*</sub> of the sequence is a train track representative of *φ*.

A consequence (requiring additional arguments) of the above theorem is the following:

- If *φ* ∈ Out(*F*<sub>*k*</sub>) is irreducible then the Perron–Frobenius eigenvalue *λ*(*f*) does not depend on the choice of a train track representative *f* of *φ* but is uniquely determined by *φ* itself and is denoted by *λ*(*φ*). The number *λ*(*φ*) is called the *growth rate* of *φ*.
- If *φ* ∈ Out(*F*<sub>*k*</sub>) is irreducible and of infinite order then *λ*(*φ*) > 1. Moreover, in this case for every free basis *X* of *F*<sub>*k*</sub> and for most nontrivial values of *w* ∈ *F*<sub>*k*</sub> there exists *C* ≥ 1 such that for all *n* ≥ 1

$$\frac{1}{C}\lambda^n(\phi) \le ||\phi^n(w)||_X\le C \lambda^n(\phi),$$

where ||*u*||<sub>*X*</sub> is the cyclically reduced length of an element *u* of *F*<sub>*k*</sub> with respect to *X*. The only exceptions occur when *F*<sub>*k*</sub> corresponds to the fundamental group of a compact surface with boundary *S*, and *φ* corresponds to a pseudo-Anosov homeomorphism of *S*, and *w* corresponds to a path going around a component of the boundary of *S*.

Unlike for elements of mapping class groups, for an irreducible *φ* ∈ Out(*F*<sub>*k*</sub>) it is often the case  that

*λ*(*φ*) ≠ *λ*(*φ*<sup>−1</sup>).
