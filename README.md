# PhD Dissertation

See Rice University thesis formatting guidelines [here](https://graduate.rice.edu/thesisformat).

**Title:** Diagnosing the Frequency of Energy Deposition in the Magnetically-closed Solar Corona

## Outlines

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
4. synthesizAR: A Python framework for forward-modeling optically-thin emission
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
5. Modeling Nanoflare Heating Frequency in AR NOAA 1158
  * Introduction
  * Heating model
  * Intensities
  * Timelags
  * EM slopes
6. Classifying Nanoflare Heating Frequency in AR NOAA 1158
  * Introduction
  * Observations
  * EM Slopes
  * Timelags
  * Classification of slopes and timelags
    * Detailed description of random forest classification
    * Results
7. ~~How does varying the LOS affect the distribution of observables?~~
8. A Probabilistic Heating Model for Bundles of Coronal Loops
9. Conclusions
10. Appendix
  * fiasco

### Notes

* Should there be a chapter for Barnes et al. (2016b)? This fits theme somewhat: first we look for hot plasma using simplified models. We find that it is hard to diagnose heating frequency via hot plasma. Then, we use more advanced models to search for signatures of heating frequency in the cooler plasma. This decision can be made towards the end.
* Should there be a separate chapter on formation of spectra and diagnostics? Good logical separation. Diagnostics chapter would be: hot plasma, density diagnostics, DEM/EM, and timelags

## Examples

* [Graham Kerr (Glasgow)](http://theses.gla.ac.uk/7895/)
* [Trinity College Theses](https://www.tcd.ie/Physics/research/themes/astrophysics/theses/)
* [Sofia Moschou (KU Leuven)](https://perswww.kuleuven.be/~u0016541/MHD_sheets_pdf/thesisSofia.pdf)
* [Jeff Reep (Rice)](https://scholarship.rice.edu/handle/1911/88108)
