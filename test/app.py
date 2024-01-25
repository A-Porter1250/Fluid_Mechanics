import numpy as np
import sympy as sp
import matplotlib as plt

'''
Lecture 4: Module 1 and Vocabulary & Eulerian and Lagrangian Perspectives

Key Points from last lecture:
• Computational methods for visualization:
• Scalars: colour maps
• Vectors: arrows
• Flow lines we can visualize:
• Streamlines: tangent to local velocity field
• Streaklines: loci of particles that passed through a given point
• Pathlines: paths travelled by particles
• All coincide for a steady state flow

Learning Objectives
• Describe fluid flows using the following terminology:
    • spatial dimensionality
    • steady/unsteady
    • laminar/turbulent
• Apply the above descriptions when analyzing fluid flows
• Distinguish between Eulerian and Lagrangian perspectives

Terms:

Laminar and Turbulant Flow for Engineerng for engineering

Laminar
    Fluid flows smoothly
    Low mixing
Turbulant
    Fluid flows erratically
    High Mixing
    
Comment from last lecture:
    Pathliens and streaklines need a time history
    Streamlines only need a time instant
    
Ex. Sketch streamlines given a vector field:
    see image "insert name (12:45)"
    
Dimensionality:
    Vector V = V(space, Time)
    Dimensionality: # of spatial directions along which the flow varies
    Steady flow : no time dependance (no change in time)
    
1D steady: "V(x)"
2D steady: "V(x,y)"
3D steady: "V(x,y,z)"
1D unsteady: "V(x,t)"
2D unsteady: "V(x,y,t)"
3D unsteady: "V(x,y,z,t)"

We have between 1 and 3 independent variables

Ex 1D flow: Fully developped pipe flow

    Generate pipe with flow
    
    ============================================
                        |->
                           |->        
                            |->    _up_ = r
                            |->
                           |->
                        |->
    ============================================
    
    No chage in x-direction (fully developped), and axisymmetric
    
    V-> = v(r) = U(r)î
    
    Ex 2D flow
        V-> = U(x,y)î + V(x,y)ĵ
        
    Ex 3D flow (unsteady)
        V-> = U(x,y,z,t)î + V(x,y,z,t)ĵ + W(x,y,z,t)k̂

    Eulerian and Lagrangian descriptions
    
    In the Eulerian perspective, we watch a fixed region in space, and we monitor the fluid parcels coming in and out of this region.
    Similar to a control volume in thermodynamics.
    
    In the lagrangian perspective, we "ride on board" with fluid parcels (ie. riding a an infinitesimally small boat)
    
    Difference: Watch space vs Watch fluid
    
    In this course, we usually use the Eulerian perspective (much more commonly used in CFD)
    
    The Eulerian and Lagrangian perspectives are related through the material derivative.

'''
x,y,z,t = sp.symbols('x','y','z','t')


laminar_v_turbulant_dict = {
                    'Laminar flow': 'Fluid flows smoothly, Low mixing',
                    'Turbulant flow': 'Fluid flows erratically, High Mixing'}

dimensionality_dict = {
                    '1D steady': "V(x)",
                    '2D steady': "V(x,y)",
                    '3D steady': "V(x,y,z)",
                    '1D unsteady': "V(x,t)",
                    '2D unsteady': "V(x,y,t)",
                    '3D unsteady': "V(x,y,z,t)"
}

three_dimensional_unstead_flow = np.array(
                                    [x,y,z,t],
                                    [x,y,z,t],
                                    [x,y,z,t])

eulerian_v_lagrangian_dict = {
                    'eulerian':'In the Eulerian perspective, we watch a fixed region in space, and we monitor the fluid parcels coming in and out of this region. Similar to a control volume in thermodynamics.'
                    'lagrangian':
}

print(laminar_v_turbulant_dict)