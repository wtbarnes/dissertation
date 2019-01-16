# Outline

1. Introduction
  * The Solar Atmosphere (layers of the Sun)
  * The Coronal Heating Problem
  * The Solar Magnetic Field
    * MHD
    * Reconnection
  * Active Regions
    * Physics
    * Characteristics
    * Why are they interesting?
  * Nanoflare Heating
    * Describe nanoflares / impulsive heating
    * Setup the problem to be solved in this thesis
2. Coronal Loop Physics
  * Brief intro to coronal loops, conceptual
  * Scaling laws
  * Cooling
  * Coronal hydrostatics
  * Coronal hydrodynamics
  * Numerical Models
    * HYDRAD
    * EBTEL + the two-fluid EBTEL model
3. Emission Diagnostics (Separate chapter for atomic physics and diagnostics?)
  * Atomic Physics
    * Coronal model approximation
    * Mechanisms for emission
    * Level population calculation
    * Ionization and recombination
    * Equilibrium versus non-equilibrium ionization
    * Computing non-equilibrium ionization
  * Temperature and density diagnostics
  * Emission Measure Distributions
    * Theory
    * Methods
    * Slope (cool)
    * "Hot" Plasma
  * Timelags (Does this go here?)
    * Theory
    * Simple Example
    * AIA Temperature Response example
4. Inferring Heating Properties from "Hot" Active Region Plasma Heated by Single Nanoflares
  * Content of Barnes et al. (2016a)
  * Use of hot plasma as a diagnostic for presence of nanoflares
  * It is hard!
  * Let's try more advanced forward modeling and looking at different diagnostics...
5. synthesizAR: A Python framework for forward-modeling optically-thin emission (should this be in the appendix?)
  * Magnetograms
  * Field extrapolations (Should this go somewhere else? It's own chapter?)
    * Potential versus non-linear force-free
    * PFSS versus AR scale
    * Detailed description of PFSS
    * Detailed description of Schmidt, oblique versus non-oblique
    * Show example with a simple dipole
  * Interfacing with hydrodynamic models
  * Computing intensities
  * Binning intensities
  * (show code examples and illustrate with an example using the Martens scaling laws)
  * (highlight that this is open-source, documented, tested, pure Python)
6. Modeling Nanoflare Heating Frequency in AR NOAA 1158
  * Introduction
  * Heating model
  * Intensities
  * Timelags
  * EM slopes
7. Classifying Nanoflare Heating Frequency in AR NOAA 1158
  * Introduction
  * Observations
  * EM Slopes
  * Timelags
  * Classification of slopes and timelags
    * Detailed description of random forest classification
    * Results
8. A Probabilistic Heating Model for Bundles of Coronal Loops
9. Conclusions
10. Appendix
  * Complete timelag and cross-correlation results from paper 1 (maps for all channel pairs)
  * fiasco