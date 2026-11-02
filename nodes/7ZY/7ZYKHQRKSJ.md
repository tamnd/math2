---
tag: 7ZYKHQRKSJ
kind: statement
role: theorem
name: Hyperbolic law of cosines
msc: [51M10, 51M09]
uses: [GCZ8EEDCHS, 036696EMG2, 0H1JFKE7H4, 060ZVZBV3E, 809288G50Y]
about: [GCZ8EEDCHS]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_law_of_cosines
same_as:
  wikidata: Q17028374
  wikipedia: Hyperbolic law of cosines
---

## Statement

Let $ABC$ be a [[hyperbolic triangle|GCZ8EEDCHS]] in the hyperbolic plane of constant curvature $-1$.
Let $a$, $b$, $c$ be the lengths of the sides opposite $A$, $B$, $C$, and let $\gamma$ be the angle at $C$.
Then
$$\cosh c = \cosh a \cosh b - \sinh a \sinh b \cos \gamma,$$
where $\cosh$ and $\sinh$ are the [[hyperbolic cosine|036696EMG2]] and [[hyperbolic sine|0H1JFKE7H4]].

## Remarks

Proof idea: work in the [[hyperboloid model|809288G50Y]] with the form $B(x, y) = x_0 y_0 - x_1 y_1 - x_2 y_2$, where $\cosh d(x, y) = B(x, y)$.
After an isometry, $C = (1, 0, 0)$, $A = (\cosh b, \sinh b, 0)$ and $B = (\cosh a, \sinh a \cos \gamma, \sinh a \sin \gamma)$.
Then $\cosh c = B(A, B) = \cosh a \cosh b - \sinh a \sinh b \cos \gamma$.
For $\gamma = \pi/2$ it gives the hyperbolic Pythagorean theorem $\cosh c = \cosh a \cosh b$.
For small sides, $\cosh x \approx 1 + x^2/2$ and $\sinh x \approx x$, and the formula reduces to the Euclidean [[law of cosines|060ZVZBV3E]] $c^2 = a^2 + b^2 - 2ab \cos \gamma$.
In curvature $-k^2$ with $k > 0$, the same formula holds with $a, b, c$ replaced by $ka, kb, kc$.
There is also a dual law, $\cos \gamma = -\cos \alpha \cos \beta + \sin \alpha \sin \beta \cosh c$, which shows that the angles determine the triangle.

## Explanations

### L1 human

If you know two sides of a hyperbolic triangle and the angle between them, this formula gives the third side.
It plays the role of the school law of cosines, with hyperbolic functions in place of squares.
For a right triangle it says $\cosh c = \cosh a \cosh b$, the hyperbolic form of Pythagoras.

### L2 human

The law of cosines is the basic tool of hyperbolic trigonometry: the law of sines, the formulas for right triangles and the angle of parallelism all follow from it.
Since the right-hand side grows like $e^{a + b}/4 \cdot (1 - \cos \gamma)$ for long sides, it shows that two geodesics leaving a point at a fixed angle diverge exponentially, a key feature of negative curvature.
It is the hyperbolic member of a family with the spherical law $\cos c = \cos a \cos b + \sin a \sin b \cos \gamma$ and the Euclidean law as the flat limit.
