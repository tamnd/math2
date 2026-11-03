---
tag: PN15F4ZS8D
kind: statement
role: theorem
name: Euler's equations of rigid body motion
msc: ["70E15", "70E17"]
uses: [EZ9P9ERKNE, WVGTEH6P10, 2FTZ7D8Z0F, 7147M98XNR, 9636MFFSGC]
about: [EZ9P9ERKNE]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_equations_(rigid_body_dynamics)
same_as:
  wikidata: Q996383
  wikipedia: Euler's equations (rigid body dynamics)
---

## Statement

Let a [[rigid body|EZ9P9ERKNE]] move either about a fixed point $O$ or freely, and in the second case let $O$ be its centre of mass.
Let $e_1, e_2, e_3$ be an orthonormal frame attached to the body along its [[principal axes|WVGTEH6P10]] at $O$, with principal moments of inertia $I_1, I_2, I_3$.
Let $\omega = \omega_1 e_1 + \omega_2 e_2 + \omega_3 e_3$ be the [[angular velocity|2FTZ7D8Z0F]] of the body.
Let $\tau = \tau_1 e_1 + \tau_2 e_2 + \tau_3 e_3$ be the total external [[torque|9636MFFSGC]] about $O$.
Then the components satisfy
$$\begin{aligned} I_1 \dot\omega_1 + (I_3 - I_2)\,\omega_2 \omega_3 &= \tau_1, \\ I_2 \dot\omega_2 + (I_1 - I_3)\,\omega_3 \omega_1 &= \tau_2, \\ I_3 \dot\omega_3 + (I_2 - I_1)\,\omega_1 \omega_2 &= \tau_3. \end{aligned}$$

## Remarks

The law of motion is $\frac{dL}{dt} = \tau$, where $L$ is the [[angular momentum|7147M98XNR]] about $O$ and the derivative is taken in a frame at rest.
In the body frame $L = I_1\omega_1 e_1 + I_2\omega_2 e_2 + I_3\omega_3 e_3$, and the frame vectors move by $\dot e_i = \omega \times e_i$.
Hence $\frac{dL}{dt} = \sum_i I_i \dot\omega_i e_i + \omega \times L$, and writing $\omega \times L$ in components gives the three equations.
In vector form, with $I$ the inertia tensor in the body frame, they read $I\dot\omega + \omega \times (I\omega) = \tau$.

Example: for a body with $I_1 = I_2$ and no torque, the third equation gives $\dot\omega_3 = 0$.
The first two become $\dot\omega_1 = -\lambda \omega_2$ and $\dot\omega_2 = \lambda\omega_1$ with $\lambda = (I_3 - I_1)\omega_3 / I_1$.
So $(\omega_1, \omega_2)$ turns with constant angular speed $\lambda$: the rotation axis circles the symmetry axis in the body.

## Explanations

### L1 human

Newton's law says that force changes momentum.
For a spinning body, torque changes angular momentum, but the body is turning while this happens.
Euler's equations write this law in axes fixed to the body, where the inertia stays constant.
The extra products $\omega_2\omega_3$ and so on come from the turning of the axes, and they make a spinning body wobble even when no torque acts.

### L2 human

With no torque, the equations conserve the kinetic energy $\tfrac12 \sum_i I_i \omega_i^2$ and the squared length $\sum_i I_i^2 \omega_i^2$ of the angular momentum.
These two integrals make the torque-free equations solvable by Jacobi elliptic functions.
They are also the basis of Poinsot's description of the motion and of the stability analysis of permanent rotations.
For a heavy body with a fixed point, the torque of gravity depends on the direction of gravity in the body frame.
Adding the equation for this direction gives the Euler–Poisson equations of the heavy top.
