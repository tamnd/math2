---
tag: WVGTEH6P10
kind: concept
name: Inertia tensor and principal axes
msc: ["70E15", "70E17"]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_of_inertia
    locator: Inertia tensor
---

## Summary

The inertia tensor of a rigid body about a point is a symmetric $3 \times 3$ matrix.
It collects the moments of inertia of the body about all axes through that point.
It turns the angular velocity of the body into its angular momentum, and it gives the kinetic energy of rotation as a quadratic form.
Its eigenvectors span the principal axes of the body, and its eigenvalues are the principal moments of inertia.
In a frame along the principal axes the equations of rigid body motion take their simplest form.

## Explanations

### L1 human

A scalar [[moment of inertia|08ANASGBXV]] tells how hard it is to spin a body about one fixed axis.
The inertia tensor stores this information for every axis through a point at once.
For a lopsided body, the angular momentum need not point along the axis of rotation, so a spinning lopsided wheel pushes sideways on its bearings.
Along a principal axis this does not happen: the angular momentum points along the axis of rotation.
A uniform box has its three principal axes through its centre, parallel to its edges.
