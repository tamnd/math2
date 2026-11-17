---
tag: TKW0RRHV88
kind: example
name: The reduction of Camestres to Celarent
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
instance_of: [MZBNX2T6Q6, S4BTTGFR6J]
uses: [MZBNX2T6Q6, S4BTTGFR6J, 1TD6HRM5NG, KSJ9W29KXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Term_logic
    locator: lead section
---

## Example

Camestres is the syllogism of mood AEE in the second figure:

- Major premise: all $P$ are $M$.
- Minor premise: no $S$ is $M$.
- Conclusion: no $S$ is $P$.

A mathematical instance: all squares are rectangles, no triangle is a rectangle, so no triangle is a square.
We check that it is a syllogism of the [[second figure|S4BTTGFR6J]], and we prove it by reduction to Celarent (EAE-1), as its name says.

1. The conclusion "no triangle is a square" has subject "triangles" and predicate "squares". So $S$ is the triangles and $P$ is the squares.
2. The middle term $M$ is "rectangles", the term that occurs in both premises. There are exactly three [[terms|KSJ9W29KXQ]].
3. In both premises $M$ is the predicate. This is the scheme of the second figure.
4. The letters of "Camestres" give the plan. The initial C points to Celarent, the m says that the premises are exchanged, and the two letters s say that the minor premise and the conclusion are converted.
5. Convert the minor premise: "no $S$ is $M$" becomes "no $M$ is $S$". This is allowed because both say that no object lies in $S$ and in $M$.
6. Exchange the premises. The new major premise is "no $M$ is $S$", and the new minor premise is "all $P$ are $M$".
7. These two premises form Celarent with middle term $M$, minor term $P$ and major term $S$: no $M$ is $S$, all $P$ are $M$, so no $P$ is $S$.
8. Celarent is valid: if $x$ is in $P$, then $x$ is in $M$, and then $x$ is not in $S$. So no $P$ is $S$.
9. Convert the conclusion: "no $P$ is $S$" becomes "no $S$ is $P$", which is the conclusion of Camestres.

In the instance, steps 5 to 9 read: no rectangle is a triangle, all squares are rectangles, so no square is a triangle, so no triangle is a square.

## Remarks

The example shows the reduction to the first figure at work: a second-figure syllogism becomes a first-figure syllogism by conversions and by an exchange of the premises.
Only E and I propositions may be converted simply, and here both converted propositions are of kind E.
Cesare (EAE-2), "no $P$ is $M$, all $S$ are $M$, so no $S$ is $P$", reduces to Celarent with only one step: the conversion of the major premise.
Baroco (AOO-2) cannot be reduced by conversion, because its O premise does not convert; its name has a c, and it is reduced to Barbara by contradiction.
If the conclusion is weakened to "some $S$ is not $P$", the mood becomes Camestros (AEO-2), which is valid only when $S$ is not empty.

## Explanations

### L1 human

The argument "all squares are rectangles, and no triangle is a rectangle, so no triangle is a square" is correct, but it is not in the simplest shape.
We can turn it around.
"No triangle is a rectangle" means the same as "no rectangle is a triangle".
Now the chain is: squares are rectangles, rectangles are never triangles, so squares are never triangles.
And "no square is a triangle" means the same as "no triangle is a square".

### L2 human

We reduce the second-figure syllogism "all primes greater than $2$ are odd, no multiple of $4$ is odd, so no multiple of $4$ is a prime greater than $2$".

1. $S$ is "multiples of $4$", $P$ is "primes greater than $2$" and $M$ is "odd numbers". The mood is AEE, so the syllogism is Camestres.
2. Convert the minor premise: no odd number is a multiple of $4$.
3. Exchange the premises: no odd number is a multiple of $4$, and all primes greater than $2$ are odd.
4. Celarent gives: no prime greater than $2$ is a multiple of $4$.
5. Convert the conclusion: no multiple of $4$ is a prime greater than $2$.

The typical use of the reduction is to prove a mood from the first-figure moods only.
The trap is to convert an A proposition in step 2 or step 5: "all primes greater than $2$ are odd" does not convert to "all odd numbers are primes greater than $2$", and $9$ shows this.
