---
tag: 23RVD8K8RB
kind: statement
role: theorem
name: Thom's classification of elementary catastrophes
msc: [58K35, 58K40, 58K60]
uses: [KSAFWZVB8K, B4FRQMWQKP, 7SWSRGDT4A, 0YTCMFB4HC, 6FKJ6SXP3G]
about: [6FKJ6SXP3G, KSAFWZVB8K]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Statement

Let $r \le 4$, and consider smooth families $V \colon \R^n \times \R^r \to \R$, $(x, u) \mapsto V_u(x)$, of functions of $n$ state variables depending on $r$ control parameters.
Give $C^\infty(\R^n \times \R^r, \R)$ the Whitney $C^\infty$ topology.
There is an open dense set of families $V$ with the following property at every point $(x_0, u_0)$.
View the germ of $V$ at $(x_0, u_0)$ as an unfolding of the [[germ|7SWSRGDT4A]] of $V_{u_0}$ at $x_0$.
This unfolding is equivalent to a nondegenerate quadratic form in some state variables plus one of the following:

1. a regular point: $x$;
2. a nondegenerate critical point: the function $0$, so that only the quadratic form remains;
3. the fold: $x^3 + a x$;
4. the cusp: $\pm(x^4 + a x^2 + b x)$;
5. the swallowtail: $x^5 + a x^3 + b x^2 + c x$;
6. the butterfly: $\pm(x^6 + a x^4 + b x^3 + c x^2 + d x)$;
7. the hyperbolic umbilic: $x^3 + y^3 + a xy + b x + c y$;
8. the elliptic umbilic: $x^3 - 3 x y^2 + a (x^2 + y^2) + b x + c y$;
9. the parabolic umbilic: $\pm(x^2 y + y^4 + a x^2 + b y^2 + c x + d y)$.

Here equivalence of unfoldings allows a change of control parameters and a change of state variables depending on the controls.
It also allows the addition of a smooth function of the controls.
The letters $a, b, c, d$ stand for the control parameters that are used.

## Remarks

Items 3 to 9 are the seven elementary catastrophes.
Each is the [[universal unfolding|KSAFWZVB8K]] of its organising centre, the germ obtained by setting the parameters to $0$.
The number of parameters is the [[codimension|B4FRQMWQKP]] of that germ.
It is $1$ for the fold, $2$ for the cusp, $3$ for the swallowtail and the hyperbolic and elliptic umbilics, and $4$ for the butterfly and the parabolic umbilic.
The idea of the proof has two parts.
By Thom's transversality theorem in jet space, germs of codimension greater than $r$ do not occur in a generic $r$-parameter family.
Up to sign and quadratic terms, the germs of codimension from $1$ to $4$ are exactly the seven organising centres.
These are $x^3$, $x^4$, $x^5$, $x^6$, $x^3 + y^3$, $x^3 - 3xy^2$ and $x^2 y + y^4$.
Each of them is finitely determined, and its universal unfolding is checked with the versality criterion.
The list of seven depends on the bound $r \le 4$: with five controls further catastrophes appear.
For $r \ge 6$, families of germs with a modulus, such as $x^3 + y^3 + z^3 + a xyz$, occur generically, and no finite list is possible.
Thom proposed the classification; complete proofs rest on the work of Mather on stability and finite determinacy.

## Explanations

### L1 human

Imagine a system that always settles in a minimum of some energy, while a few control knobs change the energy.
As the knobs turn, minima can merge and vanish, and the system then jumps.
Thom's theorem says that with at most four knobs, the ways this can happen are, after a change of coordinates, only seven.
They carry names that describe the shape of the set of knob settings where jumps occur: fold, cusp, swallowtail, butterfly and three umbilics.

### L2 human

The theorem combines the three main tools of local singularity theory: finite determinacy, the classification of germs of low codimension, and versal unfoldings.
Its organising centres are the real forms of the simple singularities $A_2$ to $A_5$, $D_4^{\pm}$ and $D_5$ from [[Arnold's classification|M5437FP73G]].
The [[fold catastrophe|E192Q8BQWJ]] and the [[cusp catastrophe|VQ7D5N3MV7]] are the two cases with one state variable and at most two controls, and they model sudden jumps and hysteresis.
