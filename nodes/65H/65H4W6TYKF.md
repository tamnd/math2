---
tag: 65H4W6TYKF
kind: definition
name: Butcher tableau
msc: [65L06]
defines: RH8BD7PW5F
uses: [7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_Runge%E2%80%93Kutta_methods
---

## Definition

Let $s \ge 1$ be an integer.
An *$s$-stage Butcher tableau* is an array
$$\begin{array}{c|c} c & A \\ \hline & b^{T} \end{array} \;=\; \begin{array}{c|ccc} c_1 & a_{11} & \cdots & a_{1s} \\ \vdots & \vdots & & \vdots \\ c_s & a_{s1} & \cdots & a_{ss} \\ \hline & b_1 & \cdots & b_s \end{array}$$
with real entries: a vector $c \in \R^s$, a matrix $A = (a_{ij}) \in \R^{s \times s}$ and a vector $b \in \R^s$.
It specifies the $s$-stage [[Runge–Kutta method|7DBPJKYC6C]] for $y' = f(t, y)$ with step $h$:
$$K_i = f\Big(t_n + c_i h, \; y_n + h \sum_{j=1}^{s} a_{ij} K_j\Big), \quad i = 1, \ldots, s, \qquad y_{n+1} = y_n + h \sum_{i=1}^{s} b_i K_i.$$

## Remarks

The method is explicit when $a_{ij} = 0$ for $j \ge i$, so the tableau is strictly lower triangular and blank entries are read as $0$.
Usually $c_i = \sum_j a_{ij}$ for each $i$.
An embedded pair adds a second row $\hat b^{T}$ of weights that gives a method of another order from the same stages.
Example: the classical fourth-order method has $c = (0, \tfrac12, \tfrac12, 1)^T$, $a_{21} = a_{32} = \tfrac12$, $a_{43} = 1$, all other $a_{ij} = 0$, and $b = (\tfrac16, \tfrac13, \tfrac13, \tfrac16)^T$.
Check of two order conditions: $\sum b_i = 1$ and $\sum b_i c_i = \frac16 + \frac16 + \frac16 = \frac12$.
Non-example: an array with $c \in \R^2$, $A \in \R^{2 \times 2}$ and $b \in \R^3$ is not a Butcher tableau, since the number of weights must equal the number of stages.

## Explanations

### L1 human

A Butcher tableau is a small table of numbers that encodes a Runge–Kutta method completely.
The left column says when in the step each stage is evaluated.
The square block says how earlier stages enter it, and the bottom row says how to average the stages.
