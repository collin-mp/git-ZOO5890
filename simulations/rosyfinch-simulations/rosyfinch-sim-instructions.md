## Goals
- Want to simulate year-round migratory patterns for interior Gray-crowned Rosy-Finch (Leucosticte tephrocotis tephrocotis)
    - ideally able to model elevational shifts between a hypothetical point A to point B
    - eventually expand to simulated movement -- timing of elevational shifts in year-round cycles
        - output individual elevation at any point based on elev data

## Assumptions, Parameters, Functions
#### Geography
- dimensionality 
    - scale -- continental/western North America (western continental US through Alaska)
        - basic topo map rendered in simulation
    - resolution? -- TBA
- elevational difference using real-world topography data
#### Movement
- movement based -- day by day? 
    - based on occurrence data?
    - departure timing adjusts with phenology?
        - 'winter' and 'summer' proceed along latitudes simulating earth tilt
- individual sources populations
    - three populations
        - stratified by wintering latitude, nonbreeding lats correspond to breeding lats
- stage structure
    - breeding
        - low movement, high specific site fidelity
    - nonbreeding
        - random movement within set range, low site fidelity
    - migration
        - directional, stopovers?
- simulation begins on Jan 1 default, or eventually custom defined parameter
#### Nonbreeding conditions
- individual bird(s) start at Jan 1 on nonbreeding grounds
- nonbreeding grounds range defined with published data on interior Gray-crowned Rosy-Finch, elevation bounds
- simulated/random 'nomadic' movement in within nonbreeding area bounds
#### Migration conditions
- individual movements begin within range from 1 Mar — 30 Apr
- full cycle of migratory movement for an individual takes ~3 weeks (estimate) to reach nonbreeding
- migration is direct with 'random' stopovers
#### Breeding conditions
- breeding grounds range defined by published data w/ elevation bounds
- behavior on breeding grounds is static relative to nonbreeding behavior

## Packages
- `seed` for reproducible result generation
- 


