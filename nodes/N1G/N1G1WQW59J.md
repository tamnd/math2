---
tag: N1G1WQW59J
kind: counterexample
name: The shift maps on sequences are injective or surjective but not bijective
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
uses: [MBK6AE6734, XYTN19EPF2, 0RJF668P1T, 0PVG1CRAJN, 0XKH881BZ7, 0XSJ25Z9M4]
sources:
  - url: https://en.wikipedia.org/wiki/Shift_operator
    locator: Sequences
  - url: https://en.wikipedia.org/wiki/Shift_operator
    locator: Properties of the shift operator
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Cokernel
---

## Counterexample

In infinite dimension a linear map from a space to itself can be one to one without being onto, and onto without being one to one.
Let $F$ be a field and let $V$ be the [[space of all sequences|XYTN19EPF2]] $x = (x_0, x_1, x_2, \dots)$ with $x_i \in F$, with addition and scalar multiplication term by term.
Define the right shift $R$ and the left shift $L$, two [[shift operators|MBK6AE6734]] on $V$, by
$$R(x_0, x_1, x_2, \dots) = (0, x_0, x_1, \dots), \qquad L(x_0, x_1, x_2, \dots) = (x_1, x_2, x_3, \dots).$$

1. Both maps are [[linear|0RJF668P1T]]: for $n \ge 1$, term $n$ of $R(ax + y)$ is $a x_{n-1} + y_{n-1}$ and term $0$ is $0$, which are the terms of $aR(x) + R(y)$, and the check for $L$ is the same.
2. The map $R$ is [[injective|0PVG1CRAJN]], since $R(x) = 0$ forces $x_i = 0$ for each $i \ge 0$.
3. The map $R$ is not [[surjective|0XKH881BZ7]], since each sequence in its image starts with $0$, so $(1, 0, 0, \dots)$ is not in the image.
4. The map $L$ is surjective, since for each $y$ the sequence $x = (0, y_0, y_1, \dots)$ satisfies $L(x) = y$.
5. The map $L$ is not injective, since $L(1, 0, 0, \dots) = (0, 0, 0, \dots)$, so $\ker L \ne \{0\}$.
6. We have $L \circ R = \id_V$, since $L(R(x)) = L(0, x_0, x_1, \dots) = x$.
7. But $R \circ L \ne \id_V$, since $R(L(1, 0, 0, \dots)) = (0, 0, 0, \dots)$.
8. So neither $R$ nor $L$ is a [[linear isomorphism|0XSJ25Z9M4]] of $V$.

## Remarks

In a finite-dimensional space, an injective or surjective endomorphism is bijective, by the [[theorem on endomorphisms|0912EEEVCT]], so the shift maps show that finite dimension is needed.
Step 6 gives a left inverse that is not a right inverse, while in finite dimension $ST = \id$ forces $TS = \id$.

The same maps work on $F[x]$, viewed as the sequences with finitely many nonzero terms, and there $R$ is multiplication by $x$.
On the Hilbert space $\ell^2$ of square-summable sequences, $R$ is an isometry.
Its Fredholm index is $0 - 1 = -1$, and the index of $L$ is $1 - 0 = 1$.

## Explanations

### L1 human

Shift every term of a sequence one place to the right and put $0$ in front.
No information is lost, but the new sequence always starts with $0$.
So the map is one to one, but it does not reach every sequence.
This cannot happen in a finite-dimensional space.

### L2 human

The left shift drops the first term, so it reaches every sequence but forgets $x_0$.
Shifting right and then left gives back the sequence.
Shifting left and then right replaces $x_0$ by $0$.
Watch out: "injective implies bijective" for endomorphisms needs finite dimension.
