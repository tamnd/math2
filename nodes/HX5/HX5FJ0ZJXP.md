---
tag: HX5FJ0ZJXP
kind: problem
name: Inverse problem for Lagrangian mechanics
msc: [70H03, 70F17, 49N45]
uses: [47JMCBM3VJ, PS0VV149ET, BEM454AYTT]
about: [47JMCBM3VJ]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_problem_for_Lagrangian_mechanics
same_as:
  wikidata: Q6060414
  wikipedia: Inverse problem for Lagrangian mechanics
history:
  posed_by: Hermann von Helmholtz
  first_stated: "1887"
---

## Problem

Let $n \ge 1$, let $W \subseteq \R \times \R^n \times \R^n$ be open, and let $F \colon W \to \R^n$ be smooth.
Consider the system of second-order ordinary differential equations
$$\ddot q_i = F_i(t, q, \dot q), \qquad i = 1, \ldots, n.$$
Consider smooth functions $L(t, q, \dot q)$ with $\det \big( \partial^2 L / \partial \dot q_i \partial \dot q_j \big) \ne 0$.
Decide whether there is such an $L$ whose [[Euler–Lagrange equations|PS0VV149ET]]
$$\frac{d}{dt} \frac{\partial L}{\partial \dot q_i} - \frac{\partial L}{\partial q_i} = 0, \qquad i = 1, \ldots, n,$$
have exactly the same solutions as the given system.
If so, describe all such $L$.

## Remarks

Equivalently, one asks for an invertible matrix of multipliers $g_{ij}(t, q, \dot q)$ such that $\sum_j g_{ij} (\ddot q_j - F_j)$ is the Euler–Lagrange expression of some $L$; then $g_{ij} = \partial^2 L / \partial \dot q_i \partial \dot q_j$.
The conditions that such a matrix must satisfy are a system of partial differential equations known as the Helmholtz conditions.
For $n = 1$, every such equation has a Lagrangian locally.
Jesse Douglas treated the case $n = 2$ in 1941 and sorted the systems into classes according to whether a Lagrangian exists and how many there are.
For $n \ge 3$ no complete answer is known.
The answer is not unique when it exists.
For $n = 1$ and $\ddot q = 0$, both $L = \frac{1}{2} \dot q^2$ and $L = e^{\dot q}$ work, since the Euler–Lagrange equation of $e^{\dot q}$ is $e^{\dot q} \ddot q = 0$, that is $\ddot q = 0$.

## Explanations

### L1 human

Usually one starts from a Lagrangian and derives the equations of motion.
The inverse problem goes the other way: given the equations of motion, is there a Lagrangian that produces them?
A positive answer gives a variational principle, conservation laws via symmetries, and a route to quantum mechanics.
For a single equation the answer is always yes locally, but for systems the answer depends delicately on the equations.
