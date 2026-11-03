---
tag: TZM7XNR4V0
kind: statement
role: theorem
name: Kutta–Joukowski theorem
msc: [76G25, 76B10]
uses: [84K7TEWZ2Z, Q4DVPTBHEE, BTHH4Y71QR]
about: [BTHH4Y71QR]
sources:
  - url: https://en.wikipedia.org/wiki/Kutta%E2%80%93Joukowski_theorem
same_as:
  wikidata: Q1752988
  wikipedia: Kutta–Joukowski theorem
---

## Statement

Consider a steady, two-dimensional, incompressible and irrotational flow of an inviscid fluid of constant density $\rho$ around a rigid body, with no body forces.
Suppose the velocity tends to the uniform stream $(U, 0)$ with $U > 0$ far from the body.
Let $\Gamma$ be the [[circulation|BTHH4Y71QR]] of the velocity around a closed curve that encloses the body, taken counterclockwise.
Then the force per unit length that the fluid exerts on the body is
$$(F_x, F_y) = (0, -\rho U \Gamma).$$
So the force is perpendicular to the stream and has magnitude $\rho U \abs{\Gamma}$.

## Remarks

The proof uses the Blasius theorem.
Far from the body the [[complex potential|Q4DVPTBHEE]] has the expansion $w(z) = Uz - \frac{i\Gamma}{2\pi}\log z + c + \frac{m}{z} + \cdots$, since the flow is a uniform stream plus a vortex plus terms that decay.
Then $(w')^2 = U^2 - \frac{iU\Gamma}{\pi z} + O(z^{-2})$, and the residue theorem on a large circle gives $F_x - i F_y = \frac{i\rho}{2} \cdot 2\pi i \cdot \left(-\frac{iU\Gamma}{\pi}\right) = i\rho U\Gamma$.
For a flat plate of chord $c$ at angle of attack $\alpha$, the Kutta condition fixes $\abs{\Gamma} = \pi U c \sin\alpha$, which gives a lift $\pi \rho U^2 c \sin\alpha$ per unit span.
Without circulation the force is zero, which is the two-dimensional form of d'Alembert's paradox.

## Explanations

### L1 human

A wing produces lift because the air flows faster over the top than under the bottom.
One can describe this difference by a net swirl of the air around the wing, called the circulation.
The theorem says that the lift equals the density of the air times the flight speed times this circulation.

### L2 human

The theorem reduces the lift of any two-dimensional profile in [[potential flow|84K7TEWZ2Z]] to a single number, the circulation.
The shape of the body enters only through the value of $\Gamma$, which potential flow alone does not determine.
In airfoil theory the Kutta condition at the sharp trailing edge selects the physical value of $\Gamma$.
The same formula, applied to each section of a wing, is the basis of lifting-line theory, and it also explains the Magnus force on a spinning cylinder.
